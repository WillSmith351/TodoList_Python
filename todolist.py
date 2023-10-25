import tkinter as tk
from tkinter import ttk, messagebox
import json

# Création de l'interface graphique.
app = tk.Tk()
app.title('To-Do List')

# Création du fichier JSON
fichier_json = 'database.json'
try:
    with open(fichier_json, 'r') as fichier:
        data = json.load(fichier)
except (json.JSONDecodeError, FileNotFoundError):
    data = {}

# Enregistrement des données dans le fichier JSON
def enregistrer_donnees():
    tache = taches_entry.get()
    date = date_entry.get()
    data[tache] = {'date': date, 'status': 'en cours'}
    with open(fichier_json, 'w') as fichier:
        json.dump(data, fichier)
    messagebox.showinfo("Succès", "Données enregistrées avec succès !")
    afficher_taches()

# Affichage de toutes les tâches
def afficher_taches():
    with open(fichier_json, 'r') as fichier:
        data = json.load(fichier)
        taches_combobox['values'] = [f"Tâche : {tache} - Date : {data[tache]['date']} - Statut : {data[tache]['status']}" for tache in data]

# Suppression de toutes les données dans le fichier JSON
def supprimer_tout():
    choice = messagebox.askyesno("Confirmation", "Voulez-vous vraiment supprimer toutes les données ?")
    delete_all_data(choice)

def delete_all_data(choice):
    if choice:
        with open(fichier_json, 'w') as fichier:
            json.dump({}, fichier)
        messagebox.showinfo("Succès", "Toutes les données ont été supprimées !")
        afficher_taches()
    else:
        messagebox.showinfo("Information", "Aucune donnée n'a été supprimée !")

# Création des labels, boutons et input.
taches_label = tk.Label(app, text="Tâches à faire", font=("Helvetica", 18), fg="blue")
taches_label.pack()
taches_entry = tk.Entry(app, font=("Helvetica", 22), width=30)
taches_entry.pack()

date_label = tk.Label(app, text="Date d'échéance (jour/mois/année)", font=("Helvetica", 18), fg="blue")
date_label.pack()
date_entry = tk.Entry(app, font=("Helvetica", 22), width=30)
date_entry.pack()

valider_button = tk.Button(app, text="Valider", font=("Helvetica", 16), bg="green", fg="white", width=13, command=enregistrer_donnees)
valider_button.pack()

supprimer_button = tk.Button(app, text="Supprimer tout", font=("Helvetica", 16), bg="red", fg="white", width=13, command=supprimer_tout)
supprimer_button.pack()

terminer_button = tk.Button(app, text="Tâche terminée", font=("Helvetica", 16), bg="white", fg="black", width=13)
terminer_button.pack()

taches_combobox = ttk.Combobox(app, font=("Helvetica", 14), width=50)
taches_combobox.pack()

# Configuration de la fenêtre.
app.geometry('1920x1080')
app.mainloop()
