import re
from colorama import Fore, Style, init

init()

#afficher les règles avant d'entrer le mot de passe
def afficher_password_policy():
    print("-------------------------------------")
    print(Fore.YELLOW + "Règles du mot de passe :")
    print("Au moins 12 caractères")
    print("Au moins une majuscule")
    print("Au moins une minuscule")
    print("Au moins un chiffre")
    print("Au moins un caractère spécial" + Style.RESET_ALL)

#gestion de mot de passe
def verif_password(password: str):
    if len(password) < 12:
        raise ValueError(Fore.RED + "Le mot de passe doit contenir au moins 12 caractères" + Style.RESET_ALL)
    
    if not re.search(r"[A-Z]", password):
        raise ValueError(Fore.RED + "Le mot de passe doit contenir au moins une majuscule" + Style.RESET_ALL)
    
    if not re.search(r"[a-z]", password):
        raise ValueError(Fore.RED + "Le mot de passe doit contenir au moins une minuscle" + Style.RESET_ALL)
    
    if not re.search(r"[0-9]", password):
        raise ValueError(Fore.RED + "Le mot de passe doit contenir au moins un chiffre" + Style.RESET_ALL)
    
    if not re.search(r"[$&+,:;=?@#|'<>.^*()%!-]", password):
        raise ValueError(Fore.RED + "Le mot de passe doit contenir au moins un caractère spécial" + Style.RESET_ALL)