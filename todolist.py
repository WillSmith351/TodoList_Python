import tkinter as tk

# Création de l'interface graphique.
app = tk.Tk()
app.title("Notre To-Do List !")


taches_label = tk.Label(app, text="Tâches à faire", font=("Helvetica", 18), fg="blue", bg="lightgray")
taches_label.pack()

taches_entry = tk.Entry(app, font=("Helvetica", 22))
taches_entry.pack()

valider_button = tk.Button(app, height=2, width=10, text="Enregistrer", command='getEntry')
valider_button.pack()

# Configuration de la fenêtre.
app.geometry('1920x1080')
app.mainloop()