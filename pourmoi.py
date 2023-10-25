import tkinter as tk

# Création de l'interface graphique.
app = tk.Tk()
app.title("Notre To-Do List !")


# Ajouter une tâche
taches_label = tk.Label(app, text="Tâches à faire", font=("Helvetica", 18), fg="blue")
taches_label.pack()
taches_entry = tk.Entry(app, font=("Helvetica", 22), width=30)
taches_entry.pack()

#Ajouter une date d'échéance pour la tâche
date_label = tk.Label(app, text="Date d'échéance", font=("Helvetica", 18), fg="blue")
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


# Configuration de la fenêtre.
app.geometry('1920x1080')
app.mainloop()