from django.urls import path
from . import views



urlpatterns = [

    path('add_plan/', views.add_plan, name='add_plan'),
    path('update_plan/<str:pk>/', views.update_plan, name='update_plan'),
    path('delete_plan/<str:pk>/', views.delete_plan, name='delete_plan'),


]