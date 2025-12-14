import requests
import json
import os

def get_gen1_pokemon():
    gen1 = "https://pokeapi.co/api/v2/generation/1/"

    print("╭"+5*"─"+"┬"+17*"─"+"┬"+22*"─"+"┬"+12*"─"+"┬"+22*"─"+"┬"+22*"─"+"┬"+22*"─"+"┬"+22*"─"+"┬"+22*"─"+"╮")
    print("│"+"  id "+"│"+" nom             "+"│"+" nom français        "+" │ "+" couleur  "+" │ "+" 1ere evo           "+" │ "+" 2eme evo           "+" │ "+" 3eme evo           "+" │ "+" habitat            "+" │ "+" habitat français   "+" │")
    print("├"+5*"─"+"┼"+17*"─"+"┼"+22*"─"+"┼"+12*"─"+"┼"+22*"─"+"┼"+22*"─"+"┼"+22*"─"+"┼"+22*"─"+"┼"+22*"─"+"┤")


    results = []

    species = requests.get(gen1).json()
    for i, sp in enumerate(species["pokemon_species"]):
        name = sp["name"] # Cherche le nom dans https://pokeapi.co/api/v2/generation/1/

#####################################################################################################

        attr = requests.get(sp["url"]).json() # Cherche l'url attaché au pokemon sp["name"]
        color = attr["color"]["name"] # Dans cette url, cherche la couleur du pokemon sp["name"]
        fr_name = attr["names"][4]["name"] # Dans cette url, cherche la traducion du nom en français du pokemon sp["name"]
        habitat = attr["habitat"]["name"] # Dans cette url, cherche l'habitat du pokemon sp["name"]
        habitat_attr = requests.get(attr["habitat"]["url"]).json() # Va cherche l'url de l'habitat pour avoir ses traductions
        fr_habitat = habitat_attr["names"][0]["name"] # Dans cette url, cherche l'habitat en français du pokemon sp["name"]

#####################################################################################################

        try: # Essaye d'obtenir chaque évolution si elle existe, sinon écrit "aucune"
            evolutions = requests.get(attr["evolution_chain"]["url"]).json()
            first = evolutions["chain"]["species"]["name"]
            second = evolutions["chain"]["evolves_to"][0]["species"]["name"]
            third = evolutions["chain"]["evolves_to"][0]["evolves_to"][0]["species"]["name"]
        except (IndexError, KeyError, TypeError):
            first = second = third = "aucune"

#####################################################################################################

        print(f"│ {i:>3} │ {name:<15} │ {fr_name:<20} │ {color:<10} │ {first:<20} │ {second:<20} │ {third:<20} │ {habitat:<20} │ {fr_habitat:<20} │")

        results.append({
            "id": i,
            "name": name,
            "fr_name": fr_name,
            "color": color,
            "evos": [first,second,third],
            "habitat": habitat,
            "fr_habitat": fr_habitat
        }) # Append chaque valeur dans une liste en tant que dictionnaire


    print("╰"+5*"─"+"┴"+17*"─"+"┴"+22*"─"+"┴"+12*"─"+"┴"+22*"─"+"┴"+22*"─"+"┴"+22*"─"+"┴"+22*"─"+"┴"+22*"─"+"╯")
    return results


gen1 = get_gen1_pokemon() # Execute la fonction

output_path = os.path.join(os.path.dirname(__file__), "gen1.json")

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(gen1, f, indent=4, ensure_ascii=False)
