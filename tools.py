# Implantations d’outils : lecture / ecriture

def lecture(fichier : str) -> str:
    """
    Lit un fichier binaire et retourne son contenu sous la forme d'une chaîne de bits.

    Args:
        fichier (str): Nom du fichier binaire à lire, contient un nombre de bits multiple de 8.

    Returns:
        str : Chaîne représentant le contenu binaire du fichier, sous forme de bits.

    Raises:
        TypeError: Si 'fichier' n'est pas une chaîne de caractères.
        ValueError: Si 'fichier' ne se termine pas par l'extension `.bin`.
    """
    if not isinstance(fichier, str):
        raise TypeError("'"+fichier+"' doit être une chaîne de caractères")
    
    suffixe = fichier[-4:]
    if (suffixe != ".bin"):
        raise ValueError("'"+fichier+"' doit être un fichier .bin")

    with open(fichier, "rb") as f:
        contenu = f.read()

        # Lecture binaire
        binaire = ""
        for i in range(len(contenu)):
            binaire += f"{contenu[i]:08b}"
        
        return binaire


def ecriture(fichier_chaine : str, fichier_binaire : str) -> None:
    """
    Ecrit le contenu de 'fichier_chaine' dans le fichier binaire 'fichier_binaire'.<br>
    Si le fichier d'origine ne contient pas un nombre de bits multiple de 8, il complète par des 0 dans le .bin de destination.

    Args:
        fichier_chaine (str): Nom du fichier contenant des bits.
        fichier_binaire (str): Nom du fichier binaire dans lequel écrire.

    Returns:
        None

    Raises:
        TypeError: Si le nom d'un des deux fichiers n'est pas une chaîne de caractères.
        ValueError:  Si :
            - fichier_chaine ne se termine pas par .txt.
            - fichier_binaire ne se termine pas par .bin.
            - fichier_chaine ne contient pas que des '0' et des '1'. 
    """
    if not isinstance(fichier_chaine, str):
        raise TypeError("'"+fichier_chaine+"' doit être une chaîne de caractères")
    if not isinstance(fichier_binaire, str):
        raise TypeError("'"+fichier_binaire+"' doit être une chaîne de caractères")
    
    suffixe_chaine = fichier_chaine[-4:]
    if (suffixe_chaine != ".txt"):
        raise ValueError("'"+fichier_chaine+"' doit être un fichier .txt")
    
    suffixe_binaire = fichier_binaire[-4:]
    if (suffixe_binaire != ".bin"):
        raise ValueError("'"+fichier_binaire+"' doit être un fichier .bin")

    with open(fichier_chaine, "r") as f:
        contenu = f.read()

        l = 0 # Nombre de bits

        # Check du contenu binaire
        for bit in contenu:
            if bit not in ('0','1'):
                raise ValueError("La chaîne doit contenir uniquement des '0' et des '1'.")
            l += 1

        if (l % 8 != 0):
            contenu += '0' * (8 - l % 8)

        octets = [int(contenu[i:i+8], 2) for i in range(0, len(contenu), 8)]

        # Écriture binaire
        with open(fichier_binaire, "wb") as f2:
            f2.write(bytes(octets))