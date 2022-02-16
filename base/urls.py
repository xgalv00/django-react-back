from django.contrib import admin
from django.urls import path, include, re_path
from actions import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('actions.urls')),
    path('', views.index, name='index'),
]
