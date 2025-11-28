# -*- coding: utf-8 -*-
import sys
import os
sys.path.append(os.path.abspath("../."))
from huffman import *

if __name__ == "__main__":
    
    if len(sys.argv) != 2:
        print("Usage : python3 "+sys.argv[0]+" <fichier_texte>")
        sys.exit(1)

    fichier = sys.argv[1]
    print("Lecture fichier "+fichier+" et insertions dans un nouvel AHA ⏳ ...\n")

    contenu = ""
    with open(fichier, "r", encoding="utf-8") as f:
        contenu = f.read()

    frequences = dict()

    arbre = ArbreHuffman()
    for c in contenu:
        if (c not in frequences):
            frequences[c] = 1
        else:
            frequences[c] += 1
        arbre.modification(c)

    noeudsDejaVus : set[ArbreHuffman.Noeud] = set()
    noeudsAVoir : list[tuple[ArbreHuffman.Noeud, int]] = [(arbre.racine, 0)]  # (noeud, profondeur)
    hauteur = 0
    sommeProfondeur = 0

    # Parcours en profondeur de l'arbre pour récupérer la hauteur
    while (len(noeudsAVoir) > 0):
        noeud, profondeur = noeudsAVoir.pop()
        if (noeud not in noeudsDejaVus):
            sommeProfondeur += profondeur
            if profondeur > hauteur:
                hauteur = profondeur
            if (noeud.filsDroit != None):
                noeudsAVoir.append((noeud.filsDroit, profondeur + 1))
            if (noeud.filsGauche != None):
                noeudsAVoir.append((noeud.filsGauche, profondeur + 1))
            noeudsDejaVus.add(noeud)

    # Nombre total de caractères
    nb_total = len(contenu)

    # Nombre de caractères uniques
    nb_uniques = len(frequences)

    # Calcul des probabilités
    probas = {c: frequences[c]/nb_total for c in frequences}   

    
    probas_tries = sorted(probas.items(), key=lambda item: item[1], reverse=True)

    # Les 5 caractères les plus fréquents
    top5 = probas_tries[:5]

    print(f"Hauteur finale de l'AHA : {hauteur}")
    print(f"Profondeur moyenne : {(sommeProfondeur/len(noeudsDejaVus)):.2f}")
    print(f"Nombre total de caractères : {nb_total}")
    print(f"Nombre de caractères uniques : {nb_uniques}")
    print("Top 5 des caractères les plus fréquents (%) :")
    for caractere, p in top5:
        print(f"'{caractere}' : {p*100:.2f}")

    def somme_top_k(k):
        if k > nb_uniques:
            print(f"⚠️ Pas assez de caractères uniques pour top {k} (uniques = {nb_uniques})")
            return None
        return sum(p for _, p in probas_tries[:k])

    # Listes des valeurs demandées
    top_list = [5, 10, 20, 50, 100, 500, 1000]

    print("\nSomme cumulée des fréquences des k caractères les plus fréquents :")
    for k in top_list:
        if (k <= nb_uniques):
            resultat = somme_top_k(k)
            if resultat is not None:
                print(f"Top {k:<5} → {resultat*100:.2f}%")