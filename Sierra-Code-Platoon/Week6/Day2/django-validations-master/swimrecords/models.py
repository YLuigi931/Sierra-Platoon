from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta

def valid_stroke(value):
    valid_lst = ['front crawl', 'butterfly', 'breast', 'back', 'freestyle']
    if value not in valid_lst:
        raise ValidationError(f'{value} is not a valid stroke')
    else:
        return
    
def valid_number(value):
    if value < 50:
        raise ValidationError('Ensure this value is greater than or equal to 50.')
    else:
        return

def valid_date(value):
    if value > timezone.now():
        raise ValidationError("Can't set record in the future.")
    else:
        return 

def valid_record(value):
    if value < timezone.now():
        raise ValidationError("Can't break record before record was set.")
    else:
        return

class SwimRecord(models.Model):
   # delete me when you start writing in validations
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    team_name = models.CharField(max_length=32)
    relay = models.BooleanField()
    stroke = models.CharField(max_length=32,validators=[valid_stroke])
    distance = models.IntegerField(validators=[valid_number])
    record_date = models.DateTimeField(validators=[valid_date])
    record_broken_date = models.DateTimeField(validators=[valid_record])
