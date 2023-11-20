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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QProgressBar, QPushButton,
    QSizePolicy, QTextBrowser, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(624, 481)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(253, 195, 0, 255), stop:0.427447 rgba(217, 7, 46, 255), stop:0.427447 rgba(217, 7, 46, 255) , stop:1 rgba(253, 195, 0, 255));\n"
"font-color: rgb(255, 255, 255);\n"
"")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.main_frame_2 = QFrame(self.centralwidget)
        self.main_frame_2.setObjectName(u"main_frame_2")
        self.main_frame_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"\n"
"")
        self.verticalLayout_5 = QVBoxLayout(self.main_frame_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
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

        self.verticalLayout.addWidget(self.description_to_load)

        self.input_link = QLineEdit(self.main_frame_2)
        self.input_link.setObjectName(u"input_link")
        font1 = QFont()
        font1.setFamilies([u"Sans Serif Collection"])
        font1.setPointSize(10)
        self.input_link.setFont(font1)
        self.input_link.setStyleSheet(u"color: white;\n"
"font-size: 10pt;\n"
"padding-left: 10px;")

        self.verticalLayout.addWidget(self.input_link)

        self.description_to_path = QLabel(self.main_frame_2)
        self.description_to_path.setObjectName(u"description_to_path")
        self.description_to_path.setFont(font)
        self.description_to_path.setStyleSheet(u"color: white;\n"
"font-size: 13pt;\n"
"background-color: none;\n"
"border: none;")
        self.description_to_path.setMargin(5)

        self.verticalLayout.addWidget(self.description_to_path)

        self.input_path = QLineEdit(self.main_frame_2)
        self.input_path.setObjectName(u"input_path")
        self.input_path.setFont(font1)
        self.input_path.setCursor(QCursor(Qt.IBeamCursor))
        self.input_path.setMouseTracking(True)
        self.input_path.setStyleSheet(u"color: white;\n"
"font-size: 10pt;\n"
"padding-left: 10px;")

        self.verticalLayout.addWidget(self.input_path)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.Description_text = QTextBrowser(self.main_frame_2)
        self.Description_text.setObjectName(u"Description_text")
        self.Description_text.setStyleSheet(u"color: white;\n"
"font-size: 18pt;")

        self.verticalLayout_3.addWidget(self.Description_text)

        self.Info_button = QPushButton(self.main_frame_2)
        self.Info_button.setObjectName(u"Info_button")
        font2 = QFont()
        font2.setBold(True)
        self.Info_button.setFont(font2)
        self.Info_button.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent; /* \u041f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u044b\u0439 \u0444\u043e\u043d */\n"
"    border: 2px solid rgba(255, 255, 175, 65);  \n"
"    color: white; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 \u0437\u0435\u043b\u0435\u043d\u044b\u0439 */\n"
"    font-size: 16px; /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    transition: background-color 0.3s ease; /* \u041f\u043b\u0430\u0432\u043d\u043e\u0435 \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u0435 \u0446\u0432\u0435\u0442\u0430 \u0444\u043e\u043d\u0430 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 255, 175, 65); /* \u041f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u044b\u0439 \u0437\u0435\u043b\u0435\u043d\u044b\u0439 \u0444\u043e\u043d \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"    color: white; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 \u0437\u0435"
                        "\u043b\u0435\u043d\u044b\u0439 */\n"
"}")

        self.verticalLayout_3.addWidget(self.Info_button)


        self.horizontalLayout.addLayout(self.verticalLayout_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.Download_bar = QProgressBar(self.main_frame_2)
        self.Download_bar.setObjectName(u"Download_bar")
        self.Download_bar.setStyleSheet(u"")
        self.Download_bar.setValue(24)
        self.Download_bar.setAlignment(Qt.AlignCenter)
        self.Download_bar.setTextDirection(QProgressBar.TopToBottom)

        self.verticalLayout_4.addWidget(self.Download_bar)

        self.Download_button = QPushButton(self.main_frame_2)
        self.Download_button.setObjectName(u"Download_button")
        font3 = QFont()
        font3.setFamilies([u"Sans Serif Collection"])
        font3.setBold(True)
        self.Download_button.setFont(font3)
        self.Download_button.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent; /* \u041f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u044b\u0439 \u0444\u043e\u043d */\n"
"    border: 2px solid rgba(255, 255, 175, 65);  \n"
"    color: white; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 \u0437\u0435\u043b\u0435\u043d\u044b\u0439 */\n"
"    font-size: 16px; /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    transition: background-color 0.3s ease; /* \u041f\u043b\u0430\u0432\u043d\u043e\u0435 \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u0435 \u0446\u0432\u0435\u0442\u0430 \u0444\u043e\u043d\u0430 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 255, 175, 65); /* \u041f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u044b\u0439 \u0437\u0435\u043b\u0435\u043d\u044b\u0439 \u0444\u043e\u043d \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"    color: white; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 \u0437\u0435"
                        "\u043b\u0435\u043d\u044b\u0439 */\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.Download_button)

        self.exit_button = QPushButton(self.main_frame_2)
        self.exit_button.setObjectName(u"exit_button")
        self.exit_button.setFont(font3)
        self.exit_button.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent; /* \u041f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u044b\u0439 \u0444\u043e\u043d */\n"
"    border: 2px solid rgba(255, 255, 175, 65);  \n"
"    color: white; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 \u0437\u0435\u043b\u0435\u043d\u044b\u0439 */\n"
"    font-size: 16px; /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    transition: background-color 0.3s ease; /* \u041f\u043b\u0430\u0432\u043d\u043e\u0435 \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u0435 \u0446\u0432\u0435\u0442\u0430 \u0444\u043e\u043d\u0430 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 255, 175, 65); /* \u041f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u044b\u0439 \u0437\u0435\u043b\u0435\u043d\u044b\u0439 \u0444\u043e\u043d \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"    color: white; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 \u0437\u0435"
                        "\u043b\u0435\u043d\u044b\u0439 */\n"
"}")

        self.verticalLayout_4.addWidget(self.exit_button)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)


        self.verticalLayout_2.addWidget(self.main_frame_2)

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
        self.Description_text.setMarkdown(QCoreApplication.translate("MainWindow", u"******\n"
"\n"
"", None))
        self.Description_text.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /"
                        "></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">******</p></body></html>", None))
        self.Info_button.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044e", None))
        self.Download_button.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430", None))
        self.exit_button.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
    # retranslateUi

