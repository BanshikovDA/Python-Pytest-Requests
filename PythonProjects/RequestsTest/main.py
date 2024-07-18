import requests

URL = 'https://api.pokemonbattle.ru/v2/'
TOKEN = 'user_token'
HEADER = {'Content-Type': 'application/json', 'trainer_token' : TOKEN}

body_registration = {
    "trainer_token": TOKEN,
    "email": "user_email",
    "password": "user_pass"
}

body_confirmation = {
    "trainer_token": TOKEN
}

body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}

'''response_registration = requests.post(url=f'{URL}trainers/reg', headers=HEADER, json=body_registration)
print(response_registration.text)

response_confirmation = requests.post(url=f'{URL}trainers/confirm_email', headers=HEADER, json=body_confirmation)
print(response_confirmation.text)'''

response_create = requests.post(url=f'{URL}pokemons', headers=HEADER, json=body_create)
print(response_create.text)

message = response_create.json()['message']
print(message)

