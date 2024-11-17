import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, newline='', encoding='utf-8') as csvfile:
        reader=csv.DictReader(csvfile)
        result=[i for i in reader]
    with open(OUTPUT_FILENAME, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
