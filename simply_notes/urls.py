from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('signup/', views.user_signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.user_logout, name='logout'),
    path("about/",views.about_page,name="about"),
]

