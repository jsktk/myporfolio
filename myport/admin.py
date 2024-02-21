# your_app_name/admin.py
from django.contrib import admin
from .models import mail  # Import your model

admin.site.register(mail)  # Register your model with the admin site
