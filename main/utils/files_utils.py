def lire_fichier(nom_fichier: str) -> list[str]:
    with open(nom_fichier, 'r') as fichier:
        return [ligne.strip() for ligne in fichier.readlines()]


def lire_fichier_no_strip(nom_fichier: str) -> list[str]:
    with open(nom_fichier, 'r') as fichier:
        return [ligne.replace("\n", "") for ligne in fichier.readlines()]
