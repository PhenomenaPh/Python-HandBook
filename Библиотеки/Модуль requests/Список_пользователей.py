import requests


def fetch_users(url: str) -> dict:
    try:
        response = requests.get(url)
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")
        return []


def get_users(users: list) -> list:
    final_store = []

    for user in users:
        final_store.append(f"{user['last_name']} {user['first_name']}")

    return sorted(final_store)


def main():
    url = f"http://{input()}/users"
    response = fetch_users(url)
    sorted_users = get_users(response)

    print("\n".join(sorted_users))


if __name__ == "__main__":
    main()
