import json

#1
participant = {
    "Имя": "Алексей",
    "Группа": "КБ-101",
    "Навыки": ["Python", "Excel"],
    "Уведомления": True
    }

#2
with open("participant.json", "w", encoding="utf-8") as file:
    json.dump(participant, file, ensure_ascii=False, indent=4)

#3
with open("participant.json", "r", encoding="utf-8") as file:
    p = json.load(file)

#4
p["Навыки"].append("CSV")
p["Уведомления"] = False

#5
with open("participant.json", "w", encoding="utf-8") as file:
    json.dump(p, file, ensure_ascii=False, indent=4)
with open("participant.json", "r", encoding="utf-8") as file:
    fp = json.load(file)
for key, value in fp.items():
    print(f"{key}: {value}")