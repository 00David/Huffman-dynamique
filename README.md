# Huffman-dynamique

## Langage utilisé

**Python** : version 3.13.5  

**Modules utilisés :** sys, time

## Tests lecture/ecriture

Les fonctions de lecture et écriture sont dans tools.py.  
Echantillons de tests situés dans le répertoire TestToolsSamples.  

Pour utiliser les programmes de tests, par exemple depuis le répertoire racine :  
```bash
python3 ./testToolsEcriture.py TestToolsSamples/chaine1.txt TestToolsSamples/chaine1.bin
```

```bash
python3 ./testToolsLecture.py TestToolsSamples/chaine1.bin
```

## Test construction de l'AHA

Toutes les méthodes de manipulation de l'AHA, ainsi que sa structure, sont dans huffman.py.  

Pour utiliser le programme de test, par exemple depuis le répertoire racine :  
```bash
python3 testHuffman.py carambarbcm
```

## Test compression

La fonction de compression est dans compresser.py, les infos des compressions sont ajoutées dans compression.txt.  

Pour utiliser directement le programme de compression, par exemple depuis le répertoire racine :  
```bash
python3 ./compresser.py TestPerfSamples/Textes/exemple1.txt TestPerfSamples/Binaires/exemple1.huff  
```

## Test décompression

La fonction de décompression est dans decompresser.py, les infos des décompressions sont ajoutées dans decompression.txt.  

Pour utiliser directement le programme de décompression, par exemple depuis le répertoire racine :  
```bash
python3 ./decompresser.py TestPerfSamples/Binaires/exemple1.huff TestPerfSamples/Textes/exemple1_decompresse.txt  
```

## Rapport

Rapport en cours : https://docs.google.com/document/d/1hVoRpPxILBle7SVB9faODcC2caK9vX3ghW3W4SfRwnM/edit?usp=sharing  
