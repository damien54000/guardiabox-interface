from security.dechiffrement_sec import dechiffrement_message, dechiffrement_fichier
#from ui.password_policy import afficher_password_policy, verif_password
from security.chemin_valide import chemin_valide
from db.actions import log_action
from colorama import Fore, Style, init

init()

def dechiffrer(user_id):
    print("##################################################")
    print(Fore.YELLOW + "MENU DECHIFFREMENT")
    print("1. Dechiffrer un message")
    print("2. Dechiffrer un fichier" + Style.RESET_ALL)

    choix = int(input("Veuillez saisir un choix : "))

    password = input("Veuillez saisir un mot de passe : ")
    
    try:
        if (choix == 1):
            message = input("Veuillez saisir un message à déchiffrer : ")
            result = dechiffrement_message(message, password)
            print(Fore.GREEN + "Message déchiffré : " + Style.RESET_ALL, result)

            #actions dans base de données
            log_action(user_id, "DECHIFFREMENT_MESSAGE", "message")

        elif (choix == 2):

            while True:
                chemin = input("Veuillez saisir le chemin du fichier à déchiffrer : ")

                try:
                    chemin_valide(chemin)
                    break
                except ValueError as e:
                    print(e)

            result = dechiffrement_fichier(chemin, password)
            print(Fore.GREEN + "Fichier chiffré : " + Style.RESET_ALL, result)

            #actions dans base de données
            log_action(user_id, "DECHIFFREMENT_FICHIER", chemin)

        else:
            print("Veuillez saisir 1 ou 2")

    except ValueError as e:
        print(Fore.RED + "Erreur : " + Style.RESET_ALL, e)

    except FileNotFoundError:
        print(Fore.RED + "Fichier introuvable" + Style.RESET_ALL)