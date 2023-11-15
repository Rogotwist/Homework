from pytube import YouTube
from sys import argv
import os


def download_on_link():
    """
    Загрузка видео по ссылке в папку download_yt
    :return:
    """
    home_link = os.getcwd() + '\\download_Yt'


    link = 'https://www.youtube.com/watch?v=FbBXtqtRnWU&ab_channel=LeilaGharani'
    yt = YouTube(link)

    print('Title: ', yt.title)
    print('View: ', yt.views)

    yd = yt.streams.get_highest_resolution()
    yd.download(home_link)
