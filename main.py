import os
import keyboard
import time
import subprocess
import tkinter as tk
from threading import Thread

version = "v0.4.5"
keyboardextensionstate = False

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
        root.title("Keycut Function Form")

        tk.Label(root, text="What keycut:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        keycut_entry = tk.Entry(root, width=30)
        keycut_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(root, text="What function:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        function_entry = tk.Entry(root, width=30)
        function_entry.grid(row=1, column=1, padx=10, pady=5)

        def submit():
            print("Keycut:", keycut_entry.get())
            print("Function:", function_entry.get())
            root.destroy()

        submit_button = tk.Button(root, text="Submit", command=submit)
        submit_button.grid(row=2, columnspan=2, pady=10)

        root.mainloop()

    Thread(target=show_form).start()

def main():
    print("Démarrage du programme version", version)
    keyboard.add_hotkey('ctrl+k+x', set_keyboard_extension_state)
    keyboard.add_hotkey('ctrl+shift+a', action)
    keyboard.add_hotkey('ctrl+alt+g+p', create_git_project)
    keyboard.add_hotkey('ctrl+alt+b+p', create_basic_project)
    keyboard.add_hotkey('ctrl+shift+k', open_form)
    keyboard.add_hotkey('esc', lambda: exit())

    while True:
        time.sleep(0.1)

if __name__ == "__main__":
    main()
