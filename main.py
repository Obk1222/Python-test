#import requests # Создать покемона ПЕРВЫЙ ТЕСТ

#URL = 'https://api.pokemonbattle.ru/v2' 
#TOKEN = 'c0dbeddcccdcd7ade91c1878c963b570'
#HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}
#create_pokemon = {
#    "name": "Kerya",
#    'photo_id': '-1'
#}

#respons = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = create_pokemon,)
#print(respons.json)





#import requests # Изменить имя покемона ВТОРОЙ ТЕСТ

#URL = 'https://api.pokemonbattle.ru/v2' 
#TOKEN = 'c0dbeddcccdcd7ade91c1878c963b570'
#HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN,}
#body_requests = {
#    "pokemon_id": "323415",
#    "name": "Чиназес",
#    "photo_id": 22
#}

#respons = requests.put(url = f'{URL}/pokemons', headers = HEADER,  json = body_requests)
#print(respons.text)



import requests # поймать покемона в покебол ТРЕТИЙ ТЕСТ

URL = 'https://api.pokemonbattle.ru/v2' 
TOKEN = 'c0dbeddcccdcd7ade91c1878c963b570'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}
pokemon_id = {
    "pokemon_id": "323415"
}

respons = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = pokemon_id)
print(respons.json)






#import requests # Удалить покемона

#URL = 'https://api.pokemonbattle.ru/v2' 
#TOKEN = 'c0dbeddcccdcd7ade91c1878c963b570'
#HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}
#pokemon_id = {
#    "pokemon_id": "278026"
#}

#respons = requests.post(url = f'{URL}/pokemons/knockout', headers = HEADER, json = pokemon_id)
#print(respons.json)
