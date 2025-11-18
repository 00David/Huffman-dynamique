from tools import lecture
import sys

if len(sys.argv) != 2:
    print("Usage : python3 testToolsLecture.py *.bin")
    sys.exit(1)

lecture(sys.argv[1])