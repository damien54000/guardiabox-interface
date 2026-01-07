from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes
import base64
from fileio.reader import lire
from fileio.writer import ecrire

#règles de chiffrement
def chiffrement_bytes(data: bytes, password: str):
    #sel aléatoire
    salt = get_random_bytes(16)

    #clé pbkdf2
    key = PBKDF2(
        password,
        salt,
        dkLen=16,
        count=1000000,
        hmac_hash_module=SHA256
    )

    #chiffrement AES
    cipher = AES.new(key,AES.MODE_CCM)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(data)

    chiffrement = salt + nonce + ciphertext + tag
    #print(len(salt))
    #print(len(nonce))
    #print(len(ciphertext))
    #print(len(tag))
    
    return chiffrement

#fontion pour chiffrer un mesage
def chiffrement_message(message: str, password: str):

    #encoder en octet le message
    data = message.encode(encoding="utf-8")

    #chiffrement du message
    message_chiffre = chiffrement_bytes(data, password)

    return base64.b64encode(message_chiffre).decode("utf-8")

#fonction pour chiffrer le fichier
def chiffrement_fichier(chemin: str, password: str):
    data = lire(chemin)

    #chiffrement du contenu du fichier
    fichier_chiffre = chiffrement_bytes(data, password)

    #creation du nouveau fichier
    nouveau_chemin = chemin + ".crypt"
    ecrire(nouveau_chemin, fichier_chiffre)

    return nouveau_chemin