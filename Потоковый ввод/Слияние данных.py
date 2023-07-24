import json


def update_values(original, update):
    for key, value in update.items():
        if value > original.get(key, ''):
            original[key] = value
    return original


def update_json(file1, file2):
    with open(file1, 'r') as user_file, open(file2, 'r') as updates_file:
        users = json.load(user_file)
        updates = json.load(updates_file)

    users_dict = {user['name']: {k: v for k, v in user.items() if k != 'name'} for user in users}

    for update in updates:
        user_name = update.pop('name')
          
        if user_name in users_dict:
            users_dict[user_name] = update_values(users_dict[user_name], update)
        else:
            users_dict[user_name] = update

    with open(file1, 'w') as user_files:
        json.dump(users_dict, user_files)


update_json(input(), input())
