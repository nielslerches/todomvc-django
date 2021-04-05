from django.urls import path, reverse_lazy, include

from .models import Todo
from .views import TodoListView, TodoCreateView, TodoDeleteView, TodoUpdateView

app_name = "todos"

urlpatterns = [
    path(
        "",
        include(
            [
                path("", TodoListView.as_view(), name="todo_list"),
                path(
                    "active/",
                    TodoListView.as_view(
                        success_url=reverse_lazy("todos:todo_active_list"),
                        queryset=Todo.objects.filter(done=False),
                    ),
                    name="todo_active_list",
                ),
                path(
                    "completed/",
                    TodoListView.as_view(
                        success_url=reverse_lazy("todos:todo_active_list"),
                        queryset=Todo.objects.filter(done=True),
                    ),
                    name="todo_completed_list",
                ),
            ]
        ),
    ),
    path(
        "create/",
        TodoCreateView.as_view(
            model=Todo,
            fields=("name", "done"),
            success_url=reverse_lazy("todos:todo_list"),
        ),
        name="todo_create",
    ),
    path(
        "<int:pk>/update/",
        TodoUpdateView.as_view(
            model=Todo,
            fields=("name", "done"),
            success_url=reverse_lazy("todos:todo_list"),
        ),
        name="todo_update",
    ),
    path(
        "<int:pk>/delete/",
        TodoDeleteView.as_view(model=Todo, success_url=reverse_lazy("todos:todo_list")),
        name="todo_delete",
    ),
]
