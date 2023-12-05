from django.urls import path, include
from . import views


urlpatterns = [
    path('register/', views.RegistrationView.as_view(), name="register"),
    path('', include('django.contrib.auth.urls'))
]