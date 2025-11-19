from tools import ecriture
import sys

if len(sys.argv) != 3:
    print("Usage : python3 testToolsEcriture.py *.txt *.bin")
    sys.exit(1)

print("Ecriture du contenu du fichier "+sys.argv[1]+" dans "+sys.argv[2]+" ...\n")

ecriture(sys.argv[1], sys.argv[2])

print("Ecriture terminée.")