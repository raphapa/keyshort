import keyboard

version = "v0.3"
keyboardextensionstate = False
def set_keyboard_extension_state():
    global keyboardextensionstate
    if keyboardextensionstate:
        keyboardextensionstate = False
    else:
        keyboardextensionstate = True
def action():
    global keyboardextensionstate
    if keyboardextensionstate:
        print("Action triggered!")
    else:
        pass
    # Here you can add the code that you want to execute when the hotkey is pressed
func = [set_keyboard_extension_state, action]
def main(*args):
    global version
    global func
    global keyboardextensionstate
    print("demarrage du programme version " + version)
    keyboard.add_hotkey('ctrl+shift+a', func[1])
    keyboard.add_hotkey('ctrl+k+x', func[0])
    while True:
        pass
if __name__ == "__main__":
    main()