from datetime import datetime
from uuid import UUID
from model import TaskManager, TaskStatus
from mvc import ConsoleView


class TaskController:

  def __init__(self):
    self.model = TaskManager()
    self.view = ConsoleView()

  def create_task_flow(self):
    desc = input("Enter task description: ").strip()
    if not desc:
      self.view.display_error("Description can't be empty!")
      return

    sched_str = input(
        "Enter schedule time in format YYYY-MM-DD HH:MM (exm. 2026-12-31"
        " 15:30): "
    ).strip()
    try:
      sched_for = datetime.strptime(sched_str, "%Y-%m-%d %H:%M")
    except ValueError:
      self.view.display_error(
          "Invalid date format! Use YYYY-MM-DD HH:MM."
      )
      return

    task = self.model.add_task(description = desc, scheduled_at = sched_for)
    self.view.display_message(f"Task successfully created with ID: {task.id}")

  def change_status_flow(self):
    task_id_str = input("Enter task ID to change status: ").strip()
    try:
      task_id = UUID(task_id_str)
    except ValueError:
      self.view.display_error("Wrong UUID format!")
      return

    task = self.model.get_task(task_id)
    if not task:
      self.view.display_error("Task with such ID was not found!")
      return

    print("Choose new status:")
    print("1. InProgress")
    print("2. Done")
    choice = input("Your choice (1-2): ").strip()

    if choice == "1":
      new_status = TaskStatus.IN_PROGRESS
    elif choice == "2":
      new_status = TaskStatus.COMPLETED
    else:
      self.view.display_error("Wrong choice!")
      return

    self.model.update_task(task_id, status=new_status)
    self.view.display_message("Task status was changed successfully!")

  def delete_task_flow(self):
    task_id_str = input("Enter task ID to delete! ").strip()
    try:
      task_id = UUID(task_id_str)
    except ValueError:
      self.view.display_error("Wrong UUID format!")
      return

    success = self.model.delete_task(task_id)
    if success:
      self.view.display_message("Task was successfully deleted!")
    else:
      self.view.display_error("Task with such ID was not found!")

  def update_task_flow(self):
    task_id_str = input("Enter Task ID to update: ").strip()
    try:
      task_id = UUID(task_id_str)
    except ValueError:
      self.view.display_error("Wrong UUID format!")
      return

    task = self.model.get_task(task_id)
    if not task:
      self.view.display_error("Task with such ID was not found!")
      return

    print(
        "Leave the field empty if you do not want to change it.."
    )
    new_desc = input(f"New description [{task.description}]: ").strip() or None

    sched_str = input(
        f"New time ({task.scheduled_at.strftime('%Y-%m-%d %H:%M')}): "
    ).strip()
    new_sched = None
    if sched_str:
      try:
        new_sched = datetime.strptime(sched_str, "%Y-%m-%d %H:%M")
      except ValueError:
        self.view.display_error("Wrong format. Time wasn't changed")

    self.model.update_task(
        task_id, description = new_desc, scheduled_at = new_sched
    )
    self.view.display_message("Task was successfully updated!")

  def show_all_tasks_flow(self):
    tasks = self.model.get_tasks()
    self.view.display_task_table(tasks)

  def filter_tasks_flow(self):
    print("Choose status to filter by:")
    print("1. ToDo")
    print("2. InProgress")
    print("3. Done")
    choice = input("Ваш вибір (1-3): ").strip()

    status_map = {
        "1": TaskStatus.TODO,
        "2": TaskStatus.IN_PROGRESS,
        "3": TaskStatus.COMPLETED,
    }
    status = status_map.get(choice)
    if not status:
      self.view.display_error("Wrong choice!")
      return

    tasks = self.model.filter_by_status(status)
    self.view.display_task_table(tasks)

  def show_task_by_id_flow(self):
    task_id_str = input("Enter task ID: ").strip()
    try:
      task_id = UUID(task_id_str)
    except ValueError:
      self.view.display_error("Wrong UUID format!")
      return

    task = self.model.get_task(task_id)
    self.view.display_single_task(task)