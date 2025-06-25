import os
import keyboard
import time
import subprocess
import tkinter as tk
from threading import Thread

version = "v0.5"
keyboardextensionstate = False

# Liste des raccourcis et fonctions
func = []

def set_keyboard_extension_state():
    global keyboardextensionstate
    keyboardextensionstate = not keyboardextensionstate
    print("Keyboard extension state is now:", keyboardextensionstate)

def action():
    global keyboardextensionstate
    if keyboardextensionstate:
        print("Action triggered!")

def create_git_project():
    if keyboardextensionstate:
        base_path = os.path.expanduser("~/Desktop")
        project_path = os.path.join(base_path, "GitProject")
        try:
            os.makedirs(project_path, exist_ok=True)
            subprocess.run(["git", "init"], cwd=project_path)
            with open(os.path.join(project_path, "README.md"), "w") as f:
                f.write("# GitProject\n\nProjet initialisé automatiquement.\n")
            print("✅ Dépôt Git initialisé dans :", project_path)
        except Exception as e:
            print("Erreur :", e)

def create_basic_project():
    if keyboardextensionstate:
        base_path = os.path.expanduser("~/Desktop")
        project_path = os.path.join(base_path, "BasicProject")
        try:
            os.makedirs(project_path, exist_ok=True)
            for i in range(1, 11):
                os.makedirs(os.path.join(project_path, f"v{i}"), exist_ok=True)
            os.makedirs(os.path.join(project_path, "vdef-beta"), exist_ok=True)
            os.makedirs(os.path.join(project_path, "vdef-fin"), exist_ok=True)
            print("Projet basique créé dans :", project_path)
        except Exception as e:
            print("Erreur :", e)

def open_form():
    def show_form():
        root = tk.Tk()
        root.title("Ajouter un raccourci clavier")

        tk.Label(root, text="Raccourci clavier (ex: ctrl+alt+k):").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        keycut_entry = tk.Entry(root, width=40)
        keycut_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(root, text="Code à exécuter (ex: print('Hello')):").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        function_entry = tk.Entry(root, width=40)
        function_entry.grid(row=1, column=1, padx=10, pady=5)

        def submit():
            keycut = keycut_entry.get()
            code = function_entry.get()

            # Enregistrement dans .keycut
            try:
                with open(".keycut", "a") as file:
                    file.write("-/-/-/z\n")
                    file.write(f"{keycut}\n")
                    file.write(f"{code}\n")
                print(f"✅ Ajouté dans .keycut : {keycut} → {code}")
            except Exception as e:
                print("Erreur d'écriture dans .keycut :", e)

            # Ajout dynamique dans func
            func.append([keycut, lambda code=code: exec(code)])
            keyboard.add_hotkey(keycut, func[-1][1])
            root.destroy()

        tk.Button(root, text="Ajouter", command=submit).grid(row=2, columnspan=2, pady=10)
        root.mainloop()

    Thread(target=show_form).start()

def main():
    print("Démarrage du programme version", version)

    # Raccourcis clavier statiques
    func.extend([
        ['ctrl+k+x', set_keyboard_extension_state],
        ['ctrl+shift+a', action],
        ['ctrl+alt+g+p', create_git_project],
        ['ctrl+alt+b+p', create_basic_project],
        ['ctrl+shift+k', open_form],
    ])

    # Enregistrement des hotkeys
    for shortcut, function in func:
        keyboard.add_hotkey(shortcut, function)

    # Sortie rapide
    keyboard.add_hotkey('esc', lambda: exit())

    while True:
        time.sleep(0.1)

if __name__ == "__main__":
    main()
