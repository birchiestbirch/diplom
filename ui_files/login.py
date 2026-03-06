# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ServerSettingsDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(545, 314)
        Dialog.setStyleSheet(u"background-color: #787878;\n"
"color: white;\n"
"font-size: 14px;")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 50, 181, 41))
        self.label.setStyleSheet(u"color: #e0e0e0;\n"
"    font-size: 15px;\n"
"    font-weight: 600;\n"
"    margin-top: 10px;\n"
"    margin-bottom: 4px;\n"
"background-color: #323232;")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 130, 181, 41))
        self.label_2.setStyleSheet(u"color: #e0e0e0;\n"
"    font-size: 15px;\n"
"    font-weight: 600;\n"
"    margin-top: 10px;\n"
"    margin-bottom: 4px;\n"
"background-color: #323232;")
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(70, 90, 401, 31))
        self.lineEdit.setStyleSheet(u"background-color: #1e1e1e;\n"
"    color: white;\n"
"    padding: 6px;\n"
"    border: 1px solid #444;\n"
"    border-radius: 4px;")
        self.lineEdit_2 = QLineEdit(Dialog)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(70, 170, 401, 31))
        self.lineEdit_2.setStyleSheet(u"background-color: #1e1e1e;\n"
"    color: white;\n"
"    padding: 6px;\n"
"    border: 1px solid #444;\n"
"    border-radius: 4px;")
        self.cancelButton = QPushButton(Dialog)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setGeometry(QRect(260, 220, 101, 31))
        self.cancelButton.setStyleSheet(u" background-color: #b53939;\n"
" border-color: #7a1f1f;\n"
"color: white;\n"
"    padding: 10px 20px;\n"
"    border-radius: 6px;\n"
"\n"
"\n"
"")
        self.okButton = QPushButton(Dialog)
        self.okButton.setObjectName(u"okButton")
        self.okButton.setGeometry(QRect(370, 220, 101, 31))
        self.okButton.setStyleSheet(u"background-color: #4CAF50;\n"
"color: white;\n"
"padding: 10px 20px;\n"
"border-radius: 6px;\n"
"")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0410\u0434\u0440\u0435\u0441 \u0441\u0435\u0440\u0432\u0435\u0440\u0430", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"API \u043a\u043b\u044e\u0447", None))
        self.lineEdit.setText(QCoreApplication.translate("Dialog", u"example.com \u0438\u043b\u0438 192.168.1.10", None))
        self.lineEdit_2.setText(QCoreApplication.translate("Dialog", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 API \u043a\u043b\u044e\u0447", None))
        self.cancelButton.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.okButton.setText(QCoreApplication.translate("Dialog", u"\u0413\u043e\u0442\u043e\u0432\u043e", None))
    # retranslateUi

