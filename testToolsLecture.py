# -*- coding: utf-8 -*-
from tools import lecture
import sys

"""
On teste la lecture du contenu d'un fichier binaire.

Argument 1 : Un fichier binaire source
"""

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage : python3 "+sys.argv[0]+" <fichier_binaire>")
        sys.exit(1)

    print("Lecture du fichier "+sys.argv[1]+" ...\n")

    chaine = lecture(sys.argv[1])

    print("Résultat lecture :")
    print(chaine)

    chaine_espaces = ' '.join(chaine[i:i+8] for i in range(0, len(chaine), 8))
    print("Par octets :")
    print(chaine_espaces)