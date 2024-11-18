import json

def task() -> float:
    with open('input.json', 'r') as file:
        data = json.load(file)

    return round(sum(item["score"] * item["weight"] for item in data), 3)



print(task())
