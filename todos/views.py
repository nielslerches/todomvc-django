from django.urls import reverse_lazy
from django.urls.base import reverse
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.views.generic.edit import FormMixin
from django.views.generic.list import MultipleObjectMixin


from .models import Todo


class NextMixin(FormMixin):
    def get_success_url(self) -> str:
        success_url = self.request.GET.get("next")
        if not success_url:
            success_url = super().get_success_url()
        return success_url


class SessionTodosMixin(MultipleObjectMixin):
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(session_key=self.request.session.session_key)
        return queryset


class TodoListView(SessionTodosMixin, ListView):
    model = Todo
    success_url = reverse_lazy("todos:todo_list")


class TodoCreateView(NextMixin, CreateView):
    model = Todo
    success_url = reverse_lazy("todos:todo_list")


class TodoUpdateView(SessionTodosMixin, NextMixin, UpdateView):
    model = Todo
    success_url = reverse_lazy("todos:todo_list")


class TodoDeleteView(SessionTodosMixin, NextMixin, DeleteView):
    model = Todo
    success_url = reverse_lazy("todos:todo_list")
