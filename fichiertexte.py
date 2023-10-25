import json

donnees = {
    "nom": "jean",
    "age": 30,
    "ville": "Paris",
    "emplois": ["developpeur", "analyste"]
}

fichier_json = 'database.json'

with open(fichier_json, 'w') as fichier:
    json.dump(donnees, fichier, indent=4)

print("Les données ont été enregistrées")

# Suppression de toutes les données de l'utilisateur dans le fichier JSON.
def delete_all_data(choice):
    if choice == 'true':
        with open(fichier_json, 'w') as fichier:
            json.dump({}, fichier)
        print("Toutes les données ont été supprimées !")
    elif choice == 'false':
        print("Aucune donnée n'a été supprimée !")
    else:
        print("Aucune donnée n'a été supprimée !")

delete_all_data('false')