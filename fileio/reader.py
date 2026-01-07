def lire(chemin: str) -> bytes:
    with open(chemin, "rb") as f:
        return f.read()
