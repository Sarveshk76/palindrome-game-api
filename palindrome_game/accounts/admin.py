from django.contrib import admin
from .models import Profile

admin.site.site_header = 'Palindrome Game Admin'
admin.site.site_title = 'Palindrome Game Admin Portal'

admin.site.register(Profile)