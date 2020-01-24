from django.contrib import admin
from .models import Action


class ActionAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'description', 'completed')


admin.site.register(Action, ActionAdmin)
