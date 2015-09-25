from django.contrib import admin

# Register your models here.
from myapp.models import SampleModel

admin.site.register(SampleModel)
