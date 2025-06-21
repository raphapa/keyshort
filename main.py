import keyboard

version = "v0.1"
def action():
    print("hello world")
func = [action]
def main(*args):
    global version
    global func
    print("demarrage du programme version " + version)
    keyboard.add_hotkey('ctrl+shift+a', func[0])
    while True:
        pass

print(__name__)

if __name__ == "__main__":
    main()