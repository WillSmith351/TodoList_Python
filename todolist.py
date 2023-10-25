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


taches_label = tk.Label(app, text="Tâches à faire", font=("Helvetica", 18), fg="blue", bg="lightgray")
taches_label.pack()

taches_entry = tk.Entry(app, font=("Helvetica", 22))
taches_entry.pack()

valider_button = tk.Button(app, height=2, width=10, text="Enregistrer", command='getEntry')
valider_button.pack()

# Configuration de la fenêtre.
app.geometry('1920x1080')
app.mainloop()