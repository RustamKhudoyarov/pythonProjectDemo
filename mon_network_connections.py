from time import sleep
from datetime import datetime
import psutil


current_time = datetime.now()

ip_adr = psutil.net_if_addrs()
connect_traffic = psutil.net_io_counters(pernic=True)['lo']
bytes_sent = getattr(connect_traffic, 'bytes_sent')
bytes_receive = getattr(connect_traffic, 'bytes_recv')

print(f'sent bytes: {bytes_sent} , received bytes: {bytes_receive}')

for hop in range(60):
    sleep(1)
    if bytes_receive != bytes_sent:
        print(f"Lost on connection: received - {bytes_receive} b, sent - {bytes_sent} b")
        with open('/mnt/hgfs/os_monitor/log_mem.log', 'a') as log:
            log.write(f'Date {current_time} - Lost on connection: received - {bytes_receive} b, sent - {bytes_sent} \n')
