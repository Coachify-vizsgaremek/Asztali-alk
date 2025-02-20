import requests

BASE_URL = "http://127.0.0.1:5000"  # Backend API címe

class APIClient:
    @staticmethod
    def get_users():
        response = requests.get(f"{BASE_URL}/kliensek")
        return response.json() if response.status_code == 200 else None

    @staticmethod
    def get_trainers():
        response = requests.get(f"{BASE_URL}/edzok")
        return response.json() if response.status_code == 200 else None

    @staticmethod
    def add_user(user_data):
        response = requests.post(f"{BASE_URL}/kliensek", json=user_data)
        return response.json() if response.status_code == 201 else None

    @staticmethod
    def add_trainer(trainer_data):
        response = requests.post(f"{BASE_URL}/edzok", json=trainer_data)
        return response.json() if response.status_code == 201 else None

    @staticmethod
    def update_user(user_id, updated_data):
        response = requests.put(f"{BASE_URL}/kliensek/{user_id}", json=updated_data)
        return response.json() if response.status_code == 200 else None

    @staticmethod
    def update_trainer(trainer_id, updated_data):
        response = requests.put(f"{BASE_URL}/edzok/{trainer_id}", json=updated_data)
        return response.json() if response.status_code == 200 else None

    @staticmethod
    def delete_user(user_id):
        response = requests.delete(f"{BASE_URL}/kliensek/{user_id}")
        return response.status_code == 200

    @staticmethod
    def delete_trainer(trainer_id):
        response = requests.delete(f"{BASE_URL}/edzok/{trainer_id}")
        return response.status_code == 200
