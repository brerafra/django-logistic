from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(City)
admin.site.register(Vehicle)
admin.site.register(Route)
admin.site.register(Event)