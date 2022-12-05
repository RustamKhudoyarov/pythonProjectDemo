import re
import subprocess

import psutil
from time import sleep


def read_command_output(command_: str, answer: str):
    all_info = subprocess.check_output(command_, shell=True).decode().strip()
    for line in all_info.split("\n"):
        if answer in line:
            return re.sub(f'.*{answer}.*:', "", line, 1)


def read_file(path: str, answer: str):
    with open(path, "r") as f:
        lines = f.readlines()
        for line in lines:
            if answer in line:
                return re.sub(f'.*{answer}.*:', "", line, 1)


def list_hw_info(checks: list):
    for check in checks:
        print(f'{check[0]}: {check[1]}')


check_list_read_file = [
    ('CPU model from file: ', read_file('/proc/cpuinfo', 'model name')),
    ('Memory info from file: ', read_file('/proc/meminfo', 'MemTotal')),


]
check_list_read_command = [
    ("Machine Hardware architecture: ", read_command_output('uname -m', '')),
    ("Machine Hardware NodeName: ", read_command_output('uname -n', '')),
    ("OS: ", read_command_output('uname -o', '')),
    ('CPU model from command: ', read_command_output('cat /proc/cpuinfo', 'model name')),
    ('VGA model', read_command_output('lspci | grep -E "VGA|3D"', ''))


]

check_list_psutil = [
    ('CPU Info: ', ''),
    ('  CPU usage is: ', psutil.cpu_percent(1)),
    ('  Logical_CPUS: ', psutil.cpu_count()),
    ('  Frequency: ', psutil.cpu_freq()),
    ('Sensors: ', psutil.sensors_temperatures(fahrenheit=False)),
    ('Fans: ', psutil.sensors_fans()),
    ('Battery:', psutil.sensors_battery()),
    ('Users: ', psutil.users()),
    ('Memory: ', ''),
    ('  RAM: ', psutil.virtual_memory()),
    ('  SWAP: ', psutil.swap_memory()),
    ('Disk Drives:', ''),
    ('Size and usage:', psutil.disk_usage('/')),
    ('Network:', ''),
    ('I/O', psutil.net_io_counters(pernic=False, nowrap=True)),
    ('Connections: ', psutil.net_if_addrs())

]

