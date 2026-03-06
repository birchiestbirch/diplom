# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ConsoleWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QSizePolicy, QStatusBar, QTextEdit, QWidget)

class Ui_ConsoleWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(792, 600)
        MainWindow.setStyleSheet(u"background-color: rgb(120, 120, 120)")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.consoleOutput = QTextEdit(self.centralwidget)
        self.consoleOutput.setObjectName(u"consoleOutput")
        self.consoleOutput.setGeometry(QRect(60, 70, 681, 391))
        self.consoleOutput.setStyleSheet(u"QTextEdit {\n"
"    background-color: #000000;\n"
"    color: #00ff00;\n"
"    font-family: Consolas, \"Courier New\", monospace;\n"
"    font-size: 14px;\n"
"    border: none;\n"
"}\n"
"")
        self.consoleOutput.setUndoRedoEnabled(False)
        self.consoleOutput.setLineWrapMode(QTextEdit.LineWrapMode.NoWrap)
        self.consoleOutput.setReadOnly(True)
        self.commandInput = QLineEdit(self.centralwidget)
        self.commandInput.setObjectName(u"commandInput")
        self.commandInput.setGeometry(QRect(60, 480, 681, 41))
        self.commandInput.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(50, 50, 50);\n"
"    color: white;\n"
"    font-family: Consolas, \"Courier New\", monospace;\n"
"    font-size: 14px;\n"
"    padding: 6px;\n"
"    border: 1px solid #444;\n"
"}\n"
"")
        self.commandInput.setClearButtonEnabled(True)
        self.consoleLabel = QLabel(self.centralwidget)
        self.consoleLabel.setObjectName(u"consoleLabel")
        self.consoleLabel.setGeometry(QRect(310, 10, 161, 51))
        self.consoleLabel.setStyleSheet(u"font-size: 26px;\n"
"background-color: rgb(50, 50, 50);\n"
"color: white;\n"
"padding: 8px 16px;\n"
"border-radius: 6px;\n"
"font-weight: 670;\n"
"")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.commandInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043a\u043e\u043c\u0430\u043d\u0434\u0443...", None))
        self.consoleLabel.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0441\u043e\u043b\u044c", None))
    # retranslateUi

