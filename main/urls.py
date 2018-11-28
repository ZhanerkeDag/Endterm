from django.urls import path
from main import views

app_name = 'main'

urlpatterns = [
    # Simple realization
    path('index/', views.index, name='index'),
    # path('<int:pk>/', views.persons_list, name='simple_details'),
    # CBV realization
    path('', views.IndexView.as_view(), name='home'),
    path('<int:pk>/', views.DetailsView.as_view(), name='details'),
    #path('', )
]