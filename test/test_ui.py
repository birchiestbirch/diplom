from oop_test import server  # Импортируем главный класс проекта, в котором и происходят все вещи
from PySide6.QtWidgets import QApplication, QMainWindow  # Импортируем нужные вещи из PySide6
from ui_files.ui import Ui_MainWindow  # Импортируем файл с разметкой пользовательского интерфейса
from pydactyl import PterodactylClient  # Главная API проекта
import sys, threading  # Необходимые библиотеки для потоков и системных процессов
from test_plots import MonitoringWindow  # Импортируем окно с графиками
from TEST_console_window import console_window # Из файла с функционалом окна консоли импортируем окно консоли
from TEST_schedule_window import schedule_window # Из файла с функционалом окна расписаний импортируем окно расписаний

srv = server(PterodactylClient('https://mgr.legistale.net', 'ptlc_inD6oIpdBSLRC4zWHlnxyFV9fkefyUcSO3PAzy40wSH'))
# Создаём объект класса server, указывая URL и API-ключ для тестов

class user_interface(QMainWindow):
    """
    Основной класс приложения.
    Принимает объект класса PterodactylClient.
    Содержит главное окно с кнопками управления и отображением статистики сервера.
    """

    def __init__(self, serv: server, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()  # Создаём объект интерфейса
        self.ui.setupUi(self)  # Настраиваем интерфейс согласно дизайну
        self.serv = serv  # Сохраняем объект сервера для дальнейшей работы

        # Добавляем аттрибут для хранения ссылки на окно мониторинга
        self.monitoring_window = None

        def boot():
            """
            :return: Возвращает нынешний статус сервера при запуске приложения
            """
            status = self.serv.get_data()[0]  # Получаем текущий статус сервера
            if status == 'offline':
                self.ui.StatusLabel.setText("Status: Выключен")
            else:
                self.ui.StatusLabel.setText("Status: Запущен")

        boot()  # Вызываем функцию при запуске, чтобы сразу отобразить актуальный статус

        def cpu():
            """
            Бесконечный цикл для обновления показателей CPU в реальном времени
            """
            while True:
                cpu_stat = serv.get_data()[2]  # Получаем загрузку процессора
                self.ui.CPULabel.setText(f"CPU: {cpu_stat}%")

        threading.Thread(target=cpu, daemon=True).start()  # Запускаем поток для CPU

        def memory():
            """Бесконечный цикл для обновления показателей RAM в реальном времени"""
            while True:
                memory_stat = serv.get_data()[1]  # Получаем использование памяти
                self.ui.RAMLabel.setText(f"RAM: {memory_stat}%")

        threading.Thread(target=memory, daemon=True).start()  # Запускаем поток для RAM

        def disk():
            """Бесконечный цикл для обновления показателей диска в реальном времени"""
            while True:
                disk_stat = serv.get_data()[3]  # Получаем использование диска
                self.ui.SSDLabel.setText(f"SSD: {disk_stat} GB")

        threading.Thread(target=disk, daemon=True).start()  # Запускаем поток для диска

        def start_serv():
            """
            :return: При нажатии на кнопку Старта отображает "Статус: Запущен"
            """
            threading.Thread(target=self.serv.start, daemon=True).start()
            #  Запускаем поток для функции запуска сервера
            self.ui.StatusLabel.setText("Status: Запущен")

        def stop_server():
            """
            :return: При нажатии на кнопку Стопа отображает "Статус: Выключен"
            """
            threading.Thread(target=self.serv.stop, daemon=True).start()
            #  Запускаем поток для функции отключения сервера
            self.ui.StatusLabel.setText("Status: Выключен")

        def reload_server():
            """
            :return: При нажатии на кнопку Перезапуска отображает сначала "Статус: Перезапускается"
            а через время отображает "Статус: Запущен"
            """
            threading.Thread(target=self.serv.reload, daemon=True).start()
            # Запускам поток для функции перезапуска

            def change_status():
                """
                Подфункция для изменения надписи с использованием функции sleep
                из модуля time
                """
                self.ui.StatusLabel.setText("Status: Перезапускается")
                from time import sleep as s
                s(5)  # Ждём 5 секунд, пока сервер перезагружается
                self.ui.StatusLabel.setText("Status: Запущен")

            threading.Thread(target=change_status, daemon=True).start()

        def open_monitoring():
            """Открытие окна мониторинга с графиками"""
            if self.monitoring_window is None:  # Если окно ещё не создано
                self.monitoring_window = MonitoringWindow(self.serv)
                self.monitoring_window.show()
                # Автоматически запускаем мониторинг при открытии
                self.monitoring_window.start_monitoring()
            else:  # Если окно уже существует, просто показываем его
                self.monitoring_window.show()
                self.monitoring_window.start_monitoring()

        def open_console():
            """
            Метод, открывающий окно консоли
            :return:
            """
            self.con_window = console_window(serv)  # Создаём окно консоли
            self.con_window.show()  # Показываем его

        def open_schedules():
            """
            Метод, открывающий окно расписаний
            :return:
            """
            self.sch_window = schedule_window(serv)  # Создаём окно расписаний
            self.sch_window.show()  # Показываем его

        self.ui.StartButton.clicked.connect(lambda: start_serv())
        # Привязываем функцию start_serv() к кнопке старта
        self.ui.ShutdownButton.clicked.connect(lambda: stop_server())
        # Привязываем функцию stop_serv() к кнопке стопа
        self.ui.RestartButton.clicked.connect(lambda: reload_server())
        # Привязываем функцию reload_serv() к кнопке перезапуска
        self.ui.ConsoleButton.clicked.connect(lambda: open_console())
        # Привязываем функцию open_console() к кнопке открытия консоли
        self.ui.ScheduleButton.clicked.connect(lambda: open_schedules())
        # Привязываем функцию open_schedules() к кнопке открытия расписаний


        self.ui.MoreButton.clicked.connect(lambda: open_monitoring())


if __name__ == "__main__":
    app = QApplication(sys.argv)  # Создаём приложение
    root = user_interface(srv)  # Создаём главное окно с тестовым сервером
    root.show()  # Показываем окно
    sys.exit(app.exec())  # Запускаем главный цикл приложения