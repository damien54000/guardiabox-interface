from security.chiffrement_secu import chiffrement_message, chiffrement_fichier
from ui.password_policy import afficher_password_policy, verif_password
from security.chemin_valide import chemin_valide
from db.actions import log_action
from colorama import Fore, Style, init

init()

def chiffrer(user_id):
    print("##################################################")
    print(Fore.YELLOW + "MENU CHIFFREMENT ")
    print("1. Chiffrer un message")
    print("2. Chiffrer un fichier" + Style.RESET_ALL)

    choix = int(input("Veuillez saisir un choix : "))

    afficher_password_policy()

    #Verification du mot de passe suivant les règles
    while True:

        password = input("Veuillez saisir un mot de passe : ")

        try:
            verif_password(password)
            break
        except ValueError as e:
            print(Fore.RED + "Mot de passe invalide :" + Style.RESET_ALL, e)

        
    if (choix == 1):
        message = input("Veuillez saisir un message à chiffrer : ")
        result = chiffrement_message(message, password)
        print(Fore.GREEN + "Message chiffré : " + Style.RESET_ALL, result)

        #actions dans base de données
        log_action(user_id, "CHIFFREMENT_MESSAGE", "message")

    elif (choix == 2):

        while True:

            chemin = input("Veuillez saisir le chemin du fichier à chiffrer : ")
            try:
                chemin_valide(chemin)
                break
            except ValueError as e:
                print(e)
                
        result = chiffrement_fichier(chemin, password)
        print(Fore.GREEN + "Fichier chiffré : " + Style.RESET_ALL, result)

        #actions dans base de données
        log_action(user_id, "CHIFFREMENT_FICHIER", chemin)

    else:
        print(Fore.RED + "Veuillez saisir 1 ou 2" + Style.RESET_ALL)