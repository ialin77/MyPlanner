from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage, name='home'),
    path('my_plans/', views.my_plans, name='my_plans'),

]