def ecrire(chemin: str, data: bytes):
    with open(chemin, "wb") as f:
        f.write(data)
