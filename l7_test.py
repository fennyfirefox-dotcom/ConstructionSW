from datetime import datetime
import unittest
from uuid import UUID

from model import TaskManager, TaskStatus, Task


class TestTaskManager(unittest.TestCase):

  def setUp(self):
    self.manager = TaskManager()
    self.now = datetime.now()

  def test_task_change_status(self):
    task = Task(description = "Method test", scheduled_at = self.now)
    self.assertEqual(task.status, TaskStatus.TODO)
    task.change_status(TaskStatus.COMPLETED)
    self.assertEqual(task.status, TaskStatus.COMPLETED)

  def test_add_task(self):
    task = self.manager.add_task("Buy milk", self.now)
    self.assertIsInstance(task.id, UUID)
    self.assertEqual(task.description, "Buy milk")
    self.assertEqual(task.status, TaskStatus.TODO)
    self.assertIn(task.id, self.manager.tasks)

  def test_get_task_success(self):
    task = self.manager.add_task("Test task", self.now)
    fetched = self.manager.get_task(task.id)
    self.assertEqual(task, fetched)

  def test_get_task_not_found(self):
    fake_id = UUID("00000000-0000-0000-0000-000000000000")
    with self.assertRaises(ValueError):
      self.manager.get_task(fake_id)

  def test_get_tasks(self):
    self.manager.add_task("Task 1", self.now)
    self.manager.add_task("Task 2", self.now)
    tasks = self.manager.get_tasks()
    self.assertEqual(len(tasks), 2)

  def test_update_task_description_and_status(self):
    task = self.manager.add_task("Old description", self.now)
    updated = self.manager.update_task(
        task.id,
        description = "New description",
        status = TaskStatus.IN_PROGRESS,
    )
    self.assertEqual(updated.description, "New description")
    self.assertEqual(updated.status, TaskStatus.IN_PROGRESS)

  def test_update_task_not_found(self):
    fake_id = UUID("00000000-0000-0000-0000-000000000000")
    with self.assertRaises(ValueError):
      self.manager.update_task(fake_id, description = "None")

  def test_delete_task(self):
    task = self.manager.add_task("Delete me", self.now)
    success = self.manager.delete_task(task.id)
    self.assertTrue(success)

    fake_id = UUID("00000000-0000-0000-0000-000000000000")
    with self.assertRaises(ValueError):
      self.manager.delete_task(fake_id)

  def test_filter_by_status(self):
    t1 = self.manager.add_task("ToDo task", self.now)
    t2 = self.manager.add_task("Completed task", self.now)
    self.manager.update_task(t2.id, status = TaskStatus.COMPLETED)

    todo_list = self.manager.filter_by_status(TaskStatus.TODO)
    completed_list = self.manager.filter_by_status(TaskStatus.COMPLETED)

    self.assertEqual(len(todo_list), 1)
    self.assertEqual(len(completed_list), 1)
    self.assertEqual(todo_list[0].id, t1.id)
    self.assertEqual(completed_list[0].id, t2.id)


if __name__ == "__main__":
  unittest.main()