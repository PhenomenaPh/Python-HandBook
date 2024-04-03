import requests


def get_data(url):
    response = requests.get(url)
    return response.json()


def main():
    url = f"http://{input()}"

    value = get_data(url)

    try:
        print(value[f"{input()}"])
    except KeyError:
        print("No data")


if __name__ == "__main__":
    main()
