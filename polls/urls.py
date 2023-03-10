from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('form/', views.form, name='form'),
    path('form/create/', views.add_product, name='create'),
    path('form_get/', views.form_get, name='form_get')
]
