import pytest
import requests
from typing import Dict, Any
import time

BASE_URL = "http://127.0.0.1:5000"

def wait_for_server():
    for _ in range(10):
        try:
            requests.get(f"{BASE_URL}/health")
            return
        except requests.exceptions.ConnectionError:
            time.sleep(0.5)
    raise RuntimeError("Server not responding")



def create_category(name: str) -> Any | None:
    try:
        response = requests.post(
            f"{BASE_URL}/api/categories/",
            json={"name": name},
            timeout=5
        )
        if response.status_code != 201:
            raise ValueError(f"Unexpected status: {response.status_code}")
        return response.json()
    except Exception as e:
        pytest.fail(f"Ошибка создания категории: {str(e)}")


def delete_category(category_id: int):
    requests.delete(f"{BASE_URL}/api/categories/{category_id}")


# Тесты для категорий
class TestCategories:
    def test_create_and_get_category(self):

        category_data = create_category("Тестовая категория")
        assert "id" in category_data
        category_id = category_data["id"]

        try:

            response = requests.get(f"{BASE_URL}/api/categories/{category_id}")
            assert response.status_code == 200
            assert response.json()["name"] == "Тестовая категория"

            response = requests.get(f"{BASE_URL}/api/categories/")
            assert response.status_code == 200
            assert any(cat["id"] == category_id for cat in response.json())
        finally:
            delete_category(category_id)

    def test_update_category(self):
        category_data = create_category("Категория для обновления")
        category_id = category_data["id"]

        try:

            response = requests.put(
                f"{BASE_URL}/api/categories/{category_id}",
                json={"name": "Обновленная категория"}
            )
            assert response.status_code == 200
            assert response.json()["name"] == "Обновленная категория"
        finally:
            delete_category(category_id)

    def test_delete_category(self):

        category_data = create_category("Категория для удаления")
        category_id = category_data["id"]

        response = requests.delete(f"{BASE_URL}/api/categories/{category_id}")
        assert response.status_code == 204

        response = requests.get(f"{BASE_URL}/api/categories/{category_id}")
        assert response.status_code == 404

    def test_get_categories(self):
        response = requests.get(f"{BASE_URL}/api/categories/")
        assert response.status_code == 200
        assert isinstance(response.json(), list)


# Тесты для вопросов с категориями
class TestQuestionsWithCategories:
    @pytest.fixture
    def setup_category(self):

        category_data = create_category("Тестовая категория для вопросов")
        yield category_data

        delete_category(category_data["id"])

    def test_create_question_with_category(self, setup_category):
        category = setup_category

        response = requests.post(
            f"{BASE_URL}/api/questions/",
            json={
                "text": "Тестовый вопрос №1",
                "category_id": category["id"]
            }
        )
        assert response.status_code == 201
        question_data = response.json()
        assert question_data["text"] == "Тестовый вопрос №1"
        assert question_data["category"]["id"] == category["id"]

        response = requests.get(f"{BASE_URL}/api/questions/{question_data['id']}")
        assert response.status_code == 200
        assert response.json()["category"]["name"] == category["name"]

        requests.delete(f"{BASE_URL}/api/questions/{question_data['id']}")


if __name__ == "__main__":
    pytest.main(["-v", "autotest.py"])