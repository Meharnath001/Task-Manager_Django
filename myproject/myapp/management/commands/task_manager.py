from django.core.management.base import BaseCommand
from myapp.models import Task

class TaskManager:
    def __init__(self):
        self.tasks = list(Task.objects.all())

    def add_task(self):
        title = input('Enter task title: ')
        description = input('Enter task description: ')
        priority = input('Enter task priority (High, Medium, Low): ')
        status = 'Pending'
        task = Task.objects.create(title=title, description=description, priority=priority, status=status)
        self.tasks.append(task)
        print('Task added successfully!')

    def edit_task(self):
        task_id = int(input('Enter the ID of the task to edit: '))
        try:
            task = Task.objects.get(id=task_id)
            title = input(f'Enter new title (current: {task.title}): ')
            description = input(f'Enter new description (current: {task.description}): ')
            priority = input(f'Enter new priority (current: {task.priority}): ')
            status = input(f'Enter new status (current: {task.status}): ')
            task.title = title
            task.description = description
            task.priority = priority
            task.status = status
            task.save()
            # Update local tasks list
            self.tasks = list(Task.objects.all())
            print('Task updated successfully!')
        except Task.DoesNotExist:
            print('Task not found.')

    def delete_task(self):
        task_id = int(input('Enter the ID of the task to delete: '))
        try:
            task = Task.objects.get(id=task_id)
            task.delete()
            # Update local tasks list
            self.tasks = list(Task.objects.all())
            print('Task deleted successfully!')
        except Task.DoesNotExist:
            print('Task not found.')

    def get_task_by_id(self, task_id):
        try:
            return Task.objects.get(id=task_id)
        except Task.DoesNotExist:
            print('Task not found.')
            return None

    def view_all_tasks(self):
        if not self.tasks:
            print('No tasks found.')
        for task in self.tasks:
            print(f'ID: {task.id}, Title: {task.title}, Description: {task.description}, Priority: {task.priority}, Status: {task.status}')

    def filter_tasks_by_priority(self):
        priority = input('Enter priority to filter by (High, Medium, Low): ')
        filtered_tasks = Task.objects.filter(priority=priority)
        if not filtered_tasks:
            print('No tasks found with the specified priority.')
        for task in filtered_tasks:
            print(f'ID: {task.id}, Title: {task.title}, Description: {task.description}, Priority: {task.priority}, Status: {task.status}')


class Command(BaseCommand):
    help = 'Manage tasks via CLI'

    def handle(self, *args, **kwargs):
        task_manager = TaskManager()
        while True:
            self.print_menu()
            choice = input('Enter your choice: ')
            
            if choice == '1':
                task_manager.add_task()
            elif choice == '2':
                task_manager.edit_task()
            elif choice == '3':
                task_manager.delete_task()
            elif choice == '4':
                task_manager.view_all_tasks()
            elif choice == '5':
                task_manager.filter_tasks_by_priority()
            elif choice == '6':
                break
            else:
                print('Invalid choice, please try again.')

    def print_menu(self):
        print('\nTask Manager Menu:')
        print('1. Add Task')
        print('2. Edit Task')
        print('3. Delete Task')
        print('4. View All Tasks')
        print('5. Filter Tasks by Priority')
        print('6. Exit')

# python manage.py task_manager
