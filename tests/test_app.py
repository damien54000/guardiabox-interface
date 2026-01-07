import pytest

from security.chiffrement_secu import chiffrement_message
from security.dechiffrement_sec import dechiffrement_message


def test_chiffrement_dechiffrement():
    message = "test"
    password = "Azerty?23456"

    message_chiffre = chiffrement_message(message, password)
    message_dechiffre = dechiffrement_message(message_chiffre, password)

    assert message_dechiffre == message

def test_dechiffrement_mauvais_mdp():
    message = "test"
    bon_mdp = "Azerty?23456"
    mauvais_mdp = "23456?Azerty"

    message_chiffre = chiffrement_message(message, bon_mdp)

    #Vérifie si ça renvoie une erreur pour un mauvais mot de passe
    with pytest.raises(ValueError):
        dechiffrement_message(message_chiffre, mauvais_mdp)
