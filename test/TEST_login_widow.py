from PySide6.QtWidgets import QApplication, QMainWindow  # Импортируем нужные вещи из PySide6
from oop_test import server  # Импортируем главный класс проекта, в котором и происходят все действия
from ui_files.login import Ui_Dialog  # Импортируем файл с разметкой пользовательского интерфейса
import sys, threading  # Необходимые библиотеки для потоков и системных процессов
import os # Модуль os для проверки наличия файла
from test_ui import user_interface as usi
from pydactyl import PterodactylClient  # Главная API проекта


class user_dialog(QMainWindow):
    """
    Класс окна авторизации. Отвечает за ввод адреса панели и API ключа,
    сохранение этих данных в файл и открытие главного окна программы.
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()  # Создаём объект интерфейса
        self.ui.setupUi(self)  # Настраиваем интерфейс согласно дизайну
        self.ip = ""  # Сюда сохраним IP после ввода
        self.api = ""  # Сюда сохраним API ключ после ввода

        def load_data_from_file():
            """
            Загружает данные из файла и вставляет их в поля ввода
            """
            file_path = 'data.txt'

            if os.path.exists(file_path):  # Проверяем, есть ли вообще файл
                with open(file_path, 'r', encoding='utf-8') as file:
                    lines = file.readlines()  # Читаем все строки
                    if len(lines) >= 2:  # Проверяем, что там хотя бы 2 строки
                        # Удаляем символы переноса строки
                        saved_ip = lines[0].strip()
                        saved_api = lines[1].strip()

                        # Вставляем данные в поля
                        self.ui.lineEdit.setText(saved_ip)
                        self.ui.lineEdit_2.setText(saved_api)
                        print("Данные загружены")

        # Загружаем данные из файла при запуске
        load_data_from_file()

        def get_data():
            """
            Функция собирает данные и записывает его в текстовый файл
            """
            ip_text = self.ui.lineEdit.text()
            api_text = self.ui.lineEdit_2.text()

            # Проверяем, не являются ли поля пустыми или содержащими текст-подсказку
            if ip_text != "example.com или 192.168.1.10" and api_text != "Введите API ключ":
                if ip_text != "" and api_text != "":
                    self.ip = ip_text
                    self.api = api_text

                    # Записываем данные в файл
                    with open('data.txt', 'w', encoding='utf-8') as file:
                        file.write(self.ip + '\n')
                        file.write(self.api + '\n')
                        print("Данные сохранены")

            # Создаём объект сервера с введёнными данными
            srv = server(PterodactylClient(f'{self.ui.lineEdit.text()}', f'{self.ui.lineEdit_2.text()}'))

            self.close()  # Закрываем окно авторизации

            # Открываем главное окно программы
            self.main_window = usi(srv)
            self.main_window.show()

        def close_window():
            """Закрывает окно без сохранения и входа"""
            self.close()

        # Привязываем кнопки к функциям
        self.ui.okButton.clicked.connect(get_data)  # Кнопка "ОК" - вход и сохранение
        self.ui.cancelButton.clicked.connect(close_window)  # Кнопка "Отмена" - просто закрыть окно


if __name__ == "__main__":
    app = QApplication()  # Создаём приложение
    root = user_dialog()  # Создаём окно авторизации
    root.show()  # Показываем окно
    sys.exit(app.exec())  # Запускаем главный цикл приложения