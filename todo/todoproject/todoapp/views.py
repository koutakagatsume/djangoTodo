from django.http import HttpResponse
from django.views.generic import ListView, DetailView
# from .models import Task


from .models import Task

# Create your views here.
class TaskList(ListView):
    model = Task
    print(model)
    context_object_name = 'tasks'

class TaskDetail(DetailView):
    model = Task
