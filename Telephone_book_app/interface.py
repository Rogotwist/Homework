import tkinter as tk
from tkinter import ttk
import app_logic


def add_contact_button_clicked():
    f_name = name_entry.get()
    l_name = surname_entry.get()
    telephone = phone_entry.get()
    address = address_entry.get()

    contact = app_logic.add_contact(f_name, l_name, telephone, address)
    app_logic.open_file(contact)



if __name__ == "__main__":
    # Создание окна приложения
    root = tk.Tk()
    root.title("Телефонная книга")

    # Создание полей для ввода
    name_label = tk.Label(root, text="Имя:")
    name_entry = tk.Entry(root)

    surname_label = tk.Label(root, text="Фамилия:")
    surname_entry = tk.Entry(root)

    phone_label = tk.Label(root, text="Телефон:")
    phone_entry = tk.Entry(root)

    address_label = tk.Label(root, text="Адрес:")
    address_entry = tk.Entry(root)

    # Создание кнопок
    add_button = tk.Button(root, text="Добавить контакт", command=add_contact_button_clicked)
    update_button = tk.Button(root, text="Изменить контакт")
    delete_button = tk.Button(root, text="Удалить контакт")
    refresh_button = tk.Button(root, text="Обновить список")
    separator = tk.Label(root, text="")

    # Создание таблицы для отображения списка контактов
    columns = ("Имя", "Фамилия", "Телефон", "Адрес")
    contact_list = ttk.Treeview(root, columns=columns, show="headings")

    # Задаем заголовки таблицы
    for col in columns:
        contact_list.heading(col, text=col)
        contact_list.column(col, width=100)  # Ширина колонок

    # Размещение элементов на форме
    name_label.grid(row=0, column=0)
    name_entry.grid(row=0, column=1)
    surname_label.grid(row=1, column=0)
    surname_entry.grid(row=1, column=1)
    phone_label.grid(row=2, column=0)
    phone_entry.grid(row=2, column=1)
    address_label.grid(row=3, column=0)
    address_entry.grid(row=3, column=1)

    add_button.grid(row=4, column=0, pady=5)
    update_button.grid(row=4, column=1, pady=5)
    delete_button.grid(row=5, column=0, pady=5)
    refresh_button.grid(row=5, column=1, pady=5)

    separator.grid(row=6, column=0, columnspan=2, pady=10)

    contact_list.grid(row=7, column=0, columnspan=2)

    # Запуск главного цикла приложения
    root.mainloop()

