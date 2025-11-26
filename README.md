# Huffman-dynamique

**David VADIMON**  
**Eduardo-Dimo ONICA**  

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
- Dans son sous-répertoire *Exemples* : des samples fournis.  
- Dans son sous-répertoire *Textes* : des fichiers textuels créés manuellement.  
- Dans son sous-répertoire *TextesDecompresses* : des fichiers textuels créés par décompression de binaires.  
- Dans son sous-répertoire *TextesAleatoires* : des fichiers textes créés aléatoirement par le code python local.  
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

## Génération aléatoire de textes

Les textes sont générés dans le sous-répertoire *TestPerfSamples/TextesAleatoires*, avec le code '*genererTexte.py*' :
Plusieurs arguments à l'appel :  
- nom_fichier_a_creer  
- nb_caracteres_fichier  
- langue (optionnel) :  
    - 1 -> tous les caractères français (par défaut)
    - 2 -> tous les caractères latins
    - 3 -> tous les caractères UTF-8 affichables
- unbalanced (optionnel) :  
    - 0 -> tirage uniforme des caractères (par défaut)
    - 1 -> tirage non uniforme des caractères

Par exemple l'appel suivant va créer un fichier textuel de 100 caractères français, avec des probas d'apparitions de caractères aléatoires :  
```bash
cd TestPerfSamples/TextesAleatoires
python3 ./genererTexte.py fr_unbalanced_100.txt 100 1 1
```

Autre exemple, pour lequel un fichier de 1000 caractères utf-8, avec probas uniformes, va être créé :  
```bash
cd TestPerfSamples/TextesAleatoires
python3 ./genererTexte.py utf8_1000.txt 1000 3 0
```

## Rapport

Rapport en cours : https://docs.google.com/document/d/1hVoRpPxILBle7SVB9faODcC2caK9vX3ghW3W4SfRwnM/edit?usp=sharing  
