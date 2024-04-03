import requests
from sys import stdin
import json


def main():

    url = f"http://{input()}/users/{int(input())}"
    user_data = stdin.read().splitlines()
    user_dict = {
        param: value for param, value in [line.split("=") for line in user_data]
    }

    requests.put(url, data=json.dumps(user_dict))


if __name__ == "__main__":
    main()
