from django.shortcuts import render
from django.shortcuts import loader
from django.http import Http404
from django.utils import timezone
from datetime import date
from datetime import datetime
import datetime

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Tasks
#from .models import TaskDetails
from .forms import AddTaskForm
from .forms import EditTaskStatus

from django.shortcuts import get_object_or_404

def index(request):
    task_list=Tasks.objects.order_by('-task_createDate')[:50]
    template=loader.get_template('polls/index.html')
    context={'task_list':task_list,}
    return HttpResponse(template.render(context,request))

def TaskInfo(request,id):
    try:
        task = Tasks.objects.get(pk=id)
        #task1 = TaskDetails.objects.get(pk=id)
    except Tasks.DoesNotExist:
        raise Http404("Task does not exist")
    #return render(request, 'polls/TaskInfo.html', {'task': task, 'task1': task1})
    return render(request, 'polls/TaskInfo.html', {'task': task})
    
def AddTask(request):
    #template=loader.get_template('polls/AddTask.html')
    #return HttpResponse(template.render(request))
    if request.method == "POST":
        form = AddTaskForm(request.POST)
        if form.is_valid():
            TasksAdded = form.save(commit=False)
            TasksAdded.task_createDate = timezone.now()
            TasksAdded.save()
            task = Tasks.objects.get(pk=TasksAdded.id)
            return render(request, 'polls/TaskInfo.html', {'task': task})
            #return redirect('TaskInfo', pk=Tasks.id)
    
    else:
        form = AddTaskForm()
    return render(request, 'polls/AddTask.html', {'form': form})
    
def EditStatus(request,pk):
    
    
    post = get_object_or_404(Tasks, pk=pk)
    if request.method == "POST":
        form = EditTaskStatus(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            task = Tasks.objects.get(pk=post.id)
            return render(request, 'polls/TaskInfo.html', {'task': task})
            #return redirect('TaskInfo', pk=post.pk)
    else:
        form = EditTaskStatus(instance=post)
    return render(request, 'polls/EditStatus.html', {'form': form})
    

    
    
def ListOnDueDate(request):
    task_list=Tasks.objects.order_by('-task_Due')[:50]
    template=loader.get_template('polls/ListOnDueDate.html')
    today =date.today()
    context={'task_list':task_list,'today':today}
    return HttpResponse(template.render(context,request))

def ListOnDay(request):
    task_list=Tasks.objects.order_by('-task_Due')[:50]
    template=loader.get_template('polls/ListOnDay.html')
    today =date.today()
    context={'task_list':task_list,'today':today}
    return HttpResponse(template.render(context,request))


def ListOnWeek(request):
    today =date.today()
    start_monday = today - datetime.timedelta(days=today.weekday())
    end_monday = today + datetime.timedelta(days=-today.weekday(), weeks=1)
    #task_list=Tasks.objects.order_by('-task_Due')[:50]
    template=loader.get_template('polls/ListOnWeek.html')
    #task_list=Tasks.objects.filter('date__range=[start_monday, end_monday]')[:50]
    task_list=Tasks.objects.filter(task_Due__range=(start_monday, end_monday))
    context={'task_list':task_list}
    return HttpResponse(template.render(context,request))
    

def ListOnMonth(request):
    task_list=Tasks.objects.order_by('-task_Due')[:50]
    template=loader.get_template('polls/ListOnMonth.html')
    today =date.today()
    context={'task_list':task_list,'today':today}
    return HttpResponse(template.render(context,request))
    
def ListOnYear(request):
    task_list=Tasks.objects.order_by('-task_Due')[:50]
    template=loader.get_template('polls/ListOnYear.html')
    today =date.today()
    context={'task_list':task_list,'today':today}
    return HttpResponse(template.render(context,request))

    
def CrossedDates(request):
    task_list=Tasks.objects.all()[:50]
    template=loader.get_template('polls/CrossedDates.html')
    today =date.today()
    context={'task_list':task_list,'today':today}
    return HttpResponse(template.render(context,request))
