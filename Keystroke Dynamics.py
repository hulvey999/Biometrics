from pynput.keyboard import Listener
import time

keystroke_data = []

def on_press(key):
    keystroke_data.append((key, time.time()))

def on_release(key):
    if key == Key.esc:  # Stop listener
        return False

# Start capturing keystrokes
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

# Save the keystroke timing data
with open('biometric_data/keystroke_data.txt', 'w') as f:
    for k in keystroke_data:
        f.write(f"{k[0]} {k[1]}\n")

print("Keystroke dynamics captured.")
