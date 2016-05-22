from django.db import models
from django.utils import timezone
from datetime import date
from datetime import datetime
from django import template


register = template.Library()    
@register.filter(name='in_the_future')
def in_the_future(value):
    return value > date.now()