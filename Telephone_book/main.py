import json
import os
import sys
from PySide6.QtCore import Qt, QAbstractTableModel, QModelIndex
from PySide6.QtWidgets import QApplication, QTableView, QVBoxLayout, QWidget, QMessageBox, QMainWindow, QHeaderView
from PySide6.QtGui import QStandardItemModel, QStandardItem
from ui_main import Ui_MainWindow


class TelephoneBook(QMainWindow):

    def __init__(self):
        super(TelephoneBook, self).__init__()
        self.list_contact = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.add_button.clicked.connect(self.add_clicked)
        self.ui.delete_button.clicked.connect(self.delete_selected_row)
        self.ui.exit_button.clicked.connect(self.close)

        # Создаем модель данных
        self.model = QStandardItemModel(self)
        self.ui.tableView.setModel(self.model)

        # Вызываем метод для загрузки данных из файла и отображения их в таблице
        self.initialize()

    def delete_selected_row(self):
        selected_indexes = self.ui.tableView.selectionModel().selectedRows()
        if selected_indexes:
            row_to_remove = selected_indexes[0].row()
            self.model.removeRow(row_to_remove)

            top_left = self.model.index(row_to_remove, 0)
            bottom_right = self.model.index(row_to_remove, self.model.columnCount() - 1)
            self.model.dataChanged.emit(top_left, bottom_right)
            self.list_contact = self.get_data_from_model()
            self.save_data()


    def input_data(self):
        data = {
            "Имя": self.ui.Edit_name.text(),
            "Фамилия": self.ui.Edit_last_name.text(),
            "Телефон": self.ui.Edit_telephone.text(),
            "Адрес": self.ui.Edit_addres.text()
        }
        return data

    def add_clicked(self):
        if self.list_contact is None:
            self.list_contact = []
        data = self.input_data()
        self.list_contact.append(data)
        self.save_data()
        self.initialize()

    def initialize(self):
        file_name = 'data.json'

        if os.path.exists(file_name):
            print("Загрузка данных")
            with open(file_name, 'r') as create:
                self.list_contact = json.load(create)
                self.display_data_in_table(self.list_contact)
                self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        else:
            print("Файл не найден")
            self.list_contact = []

    def save_data(self):
        file_name = 'data.json'
        print("Сохранение данных")
        with open(file_name, 'w') as save:
            json.dump(self.list_contact, save)

    def get_data_from_model(self):
        data = []
        for row in range(self.model.rowCount()):
            row_data = {}
            for col in range(self.model.columnCount()):
                index = self.model.index(row, col)
                header = self.model.headerData(col, Qt.Horizontal)
                row_data[header] = str(index.data())
            data.append(row_data)
        return data

    def display_data_in_table(self, data):
        # Очищаем модель перед отображением новых данных
        self.model.clear()

        # Определяем заголовки столбцов
        headers = ["Имя", "Фамилия", "Телефон", "Адрес"]

        # Устанавливаем заголовки столбцов в модель
        self.model.setHorizontalHeaderLabels(headers)

        # Заполняем модель данными
        for row, contact in enumerate(data):
            for col, key in enumerate(headers):
                item = QStandardItem(str(contact.get(key, '')))
                self.model.setItem(row, col, item)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TelephoneBook()
    window.show()

    sys.exit(app.exec())
