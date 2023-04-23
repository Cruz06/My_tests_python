import pytest
import requests

# site https://restful-booker.herokuapp.com/apidoc/index.html

BASE_URL = "https://restful-booker.herokuapp.com/booking"
AUTH_URL = "https://restful-booker.herokuapp.com/auth"
STATUS_OK = 200


@pytest.fixture(scope='module')
def auth_token():
    payload = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(AUTH_URL, json=payload)
    response_data = response.json()
    token = response_data['token']
    assert response.status_code == STATUS_OK
    yield token


@pytest.fixture(scope='module')
def booking_id():
    payload = {
        "firstname": "Alla",
        "lastname": "Claret",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2023-01-01",
            "checkout": "2023-02-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(BASE_URL, json=payload)
    booking_id = response.json()['bookingid']
    assert response.status_code == STATUS_OK
    response_get = requests.get(f'{BASE_URL}/{booking_id}')
    assert response_get.status_code == STATUS_OK
    yield booking_id


def test_get_all_bookings():
    response = requests.get(BASE_URL)
    assert response.status_code == STATUS_OK
    print(f'\n(response.headers)')
    print(response.json())


def test_get_all_requisites():
    response = requests.get(BASE_URL)
    assert response.status_code == STATUS_OK
    headers = ('Connection', 'keep-alive')
    assert headers in response.headers.items()


def test_get_how_many_requests():
    response = requests.get(BASE_URL)
    print(f'\n{len(response.json())}')
    assert response.status_code == STATUS_OK
    key = 'Connection'
    assert key in response.headers

def test_get_booking_with_id():
    response = requests.get(f'{BASE_URL}/1')
    response_data = response.json()
    print(f'\n{response_data}')


def test_get_booking_with_name():
    response = requests.get(f'{BASE_URL}/1')
    response_data = response.json()
    # assert response_data['firstname'] == 'Sally'
    print(f'\n{response_data}')


def test_get_booking_many_keys():  # check: эти поля есть в запросе Nr.1
    response = requests.get(f'{BASE_URL}/1')
    response_data = response.json()
    expected_keys = ['firstname', 'lastname', 'totalprice', 'depositpaid']
    for key in expected_keys:
        assert key in response_data.keys()
    print(f'\n{response_data}')


def test_create_booking(booking_id):
    response = requests.get(f'{BASE_URL}/{booking_id}')
    assert response.status_code == STATUS_OK
    assert response.json()['firstname'] == 'Alla'


def test_user_authorization():
    payload = {
    "username" : "admin",
    "password" : "password123"
    }
    response = requests.post(f'{AUTH_URL}', json=payload)
    response_data = response.json()
    print(response)
    assert response.status_code == STATUS_OK
    assert 'token' in response_data


def test_update_booking(booking_id, auth_token):
    payload = {
        "firstname": "Alla",
        "lastname": "Claret",
        "totalprice": 222,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2022-01-01",
            "checkout": "2022-02-01"
        },
        "additionalneeds": "Lunch"
    }
    headers = {'Cookie': f'token={auth_token}'}
    response = requests.put(f'{BASE_URL}/{booking_id}', json=payload, headers=headers)
    assert response.status_code == STATUS_OK

    response_get = requests.get(f'{BASE_URL}/{booking_id}')
    response_data = response_get.json()
    assert response_data['totalprice'] == payload['totalprice']
    assert response_data['additionalneeds'] == payload['additionalneeds']


def test_update_patch_booking(booking_id, auth_token):
    payload = {
        "firstname": "Alla New",
        "additionalneeds": "Dinner"
    }
    headers = {'Cookie': f'token={auth_token}'}
    response = requests.patch(f'{BASE_URL}/{booking_id}', json=payload, headers=headers)
    assert response.status_code == STATUS_OK

    response_get = requests.get(f'{BASE_URL}/{booking_id}')
    response_data = response_get.json()
    assert response_data['firstname'] == payload['firstname']
    assert response_data['additionalneeds'] == payload['additionalneeds']


def test_delete_booking(booking_id, auth_token):
    headers = {'Cookie': f'token={auth_token}'}
    response = requests.delete(f'{BASE_URL}/{booking_id}', headers=headers)
    assert response.status_code == 201
    response_get = requests.get(f'{BASE_URL}/{booking_id}')
    assert response_get.status_code == 404