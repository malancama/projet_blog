from django.urls import path
from authentication import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.logIn, name='login'),
    path('logout/', views.logOut, name='logout')

]
