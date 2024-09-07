# Password Manager Application

This is a simple password manager application built using Python's `Tkinter` library for the GUI and `json` for data management. The application allows users to:

- Generate random secure passwords.
- Save and store passwords associated with websites and usernames/emails.
- Search for saved passwords for specific websites.

## Features

1. **Generate Password**: Automatically generates a strong, random password that can include letters, digits, and punctuation characters.
2. **Save Password**: Saves the generated password along with a website and email/username to a local JSON file (`data.json`).
3. **Search Password**: Searches for a saved password based on the website input and retrieves the associated email/username and password.
4. **Clipboard Copying**: Generated passwords are automatically copied to the clipboard for easy pasting.

## Prerequisites

Ensure that you have the following dependencies installed:

1. **Python 3.x**
2. **Tkinter** (Included in Python standard library for most installations)
3. **Pyperclip** (For clipboard management)
