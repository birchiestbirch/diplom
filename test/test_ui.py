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
    """

    def __init__(self, serv: server, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.serv = serv

        # Добавляем аттрибут для хранения ссылки на окно мониторинга
        self.monitoring_window = None

        def boot():
            """
            :return: Возвращает нынешний статус сервера при запуске приложения
            """
            status = self.serv.get_data()[0]
            if status == 'offline':
                self.ui.StatusLabel.setText("Status: Выключен")
            else:
                self.ui.StatusLabel.setText("Status: Запущен")

        boot()  # Вызываем функцию

        def cpu():
            """
            :return:
            """
            while True:
                cpu_stat = serv.get_data()[2]
                self.ui.CPULabel.setText(f"CPU: {cpu_stat}%")

        threading.Thread(target=cpu, daemon=True).start()

        def memory():
            while True:
                memory_stat = serv.get_data()[1]
                self.ui.RAMLabel.setText(f"RAM: {memory_stat}%")

        threading.Thread(target=memory, daemon=True).start()

        def disk():
            while True:
                disk_stat = serv.get_data()[3]
                self.ui.SSDLabel.setText(f"SSD: {disk_stat} GB")

        threading.Thread(target=disk, daemon=True).start()

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
                :return: Подфункция для изменения надписи с использованием функции sleep
                из модуля time
                """
                self.ui.StatusLabel.setText("Status: Перезапускается")
                from time import sleep as s
                s(5)
                self.ui.StatusLabel.setText("Status: Запущен")

            threading.Thread(target=change_status, daemon=True).start()

        def open_monitoring():
            """Открытие окна мониторинга с графиками"""
            if self.monitoring_window is None:
                self.monitoring_window = MonitoringWindow(self.serv)
                self.monitoring_window.show()
                # Автоматически запускаем мониторинг при открытии
                self.monitoring_window.start_monitoring()
            else:
                # Если окно уже существует, просто показываем его
                self.monitoring_window.show()
                self.monitoring_window.start_monitoring()

        def open_console():
            """
            Метод, открывающий окно консоли
            :return:
            """

            self.con_window = console_window(serv)
            self.con_window.show()

        def open_schedules():
            """
            Метод, открывающий окно расписаний
            :return:
            """

            self.sch_window = schedule_window(serv)
            self.sch_window.show()

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


        # Добавляем обработчик для кнопки MoreButton
        if hasattr(self.ui, 'MoreButton'):
            self.ui.MoreButton.clicked.connect(lambda: open_monitoring())
        else:
            print("Предупреждение: кнопка MoreButton не найдена в интерфейсе")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    root = user_interface(srv)
    root.show()
    sys.exit(app.exec())