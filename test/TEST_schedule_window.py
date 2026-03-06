from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PySide6.QtCore import QTime, Qt
from ui_files.schedulew import Ui_ScheduleWindow
import sys
from pydactyl import PterodactylClient
from oop_test import server

srv = server(PterodactylClient('https://mgr.legistale.net', 'ptlc_inD6oIpdBSLRC4zWHlnxyFV9fkefyUcSO3PAzy40wSH'))


class schedule_window(QMainWindow):
    """
    Класс с окном расписаний
    """

    def __init__(self, serv: server, parent=None):
        super().__init__(parent)
        self.ui = Ui_ScheduleWindow()
        self.ui.setupUi(self)
        self.serv = serv

        # Чтение данных из файла
        file_path = 'data.txt'
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            if len(lines) >= 2:
                saved_ip = lines[0].strip()
                saved_api = lines[1].strip()
        self.ip = saved_ip
        self.api_key = saved_api

        def load_schedules():
            """
            Загружает с сервера все расписания и размещает их в таблице
            :return:
            """
            schedules = serv.load_schedules(server_id=serv.server_id)

            self.ui.QTableWidget.setRowCount(0)

            self.ui.QTableWidget.setColumnCount(4)
            self.ui.QTableWidget.setHorizontalHeaderLabels(['ID', 'Дата', 'Время', 'Команда'])

            if schedules and 'data' in schedules and len(schedules['data']) > 0:
                for schedule in schedules['data']:
                    attributes = schedule['attributes']

                    schedule_id = attributes['id']

                    cron = attributes['cron']

                    month = cron.get('month', '*')
                    day_of_month = cron.get('day_of_month', '*')
                    day_of_week = cron.get('day_of_week', '*')

                    date_parts = []

                    if month and month != '*':
                        month_names = {
                            '1': 'Янв', '2': 'Фев', '3': 'Мар', '4': 'Апр',
                            '5': 'Май', '6': 'Июн', '7': 'Июл', '8': 'Авг',
                            '9': 'Сен', '10': 'Окт', '11': 'Ноя', '12': 'Дек',
                            'JAN': 'Янв', 'FEB': 'Фев', 'MAR': 'Мар', 'APR': 'Апр',
                            'MAY': 'Май', 'JUN': 'Июн', 'JUL': 'Июл', 'AUG': 'Авг',
                            'SEP': 'Сен', 'OCT': 'Окт', 'NOV': 'Ноя', 'DEC': 'Дек'
                        }
                        month_display = month_names.get(str(month).upper(), month)
                        date_parts.append(month_display)

                    if day_of_month and day_of_month != '*':
                        date_parts.append(str(day_of_month))

                    if day_of_week and day_of_week != '*':
                        weekday_names = {
                            'MON': 'Пн', 'TUE': 'Вт', 'WED': 'Ср',
                            'THU': 'Чт', 'FRI': 'Пт', 'SAT': 'Сб', 'SUN': 'Вс',
                            '0': 'Вс', '1': 'Пн', '2': 'Вт', '3': 'Ср',
                            '4': 'Чт', '5': 'Пт', '6': 'Сб', '7': 'Вс'
                        }
                        weekday_display = weekday_names.get(str(day_of_week).upper(), day_of_week)
                        date_parts.append(f"({weekday_display})")


                    date_str = " ".join(date_parts)

                    hour = cron.get('hour', '0').zfill(2)
                    minute = cron.get('minute', '0').zfill(2)
                    time_str = f"{hour}:{minute}"

                    command = "Нет команды"
                    if 'relationships' in attributes and 'tasks' in attributes['relationships']:
                        tasks_data = attributes['relationships']['tasks'].get('data', [])
                        if tasks_data:
                            task_attributes = tasks_data[0]['attributes']
                            command = task_attributes.get('payload', 'Нет команды')

                    row_count = self.ui.QTableWidget.rowCount()
                    self.ui.QTableWidget.insertRow(row_count)

                    self.ui.QTableWidget.setItem(row_count, 0, QTableWidgetItem(str(schedule_id)))
                    self.ui.QTableWidget.setItem(row_count, 1, QTableWidgetItem(date_str))
                    self.ui.QTableWidget.setItem(row_count, 2, QTableWidgetItem(time_str))
                    self.ui.QTableWidget.setItem(row_count, 3, QTableWidgetItem(command))


                print(f"Загружено {len(schedules['data'])} расписаний")
            else:
                print("Нет расписаний для загрузки")

        def save_schedule():
            """
            Принимает данные из элементов графического интерфейса и складывает их в расписание и задачу для расписания, попутно сохраняя как новую строку в таблицу
            :return:
            """
            schedules = serv.load_schedules(server_id=serv.server_id)

            self.minute = self.ui.timeEdit.text()[0:1]
            self.hour = self.ui.timeEdit.text()[3:4]
            self.command = self.ui.actionEdit.text()
            self.day_of_week = self.ui.weekdayCombo.currentText()
            self.day_of_month = self.ui.daySpin.text()
            self.month = self.ui.monthCombo.currentText()

            serv.create_schedule(server_id=self.serv.server_id,
                                 command=self.command,
                                 minute=self.minute,
                                 hour=self.hour,
                                 day_of_month=self.day_of_month,
                                 day_of_week=self.day_of_week,
                                 month=self.month)

            table = self.ui.QTableWidget

            if schedules and 'data' in schedules and len(schedules['data']) > 0:
                last_schedule = schedules['data'][-1]
                schedule_id = last_schedule['attributes']['id']

                date_parts = []

                if self.month and self.month != '*':
                    month_names = {
                        'JAN': 'Янв', 'FEB': 'Фев', 'MAR': 'Мар', 'APR': 'Апр',
                        'MAY': 'Май', 'JUN': 'Июн', 'JUL': 'Июл', 'AUG': 'Авг',
                        'SEP': 'Сен', 'OCT': 'Окт', 'NOV': 'Ноя', 'DEC': 'Дек',
                        '1': 'Янв', '2': 'Фев', '3': 'Мар', '4': 'Апр',
                        '5': 'Май', '6': 'Июн', '7': 'Июл', '8': 'Авг',
                        '9': 'Сен', '10': 'Окт', '11': 'Ноя', '12': 'Дек'
                    }
                    month_display = month_names.get(str(self.month).upper(), self.month)
                    date_parts.append(month_display)

                if self.day_of_month and self.day_of_month != '*':
                    date_parts.append(str(self.day_of_month))

                if self.day_of_week and self.day_of_week != '*':
                    weekday_names = {
                        'MON': 'Пн', 'TUE': 'Вт', 'WED': 'Ср',
                        'THU': 'Чт', 'FRI': 'Пт', 'SAT': 'Сб', 'SUN': 'Вс',
                        'Monday': 'Пн', 'Tuesday': 'Вт', 'Wednesday': 'Ср',
                        'Thursday': 'Чт', 'Friday': 'Пт', 'Saturday': 'Сб', 'Sunday': 'Вс',
                        'Понедельник': 'Пн', 'Вторник': 'Вт', 'Среда': 'Ср',
                        'Четверг': 'Чт', 'Пятница': 'Пт', 'Суббота': 'Сб', 'Воскресенье': 'Вс'
                    }
                    weekday_display = weekday_names.get(str(self.day_of_week), self.day_of_week)
                    date_parts.append(f"({weekday_display})")

                date_str = " ".join(date_parts)

                time_str = f"{self.hour}:{self.minute}"

                row_count = table.rowCount()
                table.insertRow(row_count)
                table.setItem(row_count, 0, QTableWidgetItem(str(schedule_id)))
                table.setItem(row_count, 1, QTableWidgetItem(date_str))
                table.setItem(row_count, 2, QTableWidgetItem(time_str))
                table.setItem(row_count, 3, QTableWidgetItem(self.command))

            load_schedules()

        def delete_schedule():
            """
            Этот метод удаляет расписание вместе с задачей по идентификатору, полученному из выбранной строки таблицы, попутно удаляя выбранную строку из самой таблицы
            :return:
            """
            current_row = self.ui.QTableWidget.currentRow()
            id_item = self.ui.QTableWidget.item(current_row, 0)
            schedule_id = id_item.text()
            serv.delete_schedules(server_id=serv.server_id, schedule_id=schedule_id)
            self.ui.QTableWidget.removeRow(current_row)

        def run_schedule():
            """
            Этот метод досрочно запускает расписание, выполняя все заложенные в него задачи не дожидаясь времени и даты
            :return:
            """
            current_row = self.ui.QTableWidget.currentRow()
            id_item = self.ui.QTableWidget.item(current_row, 0)
            schedule_id = id_item.text()
            serv.run_schedule(serv.server_id, schedule_id)

        def close_window():
            """
            Закрывает окно
            :return:
            """
            self.close()

        load_schedules()
        self.ui.addButton.clicked.connect(save_schedule)
        self.ui.backButton.clicked.connect(close_window)
        self.ui.backButton_2.clicked.connect(delete_schedule)
        self.ui.launchButton.clicked.connect(run_schedule)


if __name__ == "__main__":
    app = QApplication()
    root = schedule_window(srv)
    root.show()
    sys.exit(app.exec())