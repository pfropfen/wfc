from pynput import keyboard
import threading
import time

# Global flag to stop the listener
key_pressed = False

def on_press(key):
    global key_pressed
    try:
        print(f"Key {key.char} pressed")
    except AttributeError:
        print(f"Special key {key} pressed")
    key_pressed = True
    return False  # Stop listener after first key press

def wait_for_key():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

# Start key detection in a thread
key_thread = threading.Thread(target=wait_for_key)
key_thread.start()

# Main program continues
print("Waiting for a key press...")
while not key_pressed:
    time.sleep(1)

print("Key was pressed! Exiting.")
