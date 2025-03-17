from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from tasks.models import Task

class TaskAPITestCase(APITestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="testpass")

        # Authenticate the client
        self.client.force_authenticate(user=self.user)

        # Create a test task
        self.task = Task.objects.create(
            title="Test Task",
            description="This is a test task",
            completed=False,
            owner=self.user 
        )

    def test_list_tasks(self):
        """Test retrieving the task list"""
        response = self.client.get("/api/tasks/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_task(self):
        """Test creating a new task"""
        data = {
            "title": "New Task",
            "description": "Test task description",
            "completed": False
        }
        response = self.client.post("/api/tasks/", data)
        print(response.data)  
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_task(self):
        """Test updating an existing task"""
        data = {
            "title": "Updated Task",
            "description": "Updated description",
            "completed": True
        }
        response = self.client.put(f"/api/tasks/{self.task.id}/", data)
        print(response.data) 
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_task(self):
        """Test deleting a task"""
        response = self.client.delete(f"/api/tasks/{self.task.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
