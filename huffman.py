# -*- coding: utf-8 -*-
from __future__ import annotations

# Structure de l'arbre de Huffman

class ArbreHuffman:
    """
    Représente un arbre de Huffman adaptatif, construit dynamiquement.<br>
    L'arbre ne contient qu'au plus 1 noeud feuille contenant un certain caractère. 

    Attributes:
        special (NoeudFeuille): Le noeud de notre caractère spécial (qui est en fait une chaine '##' pour éviter un conflit avec le caractère '#' solo).
        racine (Noeud): La racine de l'arbre.
        noeudsCaracteres (dict[str,NoeudFeuille]): Dictionnaire associant à chaque caractère dans l'arbre, son noeud.
    """


    """ CLASSES DES NOEUDS DE L'ARBRE """

    class Noeud:
        """
        Représente un noeud de l'arbre de Huffman.

        Attributes:
            poids (int): Le poids du noeud.
            parent (Noeud | None): Le parent du noeud. Si racine, parent = None.
            estFilsGauche (bool) : Indique si le noeud est le fils gauche de son père. Si pas de père = False.
            filsGauche (Noeud | None): Le fils gauche du noeud.
            filsDroit (Noeud | None): Le fils droit du noeud.
        """

        def __init__(self, 
                 parent: ArbreHuffman.Noeud | None,
                 estFilsGauche: bool,
                 filsGauche: ArbreHuffman.Noeud | None,
                 filsDroit: ArbreHuffman.Noeud | None):
            """
            Initialise un nouveau noeud. Son poids est de 0.
            La cohérence entre les différents noeuds pour un ajout de nouveau noeud dans l'arbre se gère dans la méthode 'remplaceSpecial' de l'arbre, utilisée dans 'modification'.
            
            Args:
                parent (Noeud | None): Le noeud parent.
                estFilsGauche (bool): Indique si le noeud est le fils gauche de son père.
                filsGauche (Noeud | None): Le fils gauche du noeud.
                filsDroit (Noeud | None): Le fils droit du noeud.
            """
            self.poids = 0
            self.parent = parent
            self.estFilsGauche = estFilsGauche
            self.filsGauche = filsGauche
            self.filsDroit = filsDroit

        def __str__(self) -> str:
            """
            Ecriture du noeud interne de la forme : (poids)
            """
            return f"({self.poids})"
        
    class NoeudFeuille(Noeud):
        """
        Représente un noeud feuille de l'arbre de Huffman, hérite de Noeud.

        Attributes:
            caractere (str): Le caractère lié au noeud.
            poids (int): Le poids du noeud (ici la fréquence du caractère).
            parent (Noeud | None): Le parent du noeud.
            estFilsGauche (bool) : Indique si le noeud est le fils gauche de son père.
            filsGauche (Noeud | None): Le fils gauche du noeud, ici toujours None.
            filsDroit (Noeud | None): Le fils droit du noeud, ici toujours None.
        """

        def __init__(self, caractere : str, 
                     frequence : int, 
                     parent : ArbreHuffman.Noeud | None,
                     estFilsGauche: bool):
            """
            Initialise un nouveau noeud feuille, avec un caractère et une fréquence (= poids) donné.

            Args:
                caractere (str): Le caractère lié au noeud feuille.
                frequence (int): La fréquence du caractère (le poids du noeud).
                parent (Noeud): Le noeud parent.
                estFilsGauche (bool): Indique si le noeud est le fils gauche de son père.
            """
            super().__init__(parent, estFilsGauche, None, None)
            self.caractere = caractere
            self.poids = frequence

        def __str__(self) -> str:
            """
            Ecriture du noeud feuille de la forme : (caractere : frequence)
            """
            return f"({self.caractere} : {self.poids})"


    """ METHODES DE L'ARBRE DE HUFFMAN """

    def __init__(self):
        """
        Initialise un nouvel arbre, avec uniquement en racine le noeud du caractère spécial.
        """
        self.special = ArbreHuffman.NoeudFeuille('##', 0, None, False)
        self.racine = self.special
        self.noeudsCaracteres = {'##':self.special}
    
    def __str__(self) -> str:
        """
        Ecriture de l'arbre sous la forme du parcours GDBH
        """
        chaine = ""
        for n in self.parcoursGDBHComplet():
            chaine += str(n) +" "
        return chaine

    def getNoeudCaractere(self, caractere : str) -> NoeudFeuille | None:
        """
        Renvoit le noeud d'un caractère de l'arbre, ou None si il n'y est pas.

        Args:
            caractere (str): Le caractère dont le noeud est à chercher dans l'arbre.

        Returns:
            NoeudFeuille | None
        """
        if caractere in self.noeudsCaracteres :
            return self.noeudsCaracteres[caractere]
        return None
    
    def getCodeCaractere(self, caractere : str) -> str:
        """
        Construit et renvoit le code d'un caractère, en partant de la feuille du caractère jusqu'à la racine.

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
    
    def parcoursGDBHComplet(self) -> list[Noeud]:
        """
        Renvoit les noeuds du parcours GDBH complet de l'arbre.

        Returns:
            list[Noeud]: La liste des noeuds du parcours.
        """

        matrice = [[]] # Contient dans le sous tableau en index i, les noeuds en profondeur i dans l'arbre (dans l'ordre de gauche à droite)

        noeudsDejaVus : set[ArbreHuffman.Noeud] = set()
        noeudsAVoir : list[tuple[ArbreHuffman.Noeud, int]] = [(self.racine, 0)]  # (noeud, profondeur)

        # Parcours en profondeur de l'arbre
        while (len(noeudsAVoir) > 0):
            noeud, profondeur = noeudsAVoir.pop()
            if (noeud not in noeudsDejaVus): # On utilise un set pour ne pas avoir à itérer sur tout 'noeudsDejaVus'.

                if (profondeur < len(matrice)):
                    matrice[profondeur].append(noeud)
                else: 
                    # La matrice n'a pas de sous tableau en indice 'profondeur', on ajoute les sous-tableaus vides nécessaires
                    while (profondeur >= len(matrice)):
                        matrice.append([])
                    matrice[profondeur].append(noeud)

                # Ajout des enfants avec profondeur + 1
                # Les fils gauches sont toujours append après les droits => les fils gauches sont ensuite parcourus avant leur frère droit (plus haut dans la pile 'noeudsAVoir') 
                # => parcours de la gauche vers la droite de l'arbre
                if (noeud.filsDroit != None):
                    noeudsAVoir.append((noeud.filsDroit, profondeur + 1))
                if (noeud.filsGauche != None):
                    noeudsAVoir.append((noeud.filsGauche, profondeur + 1))
                noeudsDejaVus.add(noeud)

        matriceInverse = matrice[::-1] # Inversion des lignes, pour passer d'un parcours de l'arbre du haut vers le bas, à bas vers le haut
        parcours = [noeud for sousListe in matriceInverse for noeud in sousListe] # Applatissement
        return parcours # Renvoit le parcours GDBH
    
    def parcoursGDBHDepuisNoeud(self, noeud : Noeud) -> list[Noeud]:
        """
        Variante renvoyant les noeuds du parcours GDBH, partant des noeuds de la profondeur du noeud donné en paramètre.
        N'effectue donc en général pas le parcours GDBH complet, à moins que le noeud donné soit à la dernière profondeur de l'arbre.
        Permet un gros speed-up par rapport à l'utilisation de parcoursGDBHComplet.
        (ça prend 10x moins de temps avec cette version sur la compression/décompression de Blaise_Pacal.txt fourni en exemple).
        
        Args:
            noeud (Noeud): Le noeud, à une profondeur p, pour lequel on va faire le parcours GDBH à partir de cette profondeur p.

        Returns:
            list[Noeud]: La liste des noeuds du parcours, à partir de la profondeur du noeud donnée en paramètre.
        """

        # Cas spécial, parcours GDBH depuis la racine
        if (noeud == self.racine):
            return [self.racine]

        p = 0 # On calcule la profondeur du noeud en remontant l'arbre
        n = noeud
        while (n.parent != None):
            n = n.parent
            p += 1

        matrice = [[]] # Contient dans le sous tableau en index i, les noeuds en profondeur i dans l'arbre (dans l'ordre de gauche à droite)

        noeudsDejaVus : set[ArbreHuffman.Noeud] = set()
        noeudsAVoir : list[tuple[ArbreHuffman.Noeud, int]] = [(self.racine, 0)]  # (noeud, profondeur)

        # Parcours en profondeur de l'arbre
        while (len(noeudsAVoir) > 0):
            noeud, profondeur = noeudsAVoir.pop()
            if (noeud not in noeudsDejaVus): # On utilise un set pour ne pas avoir à itérer sur tout 'noeudsDejaVus'.

                if (profondeur < len(matrice)):
                    matrice[profondeur].append(noeud)
                else: 
                    # La matrice n'a pas de sous tableau en indice 'profondeur', on ajoute les sous-tableaus vides nécessaires
                    while (profondeur >= len(matrice)):
                        matrice.append([])
                    matrice[profondeur].append(noeud)

                # Ajout des enfants avec profondeur + 1
                # Les fils gauches sont toujours append après les droits => les fils gauches sont ensuite parcourus avant leur frère droit (plus haut dans la pile 'noeudsAVoir') 
                # => parcours de la gauche vers la droite de l'arbre
                if ((profondeur + 1) <= p) : # Seulement fils à une profondeur <= p sont ensuite considérés
                    if (noeud.filsDroit != None):
                        noeudsAVoir.append((noeud.filsDroit, profondeur + 1))
                    if (noeud.filsGauche != None):
                        noeudsAVoir.append((noeud.filsGauche, profondeur + 1))
                noeudsDejaVus.add(noeud)

        matriceInverse = matrice[::-1] # Inversion des lignes, pour passer d'un parcours de l'arbre du haut vers le bas, à bas vers le haut
        parcours = [noeud for sousListe in matriceInverse for noeud in sousListe] # Applatissement
        return parcours # Renvoit le parcours GDBH
    
    def finBloc(self, noeud : Noeud, parcoursGDBH : list[Noeud] = []) -> Noeud:
        """
        Renvoit le 1er noeud dont le poids est < poids noeud suivant dans le parcours hiérarchique GDBH, à partir du 'noeud' fourni.

        Args:
            noeud (Noeud): Le noeud à considérer.
            parcours (Optionnal[list[Noeud]]): Le parcours GDBH de l'arbre, si déjà calculé.
        """
        # Cas spécial racine
        if (noeud.parent == None):
            return noeud

        if (parcoursGDBH == []):
            parcoursGDBH = self.parcoursGDBHDepuisNoeud(noeud)

        for i in range(parcoursGDBH.index(noeud)+1, len(parcoursGDBH)-1): # dernier i = len(parcoursGDBH)-2. À l'index len(parcoursGDBH)-1, soit le dernier du parcours, il ne reste que la racine.
            if (parcoursGDBH[i].poids < parcoursGDBH[i+1].poids):
                return parcoursGDBH[i]

        # Si on arrive jusqu'ici, c'est qu'il ne reste que la racine dans le parcours GDBH à voir => est en fin de bloc
        return self.racine
    
    def cheminIncrementable(self, noeud : Noeud, parcoursGDBH : list[Noeud] = [])->Noeud:
        """
        Parcourt le chemin depuis le 'noeud' donné jusqu'à la racine, et renvoit le premier noeud 'm' du chemin <br>
        tel que son poids == poids noeud suivant dans le chemin. <br>
        Si ce noeud retourné est le noeud racine, alors le chemin entier est incrémentable.

        Args:
            noeud (Noeud): Le noeud à partir duquel faire le chemin.
            parcours (Optionnal[list[Noeud]]): Le parcours GDBH de l'arbre, si déjà calculé.

        Returns:
            Noeud: Le premier noeud 'm' du chemin tel que son poids == poids noeud suivant dans le chemin. 
        """
        if (parcoursGDBH == []):
            parcoursGDBH = self.parcoursGDBHDepuisNoeud(noeud)

        m = noeud
        i_parcoursGDBH = parcoursGDBH.index(m) # On conserve la position du noeud m actuel dans le parcours GDBH

        # On va remonter l'arbre, tout en avançant en même temps dans le parcours GDBH
        while (m.parent != None):
            
            # On est dans le parcours GDBH à la case du noeud m considéré (forcément vrai pour la 1ère itération dans la boucle)
            if (parcoursGDBH[i_parcoursGDBH] == m):
                if (m.poids == parcoursGDBH[i_parcoursGDBH+1].poids):
                    return m
                else:
                    m = m.parent # On remonte dans le chemin

            # On avance dans le parcours GDBH, jusqu'à arriver au noeud m à considérer
            else:
                i_parcoursGDBH += 1

        # Arrivé ici, on est à la racine => tout le chemin depuis le noeud de départ est incrémentable
        return m

    def swapNoeuds(self, n1 : Noeud, n2 : Noeud):
        """
        Echange dans l'arbre les sous-arbres enracinés en n1 et en n2.<br>
        Suppose que n1 et n2 sont dans l'arbre.

        Args:
            n1 (Noeud): 1er noeud à swap.
            n2 (Noeud): 2ème noeud à swap.
        """

        tmpParent = n1.parent
        tmpEstFilsGauche = n1.estFilsGauche

        # Place n1 à la place de n2
        n1.parent = n2.parent
        n1.estFilsGauche = n2.estFilsGauche
        if (n1.estFilsGauche and n1.parent != None):
            n1.parent.filsGauche = n1
        elif (n1.parent != None):
            n1.parent.filsDroit = n1

        # Place n2 à la place de n1
        n2.parent = tmpParent
        n2.estFilsGauche = tmpEstFilsGauche
        if (n2.estFilsGauche and n2.parent != None):
            n2.parent.filsGauche = n2
        elif (n2.parent != None):
            n2.parent.filsDroit = n2

    def remplaceSpecial(self, s : str) -> Noeud:
        """
        Met à la position du noeud special un nouveau sous-arbre ayant en fils gauche le noeud spécial <br>
        et en fils droit un nouveau noeud avec le caractère 's' à une fréquence de 1.<br>
        S'occupe aussi de maintenir la cohérence dans la structure locale de l'arbre, <br>
        entre le nouveau noeud racine du sous-arbre, ses enfants et son éventuel parent.

        Args:
            s (str): Le caractère à ajouter.

        Returns:
            Noeud : Le noeud racine du nouveau sous-arbre.
        """
        Q = ArbreHuffman.NoeudFeuille(s, 1, None, False) # Noeud contenant le nouveau caractère
        nouveauPere = ArbreHuffman.Noeud(None, False, self.special, Q) # Racine du nouveau sous-arbre
        nouveauPere.poids = 1
            
        # Opérations de cohérence

        # Si le caractère spécial avait déjà un parent avant
        if (self.special.parent != None):
            nouveauPere.parent = self.special.parent
            nouveauPere.estFilsGauche = self.special.estFilsGauche
            if (self.special.estFilsGauche):
                self.special.parent.filsGauche = nouveauPere
            else:
                self.special.parent.filsDroit = nouveauPere
            self.special.parent = nouveauPere

        # Dans tous les cas
        nouveauPere.filsGauche.parent = nouveauPere
        nouveauPere.filsDroit.parent = nouveauPere

        nouveauPere.filsGauche.estFilsGauche = True # self.special.estFilsGauche = True
        nouveauPere.filsDroit.estFilsGauche = False
        
        self.noeudsCaracteres[s] = Q # Ajout du noeud avec le nouveau caractère dans le dictionnaire
        return nouveauPere

    def traitement(self, Q : Noeud, parcoursGDBH : list[Noeud] = []) -> ArbreHuffman:
        """
        S'occupe du traitement de l'arbre de Huffman actuel.

        Args:
            Q (Noeud): Noeud ayant apporté une modification à l'arbre.
            parcours (Optionnal[list[Noeud]]): Le parcours GDBH de l'abre, si déjà calculé pour l'arbre actuel. Non vide pour 1er appel par modification, vide pour appels récursifs dans traitement.
            
        Returns:
            ArbreHuffman : L'arbre actuel, après modification (pas une copie).
        """
        if (parcoursGDBH == []):
            parcoursGDBH = self.parcoursGDBHDepuisNoeud(Q)

        m = self.cheminIncrementable(Q, parcoursGDBH)

        # Si tous les noeuds du chemin sont incrémentables
        if (m == self.racine):

            # Ajoute 1 à chaque poids du chemin de Q a la racine
            while (Q.parent != None):
                Q.poids += 1
                Q = Q.parent
            Q.poids += 1 # Cas dernier noeud, quand Q == m (ici == la racine)
            
            return self
        
        else:
            
            b = self.finBloc(m, parcoursGDBH)

            # Ajoute 1 à chaque poids du chemin de Q a Q_m
            while (Q != m and Q.parent != None):
                Q.poids += 1
                Q = Q.parent
            Q.poids += 1 # Cas dernier noeud, quand Q == m

            self.swapNoeuds(m, b)

            assert m.parent is not None
            return self.traitement(m.parent)
            

    def modification(self, s : str) -> ArbreHuffman:
        """
        Modifie l'arbre de Huffman actuel, en y ajoutant le caractère 's'.

        Args:
            s (str): Le caractère à ajouter.

        Returns:
            ArbreHuffman : L'arbre actuel, après modification (pas une copie).
        """

        # Arbre ne contenant que le caractère spécial
        if (self.racine == self.special):
            Q = self.remplaceSpecial(s)
            self.racine = Q
            return self
        
        # Arbre ne contenant pas le nouveau caractère
        elif s not in self.noeudsCaracteres:
            Q = self.special.parent # Q est forcément non None, le parent de la racine du nouveau sous-arbre
            assert Q is not None
            nouveau = self.remplaceSpecial(s)

            if (nouveau.estFilsGauche):
                Q.filsGauche = nouveau
            else:
                Q.filsDroit = nouveau
            return self.traitement(Q)
        
        # Arbre contenant déjà une feuille pour le caractère
        else:
            Q = self.getNoeudCaractere(s)
            assert Q is not None

            parcoursGDBH = self.parcoursGDBHDepuisNoeud(Q)

            if ({Q.parent.filsGauche, Q.parent.filsDroit} == {Q, self.special} and Q.parent == self.finBloc(Q, parcoursGDBH)):
                Q.poids += 1
                Q = Q.parent
                assert Q is not None
                # Même si on change Q, l'arbre n'est pas modifié donc le parcoursGDBH actuel reste le même : pas besoin de le recalculer

            return self.traitement(Q, parcoursGDBH)