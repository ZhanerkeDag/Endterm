from django.urls import path
from api import views

app_name = 'api'

urlpatterns=[
    path('login/', views.login),
    path('persons/', views.persons_list),
    path('persons/<int:pk>/', views.persons_detail),
    path('categories/', views.categories_list),
    path('categories/<int:pk>/', views.categories_detail),
    path('achievements/', views.achievements_list),
    path('achievements/<int:pk>/', views.achievements_detail)
]

