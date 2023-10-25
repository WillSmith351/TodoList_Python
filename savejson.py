import tkinter as tk
import json

# Fonction pour sauvegarder les tâches dans un fichier JSON
def sauvegarder_taches():
    with open("database.json", "w") as fichier:
        json.dump(tasks, fichier)

# Fonction pour charger les tâches depuis un fichier JSON
def charger_taches():
    try:
        with open("database.json", "r") as fichier:
            taches = json.load(fichier)
            return taches
    except FileNotFoundError:
        return []

# Fonction pour ajouter une tâche
def ajouter_taches():
    description_tache = entry.get()
    if description_tache:
        tasks.append({"description": description_tache, "completed": False})
        listbox.insert(tk.END, description_tache)
        entry.delete(0, tk.END)
        sauvegarder_taches()

# Fonction pour marquer une tâche comme terminée
def taches_terminer():
    selected_index = listbox.curselection()
    if selected_index:
        index = int(selected_index[0])
        tasks[index]["completed"] = True
        listbox.itemconfig(index, {'bg': 'light green'})
        sauvegarder_taches()

# Fonction pour supprimer une tâche
def suppression_taches():
    selected_index = listbox.curselection()
    if selected_index:
        index = int(selected_index[0])
        listbox.delete(index)
        del tasks[index]
        sauvegarder_taches()

# Création de la fenêtre principale
app = tk.Tk()
app.title("Gestionnaire de Tâches Personnelles")

# Chargement des tâches depuis le fichier JSON
tasks = charger_taches()

# Création des widgets
entry = tk.Entry(app, width=40)
entry.pack(pady=10)

add_button = tk.Button(app, text="Ajouter une tâche", command=ajouter_taches)
add_button.pack()

listbox = tk.Listbox(app, selectmode=tk.SINGLE, height=10, width=40)
listbox.pack(pady=10)

mark_completed_button = tk.Button(app, text="Marquer comme terminée", command=taches_terminer)
mark_completed_button.pack()

delete_button = tk.Button(app, text="Supprimer la tâche", command=suppression_taches)
delete_button.pack()

# Remplissage de la liste des tâches depuis la sauvegarde
for task in tasks:
    listbox.insert(tk.END, task["description"])
    if task["completer"]:
        index = tasks.index(task)
        listbox.itemconfig(index, {'bg': 'light green'})

# Boucle principale pour la fenêtre
app.mainloop()








delete_button_tache = tk.Button(app, text="Supprimer la tâche sélectionnée", command=supprimer_tache)
delete_button_tache.pack()
listbox = tk.Listbox(app, selectmode=tk.SINGLE, height=10, width=40)
listbox.pack(pady=10)


tache = afficher_taches()






