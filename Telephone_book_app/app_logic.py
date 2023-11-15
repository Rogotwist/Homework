import os
import json


def load_data_start(list_contacts):
    for file in os.listdir(os.getcwd()):
        if file == 'data.json':
            with open(file, 'r') as json_file:
                load_data = json.load(json_file)
                list_contacts.append(load_data)
                print('Данные обновлены!')
                print(list_contacts)


def add_contact(f_name, l_name, telephone, address):
    """
    Запись информации о контакте в БД

    :param f_name: Данные берутся из полей ввода интерфейса
    :param l_name:
    :param telephone:
    :param addres:
    :return: возвращает словарь данных
    """
    full_address = address
    city = full_address.split(', ')
    contact = {
        'Name': f_name,
        'Last Name': l_name,
        'Telephone': telephone,
        'Address': address[1:],
        'City': city[0]
    }
    return contact


def change_contact():
    """
    Изменяет информацию выбранного контакта
    :return:
    """
    pass


def delete_contact():
    """Удаление выбранного контакта """

    pass


def search_contact():
    """
    Поиск по базе контактов ( имя, фамилия, телефон, адрес)
    :return:
    """


def open_file(data, list_contacts):
    """
    Открывает файл \ создает файл при первом открытии -> берет все данные файла -> Закрывает файл
    :return: Данные файла в виде списка-словарей
    """
    filepath = "data.json"
    print(data)
    if not data:
        try:
            with open(filepath, "r") as json_file:
                load_data = json.load(json_file)
                list_contacts.append(load_data)
                print(list_contacts)
            return list_contacts
        except FileNotFoundError:
            # Если файл не существует, создаем новый и записываем в него данные по умолчанию
            with open(filepath, 'w') as json_file:
                print('Файл создан, запись обновлена')
                json.dump(data, json_file)
    else:
        with open(filepath, "w") as json_file:
            list_contacts.append(data)
            json.dump(list_contacts, json_file)
def main():
    num = 0
    print(f"""
        Приветствую , это записная книга для ваших контактов 
        На данный момент существует {num} записи\ей
    """)

    pass

main()


