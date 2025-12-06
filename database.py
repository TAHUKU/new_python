import json
import os

FILE = "users.json"

# Jika file belum ada → buat default admin + struktur lengkap
if not os.path.exists(FILE):
    data = {
        "admin": {"username": "admin", "password": "admin123"},
        "users": [],
        "pendaftaran": []
    }
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)


def load_data():
    with open(FILE, "r") as f:
        data = json.load(f)

    # Jika "pendaftaran" hilang (file lama) → tambahkan
    if "pendaftaran" not in data:
        data["pendaftaran"] = []

    # Jika "users" hilang → tambahkan
    if "users" not in data:
        data["users"] = []

    return data


def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)
