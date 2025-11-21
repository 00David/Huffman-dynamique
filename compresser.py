from huffman import *
from tools import *
import sys
import time

def compression(fichier_texte : str, fichier_binaire : str) -> None:
        """
        Compresse le contenu de 'fichier_chaine' dans le fichier binaire 'fichier_binaire'.

        Args:
            fichier_chaine (str): Nom du fichier textuel source.
            fichier_binaire (str): Nom du fichier binaire dans lequel écrire le texte compressé.

        Returns:
            None
        """
        start_time = time.perf_counter()
        
        with open(fichier_texte, "r", encoding="utf-8") as f:
            contenu = f.read()

            bits = ""
            nbOctetsEntree = 0

            arbre = ArbreHuffman()
            for c in contenu:

                bitsC = charToBits(c)
                nbOctetsEntree += int(len(bitsC)/8)
                
                if (arbre.getNoeudCaractere(c) == None): # Si première occurrence du caractère (n'est pas encore dans l'arbre)
                    bits = bits + arbre.getCodeCaractere("##") + bitsC
                else:
                    bits = bits + arbre.getCodeCaractere(c)
                arbre.modification(c)

            # On complète le dernier octet si nécessaire
            l = len(bits)
            if (l % 8 != 0):
                bits += '0' * (8 - l % 8)

            nbOctetsSortie = int(len(bits)/8)

            octets = [int(bits[i:i+8], 2) for i in range(0, len(bits), 8)]
            # Écriture binaire
            with open(fichier_binaire, "wb") as f2:
                f2.write(bytes(octets))

        end_time = time.perf_counter()
        temps_compression_ms = round((end_time - start_time) * 1000, 3)

        taux_compression = round(nbOctetsSortie/nbOctetsEntree, 5)

        with open("compression.txt", "a", encoding="utf-8") as infos:
            infos.write(f"{fichier_texte};{fichier_binaire};{nbOctetsEntree};{nbOctetsSortie};{taux_compression};{temps_compression_ms}\n")



if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage : python3 "+sys.argv[0]+" <fichier_textuel_src> <fichier_binaire_dest>")
        sys.exit(1)

    compression(sys.argv[1], sys.argv[2])