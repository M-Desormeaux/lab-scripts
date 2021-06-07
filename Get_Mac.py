from getmac import get_mac_address as get_mac
import json

dict_comps = {}
file_lc_computers = 'Computer_Names.txt'

with open(file_lc_computers) as f:
    content = f.read().splitlines()

for x, line in enumerate(content):
    if x == x:
        target = get_mac(hostname=f'{line}')
        dict_comps[line] = (target)

with open('Computers.json', 'w') as json_file:
    json.dump(dict_comps, json_file, indent=4, sort_keys=True)