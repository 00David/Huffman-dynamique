# Huffman-dynamique

## Langage utilisé

**Python** : version 3.13.5  

## Tests lecture/écriture

Les fonctions de lecture et d'écriture sont dans *tools.py*.  
Les échantillons de tests sont situés dans le répertoire *TestToolsSamples*.  

Pour utiliser les programmes de tests, par exemple depuis le répertoire racine :  
```bash
python3 ./testToolsEcriture.py TestToolsSamples/chaine1.txt TestToolsSamples/chaine1.bin
```

```bash
python3 ./testToolsLecture.py TestToolsSamples/chaine1.bin
```

## Test construction de l'AHA

Toutes les méthodes de manipulation de l'AHA, ainsi que sa structure, sont dans *huffman.py*.  

Pour utiliser le programme de test, par exemple depuis le répertoire racine :  
```bash
python3 ./testHuffman.py carambarbcm
```
À noter qu'il est possible de construire l'AHA étape par étape en appellant successivement le programme avec les chaînes 'c', puis 'ca', puis 'car', etc.. jusqu'à arriver à 'carambarbcm'. Alors, à chaque étape l'arbre donne les codes attendus tels que dans le cours.  

## Test compression/décompression

Les différents samples de tests sont dans le répertoire *TestPerfSamples*.  
- Dans son sous-répertoire *Examples* : des samples fournis.  
- Dans son sous-répertoire *Textes* : des fichiers textuels créés (manuellement ou par décompression de binaires).  
- Dans son sous-répertoire *Binaires* : des fichiers binaires créés (par compression de textes).  

### Compression

La fonction de compression est dans *compresser.py*, les infos des compressions sont ajoutées dans *compression.txt*.  

Pour utiliser directement le programme de compression, par exemple depuis le répertoire racine :  
```bash
python3 ./compresser.py TestPerfSamples/Textes/exemple1.txt TestPerfSamples/Binaires/exemple1.huff  
```

### Décompression

La fonction de décompression est dans *decompresser.py*, les infos des décompressions sont ajoutées *dans decompression.txt*.  

Pour utiliser directement le programme de décompression, par exemple depuis le répertoire racine :  
```bash
python3 ./decompresser.py TestPerfSamples/Binaires/exemple1.huff TestPerfSamples/Textes/exemple1_decompresse.txt  
```

## Rapport

Rapport en cours : https://docs.google.com/document/d/1hVoRpPxILBle7SVB9faODcC2caK9vX3ghW3W4SfRwnM/edit?usp=sharing  
