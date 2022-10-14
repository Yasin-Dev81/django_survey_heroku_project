from django.urls import path
from .views import SignUpView, profile_view, UpdateProfileView

urlpatterns = [
    # path('signup/', SignUpView.as_view(), name='signup_url'),
    path('profile/', UpdateProfileView.as_view(), name='profile_url'),
]
