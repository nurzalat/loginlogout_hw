from django.urls import path

from account import views

urlpatterns = [
    path('account/register/', views.UserRegistrationView.as_view()),
]
