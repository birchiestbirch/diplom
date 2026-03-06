from pydactyl import PterodactylClient

api = PterodactylClient('https://mgr.legistale.net', 'ptlc_inD6oIpdBSLRC4zWHlnxyFV9fkefyUcSO3PAzy40wSH')
server = api.client.servers.list_servers()
server_id = server[0]['attributes']['identifier']

print([i for i in dir(api.client.servers.schedules) if not i.startswith('_')])

print("api.client.servers.schedules.run_schedule:\n")
print(api.client.servers.schedules.run_schedule.__doc__)

"""api.client.servers.schedules.create_schedule(server_id=server_id,
                                             name="test",
                                             minute="0",
                                             hour="0",
                                             is_active=True,
                                             day_of_week="MON",
                                             month="MAR",
                                             day_of_month="2")"""

#print(api.client.servers.schedules.list_schedules(server_id))

#api.client.servers.schedules.delete_schedule(server_id, schedule_id=51)

"""
Examples
*/5 * * * *
every 5 minutes
0 */1 * * *
every hour
0 8-12 * * *
hour range
0 0 * * *
once a day
0 0 * * MON
every Monday


Special Characters
*
any value
,
value list separator
-
range values
/
step values"""