from django.contrib import admin

from .models import TrainData, CnnModel

admin.site.register(TrainData)
admin.site.register(CnnModel)
