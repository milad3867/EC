from django.urls import path
from . import views

app_name = 'userManager'

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('create_account/',
         views.CreateAccount.as_view(), name='create_account'),
    path('profile/',
         views.UserPage.as_view(), name='profile'),
    path('logout/',
         views.Logout, name='logout'),

]
