import requests


url = input()

values = 0
while True:
    responce = requests.get(f"http://{url}")
    value = int(responce.content.decode())
    if value == 0:
        break
    else:
        values += value

print(values)
