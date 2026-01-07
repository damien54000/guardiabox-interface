from ui.chiffrer import chiffrer
from ui.dechiffrer import dechiffrer
from colorama import Fore, Style, init

init()

def menu(user_id):
    while True:
        print("##################################################")
        print(Fore.YELLOW + "MENU")
        print("1. Chiffrer un fichier ou un message")
        print("2. Déchiffrer un fichier ou un message")
        print("3. Quitter" + Style.RESET_ALL)


        try:
            choix = int(input("Veuillez saisir un choix : "))
        
        except ValueError:
            print("Veuillez entrer un nombre")
            continue

        if(choix == 1):
            chiffrer(user_id)
        
        elif(choix == 2):
            dechiffrer(user_id)

        elif(choix == 3):
            print(Fore.YELLOW + "Quitter" + Style.RESET_ALL)
            break

        else:
            print("Veuillez saisir 1, 2 ou 3")