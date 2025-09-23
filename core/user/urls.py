from django.urls import path
from core.user.views import RegisterView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
]