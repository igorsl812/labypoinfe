# TODO решите задачу
import json
with open('input.json') as file:
    json_data = json.load(file)
def task(json_data):
    total = 0.0
    for item in json_data:
        if isinstance(item, dict) and "score" in item and "weight" in item:
            total += item["score"] * item["weight"]
    return round(total, 3)

print(task(json_data))
