#--------------------------------------quel est son type ? ---------------------------------------------#

import requests

print("🎮 Akinator Pokémon")
print("Pense à un Pokémon.\n")

# 1. Récupérer la liste des types
url_types = "https://pokeapi.co/api/v2/type"
reponse = requests.get(url_types)
donnees_types = reponse.json()

types = donnees_types["results"]

# 2. Affichage des types
print("Quel est le type de ton Pokémon ?\n")
for i in range(len(types)):
    print(i + 1, "-", types[i]["name"])

# 3. Choix utilisateur
choix = int(input("\nNuméro du type : "))

# 4. Récupération du type choisi
url_type = types[choix - 1]["url"]
donnees_type = requests.get(url_type).json()

# 5. Liste des espèces correspondantes
especes = []

for pokemon in donnees_type["pokemon"]:
    url_pokemon = pokemon["pokemon"]["url"]
    donnees_pokemon = requests.get(url_pokemon).json()
    nom_espece = donnees_pokemon["species"]["name"]

    if nom_espece not in especes:
        especes.append(nom_espece)

# 6. Résultat
print("\n Il reste", len(especes), "Pokémon possibles.")
print("Quelques exemples :")
for i in range(min(10, len(especes))):
    print("-", especes[i])
