from tools import ecriture
import sys

if len(sys.argv) != 3:
    print("Usage : python3 testToolsEcriture.py *.txt *.bin")
    sys.exit(1)

ecriture(sys.argv[1], sys.argv[2])