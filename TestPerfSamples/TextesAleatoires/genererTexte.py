import random
import sys
import unicodedata
import string

def fichierAleatoire(fichier: str, n: int, langue: str = "fr", unbalanced : bool = False):
    """
    Génère un fichier UTF-8 avec n caractères aléatoires.
    Comprend des caractères de contrôle.

    Args:
        fichier (str): Nom du fichier texte à créer.
        n (int): Nombre de caractères à générer.
        langue (str): 
            -"fr" pour toutes les lettres françaises. Par défaut.
            -"latin" pour toutes les lettres latines.
            -autre, pour tous les caractères UTF-8 affichables
        unbalanced (bool): False : tirage uniforme, True : tirage non uniforme. Par défaut False.
    """
    caracteres = [] # Liste des caractères possibles

    if langue == "fr":
        # Lettres ASCII + lettres accentuées françaises
        lettres = string.ascii_letters + "éèêëàâôùûîïçÉÈÊËÀÂÔÙÛÎÏÇ"
        chiffres = string.digits
        ponctuation = string.punctuation
        caracteres = list(lettres + chiffres + ponctuation)
    elif langue == "latin":
        # Lettres latines Unicode affichables
        for code in range(0, 0x10000):
            try:
                c = chr(code)
                cat = unicodedata.category(c)
                name = unicodedata.name(c, "")
                if cat[0] == 'L' and 'LATIN' in name:
                    caracteres.append(c)
            except:
                continue
    else:
        # Tous les caractères UTF-8 affichables
        for code in range(0, 0x110000):
            if 0xD800 <= code <= 0xDFFF:  # Ignorer 'surrogates'
                continue
            try:
                c = chr(code)
                cat = unicodedata.category(c)
                if cat[0] in ('L', 'N', 'P', 'S'):  # Lettres, nombres, ponctuation, symboles
                    caracteres.append(c)
            except:
                continue

    caracteres.extend(['\n', '\r', '\t', ' ']) # Ajout de caractères de contrôle pour aérer

    if (unbalanced):
        poids = [random.randint(0, 10000) for _ in caracteres]
        texte = ''.join(random.choices(caracteres, weights=poids, k=n))
    else:
        texte = ''.join(random.choice(caracteres) for _ in range(n))

    with open(fichier, "w", encoding="utf-8") as f:
        f.write(texte)


if __name__ == "__main__":

    if (len(sys.argv) < 3 or len(sys.argv) > 5):
        print("Usage : python3 "+sys.argv[0]+" <nom_fichier_a_creer> <nb_caracteres_fichier> [<langue>] [<unbalanced>]")
        print("langue (optionnel) :")
        print(" 1 -> tous les caractères français (par défaut)")
        print(" 2 -> tous les caractères latins")
        print(" 3 -> tous les caractères UTF-8 affichables")
        print("unbalanced (optionnel) :")
        print(" 0 -> tirage uniforme des caractères (par défaut)")
        print(" 1 -> tirage non uniforme des caractères")
        sys.exit(1)

    langue = "fr"
    if (len(sys.argv) >= 4):
        if (int(sys.argv[3]) == 1):
            langue = "fr"
        elif (int(sys.argv[3]) == 2):
            langue = "latin"
        elif (int(sys.argv[3]) == 3):
            langue = "everything"

    unbalanced = False
    if (len(sys.argv) == 5 and int(sys.argv[4]) == 1):
        unbalanced = True

    print("Génération aléatoire du fichier "+sys.argv[1]+" ⏳ ...\n")

    fichierAleatoire(sys.argv[1], int(sys.argv[2]), langue, unbalanced)

    print("Fichier généré !")