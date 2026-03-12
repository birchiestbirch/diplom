from pydactyl import PterodactylClient  # Импортируем основную библиотеку проекта


class server():
    """
    Главный класс проекта, принимающий в себя данные о сервере и содержит основные
    методы взаимодействия с серверами.

    start(self) - Метод, отправляющий запрос на включение сервера
    stop(self) - Метод, отправляющий запрос на отключение сервера
    reload(self) - Метод, отправляющий сначала запрос на отключение сервера,
    ждёт пару секунд, а потом отправляет запрос на включение.
    get_data(self) - Метод, запрашивающий с сервера данные о его состоянии и оформляет их в удобный массив для работы.
    send_command(self, command) - Принимает команду и отправляет её на сервер для дальнейшего выполнения
    create_schedule(self, server_id, command, minute, hour, day_of_month, day_of_week, month) - Метод принимающий параметры
    для создания расписания в нужном формате и отправляет всё расписание на сервер.
    load_schedules(self, server_id) - Запрашивает и возвращает все расписания с сервера.
    delete_schedules(self, server_id, schedule_id) - Удаляет указанное расписание и выводит оставшиеся
    run_schedule(self, server_id, schedule_id) - Принудительно запускает расписание по его ID
    """

    def __init__(self, api: PterodactylClient):
        self.api = api  # Сохраняем объект API для дальнейшей работы
        self.server = self.api.client.servers.list_servers()  # Получаем список всех доступных серверов
        self.server_id = self.server[0]['attributes']['identifier']  # Берём ID первого сервера из списка

    def start(self):
        """Отправляет сигнал на запуск сервера"""
        self.api.client.servers.send_power_action(server_id=self.server_id, signal='start')
        return 'server started'

    def stop(self):
        """Отправляет сигнал на остановку сервера"""
        self.api.client.servers.send_power_action(server_id=self.server_id, signal='stop')
        return 'server stopped'

    def reload(self):
        """Перезапускает сервер с небольшой задержкой и обратным отсчётом"""
        from time import sleep as s  # Импортируем функцию для создания задержки
        self.api.client.servers.send_power_action(server_id=self.server_id, signal='stop')
        for i in range(5):  # Считаем до пяти перед запуском
            s(0.5)
            print(f"{i}...")
        self.api.client.servers.send_power_action(server_id=self.server_id, signal="start")
        return 'server restarted'

    def get_data(self):
        """
        Получает актуальные данные о состоянии сервера и преобразует их в удобный формат.
        Возвращает массив: [статус, RAM(GB), CPU(%), диск(GB), время работы(часы, минуты, секунды)]
        """
        self.server_util = self.api.client.servers.get_server_utilization(
            server_id=self.server_id)  # Запрашиваем использование ресурсов
        self.server_data = [
            self.server_util["current_state"],  # Текущий статус (running/offline)
            round(((int(self.server_util["resources"]["memory_bytes"]) / 1024) / 1024) / 1024, 2),
            # Переводим байты в гигабайты
            self.server_util["resources"]["cpu_absolute"],  # Загрузка процессора в процентах
            round(((int(self.server_util["resources"]["disk_bytes"]) / 1024) / 1024) / 1024, 2),
            # Переводим байты в гигабайты
            round(self.server_util["resources"]["uptime"] / 1000, 2)  # Переводим миллисекунды в секунды
        ]
        self.sec = self.server_data[-1]  # Сохраняем сырое значение аптайма

        def convert(secund):
            """Вспомогательная функция для конвертации секунд в часы:минуты:секунды"""
            return [int(round((secund // 3600), 0)), int(round(((secund % 3600) // 60), 0)),
                    int(round((secund % 60), 0))]

        self.server_data[-1] = convert(self.sec)  # Заменяем сырые секунды на нормальное время

        return self.server_data

    def send_command(self, command):
        """Отправляет произвольную команду в консоль сервера"""
        self.api.client.servers.send_console_command(self.server_id, command)

    def create_schedule(self, server_id, command, minute, hour, day_of_month, day_of_week, month):
        """
        Функция создаёт отложенное действие на сервере
        :param server_id: Идентификатор сервера
        :param command: Команда в консоль для выполнения
        :param minute: Минута
        :param hour: Час
        :param day_of_month: День месяца (числовое значение)
        :param day_of_week: День недели (MON/TUE и так далее)
        :param month: Месяц (DEC/JAN и так далее)
        :return: ID созданного расписания
        """
        schedule = self.api.client.servers.schedules.create_schedule(server_id=server_id,
                                                                     name=command[:10],
                                                                     # Обрезаем название до 10 символов
                                                                     minute=minute,
                                                                     hour=hour,
                                                                     day_of_month=day_of_month,
                                                                     day_of_week=day_of_week,
                                                                     month=month,
                                                                     is_active=True,
                                                                     # Расписание создаётся сразу активным
                                                                     only_when_online=True)  # Выполнять только когда сервер включён

        self.api.client.servers.schedules.create_task(server_id=server_id,
                                                      schedule_id=schedule["attributes"]["id"],
                                                      action="command",  # Тип действия - команда
                                                      payload=command,  # Сама команда
                                                      time_offset="0",  # Без задержки
                                                      continue_on_failure=False)  # Не продолжать при ошибке
        return schedule["attributes"]["id"]

    def load_schedules(self, server_id):
        """
        Возвращает список всех расписаний сервера
        :param server_id: Идентификатор сервера
        :return: Список всех расписаний
        """
        schedules = self.api.client.servers.schedules.list_schedules(server_id)
        return schedules

    def delete_schedules(self, server_id, schedule_id):
        """
        Удаляет указанное расписание
        :param server_id: Идентификатор сервера
        :param schedule_id: Идентификатор расписания
        :return: Печатает в консоль ещё не удалённые расписания
        """
        self.api.client.servers.schedules.delete_schedule(server_id, schedule_id)
        print(self.load_schedules(server_id))  # Показываем оставшиеся после удаления расписания

    def run_schedule(self, server_id, schedule_id):
        """
        Запускает расписание досрочно
        :param server_id: Идентификатор сервера
        :param schedule_id: Идентификатор расписания
        :return:
        """
        self.api.client.servers.schedules.run_schedule(server_id, schedule_id)


if __name__ == "__main__":
    test = server(PterodactylClient('https://mgr.legistale.net', 'ptlc_inD6oIpdBSLRC4zWHlnxyFV9fkefyUcSO3PAzy40wSH'))
    a = [0]  # Какая-то переменная (похоже, что отладка)
    print(test.get_data())