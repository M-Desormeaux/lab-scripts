from wakeonlan import send_magic_packet
import json

with open("LC_Computers.json") as file:
    data = json.load(file)

for address in data.values():
    send_magic_packet(address)

print("All Machines Have Been Woken Up...")