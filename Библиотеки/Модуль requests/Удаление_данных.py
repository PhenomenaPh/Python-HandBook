import requests


def main():

    url = f"http://{input()}/users/{int(input())}"

    requests.delete(url)


if __name__ == "__main__":
    main()
