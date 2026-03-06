# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainMenu2.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 482)
        MainWindow.setStyleSheet(u"background-color: rgb(120, 120, 120)")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(60, 50, 681, 201))
        self.frame.setStyleSheet(u"background-color: rgb(0, 0, 0)")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayoutWidget = QWidget(self.frame)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 681, 201))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.RAMLabel = QLabel(self.gridLayoutWidget)
        self.RAMLabel.setObjectName(u"RAMLabel")
        font = QFont()
        font.setPointSize(13)
        font.setWeight(QFont.Black)
        self.RAMLabel.setFont(font)
        self.RAMLabel.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(250, 250, 250);\n"
"padding-left: 5px;\n"
"padding-bottom: 4px")

        self.gridLayout.addWidget(self.RAMLabel, 3, 0, 1, 1)

        self.CPULabel = QLabel(self.gridLayoutWidget)
        self.CPULabel.setObjectName(u"CPULabel")
        self.CPULabel.setFont(font)
        self.CPULabel.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(250, 250, 250);\n"
"padding-left: 5px;\n"
"padding-bottom: 3px")

        self.gridLayout.addWidget(self.CPULabel, 1, 0, 1, 1)

        self.SSDLabel = QLabel(self.gridLayoutWidget)
        self.SSDLabel.setObjectName(u"SSDLabel")
        self.SSDLabel.setFont(font)
        self.SSDLabel.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(250, 250, 250);\n"
"padding-left: 5px;\n"
"padding-bottom: 4px")

        self.gridLayout.addWidget(self.SSDLabel, 2, 0, 1, 1)

        self.StatusLabel = QLabel(self.gridLayoutWidget)
        self.StatusLabel.setObjectName(u"StatusLabel")
        self.StatusLabel.setFont(font)
        self.StatusLabel.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(250, 250, 250);\n"
"padding-left: 5px;\n"
"padding-bottom: 3px")

        self.gridLayout.addWidget(self.StatusLabel, 0, 0, 1, 1)

        self.StartButton = QPushButton(self.centralwidget)
        self.StartButton.setObjectName(u"StartButton")
        self.StartButton.setGeometry(QRect(70, 380, 51, 51))
        font1 = QFont()
        font1.setWeight(QFont.Thin)
        self.StartButton.setFont(font1)
        self.StartButton.setStyleSheet(u"background-color: transparent;\n"
"border: none;\n"
"color: transparent;")
        icon = QIcon()
        icon.addFile(u"green-circle.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.StartButton.setIcon(icon)
        self.StartButton.setIconSize(QSize(48, 48))
        self.ShutdownButton = QPushButton(self.centralwidget)
        self.ShutdownButton.setObjectName(u"ShutdownButton")
        self.ShutdownButton.setGeometry(QRect(150, 380, 51, 51))
        self.ShutdownButton.setStyleSheet(u"background-color: transparent;\n"
"border: none;\n"
"color: transparent;")
        icon1 = QIcon()
        icon1.addFile(u"red-circle.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ShutdownButton.setIcon(icon1)
        self.ShutdownButton.setIconSize(QSize(48, 48))
        self.RestartButton = QPushButton(self.centralwidget)
        self.RestartButton.setObjectName(u"RestartButton")
        self.RestartButton.setGeometry(QRect(230, 380, 51, 51))
        self.RestartButton.setStyleSheet(u"background-color: transparent;\n"
"border: none;\n"
"color: transparent;")
        icon2 = QIcon()
        icon2.addFile(u"yellow-circle.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.RestartButton.setIcon(icon2)
        self.RestartButton.setIconSize(QSize(48, 48))
        self.ConsoleButton = QPushButton(self.centralwidget)
        self.ConsoleButton.setObjectName(u"ConsoleButton")
        self.ConsoleButton.setGeometry(QRect(570, 380, 171, 51))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.ConsoleButton.setFont(font2)
        self.ConsoleButton.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(250, 250, 250);")
        self.ScheduleButton = QPushButton(self.centralwidget)
        self.ScheduleButton.setObjectName(u"ScheduleButton")
        self.ScheduleButton.setGeometry(QRect(330, 380, 171, 51))
        self.ScheduleButton.setFont(font2)
        self.ScheduleButton.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(250, 250, 250);")
        self.MoreButton = QPushButton(self.centralwidget)
        self.MoreButton.setObjectName(u"MoreButton")
        self.MoreButton.setGeometry(QRect(60, 270, 141, 41))
        font3 = QFont()
        font3.setPointSize(11)
        font3.setBold(True)
        self.MoreButton.setFont(font3)
        self.MoreButton.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(250, 250, 250);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.RAMLabel.setText(QCoreApplication.translate("MainWindow", u"RAM:", None))
        self.CPULabel.setText(QCoreApplication.translate("MainWindow", u"CPU:", None))
        self.SSDLabel.setText(QCoreApplication.translate("MainWindow", u"SSD:", None))
        self.StatusLabel.setText(QCoreApplication.translate("MainWindow", u"Status:", None))
        self.StartButton.setText("")
        self.ShutdownButton.setText("")
        self.RestartButton.setText("")
        self.ConsoleButton.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0441\u043e\u043b\u044c", None))
        self.ScheduleButton.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.MoreButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0440\u043e\u0431\u043d\u0435\u0435...", None))
    # retranslateUi

