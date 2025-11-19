from tools import lecture
import sys

if len(sys.argv) != 2:
    print("Usage : python3 testToolsLecture.py *.bin")
    sys.exit(1)

print("Lecture du fichier "+sys.argv[1]+" ...\n")

chaine = lecture(sys.argv[1])

print("Résultat lecture :")
print(chaine)

chaine_espaces = ' '.join(chaine[i:i+8] for i in range(0, len(chaine), 8))
print("Par octets :")
print(chaine_espaces)