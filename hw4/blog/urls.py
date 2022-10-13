from django.urls import path
from blog import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('token/', views.token, name='token'),
]
