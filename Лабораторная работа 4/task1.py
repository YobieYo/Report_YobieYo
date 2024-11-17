# TODO решите задачу
import json

def task() -> float:
    with open('input.json', 'r') as file:
        data = json.load(file)

    total_sum = 0.0

    for i in data:
        score=i.get('score',0)
        weight = i.get('weight', 0)
        total_sum += score*weight

    return round(total_sum,3)



print(task())
