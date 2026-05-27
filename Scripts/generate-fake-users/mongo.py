import json
import os
import random as rd
from datetime import datetime
from faker import Faker

fk = Faker()
TOTAL_RECORDS = 50_000_000
OUTPUT_FILE = "./data/users.jsonl"

os.makedirs("./data", exist_ok=True)

def user_generator():
    """Generador que crea un usuario a la vez (ahorra RAM)."""
    countries = ["US", "DK", "FR", "ES", "BR", "CA", "DE"]

    for i in range(1, TOTAL_RECORDS + 1):
        male = i % 2 == 0
        gender = "male" if male else "female"
        first_name = fk.first_name_male() if male else fk.first_name_female()
        last_name = fk.last_name()
        pic_id = rd.randint(1, 99)
        gender_path = "men" if male else "women"

        yield {
            "gender": gender,
            "name": {
                "title": "mr" if male else "ms",
                "first": first_name.lower(),
                "last": last_name.lower(),
            },
            "location": {
                "street": f"{rd.randint(100, 9999)} {fk.street_name().lower()}",
                "city": fk.city().lower(),
                "state": fk.state().lower(),
                "postcode": rd.randint(10000, 99999),
                "coordinates": {
                    "latitude": f"{rd.uniform(-90, 90):.4f}",
                    "longitude": f"{rd.uniform(-180, 180):.4f}",
                },
                "timezone": {"offset": "+1:00", "description": "Europe/Madrid"},
            },
            "email": f"{first_name.lower()}.{last_name.lower()}@example.com",
            "login": {
                "uuid": fk.uuid4(),
                "username": f"{first_name.lower()}{rd.randint(10,999)}",
                "password": "password123",
                "salt": "salt",
                "md5": "md5hash",
                "sha1": "sha1hash",
                "sha256": "sha256hash",
            },
            "dob": {"date": "1990-01-01T00:00:00Z", "age": 36},
            "registered": {"date": "2020-01-01T00:00:00Z", "age": 6},
            "phone": "123-4567",
            "cell": "987-6543",
            "id": {"name": "DNI", "value": f"{rd.randint(100000,999999)}"},
            "picture": {
                "large": f"https://randomuser.me/api/portraits/{gender_path}/{pic_id}.jpg",
                "medium": f"https://randomuser.me/api/portraits/med/{gender_path}/{pic_id}.jpg",
                "thumbnail": f"https://randomuser.me/api/portraits/thumb/{gender_path}/{pic_id}.jpg",
            },
            "nat": rd.choice(countries),
        }


with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    for count, user in enumerate(user_generator(), 1):
        f.write(json.dumps(user, ensure_ascii=False) + "\n")

        if count % 500_000 == 0:
            print(f"Guardados {count:,} usuarios...")