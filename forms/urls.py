from django.urls import path

from . import views

app_name = 'forms'
urlpatterns = [
    path('form-1/', views.form_1, name='form_1'),
    path('form-2/', views.form_2, name='form_2'),
    path('form-3/', views.form_3, name='form_3'),
    path('form-4/', views.form_4, name='form-4'),
    path('form-5/', views.form_5, name='form-5'),
    path('form-6/', views.form_6, name='form-6'),
    path('form-7/', views.form_7, name='form-7'),
    path('form-8/', views.form_8, name='form-8'),
    path('form-9/', views.form_9, name='form-9'),
    path('form-10/', views.form_10, name='form-10'),
]
