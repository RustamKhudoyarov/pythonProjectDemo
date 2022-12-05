import time
from datetime import datetime
import psutil
from time import sleep

current_time = datetime.now()


def collect_log_by_mem_cpu():
    for i in range(60):
        cpu_usage = psutil.cpu_percent(1)
        memory_usage = psutil.virtual_memory()[2]
        print(memory_usage, cpu_usage)
        sleep(1)

        if memory_usage > 20.4:
            print(f'Mem usage more then 20%')
            with open('/mnt/hgfs/os_monitor/log_mem.log', 'a') as log:
                log.write(f'Date: {current_time} - Memory usage more then 20% - {memory_usage}\n')

        if cpu_usage > 0.4:
            print(f'CPU usage more then 80% ')
            with open('/mnt/hgfs/os_monitor/log_mem.log', 'a') as log:
                log.write(f'Date: {current_time} - CPU usage more then 80% - {cpu_usage}\n')


collect_log_by_mem_cpu()
