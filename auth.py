from sanic_jwt import exceptions
import csv


def authenticate_csv(request, *args, **kwargs):
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    found_user = None

    if not username or not password:
        raise exceptions.AuthenticationFailed("Missing username or password.")

    with open('users.csv', newline='') as csv_file:
        users_reader = csv.reader(csv_file, delimiter=',')
        for row in users_reader:
            _username, _password = row
            if username == _username and password == _password:
                found_user = {'user_id': username}
                break
    if found_user:
        return found_user
    raise exceptions.AuthenticationFailed("Bad username or password.")