import sys

from pytube import YouTube
from sys import argv
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_main import Ui_MainWindow
import os


def download_on_link(download_link, input_dest):
    """
    Загрузка видео по ссылке в папку download_yt
    :return:
    """
    yt = YouTube(download_link)

    print('Title: ', yt.title)
    print('View: ', yt.views)

    yd = yt.streams.get_highest_resolution()
    yd.download(input_dest)


class DownloadLink(QMainWindow):
    def __init__(self):
        super(DownloadLink, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Download_button.clicked.connect(self.button_clicked)
        self.ui.exit_button.clicked.connect(self.close)

    def button_clicked(self):
        download_link = self.ui.input_link.text()
        input_dest = self.ui.input_path.text()
        download_on_link(download_link, input_dest)
        print('В процессе')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DownloadLink()
    window.show()
