from django.urls import path
from . import views

from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile_management/', views.profile_management, name='profile_management'),
    path('delete_account/', views.delete_account, name='delete_account'),


    # Password management

    # 1 - Allow us to enter our email in order to receive a password reset link

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='account/password_reset.html'), name='reset_password'),

    # 2 - Show a success message stating that an email was sent to reset our password

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='account/password_reset_sent.html'), name='reset_password_done'),

    # 3 - Send a link to our email so that we can reset our password

    path('reset<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='account/password_reset_form.html'), name='password_reset_confirm'),

    # 4 - Show a success message that our password wa changed

    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'), name='password_reset_complete')


]