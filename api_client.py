import requests
from requests.exceptions import RequestException

BASE_URL = "http://127.0.0.1:5000"  # Backend API címe

class APIClient:
    @staticmethod
    def get_users():
        try:
            response = requests.get(f"{BASE_URL}/kliensek")
            response.raise_for_status()  # Hibát dob, ha a válasz státuszkódja nem 200
            return response.json() if response.status_code == 200 else None
        except RequestException as e:
            print(f"Hiba történt a felhasználók lekérésekor: {e}")
            return None

    @staticmethod
    def get_user(user_id):
        try:
            response = requests.get(f"{BASE_URL}/kliensek/{user_id}")
            response.raise_for_status()
            return response.json() if response.status_code == 200 else None
        except RequestException as e:
            print(f"Hiba történt a felhasználó lekérésekor: {e}")
            return None

    @staticmethod
    def get_trainers():
        try:
            response = requests.get(f"{BASE_URL}/edzok")
            response.raise_for_status()
            return response.json() if response.status_code == 200 else None
        except RequestException as e:
            print(f"Hiba történt az edzők lekérésekor: {e}")
            return None

    @staticmethod
    def get_trainer(trainer_id):
        try:
            response = requests.get(f"{BASE_URL}/edzok/{trainer_id}")
            response.raise_for_status()
            return response.json() if response.status_code == 200 else None
        except RequestException as e:
            print(f"Hiba történt az edző lekérésekor: {e}")
            return None

    @staticmethod
    def add_user(user_data):
        try:
            response = requests.post(f"{BASE_URL}/kliensek", json=user_data)
            response.raise_for_status()
            return response.json() if response.status_code == 201 else None
        except RequestException as e:
            print(f"Hiba történt a felhasználó hozzáadásakor: {e}")
            return None

    @staticmethod
    def add_trainer(trainer_data):
        try:
            response = requests.post(f"{BASE_URL}/edzok", json=trainer_data)
            response.raise_for_status()
            return response.json() if response.status_code == 201 else None
        except RequestException as e:
            print(f"Hiba történt az edző hozzáadásakor: {e}")
            return None

    @staticmethod
    def update_user(user_id, updated_data):
        try:
            response = requests.put(f"{BASE_URL}/kliensek/{user_id}", json=updated_data)
            response.raise_for_status()
            return response.json() if response.status_code == 200 else None
        except RequestException as e:
            print(f"Hiba történt a felhasználó frissítésekor: {e}")
            return None

    @staticmethod
    def update_trainer(trainer_id, updated_data):
        try:
            response = requests.put(f"{BASE_URL}/edzok/{trainer_id}", json=updated_data)
            response.raise_for_status()
            return response.json() if response.status_code == 200 else None
        except RequestException as e:
            print(f"Hiba történt az edző frissítésekor: {e}")
            return None

    @staticmethod
    def delete_user(user_id):
        try:
            response = requests.delete(f"{BASE_URL}/kliensek/{user_id}")
            response.raise_for_status()
            return response.status_code == 200
        except RequestException as e:
            print(f"Hiba történt a felhasználó törlésekor: {e}")
            return False

    @staticmethod
    def delete_trainer(trainer_id):
        try:
            response = requests.delete(f"{BASE_URL}/edzok/{trainer_id}")
            response.raise_for_status()
            return response.status_code == 200
        except RequestException as e:
            print(f"Hiba történt az edző törlésekor: {e}")
            return False