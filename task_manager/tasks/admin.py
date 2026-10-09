from django.contrib import admin
from .models import Task, Project, Tag


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner', 'created_at')
    search_fields = ('name', 'description')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    search_fields = ('name',)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'priority', 'project', 'owner', 'due_date')
    list_filter = ('status', 'priority', 'project', 'created_at')
    search_fields = ('title', 'description')
    filter_horizontal = ('tags',)
