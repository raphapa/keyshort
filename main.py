import os
import keyboard
import time
import subprocess
version = "v0.4"
keyboardextensionstate = False

def set_keyboard_extension_state():
    global keyboardextensionstate
    keyboardextensionstate = not keyboardextensionstate

def action():
    global keyboardextensionstate
    if keyboardextensionstate:
        print("Action triggered!")
def create_git_project():
    global keyboardextensionstate
    if keyboardextensionstate:
        base_path = os.path.expanduser("~/Desktop")
        project_path = os.path.join(base_path, "GitProject")

        try:
            os.makedirs(project_path, exist_ok=True)

            # Initialisation du dépôt Git
            subprocess.run(["git", "init"], cwd=project_path)

            # Création optionnelle d'un README.md vide
            with open(os.path.join(project_path, "README.md"), "w") as f:
                f.write("# GitProject\n\nProjet initialisé automatiquement.\n")

            print("✅ Dépôt Git initialisé dans :", project_path)

        except Exception as e:
            print("Erreur lors de la création du Git Project :", e)

def create_basic_project():
    global keyboardextensionstate
    if keyboardextensionstate:
        base_path = os.path.expanduser("~/Desktop")
        project_path = os.path.join(base_path, "BasicProject")

        try:
            os.makedirs(project_path, exist_ok=True)

            # Créer les sous-dossiers v1 à v10
            for i in range(1, 11):
                os.makedirs(os.path.join(project_path, f"v{i}"), exist_ok=True)

            # Créer les sous-dossiers vdef-beta et vdef-fin
            os.makedirs(os.path.join(project_path, "vdef-beta"), exist_ok=True)
            os.makedirs(os.path.join(project_path, "vdef-fin"), exist_ok=True)

            # Message d'information sans emoji
            print("Projet basique créé dans :", project_path)

        except Exception as e:
            print("Erreur lors de la création du projet :", e)

func = [set_keyboard_extension_state, action]

def main(*args):
    print("Démarrage du programme version", version)
    keyboard.add_hotkey('ctrl+shift+a', func[1])
    keyboard.add_hotkey('ctrl+k+x', func[0])
    keyboard.add_hotkey('ctrl+alt+g+p', create_git_project)
    keyboard.add_hotkey('ctrl+alt+b+p', create_basic_project)
    keyboard.add_hotkey('esc', lambda: exit())

    while True:
        time.sleep(0.1)

if __name__ == "__main__":
    main()
