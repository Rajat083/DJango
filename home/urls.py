from home import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('login', views.loginUser, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('signup', views.signUp, name='signup'),
    path("user", views.userInfo, name='user'),
    path('contact', views.contact, name='contact'),
]