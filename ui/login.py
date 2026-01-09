from db.creation_compte import create_user
from db.connexion_compte import login_user
from colorama import Fore, Style, init
import getpass

init()

def login_menu():
    print(Fore.YELLOW + "1. Créer un compte")
    print("2. Se connecter" + Style.RESET_ALL)

    choix = input("Choix : ")

    if choix == "1":
        username = input("Nom d'utilisateur : ")
        password = getpass.getpass("Mot de passe : ")
        create_user(username, password)
        return None

    elif choix == "2":
        username = input("Nom d'utilisateur : ")
        password = getpass.getpass("Mot de passe : ")
        return login_user(username, password)

    else:
        print(Fore.RED + "Choix invalide" + Style.RESET_ALL)
        return None
