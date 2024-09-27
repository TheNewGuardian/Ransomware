import os
import sys

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

#if __name__ == '__main__':
#    autostart()
autostart()
