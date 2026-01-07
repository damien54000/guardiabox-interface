import os
from colorama import Fore, Style, init

init()

BASE_DIR = os.path.abspath("data")

#Restriction et le seul chemin possible est à partir du dossier "data"
def chemin_valide(chemin: str) -> str:
    chemin_absolu = os.path.abspath(chemin)

    if not chemin_absolu.startswith(BASE_DIR):
        raise ValueError(Fore.RED + "Chemin non autorisé" + Style.RESET_ALL)

    return chemin_absolu