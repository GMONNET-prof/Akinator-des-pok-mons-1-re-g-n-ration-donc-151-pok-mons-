import requests
import json

api = "https://pokeapi.co/api/v2/generation/1/" # lien de l'API

dictionnaireAPI = requests.get(api) # requests.get = récupère le json de l'API (sous forme d'objet illisible ni par python ni par l'humain)
print(dictionnaireAPI)
input()

dictionnaireAPI = requests.get(api).json() # convertit le json en dictionnaire python
print(dictionnaireAPI)
input()

print("\n"*20 + dictionnaireAPI["pokemon_species"][0]["name"]) # print le nom du premier pokemon
input()

for i in range(10):
    print(dictionnaireAPI["pokemon_species"][i]["name"]) # print les 10 premiers pokemons
input()

url_premier_pokemon = dictionnaireAPI["pokemon_species"][0]["url"] # récupère l'url associé au premier pokémon
print(url_premier_pokemon)
bulbasaur = requests.get(url_premier_pokemon).json() # récupère le json de l'url et le converti en dictionnaire python
input()

print(bulbasaur["color"]["name"]) # print la couleur du premier pokemon via l'url associé à celui ci
input()

# EXEMPLE

exemple = []

for i in range(20):
    nom = dictionnaireAPI["pokemon_species"][i]["name"] # nom du pokemon numero i
    couleur = requests.get(dictionnaireAPI["pokemon_species"][i]["url"]).json()["color"]["name"] # couleur du pokemon numero i obtenue via l'url associé à celui ci
    print(nom, couleur)
    exemple.append({ # création d'un dictionnaire qu'on append pour chaque pokemon avec pour clé son nom et sa couleur
        "nom":nom,
        "couleur":couleur,
    })
for d in exemple:
    print(d)