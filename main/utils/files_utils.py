def lire_fichier(nom_fichier):
    try:
        with open(nom_fichier, 'r') as fichier:
            # Lire les lignes du fichier dans une liste
            lignes = fichier.readlines()
            return lignes
    except FileNotFoundError:
        print(f"Le fichier '{nom_fichier}' n'a pas été trouvé.")
        return None
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        return None
