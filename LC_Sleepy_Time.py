from subprocess import run
import json

with open("LC_Computers.json") as file:
    data = json.load(file)

for name in data.keys():
    run("shutdown /s /t 0 /m \\\\" + name, shell=True)
    print(name + " Shutting Down...")

print("All Machines Have Shutdown...")