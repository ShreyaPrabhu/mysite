from django.db import models
from django.utils import timezone
from datetime import date


# Create your models here.

PRIORITY_CHOICES = ( 

  (1, 'ONE (LOW)'), 

  (2, 'TWO'), 

  (3, 'THREE (NORMAL)'), 
  
  (4, 'FOUR'), 

  (5, 'FIVE (HIGH)'), 

) 

STATUS_CHOICES = ( 

  (1, 'To do'), 

  (2, 'Doing'), 

  (3, 'Done'), 

) 



class Tasks(models.Model):
    task_name=models.CharField(max_length=200)
    task_createDate=models.DateTimeField(timezone.now())
    task_desc=models.CharField(max_length=200)
    task_status=models.IntegerField(choices=STATUS_CHOICES, default=1)
    task_priority=models.IntegerField(choices=PRIORITY_CHOICES, default=3)
    task_Due=models.DateField()
    

@property
def is_past_due(self):
    if date.today() > self.date:
        return True
    return False



#class TaskDetails(models.Model):
#tasks=models.ForeignKey(Tasks, on_delete=models.CASCADE)
#task_desc=models.CharField(max_length=200)
#task_status=models.CharField(max_length=200)
#task_priority=models.IntegerField(default=3)
#task_Due=models.DateField()
    

    