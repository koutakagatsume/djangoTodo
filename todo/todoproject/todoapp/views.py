from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView

from .models import Task

# Create your views here.

# タスク一覧
class TaskList(ListView):
    model = Task
    print(model)
    context_object_name = 'tasks'

# タスク詳細
class TaskDetail(DetailView):
    model = Task

# タスク作成
class TaskCreate(CreateView):
    model = Task
    # 全てのフィールド
    fields = "__all__"
    success_url = reverse_lazy('task_list')

# タスク更新
class TaskUpdate(UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy('task_list')

# タスク削除
class TaskDelete(DeleteView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy('task_list')
    context_object_name = 'task'

# ログイン
class TaskListLoginView(LoginView):
    fields = "__all__"
    # テンプレートディレクトを参照する
    template_name = 'todoapp/login.html'
    def get_success_url(self):
        return reverse_lazy('task_list')
