import requests


def fetch_content(url: str) -> list:
    response = requests.get(url)
    return response.json()


def accumulate_values(values: list) -> int:
    total_values = 0

    try:
        for value in values:
            if isinstance(value, int):
                total_values += value
    except TypeError:
        raise TypeError("Invalid data type")

    return total_values


def main():

    url = f"http://{input()}"
    container = fetch_content(url)
    total_values = accumulate_values(container)

    print(total_values)


if __name__ == "__main__":
    main()
