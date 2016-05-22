from django.contrib import admin

# Register your models here.
from .models import Tasks
#from .models import TaskDetails
admin.site.register(Tasks)