from django.urls import path
from .views import SignUpView
from . import views
urlpatterns = [
    path('registration/signup/', SignUpView.as_view(), name='signup'),
]