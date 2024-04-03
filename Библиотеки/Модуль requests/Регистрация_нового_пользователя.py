import requests
import json


def main():

    url = f"http://{input()}/users"
    username = input()
    last_name = input()
    first_name = input()
    email = input()

    data = {
        "username": username,
        "last_name": last_name,
        "first_name": first_name,
        "email": email,
    }

    requests.post(url, data=json.dumps(data))


if __name__ == "__main__":
    main()
