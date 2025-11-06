import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from core.models import CustomUser
from core.tenant_organization.models import TenantOrganization
from core.project_workflow.models import ProjectWorkflow
from rest_framework_simplejwt.tokens import RefreshToken


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def auth_headers():
    def make_headers(user):
        refresh = RefreshToken.for_user(user)
        return {"HTTP_AUTHORIZATION": f"Bearer {str(refresh.access_token)}"}
    return make_headers


@pytest.fixture
def setup_data(db):
    org1 = TenantOrganization.objects.create(name="Org One")
    org2 = TenantOrganization.objects.create(name="Org Two")

    user1 = CustomUser.objects.create_user(
        email="user1@example.com",
        password="pass1234",
        tenant=org1,
    )
    user2 = CustomUser.objects.create_user(
        email="user2@example.com",
        password="pass1234",
        tenant=org2,
    )

    workflow1 = ProjectWorkflow.objects.create(
        tenant=org1, name="Org1 Workflow"
    )
    workflow2 = ProjectWorkflow.objects.create(
        tenant=org2, name="Org2 Workflow"
    )

    return {
        "org1": org1,
        "org2": org2,
        "user1": user1,
        "user2": user2,
        "workflow1": workflow1,
        "workflow2": workflow2,
    }


@pytest.mark.django_db
def test_list_only_user_tenant_organization_workflows(api_client, auth_headers, setup_data):
    user1 = setup_data["user1"]
    response = api_client.get(reverse("project-workflow-list"), **auth_headers(user1))
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]["name"] == "Org1 Workflow"


@pytest.mark.django_db
def test_create_workflow_auto_assigns_tenant_organization(api_client, auth_headers, setup_data):
    user1 = setup_data["user1"]
    payload = {"name": "Internal Projects"}
    response = api_client.post(reverse("project-workflow-list"), payload, **auth_headers(user1))
    assert response.status_code == status.HTTP_201_CREATED

    workflow = ProjectWorkflow.objects.get(name="Internal Projects")
    assert workflow.tenant == user1.tenant


@pytest.mark.django_db
def test_retrieve_workflow_detail(api_client, auth_headers, setup_data):
    """User should be able to retrieve details of their own workflow"""
    user1 = setup_data["user1"]
    workflow1 = setup_data["workflow1"]
    url = reverse("project-workflow-details", args=[workflow1.id])

    response = api_client.get(url, **auth_headers(user1))
    assert response.status_code == status.HTTP_200_OK
    assert response.data["name"] == workflow1.name


@pytest.mark.django_db
def test_retrieve_other_org_workflow_forbidden(api_client, auth_headers, setup_data):
    """User should not be able to access workflows from other tenant_organizations"""
    user1 = setup_data["user1"]
    workflow2 = setup_data["workflow2"]
    url = reverse("project-workflow-details", args=[workflow2.id])

    response = api_client.get(url, **auth_headers(user1))
    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
def test_update_workflow_name(api_client, auth_headers, setup_data):
    """User can update their own workflow"""
    user1 = setup_data["user1"]
    workflow1 = setup_data["workflow1"]
    url = reverse("project-workflow-details", args=[workflow1.id])

    payload = {"name": "Updated Workflow"}
    response = api_client.patch(url, payload, **auth_headers(user1))
    assert response.status_code == status.HTTP_200_OK

    workflow1.refresh_from_db()
    assert workflow1.name == "Updated Workflow"


@pytest.mark.django_db
def test_update_other_org_workflow_forbidden(api_client, auth_headers, setup_data):
    """User cannot update workflow from another tenant_organization"""
    user1 = setup_data["user1"]
    workflow2 = setup_data["workflow2"]
    url = reverse("project-workflow-details", args=[workflow2.id])

    response = api_client.patch(url, {"name": "Hacked!"}, **auth_headers(user1))
    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
def test_delete_own_workflow(api_client, auth_headers, setup_data):
    """User can delete their own workflow"""
    user1 = setup_data["user1"]
    workflow1 = setup_data["workflow1"]
    url = reverse("project-workflow-details", args=[workflow1.id])

    response = api_client.delete(url, **auth_headers(user1))
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not ProjectWorkflow.objects.filter(id=workflow1.id).exists()


@pytest.mark.django_db
def test_delete_other_org_workflow_forbidden(api_client, auth_headers, setup_data):
    """User cannot delete workflow from another tenant_organization"""
    user1 = setup_data["user1"]
    workflow2 = setup_data["workflow2"]
    url = reverse("project-workflow-details", args=[workflow2.id])

    response = api_client.delete(url, **auth_headers(user1))
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert ProjectWorkflow.objects.filter(id=workflow2.id).exists()


@pytest.mark.django_db
def test_create_workflow_without_name_fails(api_client, auth_headers, setup_data):
    """POST without required field should fail"""
    user1 = setup_data["user1"]
    payload = {}
    response = api_client.post(reverse("project-workflow-list"), payload, **auth_headers(user1))
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "name" in response.data