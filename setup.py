import os
import subprocess
import shutil

code_source = '''import os
import keyboard
import time
import subprocess
import tkinter as tk
from threading import Thread

version = "v0.5"
keyboardextensionstate = False

func = []

def set_keyboard_extension_state():
    global keyboardextensionstate
    keyboardextensionstate = not keyboardextensionstate

def create_git_project():
    if keyboardextensionstate:
        base_path = os.path.expanduser("~/Desktop")
        project_path = os.path.join(base_path, "GitProject")
        try:
            os.makedirs(project_path, exist_ok=True)
            subprocess.run(["git", "init"], cwd=project_path)
            with open(os.path.join(project_path, "README.md"), "w") as f:
                f.write("# GitProject\\n\\nProjet initialisé automatiquement.\\n")
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

            try:
                with open(".keycut", "a") as file:
                    file.write("-/-/-/z\\n")
                    file.write(f"{keycut}\\n")
                    file.write(f"{code}\\n")
                print(f"✅ Ajouté dans .keycut : {keycut} → {code}")
            except Exception as e:
                print("Erreur d'écriture dans .keycut :", e)

            func.append([keycut, lambda code=code: exec(code)])
            keyboard.add_hotkey(keycut, func[-1][1])
            root.destroy()

        tk.Button(root, text="Ajouter", command=submit).grid(row=2, columnspan=2, pady=10)
        root.mainloop()

    Thread(target=show_form).start()

def main():
    print("Démarrage du programme version", version)

    func.extend([
        ['ctrl+k+x', set_keyboard_extension_state],
        ['ctrl+shift+a', lambda: print("⛔ Fonction 'action' non définie")],
        ['ctrl+alt+g+p', create_git_project],
        ['ctrl+alt+b+p', create_basic_project],
        ['ctrl+shift+k', open_form],
    ])

    for shortcut, function in func:
        keyboard.add_hotkey(shortcut, function)

    keyboard.add_hotkey('esc', lambda: exit())

    while True:
        time.sleep(0.1)

if __name__ == "__main__":
    main()'''

# --- Installation ---

print("📦 Installation de MonApp...")

dest_folder = os.path.join(os.path.expanduser("~/Documents"), "MonApp")
os.makedirs(dest_folder, exist_ok=True)

app_py_path = os.path.join(dest_folder, "app.py")
with open(app_py_path, "w", encoding="utf-8") as f:
    f.write(code_source)

build_dir = os.path.join(os.getcwd(), "build_monapp")
os.makedirs(build_dir, exist_ok=True)

print("🔧 Compilation avec PyInstaller...")
subprocess.run([
    "pyinstaller",
    "--onefile",
    "--distpath", build_dir,
    app_py_path
], shell=True)

exe_src = os.path.join(build_dir, "app.exe")
exe_dest = os.path.join(dest_folder, "app.exe")

if os.path.exists(exe_src):
    shutil.move(exe_src, exe_dest)
else:
    raise FileNotFoundError(f"⚠️ Le fichier {exe_src} est introuvable. Compilation échouée.")

print("📌 Ajout au démarrage (via .bat)...")
startup_folder = os.path.join(os.environ["APPDATA"], r"Microsoft\Windows\Start Menu\Programs\Startup")
shortcut_path = os.path.join(startup_folder, "MonApp.bat")

with open(shortcut_path, "w", encoding="utf-8") as f:
    f.write(f'start "" "{exe_dest}"\n')

print("✅ Terminé. MonApp est installé dans Documents et sera lancé au démarrage.")
