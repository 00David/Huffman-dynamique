# -*- coding: utf-8 -*-
from tools import ecriture
import sys

"""
On teste l'écriture du contenu d'un fichier texte contenant des bits dans un fichier binaire.

Argument 1 : Un fichier textuel source contenant des bits
Argument 2 : Un fichier binaire de destination
"""

if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage : python3 "+sys.argv[0]+" <fichier_textuel_src> <fichier_binaire_dest>")
        sys.exit(1)

    print("Ecriture du contenu du fichier "+sys.argv[1]+" dans "+sys.argv[2]+" ⏳ ...\n")

    ecriture(sys.argv[1], sys.argv[2])

    print("Ecriture terminée.")