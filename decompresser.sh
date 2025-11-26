#!/bin/bash

if [ "$#" -ne 2 ]; then
    echo "Usage : $0 <fichier_binaire_src> <fichier_textuel_dest>"
    exit 1
fi

python3 ./decompresser.py "$1" "$2"