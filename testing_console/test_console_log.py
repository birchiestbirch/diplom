from pydactyl import PterodactylClient

api = PterodactylClient('https://mgr.legistale.net', 'ptlc_inD6oIpdBSLRC4zWHlnxyFV9fkefyUcSO3PAzy40wSH')

servers = api.client.servers.list_servers()

server_id = servers[0]['attributes']['identifier']

