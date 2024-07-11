from django.contrib import admin
from .models import creditform
from .models import debitform
# Register your models here.
admin.site.register(creditform)
admin.site.register(debitform)