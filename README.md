# Huffman-dynamique

**David VADIMON**  

## Rapport

[Rapport_projet_VADIMON.pdf](Rapport_projet_VADIMON.pdf)

## Transparents de la soutenance

[Transparents_projet_VADIMON.pdf](Transparents_projet_VADIMON.pdf)

## Modifications suite à la soutenance

Je n'ai effectué qu'une légère modification du code à la fin de la méthode de traitement dans le fichier '*huffman.py*' (plus de précisions à la fin du rapport).  
Les transparents de la soutenance ont été gardés originaux, tandis que mes graphes dans mon rapport ont été refaits avec les nouvelles mesures temporelles.  

## Entrées/Sorties du code

Comme spécifié dans le sujet :  

Pour lancer une **compression**, par exemple depuis le répertoire racine :
```bash
bash compresser.sh TestPerfSamples/Textes/exemple1.txt TestPerfSamples/Binaires/exemple1.huff
```

Pour lancer une **décompression**, par exemple depuis le répertoire racine :
```bash
bash decompresser.sh TestPerfSamples/Binaires/exemple1.huff TestPerfSamples/TextesDecompresses/exemple1_res.txt
```

Étant donné que l'algorithme de décompression n'a aucun moyen de savoir quand les bits du texte compressé ont été entièrement visités, il va donc également visiter les bits '0' de padding en fin, et en fonction peut ajouter un ou plusieurs caractères parasites si ces '0' le font tomber sur une feuille dans l'arbre de Huffman.   

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
- Dans son sous-répertoire *Textes* : des fichiers textuels créés manuellement ou recueillis via le projet Gutenberg.  
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
python3 ./decompresser.py TestPerfSamples/Binaires/exemple1.huff TestPerfSamples/TextesDecompresses/exemple1_res.txt
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

## Récupération des infos d'un fichier texte (utilisé pour l'analyse)

```bash
cd TestPerfSamples
python3 ./recupererInfosTexte.py Textes/exemple2.txt
```