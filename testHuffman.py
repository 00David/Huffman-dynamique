# -*- coding: utf-8 -*-
from huffman import *
import sys

"""
On regarde ici les codes donnés par insertions successives des caractères d'une chaine dans un AHA.

Argument 1 : une chaine à insérer dans un AHA.
"""

if __name__ == "__main__":
    
    if len(sys.argv) != 2:
        print("Usage : python3 "+sys.argv[0]+" <str>")
        sys.exit(1)

    chaine = sys.argv[1]
    print("Insertion de la chaine : "+chaine+" dans un nouvel AHA ⏳ ...\n")

    arbre = ArbreHuffman()
    for c in chaine:
        arbre.modification(c)

    print("Insertion terminée")

    for c in set(chaine):
        noeudC = arbre.getNoeudCaractere(c)
        assert noeudC is not None
        print("Code de '"+c+"', de fréquence "+str(noeudC.poids)+" : "+arbre.getCodeCaractere(c))

    noeudSpecial = arbre.getNoeudCaractere("##")
    assert noeudSpecial is not None
    print("Code de '##', de fréquence "+str(noeudSpecial.poids)+" : "+arbre.getCodeCaractere("##"))

    print("Parcours GDBH de l'arbre :")
    print(arbre)