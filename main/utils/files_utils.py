def lire_fichier(nom_fichier: str) -> list[str]:
    with open(nom_fichier, 'r') as fichier:
        return [ligne.strip() for ligne in fichier.readlines()]
