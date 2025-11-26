#!/bin/bash

if [ "$#" -ne 2 ]; then
    echo "Usage : $0 <fichier_textuel_src> <fichier_binaire_dest>"
    exit 1
fi

python3 ./compresser.py "$1" "$2"