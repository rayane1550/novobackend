from .views import listar_tasks, criar_tasks
from django.urls import path


urlpatterns = [
    path('tasks/', listar_tasks),
    path('criartasks/', criar_tasks),
]