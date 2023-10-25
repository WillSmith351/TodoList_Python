import tkinter as tk
import json


# Création de l'interface graphique.
app = tk.Tk()
app.title('To-Do List')

# Création du fichier JSON
fichier_json = 'database.json'

# Ajouter une tâche
taches_label = tk.Label(app, text="Tâches à faire", font=("Helvetica", 18), fg="blue")
taches_label.pack()
taches_entry = tk.Entry(app, font=("Helvetica", 22), width=30)
taches_entry.pack()

#Ajouter une date d'échéance pour la tâche
date_label = tk.Label(app, text="Date d'échéance (jour/mois/année)", font=("Helvetica", 18), fg="blue")
date_label.pack()
date_entry = tk.Entry(app, font=("Helvetica", 22), width=30)
date_entry.pack()


# Boutton valider
valider_button = tk.Button(app, text="Valider", font=("Helvetica", 16), bg="green", fg="white", width=13)
valider_button.pack()

# Boutton supprimer
supprimer_button = tk.Button(app, text="Supprimer", font=("Helvetica", 16), bg="red", fg="white", width=13)
supprimer_button.pack()

# Boutton Terminer
terminer_button = tk.Button(app, text="Tâche terminée", font=("Helvetica", 16), bg="white", fg="black", width=13)
terminer_button.pack()

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