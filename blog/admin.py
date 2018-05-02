from django.contrib import admin
from blog.models import DashaPost

# Register your models here.

class DashaPost_Admin(admin.ModelAdmin):
	list_display =('title','timestamp', 'body')

admin.site.register(DashaPost, DashaPost_Admin)
