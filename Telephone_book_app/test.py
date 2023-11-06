import os
import json

def open_file(data):
    """
    Открывает файл \ создает файл при первом открытии -> берет все данные файла -> Закрывает файл
    :return: Данные файла в виде списка-словарей
    """
    filepath = "data.json"
    try:
        with open(filepath, "r") as json_file:
            load_data = json.load(json_file)
        return load_data
    except FileNotFoundError:
        # Если файл не существует, создаем новый и записываем в него данные по умолчанию
        if data is not None:
            with open(filepath, 'w') as json_file:
                json.dump(data, json_file)
            return data
        else:
            # Если нет данных по умолчанию, просто возвращаем None
            return None

print(open_file(data))


