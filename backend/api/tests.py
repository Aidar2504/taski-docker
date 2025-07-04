from http import HTTPStatus

from django.test import Client, TestCase

from api import models


class TaskiAPITestCase(TestCase):
    """Набор тестов для API приложения Taski."""

    def setUp(self):
        """Создание неавторизованного клиента перед каждым тестом."""
        self.guest_client = Client()

    def test_list_exists(self):
        """Проверка доступности списка задач."""
        response = self.guest_client.get('/api/tasks/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_task_creation(self):
        """Проверка создания задачи."""
        data = {'title': 'Test', 'description': 'Test'}
        response = self.guest_client.post('/api/tasks/', data=data)
        self.assertEqual(response.status_code, HTTPStatus.CREATED)
        self.assertTrue(models.Task.objects.filter(title='Test').exists())
