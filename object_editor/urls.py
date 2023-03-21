from django.urls import path

from . import views

app_name = 'objs'
urlpatterns = [
    path('', views.index, name='index'),
    path('edit/<int:pk>', views.edit_page, name='obj-view'),
    path('delete/<int:pk>', views.delete_page, name='obj-delete'),
]
