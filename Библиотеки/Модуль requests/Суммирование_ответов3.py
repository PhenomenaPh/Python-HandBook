import requests
from sys import stdin


def fetch_content(url: str) -> list:
    response = requests.get(url)
    return response.json()


def accumulate_values(server: str, paths: list) -> int:
    total_values = 0

    for path in paths:
        url = f"http://{server}/{path}"
        values = fetch_content(url)

        for value in values:
            if isinstance(value, int):
                total_values += value

    return total_values


def main():
    input_values = stdin.read().splitlines()
    server_ip = input_values[0]
    paths = input_values[1:]

    try:
        total_values = accumulate_values(server_ip, paths)
        print(total_values)
    except requests.exceptions.ConnectionError:
        print("Connection error")


if __name__ == "__main__":
    main()
