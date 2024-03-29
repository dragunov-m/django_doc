from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('posts/', include('posts.urls')),
    path('forms/', include('forms.urls')),
    path('objs/', include('object_editor.urls')),
    path('auth/', include('auth_task.urls')),
    path('admin/', admin.site.urls),
]
