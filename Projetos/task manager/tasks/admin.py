from django.contrib import admin
from .models import Task
from .utils import export_task_to_csv, import_tasks_from_csv

@admin.action(description="Exportar tarefas para CSV")
def export_csv(modeladmin, request, queryset):
    export_task_to_csv()

@admin.action(description="Importar tarefas do CSV")
def import_csv(modeladmin, request, queryset):
    import_tasks_from_csv()

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'status']
    actions = [export_csv, import_csv]
