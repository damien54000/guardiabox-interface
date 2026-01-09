from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes
import base64
from fileio.reader import lire
from fileio.writer import ecrire
from colorama import Fore, Style, init

init()

#règles de dechiffrement
def dechiffrement_bytes(data: bytes, password: str):
    
    #découpage
    salt = data[:16]
    nonce = data[16:27]
    tag = data[-16:]
    ciphertext = data[27:-16]

    #clé redérivé pbkdf2
    key = PBKDF2(
        password,
        salt,
        dkLen=16,
        count=1000000,
        hmac_hash_module=SHA256
    )

    #Initialisation AES
    cipher = AES.new(key,AES.MODE_CCM, nonce = nonce)
    dechiffrement = cipher.decrypt_and_verify(ciphertext, tag)

    return dechiffrement


#fontion pour chiffrer un mesage
def dechiffrement_message(message: str, password: str):

    #encoder en octet le message
    data = base64.b64decode(message)

    #gestion erreur mauvais mdp ou message modifié
    try:
        #chiffrement du message
        message_dechiffre = dechiffrement_bytes(data, password).decode("utf-8")
        return message_dechiffre
    
    except ValueError:
        raise ValueError(Fore.RED + "Mot de passe incorrect ou message modifié" + Style.RESET_ALL)

def dechiffrement_fichier(chemin: str, password: str):
    data = lire(chemin)

    try:
        #déchiffrement du contenu du fichier
        fichier_dechiffre = dechiffrement_bytes(data, password)

    except:
        raise ValueError(Fore.RED + "Mot de passe incorrect ou fichier modifié" + Style.RESET_ALL)
    
    #creation du nouveau fichier
    nouveau_chemin = chemin + ".decrypt"
    ecrire(nouveau_chemin, fichier_dechiffre)

    return nouveau_chemin