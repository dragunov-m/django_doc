from django.urls import path, include
from . import views

app_name = 'auth_task'
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('reg/', views.registration, name='registration'),
]
