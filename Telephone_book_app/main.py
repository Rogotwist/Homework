import os
import json



def add_contact(f_name, l_name, telephone, addres):
    """
    Запись информации о контакте в БД

    :param f_name: Данные берутся из полей ввода интерфейса
    :param l_name:
    :param telephone:
    :param addres:
    :return: возвращает словарь данных
    """


    pass


def view_contacts():
    """
    Отображение контактов в интерфейсе программы
    :return:
    """
    pass


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


def open_file():
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
        with open(filepath, 'w') as json_file:
            print('Файл создан')
def main():
    num = 0
    print(f"""
        Приветствую , это записная книга для ваших контактов 
        На данный момент существует {num} записи\ей
    """)

    pass

main()


