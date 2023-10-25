import tkinter as tk
import json

# Fonction pour sauvegarder les tâches dans un fichier JSON
def sauvegarder_taches():
    with open("taches.json", "w") as fichier:
        json.dump(tasks, fichier)

# Fonction pour charger les tâches depuis un fichier JSON
def charger_taches():
    try:
        with open("taches.json", "r") as fichier:
            tasks = json.load(fichier)
            return tasks
    except FileNotFoundError:
        return []

# Fonction pour ajouter une tâche
def add_task():
    task_description = entry.get()
    if task_description:
        tasks.append({"description": task_description, "completed": False})
        listbox.insert(tk.END, task_description)
        entry.delete(0, tk.END)
        sauvegarder_taches()

# Fonction pour marquer une tâche comme terminée
def mark_task_completed():
    selected_index = listbox.curselection()
    if selected_index:
        index = int(selected_index[0])
        tasks[index]["completed"] = True
        listbox.itemconfig(index, {'bg': 'light green'})
        sauvegarder_taches()

# Fonction pour supprimer une tâche
def delete_task():
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

add_button = tk.Button(app, text="Ajouter une tâche", command=add_task)
add_button.pack()

listbox = tk.Listbox(app, selectmode=tk.SINGLE, height=10, width=40)
listbox.pack(pady=10)

mark_completed_button = tk.Button(app, text="Marquer comme terminée", command=mark_task_completed)
mark_completed_button.pack()

delete_button = tk.Button(app, text="Supprimer la tâche", command=delete_task)
delete_button.pack()

# Remplissage de la liste des tâches depuis la sauvegarde
for task in tasks:
    listbox.insert(tk.END, task["description"])
    if task["completed"]:
        index = tasks.index(task)
        listbox.itemconfig(index, {'bg': 'light green'})

# Boucle principale pour la fenêtre
app.mainloop()
