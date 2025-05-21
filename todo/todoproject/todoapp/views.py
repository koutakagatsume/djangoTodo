from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy


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

