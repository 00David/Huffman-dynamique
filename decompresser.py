# -*- coding: utf-8 -*-
from huffman import *
from tools import *
import sys
import time

def decompression(fichier_binaire : str, fichier_texte : str) -> None:
        """
        Décompresse le contenu binaire de 'fichier_binaire' dans le fichier textuel 'fichier_texte'.
        Les bits de padding peuvent amener l'algo à ajouter un ou plusieurs caractères parasites à la fin.

        Args:
            fichier_binaire (str): Nom du fichier binaire depuis lequel extraire le texte compressé.
            fichier_chaine (str): Nom du fichier textuel de destination.

        Returns:
            None
        """
        start_time = time.perf_counter()
        
        with open(fichier_binaire, "rb") as f:
            contenu = f.read()

            texte = ""
            nbOctetsEntree = int(len(contenu))

            bits = ''.join(f'{byte:08b}' for byte in contenu)  # Convertit les octets en string de bits
            
            nbOctetsSortie = 0
            i = 0
            arbre = ArbreHuffman()

            # Lit le 1er caractère et l'ajoute à l'arbre
            if (len(bits) > 0):
                c, nbOctetsLus = bitsToChar(bits, i)
                texte += c
                nbOctetsSortie += nbOctetsLus
                i += nbOctetsLus * 8
                arbre.modification(c)

            l = len(bits)
            while i < l: # On parcourt chaque bit du binaire

                noeud = arbre.racine
                # Parcourt l'arbre de la racine vers une feuille
                while (noeud.filsGauche != None and noeud.filsDroit != None):
                    if i >= l:
                        break  # On a fini de lire tous les bits
                    bit = bits[i]
                    if (bit == '0'):
                        noeud = noeud.filsGauche
                    else:
                        noeud = noeud.filsDroit
                    i += 1

                # On est arrivé sur une feuille
                if isinstance(noeud, ArbreHuffman.NoeudFeuille):
                    if noeud.caractere == "##":
                        # Vérifie qu'on a bien assez de bits restants (pour décoder en un caractère UTF-8)
                        if i + 8 > l:
                            break  # On arrête proprement

                        # Lecture du caractère dans les octets suivants
                        c, nbOctetsLus = bitsToChar(bits, i)
                        i += nbOctetsLus * 8
                    else:
                        # Caractère déjà dans l'arbre
                        c = noeud.caractere
                        nbOctetsLus = len(c.encode('utf-8'))
                    
                    texte += c
                    nbOctetsSortie += nbOctetsLus
                    arbre.modification(c)
                else:
                    # Arrivé ici, il n'y a plus de caractères à lire
                    break

            # Écriture dans le fichier textuel
            with open(fichier_texte, "w", newline='', encoding="utf-8") as f2: # newline : garde les '\r' dans les '\r\n' en fin de ligne
                f2.write(texte)

        if (nbOctetsEntree > 0):
            taux_compression = round(nbOctetsSortie/nbOctetsEntree, 5)
        else:
            taux_compression = 0
        end_time = time.perf_counter()
        temps_compression_ms = round((end_time - start_time) * 1000, 3)

        with open("decompression.txt", "a", encoding="utf-8") as infos:
            infos.write(f"{fichier_binaire};{fichier_texte};{nbOctetsEntree};{nbOctetsSortie};{taux_compression};{temps_compression_ms}\n")



if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage : python3 "+sys.argv[0]+" <fichier_binaire_src> <fichier_textuel_dest>")
        sys.exit(1)

    print("Début décompression ⏳ ...\n")
    decompression(sys.argv[1], sys.argv[2])
    print("Fichier décompressé dans "+sys.argv[2]+" !")