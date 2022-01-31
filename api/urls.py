from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from api.views import TaskListView, CreateUserView, TaskViewSet, TaskRetrieveView


router = routers.DefaultRouter()
router.register('tasks', TaskViewSet, basename='tasks')

urlpatterns = [
    path('task-list/', TaskListView.as_view(), name='task-list'),
    path('task-detail/<int:pk>/', TaskRetrieveView.as_view(), name='task-detail'),
    path('register/', CreateUserView.as_view(), name='register'),
    path('auth/', include('djoser.urls.jwt')),
    path('', include(router.urls)),
]