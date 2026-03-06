from pydactyl import PterodactylClient

class server():
    def __init__(self, api: PterodactylClient):
        self.api = api
        self.server = self.api.client.servers.list_servers()
        self.server_id = self.server[0]['attributes']['identifier']

    def start(self):
        self.api.client.servers.send_power_action(server_id=self.server_id, signal='start')
        return 'server started' 
    
    def stop(self):
        self.api.client.servers.send_power_action(server_id=self.server_id, signal='stop')
        return 'server stopped' 
    
    def reload(self):
        from time import sleep as s
        self.api.client.servers.send_power_action(server_id=self.server_id, signal='stop')
        for i in range(5):
            s(0.5)
            print(f"{i}...")
        self.api.client.servers.send_power_action(server_id=self.server_id, signal="start")
        return 'server restarted' 

    def get_data(self):
        self.server_util = self.api.client.servers.get_server_utilization(server_id=self.server_id)
        self.server_data = [
            self.server_util["current_state"],
            round(((int(self.server_util["resources"]["memory_bytes"])/1024)/1024)/1024, 2),
            self.server_util["resources"]["cpu_absolute"],
            round(((int(self.server_util["resources"]["disk_bytes"])/1024)/1024)/1024, 2),
            round(self.server_util["resources"]["uptime"]/1000, 2)
        ]
        self.sec = self.server_data[-1]
        def convert(secund):
            return [int(round((secund//3600), 0)), int(round(((secund%3600) // 60), 0)), int(round((secund % 60), 0))]
        self.server_data[-1] = convert(self.sec)

        return self.server_data

    def send_command(self, command):
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
        :return:
        """
        schedule = self.api.client.servers.schedules.create_schedule(server_id=server_id,
                                                          name=command[:10],
                                                          minute=minute,
                                                          hour=hour,
                                                          day_of_month=day_of_month,
                                                          day_of_week=day_of_week,
                                                          month=month,
                                                          is_active=True,
                                                          only_when_online=True)

        self.api.client.servers.schedules.create_task(server_id=server_id,
                                                      schedule_id=schedule["attributes"]["id"],
                                                      action="command",
                                                      payload=command,
                                                      time_offset="0",
                                                      continue_on_failure=False)
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
        print(self.load_schedules(server_id))

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
    a = [0]
    """    from time import sleep as s
    timer = 0
    while len(a) != 3:
        timer = timer + 1
        print(timer, "sec")
        s(1)
        if a[-1] != test.get_data()[2]:
            a.append(test.get_data()[2])
            print(a)"""
    print(test.get_data())