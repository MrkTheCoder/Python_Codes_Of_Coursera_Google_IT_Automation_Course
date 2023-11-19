#!/usr/bin/env python3
import shutil
import psutil

MIN_HEALTHY_DISK_FREE_SPACE = 20
MAX_HEALTHY_CPU_USAGE = 75


def check_disk_usage(disk):
    ds = shutil.disk_usage(disk)
    du = ds.free / ds.total * 100
    return (du, du > MIN_HEALTHY_DISK_FREE_SPACE)


def check_cpu_usage():
    cu = psutil.cpu_percent(1)
    return (cu, cu < MAX_HEALTHY_CPU_USAGE)


all_partitions_health_stats = [(pa.mountpoint, check_disk_usage(pa.device))
                               for pa in psutil.disk_partitions(all=False) if pa.opts.find('rw') != -1]

if any(not healthy for _, (_, healthy) in all_partitions_health_stats):
    for pa, (du, healthy) in all_partitions_health_stats:
        if not healthy:
            print(f"{pa} has {du:.2f}% only free space.")
else:
    print('All partitions have enough free space.')


cpu_usage, is_cpu_healthy = check_cpu_usage()
if not is_cpu_healthy:
    print(f'CPU is so busy at {cpu_usage}%!')
else:
    print(f'CPU is working properly at {cpu_usage}%.')

print('-' * 20)
print("Partitions stats:")
for pa, (_, healthy) in all_partitions_health_stats:
    print(f"Partition: '{pa}' Space Used: '{psutil.disk_usage(
        pa).percent:>5.2f}'%{' Not Healthy' if not healthy else ''}")
