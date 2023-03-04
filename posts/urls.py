from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:post_id>/', views.post_view, name='post'),
    path('post/', views.post_view, name='post_id'),
    path('get_parameter/', views.get_parameter, name='get_parameter'),
]
