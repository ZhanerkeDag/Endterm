from django.urls import path
from auth_ import views

app_name = 'auth_'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),

]