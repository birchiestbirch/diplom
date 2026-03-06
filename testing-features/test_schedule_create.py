from pydactyl import PterodactylClient
from oop_test import server

api = PterodactylClient('https://mgr.legistale.net', 'ptlc_inD6oIpdBSLRC4zWHlnxyFV9fkefyUcSO3PAzy40wSH')
serv = api.client.servers.list_servers()
server_id = serv[0]['attributes']['identifier']

srv = server(api)

print(srv.load_schedules(server_id))