import tkinter as tk
import json


# Création de l'interface graphique.
app = tk.Tk()
app.title('To-Do List')

# Création du fichier JSON
fichier_json = 'database.json'

# Suppression de toutes les données de l'utilisateur dans le fichier JSON.
def delete_all_data(choice):
    if choice == 'true':
        with open(fichier_json, 'w') as fichier:
            json.dump({}, fichier)
        print("Toutes les données ont été supprimées !")
    elif choice == 'false':
        print("Aucune donnée n'a été supprimée !")


# ~~ Utilisation de nos fonctions ~~

delete_all_data('true')

# Configuration de la fenêtre.
app.geometry('1920x1080')
app.mainloop()