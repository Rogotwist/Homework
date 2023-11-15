# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(624, 308)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(253, 195, 0, 255), stop:0.427447 rgba(217, 7, 46, 255), stop:0.427447 rgba(217, 7, 46, 255) , stop:1 rgba(253, 195, 0, 255));\n"
"font-color: rgb(255, 255, 255);\n"
"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.main_frame_2 = QFrame(self.centralwidget)
        self.main_frame_2.setObjectName(u"main_frame_2")
        self.main_frame_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"\n"
"")
        self.verticalLayout_2 = QVBoxLayout(self.main_frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.description_to_load = QLabel(self.main_frame_2)
        self.description_to_load.setObjectName(u"description_to_load")
        font = QFont()
        font.setFamilies([u"Sans Serif Collection"])
        font.setPointSize(13)
        self.description_to_load.setFont(font)
        self.description_to_load.setStyleSheet(u"color: white;\n"
"font-size: 13pt;\n"
"background-color: none;\n"
"border: none;")
        self.description_to_load.setMargin(5)

        self.verticalLayout_2.addWidget(self.description_to_load)

        self.input_link = QLineEdit(self.main_frame_2)
        self.input_link.setObjectName(u"input_link")
        font1 = QFont()
        font1.setFamilies([u"Sans Serif Collection"])
        font1.setPointSize(10)
        self.input_link.setFont(font1)
        self.input_link.setStyleSheet(u"color: white;\n"
"font-size: 10pt;\n"
"padding-left: 10px;")

        self.verticalLayout_2.addWidget(self.input_link)

        self.description_to_path = QLabel(self.main_frame_2)
        self.description_to_path.setObjectName(u"description_to_path")
        self.description_to_path.setFont(font)
        self.description_to_path.setStyleSheet(u"color: white;\n"
"font-size: 13pt;\n"
"background-color: none;\n"
"border: none;")
        self.description_to_path.setMargin(5)

        self.verticalLayout_2.addWidget(self.description_to_path)

        self.input_path = QLineEdit(self.main_frame_2)
        self.input_path.setObjectName(u"input_path")
        self.input_path.setFont(font1)
        self.input_path.setCursor(QCursor(Qt.IBeamCursor))
        self.input_path.setMouseTracking(True)
        self.input_path.setStyleSheet(u"color: white;\n"
"font-size: 10pt;\n"
"padding-left: 10px;")

        self.verticalLayout_2.addWidget(self.input_path)

        self.Download_button = QPushButton(self.main_frame_2)
        self.Download_button.setObjectName(u"Download_button")
        font2 = QFont()
        font2.setFamilies([u"Sans Serif Collection"])
        font2.setBold(True)
        self.Download_button.setFont(font2)
        self.Download_button.setStyleSheet(u"color: white;")

        self.verticalLayout_2.addWidget(self.Download_button)

        self.exit_button = QPushButton(self.main_frame_2)
        self.exit_button.setObjectName(u"exit_button")
        self.exit_button.setFont(font2)
        self.exit_button.setStyleSheet(u"color: white;")

        self.verticalLayout_2.addWidget(self.exit_button)


        self.verticalLayout.addWidget(self.main_frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Downloader YouTube videos", None))
        self.description_to_load.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0442\u0430\u0432\u044c\u0442\u0435 \u0441\u0441\u044b\u043b\u043a\u0443 \u0441\u043a\u0430\u0447\u0438\u0432\u0430\u0435\u043c\u043e\u0433\u043e \u0432\u0438\u0434\u0435\u043e", None))
        self.input_link.setText("")
        self.input_link.setPlaceholderText(QCoreApplication.translate("MainWindow", u"https://www.youtube.com/watch-code-video", None))
        self.description_to_path.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043f\u0443\u0442\u044c \u0437\u0430\u0433\u0440\u0443\u0437\u043a\u0438 \u0432\u0438\u0434\u0435\u043e ", None))
        self.input_path.setText("")
        self.input_path.setPlaceholderText(QCoreApplication.translate("MainWindow", u"C:\\Users\\User\\Desktop\\Download", None))
        self.Download_button.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430", None))
        self.exit_button.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
    # retranslateUi

