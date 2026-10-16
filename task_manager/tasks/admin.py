from django.contrib import admin
from .models import Task, Project, Tag, Notification


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


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'recipient', 'actor', 'verb', 'task', 'is_read', 'created_at')
    list_filter = ('is_read', 'created_at')
    search_fields = ('verb', 'recipient__username', 'actor__username')

