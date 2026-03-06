from PySide6.QtWidgets import QApplication, QMainWindow  # Импортируем нужные вещи из PySide6
from ui_files.consolew import Ui_ConsoleWindow
import sys
from pydactyl import PterodactylClient
from oop_test import server  # Импортируем главный класс проекта, в котором и происходят все вещи

srv = server(PterodactylClient('https://mgr.legistale.net', 'ptlc_inD6oIpdBSLRC4zWHlnxyFV9fkefyUcSO3PAzy40wSH'))


class console_window(QMainWindow):
    """
    Класс с окном консоли
    """

    def __init__(self, serv: server, parent=None):
        super().__init__(parent)
        self.ui = Ui_ConsoleWindow()
        self.ui.setupUi(self)
        self.serv = serv

        file_path = 'data.txt'
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            if len(lines) >= 2:
                saved_ip = lines[0].strip()
                saved_api = lines[1].strip()
        self.ip = saved_ip
        self.api = saved_api

        self.ui.commandInput.returnPressed.connect(self.send_command)

    def send_command(self):
        """
        Отправляет команду на сервер при нажатии Enter
        """
        command = self.ui.commandInput.text()
        if command.strip():

            self.serv.send_command(command)

            self.ui.commandInput.clear()

if __name__ == "__main__":
    app = QApplication()
    root = console_window(srv)
    root.show()
    sys.exit(app.exec())