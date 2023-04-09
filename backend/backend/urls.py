from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from todo import views
from . import api

router = routers.DefaultRouter()
router.register(r'todos', views.TodoView, 'todo')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/getResult', api.getResult),
    path('api/', include(router.urls)),
]