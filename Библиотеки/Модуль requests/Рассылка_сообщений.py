import requests as rq
from sys import stdin


def fetch_user(url: str) -> dict:
    try:
        response = rq.get(url)
        response.raise_for_status()
        user_data = response.json()
        return user_data

    except rq.exceptions.HTTPError:
        print(f"Пользователь не найден")


def main():
    url = f"http://{input()}/users/{int(input())}"

    try:
        response = fetch_user(url)
        text = stdin.read()
        formatted_text = text.format_map(response)
        print(formatted_text)

    except KeyError:
        print("Пользователь не найден")


if __name__ == "__main__":
    main()
