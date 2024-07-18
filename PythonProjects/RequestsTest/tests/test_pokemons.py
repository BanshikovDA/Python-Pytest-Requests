import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2/'
TOKEN = 'user_token'
HEADER = {'Content-Type': 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '6524'

def test_status_code():
    response = requests.get(url = f'{URL}pokemons', params={'trainer_id': TRAINER_ID}, headers=HEADER)
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}pokemons', params = {'trainer_id': TRAINER_ID})
    assert response_get.json()["data"][0]["name"] == 'Бульбазавр'

@pytest.mark.parametrize('key, value', [{'name', 'Бульбазавр'}, ('trainer_id', TRAINER_ID), ('id', '43969')])
def test_parametrize(key, value):
    response_parametrize = requests.get(url = f'{URL}pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response_parametrize.json()["data"][0][key] == value
