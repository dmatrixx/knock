import os.path

_ROOT = os.path.abspath(os.path.dirname(__file__))
file = os.path.join(_ROOT, 'FQDN.txt')

def get_subdomains():
    d = []
    with open(file) as f:
        for line in f:
            d.append(line)
    return d
