from oop_test import server  # Импортируем основной класс со всем функционалом
from PySide6.QtWidgets import QApplication, QMainWindow  # Импортируем всё необходимое для
from ui import Ui_MainWindow  # Графического интерфейса
from pydactyl import PterodactylClient  # Импортируем основную API для работы с сервером и панелью
import sys, threading  # Необходимые технические библиотеки для UI и потоков.

srv = server(PterodactylClient('https://mgr.legistale.net', 'ptlc_inD6oIpdBSLRC4zWHlnxyFV9fkefyUcSO3PAzy40wSH'))
# В переменную srv записываем данные для API, включая ключ
class user_interface(QMainWindow):
    """
    Основной класс приложения.
    Принимает объект класса PterodactylClient.
    """
    def __init__(self, serv:server, parent=None):
        super().__init__(parent)  # Изменено здесь
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.serv = serv

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

        self.ui.StartButton.clicked.connect(lambda: start_serv())
        # Привязываем функцию start_serv() к кнопке старта
        self.ui.ShutdownButton.clicked.connect(lambda: stop_server())
        # Привязываем функцию stop_serv() к кнопке стопа
        self.ui.RestartButton.clicked.connect(lambda: reload_server())
        # Привязываем функцию reload_serv() к кнопке перезапуска

if __name__ == "__main__":
    app = QApplication(sys.argv)
    root = user_interface(srv)
    root.show()
    sys.exit(app.exec())