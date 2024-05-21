# classes/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add_course/', views.add_course, name='add_course'),
    path('view_registrations/', views.view_registrations, name='view_registrations'),
    path('register_course/<int:course_id>/', views.register_course, name='register_course'),
    path('delete_course/<int:course_id>/', views.delete_course, name='delete_course'),  # New URL pattern
]
