from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PySide6.QtCore import QTime, Qt
from ui_files.schedulew import Ui_ScheduleWindow
import sys
from pydactyl import PterodactylClient
from oop_test import server

srv = server(PterodactylClient('https://mgr.legistale.net', 'ptlc_inD6oIpdBSLRC4zWHlnxyFV9fkefyUcSO3PAzy40wSH'))
# Создаём объект класса server для тестов


class schedule_window(QMainWindow):
    """
    Класс с окном расписаний.
    Отвечает за просмотр, создание, удаление и ручной запуск расписаний на сервере.
    """

    def __init__(self, serv: server, parent=None):
        super().__init__(parent)
        self.ui = Ui_ScheduleWindow()  # Создаём объект интерфейса
        self.ui.setupUi(self)  # Настраиваем интерфейс согласно дизайну
        self.serv = serv  # Сохраняем объект сервера для дальнейшей работы

        # Чтение данных из файла
        file_path = 'data.txt'
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            if len(lines) >= 2:  # Проверяем, что там хотя бы 2 строки
                saved_ip = lines[0].strip()
                saved_api = lines[1].strip()
        self.ip = saved_ip  # Сохраняем IP для дальнейшего использования
        self.api_key = saved_api  # Сохраняем API ключ для дальнейшего использования

        def load_schedules():
            """
            Загружает с сервера все расписания и размещает их в таблице
            :return:
            """
            schedules = serv.load_schedules(server_id=serv.server_id)  # Получаем список расписаний с сервера

            self.ui.QTableWidget.setRowCount(0)  # Очищаем таблицу перед загрузкой

            self.ui.QTableWidget.setColumnCount(4)  # Устанавливаем 4 колонки
            self.ui.QTableWidget.setHorizontalHeaderLabels(['ID', 'Дата', 'Время', 'Команда'])  # Называем колонки

            if schedules and 'data' in schedules and len(schedules['data']) > 0:  # Проверяем, есть ли расписания
                for schedule in schedules['data']:  # Проходим по каждому расписанию
                    attributes = schedule['attributes']

                    schedule_id = attributes['id']  # ID расписания

                    cron = attributes['cron']  # Cron-выражение расписания

                    month = cron.get('month', '*')
                    day_of_month = cron.get('day_of_month', '*')
                    day_of_week = cron.get('day_of_week', '*')

                    date_parts = []  # Собираем части даты в читаемый вид

                    if month and month != '*':
                        month_names = {
                            '1': 'Янв', '2': 'Фев', '3': 'Мар', '4': 'Апр',
                            '5': 'Май', '6': 'Июн', '7': 'Июл', '8': 'Авг',
                            '9': 'Сен', '10': 'Окт', '11': 'Ноя', '12': 'Дек'
                        }
                        month_display = month_names.get(str(month).upper(), month)
                        date_parts.append(month_display)

                    if day_of_month and day_of_month != '*':
                        date_parts.append(str(day_of_month))  # Добавляем день месяца

                    if day_of_week and day_of_week != '*':
                        weekday_names = {
                            'MON': 'Пн', 'TUE': 'Вт', 'WED': 'Ср',
                            'THU': 'Чт', 'FRI': 'Пт', 'SAT': 'Сб', 'SUN': 'Вс'
                        }
                        weekday_display = weekday_names.get(str(day_of_week).upper(), day_of_week)
                        date_parts.append(f"({weekday_display})")  # Добавляем день недели в скобках

                    date_str = " ".join(date_parts)  # Склеиваем части даты

                    hour = cron.get('hour', '0').zfill(2)  # Добавляем ноль впереди, если нужно
                    minute = cron.get('minute', '0').zfill(2)  # Добавляем ноль впереди, если нужно
                    time_str = f"{hour}:{minute}"  # Формируем время

                    command = "Нет команды"  # Значение по умолчанию
                    if 'relationships' in attributes and 'tasks' in attributes['relationships']:
                        tasks_data = attributes['relationships']['tasks'].get('data', [])
                        if tasks_data:
                            task_attributes = tasks_data[0]['attributes']
                            command = task_attributes.get('payload', 'Нет команды')  # Получаем команду задачи

                    row_count = self.ui.QTableWidget.rowCount()  # Текущее количество строк
                    self.ui.QTableWidget.insertRow(row_count)  # Добавляем новую строку

                    # Заполняем ячейки данными
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
            schedules = serv.load_schedules(server_id=serv.server_id)  # Получаем текущие расписания

            self.minute = self.ui.timeEdit.text()[0:1]  # Берём минуты из поля времени
            self.hour = self.ui.timeEdit.text()[3:4]  # Берём часы из поля времени
            self.command = self.ui.actionEdit.text()  # Берём команду из поля ввода
            self.day_of_week = self.ui.weekdayCombo.currentText()  # Берём день недели из выпадающего списка
            self.day_of_month = self.ui.daySpin.text()  # Берём день месяца из спиннера
            self.month = self.ui.monthCombo.currentText()  # Берём месяц из выпадающего списка

            # Создаём новое расписание на сервере
            serv.create_schedule(server_id=self.serv.server_id,
                                 command=self.command,
                                 minute=self.minute,
                                 hour=self.hour,
                                 day_of_month=self.day_of_month,
                                 day_of_week=self.day_of_week,
                                 month=self.month)

            table = self.ui.QTableWidget

            if schedules and 'data' in schedules and len(schedules['data']) > 0:
                last_schedule = schedules['data'][-1]  # Берём последнее расписание
                schedule_id = last_schedule['attributes']['id']  # Получаем его ID

                date_parts = []  # Собираем части даты для отображения

                if self.month and self.month != '*':
                    month_names = {
                        'JAN': 'Янв', 'FEB': 'Фев', 'MAR': 'Мар', 'APR': 'Апр',
                        'MAY': 'Май', 'JUN': 'Июн', 'JUL': 'Июл', 'AUG': 'Авг',
                        'SEP': 'Сен', 'OCT': 'Окт', 'NOV': 'Ноя', 'DEC': 'Дек'
                    }
                    month_display = month_names.get(str(self.month).upper(), self.month)
                    date_parts.append(month_display)

                if self.day_of_month and self.day_of_month != '*':
                    date_parts.append(str(self.day_of_month))

                if self.day_of_week and self.day_of_week != '*':
                    weekday_names = {
                        'MON': 'Пн', 'TUE': 'Вт', 'WED': 'Ср',
                        'THU': 'Чт', 'FRI': 'Пт', 'SAT': 'Сб', 'SUN': 'Вс',
                        'Monday': 'Пн', 'Tuesday': 'Вт', 'Wednesday': 'Ср'
                    }
                    weekday_display = weekday_names.get(str(self.day_of_week), self.day_of_week)
                    date_parts.append(f"({weekday_display})")

                date_str = " ".join(date_parts)  # Склеиваем дату

                time_str = f"{self.hour}:{self.minute}"  # Формируем время

                # Добавляем новую строку в таблицу
                row_count = table.rowCount()
                table.insertRow(row_count)
                table.setItem(row_count, 0, QTableWidgetItem(str(schedule_id)))
                table.setItem(row_count, 1, QTableWidgetItem(date_str))
                table.setItem(row_count, 2, QTableWidgetItem(time_str))
                table.setItem(row_count, 3, QTableWidgetItem(self.command))

            load_schedules()  # Перезагружаем таблицу для синхронизации с сервером

        def delete_schedule():
            """
            Этот метод удаляет расписание вместе с задачей по идентификатору, полученному из выбранной строки таблицы, попутно удаляя выбранную строку из самой таблицы
            :return:
            """
            current_row = self.ui.QTableWidget.currentRow()  # Получаем выбранную строку
            id_item = self.ui.QTableWidget.item(current_row, 0)  # Берём ID из первого столбца
            schedule_id = id_item.text()  # Извлекаем текст ID
            serv.delete_schedules(server_id=serv.server_id, schedule_id=schedule_id)  # Удаляем расписание с сервера
            self.ui.QTableWidget.removeRow(current_row)  # Удаляем строку из таблицы

        def run_schedule():
            """
            Этот метод досрочно запускает расписание, выполняя все заложенные в него задачи не дожидаясь времени и даты
            :return:
            """
            current_row = self.ui.QTableWidget.currentRow()  # Получаем выбранную строку
            id_item = self.ui.QTableWidget.item(current_row, 0)  # Берём ID из первого столбца
            schedule_id = id_item.text()  # Извлекаем текст ID
            serv.run_schedule(serv.server_id, schedule_id)  # Запускаем расписание досрочно

        def close_window():
            """
            Закрывает окно
            :return:
            """
            self.close()

        load_schedules()  # Загружаем расписания при открытии окна
        # Привязываем кнопки к функциям
        self.ui.addButton.clicked.connect(save_schedule)  # Кнопка "Добавить"
        self.ui.backButton.clicked.connect(close_window)  # Кнопка "Назад"
        self.ui.backButton_2.clicked.connect(delete_schedule)  # Кнопка "Удалить"
        self.ui.launchButton.clicked.connect(run_schedule)  # Кнопка "Запустить"


if __name__ == "__main__":
    app = QApplication()  # Создаём приложение
    root = schedule_window(srv)  # Создаём окно расписаний с тестовым сервером
    root.show()  # Показываем окно
    sys.exit(app.exec())  # Запускаем главный цикл приложения