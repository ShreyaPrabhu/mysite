from django import forms
from .models import Tasks
#from .models import TaskDetails

class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ('task_name', 'task_desc','task_priority', 'task_status','task_Due',)
      
class EditTaskStatus(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ('task_status',)
