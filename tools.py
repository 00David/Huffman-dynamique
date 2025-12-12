# -*- coding: utf-8 -*-

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
        ValueError: Si 'fichier' ne se termine pas par l'extension .bin ou .huff.
    """
    if not isinstance(fichier, str):
        raise TypeError("'"+fichier+"' doit être une chaîne de caractères")
    
    suffixe_binaire = fichier[-4:]
    suffixe_huff = fichier[-5:]
    if (suffixe_binaire != ".bin" and suffixe_huff != ".huff"):
        raise ValueError("'"+fichier+"' doit être un fichier .bin ou .huff")

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
    Si le fichier d'origine ne contient pas un nombre de bits multiple de 8, il  est complété par des 0 dans le binaire de destination.

    Args:
        fichier_chaine (str): Nom du fichier contenant des bits.
        fichier_binaire (str): Nom du fichier binaire dans lequel écrire.

    Returns:
        None

    Raises:
        TypeError: Si le nom d'un des deux fichiers n'est pas une chaîne de caractères.
        ValueError:  Si :
            - fichier_binaire ne se termine pas par .bin ou .huff.
            - fichier_chaine ne contient pas que des '0' et des '1'. 
    """

    if not isinstance(fichier_chaine, str):
        raise TypeError("'"+fichier_chaine+"' doit être une chaîne de caractères")
    if not isinstance(fichier_binaire, str):
        raise TypeError("'"+fichier_binaire+"' doit être une chaîne de caractères")
    
    suffixe_binaire = fichier_binaire[-4:]
    suffixe_huff = fichier_binaire[-5:]
    if (suffixe_binaire != ".bin" and suffixe_huff != ".huff"):
        raise ValueError("'"+fichier_binaire+"' doit être un fichier .bin ou .huff")

    with open(fichier_chaine, "r", newline='', encoding="utf-8") as f:
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

def charToBits(c : str) ->str:
    """
    Transforme un caractère UTF-8 en sa chaîne de bits.

    Args:
        c (str): Un caractère UTF-8.

    Returns:
        str : La chaîne de bits correspondante, sans espaces. (entre 1 et 4 octets complets)
    """
    utf8_bytes = c.encode('utf-8') # Conversion en bytes UTF-8
    bits = ' '.join(f'{byte:08b}' for byte in utf8_bytes) # Conversion de chaque byte en bits
    bits = bits.replace(' ', '') # Supprime les espaces
    return bits

def bitsToChar(bits: str, i : int) -> tuple[str, int]:
    """
    Lit à partir de 'i' une séquence de bits et renvoie le caractère UTF-8 décodé ainsi que le nombre d'octets lus.

    Args:
        bits (str): La chaîne de bits (sans espaces) contenant le texte encodé en UTF-8.
        i (int): L'indice de départ dans la chaîne 'bits' pour commencer la lecture.

    Returns:
        tuple[str, int]:
            - Le caractère UTF-8 décodé.
            - Le nombre d'octets lus dans 'bits' pour obtenir ce caractère.

    Raises:
        ValueError: Si les bits restants sont insuffisants pour former un caractère UTF-8 complet.
    """

    octets = []
    nbOctetsLus = 0
    while True:
        if (i + 8 > len(bits)):
            raise ValueError("Bits insuffisants pour décoder le caractère")
        byte_val = int(bits[i:i+8], 2)
        octets.append(byte_val)
        i += 8
        nbOctetsLus += 1
        try:
            c = bytes(octets).decode('utf-8')
            break # Décodage réussi
        except UnicodeDecodeError:
            if (i + 8 > len(bits)):
                raise ValueError("Bits insuffisants pour décoder le caractère")
            continue # Besoin de plus d'octets
    return c, nbOctetsLus