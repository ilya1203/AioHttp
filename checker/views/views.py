from aiohttp import web
from scaner import Sock, Logs

async def index(requset):
    sc = Sock()
    ip = requset.match_info.get('ip')
    start_port = int(requset.match_info.get('begin_port'))
    end_port = int(requset.match_info.get('end_port'))
    lg = Logs()
    lg.write_log(messeg=f'START as /scan/{ip}{start_port}/{end_port}')
    data = await sc.check_ports(ip=ip, from_port=start_port, to_port=end_port)
    return web.json_response(data)
