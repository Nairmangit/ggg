from django.contrib import admin
from .models import obj, sens, values_sens
# Register your models here.
admin.site.register(obj)
admin.site.register(sens)
admin.site.register(values_sens)
