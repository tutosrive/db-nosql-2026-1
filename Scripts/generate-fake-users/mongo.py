from faker import Faker
import random as rd
import json

fk = Faker()

folder = "./data"
age_range = [18, 65]
data = []

for i in range(1, 100000):
    male = True if (i % 2 == 0) else False
    data.append(
        {
            "id": i,
            "name": fk.name_male() if male else fk.name_female(),
            "job": fk.job_male() if male else fk.job_female(),
            "age": rd.randint(age_range[0], age_range[1]),
            "city": fk.city(),
            "email": fk.email(True),
            "company": fk.company(),
            "username": fk.user_name()
        }
    )


with open(f"{folder}/users.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)