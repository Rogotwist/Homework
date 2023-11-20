import sys
from pytube import YouTube
from sys import argv
from PyQt5.QtCore import Qt, QThread, QObject, pyqtSignal
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_main import Ui_MainWindow
import os





class main_wiget(QMainWindow):

    def __init__(self):
        super(main_wiget, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Download_button.clicked.connect(self.button_clicked)
        self.ui.Info_button.clicked.connect(self.descryption_video)
        self.ui.exit_button.clicked.connect(self.close)
        self.ui.Download_bar.valueChanged.connect(self.update_progress)


    def download_on_link(self, download_link, input_dest):
        """
        Загрузка видео по ссылке в папку download_yt
        """
        yt = YouTube(download_link, on_progress_callback=self.update_progress)
        print('Title: ', yt.title)
        print('View: ', yt.views)
        yd = yt.streams.get_highest_resolution()
        yd.download(input_dest)


    def button_clicked(self):
        """
        Реализация функции работы кнопки загрузки
        :return:
        """
        download_link = self.ui.input_link.text()
        input_dest = self.ui.input_path.text()
        self.download_on_link(download_link, input_dest)
        print('В процессе')


    def descryption_video(self):
        """
        Функция отображения информации о видео
        :return:
        """
        try:
            # Создаем объект YouTube с использованием переданного URL
            download_link = self.ui.input_link.text()
            video = YouTube(download_link)

            # Получаем информацию о размере и формате видео
            video_size = video.streams.get_highest_resolution().filesize
            video_format = video.streams.get_highest_resolution().mime_type
            info = {
                'title': video.title,
                'author': video.author,
                'views': video.views,
                'duration': video.length,
                'size': video_size,
                'format': video_format
            }
            video_info = f"""
                Название видео: {info["title"]}
                Автор: {info["author"]}
                Просмотры: {info["views"]}
                Размер: {info["size"]}
                Формат видео: {info["format"]}
                """
            self.ui.Description_text.setPlainText(video_info)
        except Exception as e:
            return {'error': str(e)}

    def update_progress(self, stream, chunk=None, bytes_remaining=0):
        """
        Заполнение прогресс бара интерфейса
        """
        total_size = stream.filesize # почему то не находит атрибут размера файла
        bytes_downloaded = total_size - bytes_remaining
        progress = int(bytes_downloaded / total_size * 100)

        self.ui.Download_bar.setValue(progress)


if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        widget = main_wiget()
        widget.show()
        sys.exit(app.exec())
    except Exception as e:
        print(f"An error occurred: {e}")
