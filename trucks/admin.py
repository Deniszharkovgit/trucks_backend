from django.contrib import admin

# Register your models here.
from .models import Truck
from .models import TruckModel

admin.site.register(Truck)
admin.site.register(TruckModel)
