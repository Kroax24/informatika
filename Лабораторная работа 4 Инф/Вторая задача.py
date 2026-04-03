# TODO импортировать необходимые молули
import csv                          # Подключаем библиотеки
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:                                               # TODO считать содержимое csv файла
    with open(INPUT_FILENAME, mode="r", encoding="utf-8") as f:   # Открываем файл для чтения csv
        reader = csv.DictReader(f)                          # Создаем объект, который превращает каждую строку в словарь
        data = [row for row in reader]                      # Собираем все словари в общий список
    # TODO Сериализовать в файл с отступами равными 4
    with open(OUTPUT_FILENAME, mode="w", encoding="utf-8") as f:  # Открываем json файл для записи
        json.dump(data, f, indent=4, ensure_ascii=False)       # Записываем список словарей в файл в правильном формате


if __name__ == '__main__':
    # Нужно для проверки
    task()                                                    # Вызываем функцию

    with open(OUTPUT_FILENAME) as output_f:                   # Открываем файл для проверки результата
        for line in output_f:                                 # Проходимся циклом по каждой строке получившегося файла
            print(line, end="")                               # Выводим ответ
