import socket
from pprint import pprint
from time import sleep, gmtime
import os
import logging

class Sock:

    async def check_port(self, ip, port):
        sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        log = logging.getLogger('LOGS')
        log.info(f'start {ip}:{port}')
        try:
            result = 'open' if sc.connect((ip, port)) == 0 else 'close'
        except Exception as ex:
            print(f'{ex}')
            lg = Logs()
            lg.write_exctention(masseg=ex)
            result = 'close'
        sc.close()

        logs = Logs()
        logs.write_log(messeg=f'{ip}:{port}::{result}')

        return result


    async def check_ports(self, ip, from_port, to_port):
        to_return = []

        for port in range(from_port, to_port+1):
            print(f'Check: {ip}:{port}', end=' ')
            try:
                result = await self.check_port(ip=ip, port=port)
                to_return.append({
                    'ip': ip,
                    'port': f'{port}',
                    'status': result
                })
                print(result)
            except Exception as ex:
                print(f'\n{ex}\n')
                lg = Logs()
                lg.write_exctention(masseg=ex)
                to_return.append({
                    'ip': ip,
                    'port': port,
                    'status': 'close'
                })
            sleep(2)
            print()

        return to_return

class Logs:

    def __init__(self):
        self.path = './logs/logs_check.txt'
        self.pathE = './logs/logs_exctention.txt'

    def write_log(self, messeg):
        try:
            file = open(self.path, 'a', encoding='utf-8')
        except:
            try:
                os.mkdir(self.path.split('/')[1])
            except:
                pass
            file = open(self.path, 'w', encoding='utf-8')

        tm = gmtime()
        date = f'{tm.tm_mday}.{tm.tm_mon}.{tm.tm_year}||{tm.tm_hour}:{tm.tm_min}:{tm.tm_sec}'
        file.write(date+f'\t::\t{messeg}\n')
        file.close()

    def write_exctention(self, masseg):
        try:
            file = open(self.pathE, 'a', encoding='utf-8')
        except:
            try:
                os.mkdir(self.pathE.split('/')[1])
            except:
                pass
            file = open(self.pathE, 'w', encoding='utf-8')

        tm = gmtime()
        date = f'{tm.tm_mday}.{tm.tm_mon}.{tm.tm_year}||{tm.tm_hour}:{tm.tm_min}:{tm.tm_sec}'
        file.write('EX:\t'+date+f'\t::\t{masseg}\n')
        file.close()