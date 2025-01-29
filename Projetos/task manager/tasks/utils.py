import csv
from .models import Task

def export_task_to_csv():
    tasks = Task.objects.all()
    with open('task.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Description', 'Status', 'Due Date'])
        for task in tasks:
            writer.writerow([task.title, task.description, task.status, task.due_date])

def import_tasks_from_csv():
    with open('tasks.csv', mode='r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            Task.objects.create(title=row[0], description=row[1], status=row[2], due_date=row[3])