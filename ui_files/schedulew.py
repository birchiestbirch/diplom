# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ScheduleWindow.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpinBox, QStatusBar,
    QTableWidget, QTableWidgetItem, QTimeEdit, QWidget)

class Ui_ScheduleWindow(object):
    def setupUi(self, ScheduleWindow):
        if not ScheduleWindow.objectName():
            ScheduleWindow.setObjectName(u"ScheduleWindow")
        ScheduleWindow.resize(796, 559)
        ScheduleWindow.setStyleSheet(u"background-color: rgb(120, 120, 120);")
        self.centralwidget = QWidget(ScheduleWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(120, 120, 120);\n"
"")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(290, 10, 191, 51))
        self.label.setStyleSheet(u"font-size: 26px;\n"
"background-color: rgb(50, 50, 50);\n"
"color: white;\n"
"padding: 8px 16px;\n"
"border-radius: 6px;\n"
"font-weight: 670;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(59, 70, 681, 91))
        self.frame.setStyleSheet(u"background-color: rgb(50, 50, 50)")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.timeEdit = QTimeEdit(self.frame)
        self.timeEdit.setObjectName(u"timeEdit")
        self.timeEdit.setGeometry(QRect(470, 10, 71, 31))
        self.timeEdit.setStyleSheet(u"QTimeEdit {\n"
"    background-color: #3a3a3a;\n"
"    border: 1px solid #1f1f1f;\n"
"    border-radius: 6px;\n"
"    padding: 6px;\n"
"    color: white;\n"
"    font-weight: 600;\n"
"}")
        self.timeEdit.setTime(QTime(0, 0, 0))
        self.actionEdit = QLineEdit(self.frame)
        self.actionEdit.setObjectName(u"actionEdit")
        self.actionEdit.setGeometry(QRect(20, 50, 641, 31))
        self.actionEdit.setStyleSheet(u"QLineEdit {\n"
"    background-color: #2f2f2f;\n"
"    border: 1px solid #1f1f1f;\n"
"    border-radius: 6px;\n"
"    padding: 8px;\n"
"    color: white;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #4CAF50;\n"
"}")
        self.addButton = QPushButton(self.frame)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setGeometry(QRect(550, 10, 111, 31))
        self.addButton.setStyleSheet(u"background-color: #4CAF50;\n"
"color: white;\n"
"font-size: 16px;\n"
"padding: 8px 16px;\n"
"border-radius: 6px;\n"
"font-weight: 670;\n"
"")
        self.weekdayCombo = QComboBox(self.frame)
        self.weekdayCombo.addItem("")
        self.weekdayCombo.addItem("")
        self.weekdayCombo.addItem("")
        self.weekdayCombo.addItem("")
        self.weekdayCombo.addItem("")
        self.weekdayCombo.addItem("")
        self.weekdayCombo.addItem("")
        self.weekdayCombo.addItem("")
        self.weekdayCombo.setObjectName(u"weekdayCombo")
        self.weekdayCombo.setGeometry(QRect(20, 10, 171, 31))
        self.weekdayCombo.setStyleSheet(u"QComboBox {\n"
"    background-color: #3a3a3a;\n"
"    border: 1px solid #1f1f1f;\n"
"    border-radius: 6px;\n"
"    padding: 6px 10px;\n"
"    color: white;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"")
        self.monthCombo = QComboBox(self.frame)
        self.monthCombo.addItem("")
        self.monthCombo.addItem("")
        self.monthCombo.addItem("")
        self.monthCombo.addItem("")
        self.monthCombo.addItem("")
        self.monthCombo.addItem("")
        self.monthCombo.addItem("")
        self.monthCombo.addItem("")
        self.monthCombo.addItem("")
        self.monthCombo.addItem("")
        self.monthCombo.addItem("")
        self.monthCombo.addItem("")
        self.monthCombo.addItem("")
        self.monthCombo.setObjectName(u"monthCombo")
        self.monthCombo.setGeometry(QRect(280, 10, 181, 31))
        self.monthCombo.setStyleSheet(u"QComboBox {\n"
"    background-color: #3a3a3a;\n"
"    border: 1px solid #1f1f1f;\n"
"    border-radius: 6px;\n"
"    padding: 6px 10px;\n"
"    color: white;\n"
"    font-weight: 600;\n"
"}\n"
"")
        self.daySpin = QSpinBox(self.frame)
        self.daySpin.setObjectName(u"daySpin")
        self.daySpin.setGeometry(QRect(200, 10, 71, 31))
        self.daySpin.setStyleSheet(u"QSpinBox {\n"
"    background-color: #3a3a3a;\n"
"    border: 1px solid #1f1f1f;\n"
"    border-radius: 6px;\n"
"    padding: 6px;\n"
"    color: white;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"QSpinBox:hover {\n"
"    background-color: #444444;\n"
"}\n"
"")
        self.daySpin.setMinimum(1)
        self.daySpin.setMaximum(31)
        self.daySpin.setValue(31)
        self.backButton = QPushButton(self.centralwidget)
        self.backButton.setObjectName(u"backButton")
        self.backButton.setGeometry(QRect(60, 490, 161, 41))
        self.backButton.setStyleSheet(u"background-color: rgb(50, 50, 50);\n"
"color: white;\n"
"font-size: 16px;\n"
"padding: 8px 16px;\n"
"border-radius: 6px;\n"
"font-weight: 670;\n"
"")
        self.QTableWidget = QTableWidget(self.centralwidget)
        if (self.QTableWidget.columnCount() < 4):
            self.QTableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.QTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.QTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.QTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.QTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.QTableWidget.setObjectName(u"QTableWidget")
        self.QTableWidget.setGeometry(QRect(60, 160, 681, 321))
        self.QTableWidget.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.QTableWidget.setStyleSheet(u"QTableWidget {\n"
"    background-color: #1e1e1e;\n"
"    color: white;\n"
"    gridline-color: #444;\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: #2b2b2b;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"}\n"
"")
        self.QTableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.QTableWidget.setAlternatingRowColors(True)
        self.QTableWidget.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.QTableWidget.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.QTableWidget.setShowGrid(False)
        self.QTableWidget.setColumnCount(4)
        self.QTableWidget.horizontalHeader().setStretchLastSection(True)
        self.QTableWidget.verticalHeader().setVisible(False)
        self.backButton_2 = QPushButton(self.centralwidget)
        self.backButton_2.setObjectName(u"backButton_2")
        self.backButton_2.setGeometry(QRect(320, 490, 161, 41))
        self.backButton_2.setStyleSheet(u"background-color: rgb(50, 50, 50);\n"
"color: white;\n"
"font-size: 16px;\n"
"padding: 8px 16px;\n"
"border-radius: 6px;\n"
"font-weight: 670;\n"
"")
        self.launchButton = QPushButton(self.centralwidget)
        self.launchButton.setObjectName(u"launchButton")
        self.launchButton.setGeometry(QRect(580, 490, 161, 41))
        self.launchButton.setStyleSheet(u"background-color: rgb(50, 50, 50);\n"
"color: white;\n"
"font-size: 16px;\n"
"padding: 8px 16px;\n"
"border-radius: 6px;\n"
"font-weight: 670;\n"
"")
        ScheduleWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(ScheduleWindow)
        self.statusbar.setObjectName(u"statusbar")
        ScheduleWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ScheduleWindow)

        QMetaObject.connectSlotsByName(ScheduleWindow)
    # setupUi

    def retranslateUi(self, ScheduleWindow):
        ScheduleWindow.setWindowTitle(QCoreApplication.translate("ScheduleWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("ScheduleWindow", u"\u0420\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.actionEdit.setPlaceholderText(QCoreApplication.translate("ScheduleWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u0435...", None))
        self.addButton.setText(QCoreApplication.translate("ScheduleWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.weekdayCombo.setItemText(0, QCoreApplication.translate("ScheduleWindow", u"MON", None))
        self.weekdayCombo.setItemText(1, QCoreApplication.translate("ScheduleWindow", u"TUE", None))
        self.weekdayCombo.setItemText(2, QCoreApplication.translate("ScheduleWindow", u"WED", None))
        self.weekdayCombo.setItemText(3, QCoreApplication.translate("ScheduleWindow", u"THU", None))
        self.weekdayCombo.setItemText(4, QCoreApplication.translate("ScheduleWindow", u"FRI", None))
        self.weekdayCombo.setItemText(5, QCoreApplication.translate("ScheduleWindow", u"SAT", None))
        self.weekdayCombo.setItemText(6, QCoreApplication.translate("ScheduleWindow", u"SUN", None))
        self.weekdayCombo.setItemText(7, QCoreApplication.translate("ScheduleWindow", u"*", None))

        self.monthCombo.setItemText(0, QCoreApplication.translate("ScheduleWindow", u"JAN", None))
        self.monthCombo.setItemText(1, QCoreApplication.translate("ScheduleWindow", u"FEB", None))
        self.monthCombo.setItemText(2, QCoreApplication.translate("ScheduleWindow", u"MAR", None))
        self.monthCombo.setItemText(3, QCoreApplication.translate("ScheduleWindow", u"APR", None))
        self.monthCombo.setItemText(4, QCoreApplication.translate("ScheduleWindow", u"MAY", None))
        self.monthCombo.setItemText(5, QCoreApplication.translate("ScheduleWindow", u"JUN", None))
        self.monthCombo.setItemText(6, QCoreApplication.translate("ScheduleWindow", u"JUL", None))
        self.monthCombo.setItemText(7, QCoreApplication.translate("ScheduleWindow", u"AUG", None))
        self.monthCombo.setItemText(8, QCoreApplication.translate("ScheduleWindow", u"SEN", None))
        self.monthCombo.setItemText(9, QCoreApplication.translate("ScheduleWindow", u"OCT", None))
        self.monthCombo.setItemText(10, QCoreApplication.translate("ScheduleWindow", u"NOV", None))
        self.monthCombo.setItemText(11, QCoreApplication.translate("ScheduleWindow", u"DEC", None))
        self.monthCombo.setItemText(12, QCoreApplication.translate("ScheduleWindow", u"*", None))

        self.backButton.setText(QCoreApplication.translate("ScheduleWindow", u"\u041d\u0430\u0437\u0430\u0434", None))
        ___qtablewidgetitem = self.QTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("ScheduleWindow", u"ID", None));
        ___qtablewidgetitem1 = self.QTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("ScheduleWindow", u"\u0414\u0430\u0442\u0430", None));
        ___qtablewidgetitem2 = self.QTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("ScheduleWindow", u"\u0412\u0440\u0435\u043c\u044f", None));
        ___qtablewidgetitem3 = self.QTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("ScheduleWindow", u"\u0414\u0435\u0439\u0441\u0442\u0432\u0438\u0435", None));
        self.backButton_2.setText(QCoreApplication.translate("ScheduleWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.launchButton.setText(QCoreApplication.translate("ScheduleWindow", u"\u0417\u0430\u043f\u0443\u0441\u043a", None))
    # retranslateUi

