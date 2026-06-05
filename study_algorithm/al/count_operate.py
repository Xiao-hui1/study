import keyboard

def press(event):
    print(event)

keyboard.on_press(press)
keyboard.wait()