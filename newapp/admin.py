from django.contrib import admin
from .models import api_keys, form_submission

admin.site.register(api_keys)
admin.site.register(form_submission)