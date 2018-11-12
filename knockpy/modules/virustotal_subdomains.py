import os.path

from datetime import datetime

now = datetime.now()
day = str(now.day)+"-"+str(now.month)+"-"+str(now.year)
root = '/home/ubuntu/asset'
file = os.path.join(root, target, day,'FQDN.txt')

def get_subdomains():
    d = []
    with open(file) as f:
        for line in f:
            d.append(line.replace('\n',''))
    return d
