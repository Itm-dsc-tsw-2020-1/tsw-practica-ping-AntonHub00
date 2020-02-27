import os

hosts_amount = 0

for host in range(1, 255):
    hosts_amount += 1 if not os.system(f'ping -c 1 200.33.171.{host}') else 0

print(f'There are {hosts_amount} hosts!')
