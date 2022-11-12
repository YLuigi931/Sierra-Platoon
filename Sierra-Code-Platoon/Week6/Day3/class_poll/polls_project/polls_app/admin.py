from django.contrib import admin
from .models import *

# Register your models here.
# put it in list
admin.site.register([Question, Choice])