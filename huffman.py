import numpy as np

# Structure de l'arbre de Huffman

class ArbreHuffman:
    """
    Représente un arbre de Huffman, construit dynamiquement.<br>
    L'arbre ne contient qu'au plus 1 noeud contenant un certain caractère. 

    Attributes:
        special (Noeud): Le noeud de notre caractère spécial (qui est en fait une chaine pour éviter un conflit avec le caractère '#' solo).
        racine (Noeud): La racine de l'arbre.
        noeudsCaracteres (list[NoeudFeuille]): Tableau des noeuds feuilles de l'arbre.
    """

    class Noeud:
        """
        Représente un noeud de l'arbre de Huffman.

        Attributes:
            poids (int): Le poids du caractère du noeud.
            profondeur (int): La profondeur du noeud dans l'arbre, commence à 0 pour la racine.
            parent (Noeud | None): Le parent du noeud.
            filsGauche (Noeud | None): Le fils gauche du noeud.
            filsDroit (Noeud | None): Le fils droit du noeud.
            estFilsGauche (bool) : Indique si le noeud est un fils gauche.
        """

        def __init__(self, poids : int):
            """
            Initialise un nouveau noeud.

            Args:
                poids (int): Le poids du noeud.
            """
            self.poids = poids
            self.profondeur = 0
            self.parent = None
            self.filsGauche = None
            self.filsDroit = None
            self.estFilsGauche = False


        def estFeuille(self) -> bool:
            """
            Indique si un noeud est une feuille.

            Returns:
                bool
            """
            return self.filsGauche == None and self.filsDroit == None
        
        def estRacine(self) -> bool:
            """
            Indique si un noeud est une racine.

            Returns:
                bool
            """
            return self.parent == None

        def __str__(self) -> str:
            return f"({self.poids})"
        
    class NoeudFeuille(Noeud):
        """
        Représente un noeud feuille de l'arbre de Huffman, hérite de Noeud.

        Attributes:
            caractere (str): Le caractère lié au noeud.
            poids (int): Le poids du caractère du noeud (ici la fréquence du caractère).
            parent (Noeud | None): Le parent du noeud.
            filsGauche (Noeud | None): Le fils gauche du noeud.
            filsDroit (Noeud | None): Le fils droit du noeud.
            estFilsGauche (bool) : Indique si le noeud est un fils gauche.
        """

        def __init__(self, caractere : str, frequence : int, parent):
            """
            Initialise un nouveau noeud interne.

            Args:
                caractere (str): Le caractère lié au noeud feuille.
                frequence (int): La fréquence du caractère (le poids du noeud).
                parent (Noeud): Le noeud parent.
            """
            super().__init__(frequence)
            self.caractere = caractere
            self.parent = parent
            self.profondeur = parent.profondeur+1

    def __init__(self):
        """
        Initialise un nouvel arbre, avec uniquement en racine le noeud du caractère spécial.
        """
        self.special = ArbreHuffman.NoeudFeuille('##', 0, None)
        self.racine = self.special
        self.noeudsCaracteres = [self.special]
    
    def getNoeudCaractere(self, caractere : str) -> NoeudFeuille | None:
        """
        Renvoit le noeud d'un caractère de l'arbre, ou None si n'y est pas.

        Args:
            caractere (str): Le caractère dont le noeud est à chercher dans l'arbre.

        Returns:
            NoeudFeuille | None
        """
        for n in self.noeudsCaracteres :
            if n.caractere == caractere:
                return n
        return None
    
    def contientCaractere(self, caractere : str) -> bool:
        """
        Indique si un caractère est dans l'arbre.

        Args:
            caractere (str): Le caractère à chercher dans l'arbre.

        Returns:
            bool
        """
        return self.getNoeudCaractere(caractere) != None
    
    def codeCaractere(self, caractere : str) -> str:
        """
        Construit et renvoit le code d'un caractère.

        Args:
            caractere (str): Le caractère à chercher dans l'arbre.

        Returns:
            str : Le code binaire du caractère dans l'arbre.

        Raises:
            ValueError: Si le caractère n'est pas dans l'arbre.
        """
        code = ""
        noeud = self.getNoeudCaractere(caractere)
        if (noeud == None):
            raise ValueError("Caractère non présent dans l'arbre.")

        while (noeud.parent != None):
            if (noeud.estFilsGauche):
                code = '0' + code
            else:
                code = '1' + code
            noeud = noeud.parent

        return code
    
    def parcoursGDBH(self) -> list[Noeud]:
        """
        Renvoit les noeuds du parcours GDBH de l'arbre.

        Returns:
            list[Noeud]: La liste des noeuds du parcours.
        """

        matrice = [[]]

        noeudsDejaVus = []
        noeudsAVoir = [self.racine]

        # Parcours de l'arbre
        while (len(noeudsAVoir) > 0):
            noeud = noeudsAVoir.pop()
            if (noeud not in noeudsDejaVus):

                if (noeud.profondeur < len(matrice)):
                    matrice[noeud.profondeur].append(noeud)
                else:
                    while (noeud.profondeur >= len(matrice)):
                        matrice.append([])
                    matrice[noeud.profondeur].append(noeud)

                if (noeud.filsDroit != None):
                    noeudsAVoir.append(noeud.filsDroit)
                if (noeud.filsGauche != None):
                    noeudsAVoir.append(noeud.filsGauche)
                noeudsDejaVus.append(noeud)

        # Conversion de la matrice python en matrice numpy car applatissement ensuite est mieux optimisé
        # pour matrice de grande taille
        arrMatriceInverse = np.array(matrice)[::-1, :] # Conversion + Inversion des lignes
        return arrMatriceInverse.flatten().tolist() # Renvoit le parcours GDBH
    
    def finBloc(self, noeud : Noeud) -> Noeud:
        """
        Renvoit le 1er noeud dont le poids est < poids noeud suivant dans le parcours hiérarchique GDBH

        Args:
            noeud (Noeud): Le noeud à considérer.
        """
        # Cas spécial racine
        if (noeud.parent == None):
            return noeud

        parcoursGDBH = self.parcoursGDBH()
        for i in range(parcoursGDBH.index(noeud)+1, len(parcoursGDBH)-1): # dernier i = len(parcoursGDBH)-2. À l'index len(parcoursGDBH)-1, soit le dernier du parcours, il ne reste que la racine.
            if (parcoursGDBH[i].poids < parcoursGDBH[i+1].poids):
                return parcoursGDBH[i]

        # Si on arrive jusqu'ici, c'est qu'il ne reste que la racine dans le parcours GDBH à voir => est en fin de bloc
        return self.racine