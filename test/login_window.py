from PySide6.QtWidgets import QApplication, QMainWindow  # Импортируем нужные вещи из PySide6
from ui_files.login import Ui_Dialog  # Импортируем файл с разметкой пользовательского интерфейса
import sys, threading  # Необходимые библиотеки для потоков и системных процессов

class user_dialog(QMainWindow):
    """
    Класс с окном выбора сервера
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ip = ""
        self.api = ""

        def get_data():
            """
            Функция собирает данные и записывает его в текстовый файл, попутно запуская основную программу
            :return:
            """
            if self.ui.lineEdit.text() != "example.com или 192.168.1.10" and self.ui.lineEdit_2.text() != "Введите API ключ":
                if self.ui.lineEdit.text() != "" and self.ui.lineEdit_2.text() != "":

                    self.ip = self.ui.lineEdit.text()
                    self.api = self.ui.lineEdit_2.text()
                    with open('D:/data', 'a', encoding='utf-8') as file:
                        text = file.read()
                        if text == "":
                            file.write(self.ip+'\n')
                            file.write(self.api+'\n')
                            print(self.ip, self.api)
                        elif text != "":
                            text = file.read()
                            print(text)

        def close_window():
            self.close()

        self.ui.okButton.clicked.connect(get_data)
        self.ui.cancelButton.clicked.connect(close_window)

if __name__ == "__main__":
    app = QApplication()
    root = user_dialog()
    root.show()
    sys.exit(app.exec())