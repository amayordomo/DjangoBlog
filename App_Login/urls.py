from django.urls import path
from . import views

app_name = 'App_Login'

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('profile', views.profile, name='profile'),
    path('change-profile', views.change_profile, name='user_change'),
    path('change-password', views.change_password, name='password_change'),

]
