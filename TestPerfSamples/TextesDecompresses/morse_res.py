# -*- coding: utf-8 -*-

# Importation de Flask et des autres codes python comportant les définitions pythons normales
from flask import Flask, request, render_template, redirect
from actions_bdd import *
from actions_traduction import *
from setup_raspi import *

"""

1er bouton -> pin 22 
2ème bouton -> pin 24
Une led -> pin 5
Un buzzer -> pin 16


A titre indicatif, pour les définitions utilisées ici on retrouve :

Dans setup_raspi.py :
    -press_button_sans_son
    -release_button_bouton_sans_son
    -press_button_avec_son
    -release_button_bouton_avec_son
    -timer_appui
    -crea_sequence_morse

Dans actions_traduction.py :
    -texte_to_morse
    -affiche
    -morse_to_texte
    -exo_facile
    -exo_moyen
    -exo_difficile
    -renvoie_mot
    -parametres_to_bool
    -choix_type_renvoi_morse
    
Dans actions_bdd.py :
    -return_table
    -return_histo_selon_id
    -insert_comptes
    -insert_historique
    -reset_hisorique
    -init_bdd
    -compte_connecté
    -connecte_compte
    -infos_compte
    -supprimer_compte


"""



#On initiale la base de donnée au lancement
init_bdd()


""" Partie Python Flask """


app = Flask(__name__, template_folder='templates', static_folder='static') # On démarre l'application Flask
# Accueil du site sur http://127.0.0.1:5000/



"""            """
""" Traduction """
"""            """


# Notre page d'accueil 
@app.route("/",methods=["GET", "POST"]) # En cliquant sur "Traduction" en haut des pages on arrive sur cette route sans requête
def accueil():
    
    # Si requête post ( en l'occurence ça peut que venir de '/profil' )
    if request.method == "POST":
        
        if request.form.get('deconnecter') == "True": # Si déconnexion
            connecte_compte("Non connecté") # On se connecte au compte par défault "Non connecté", qui déconnecte les autres comptes.
            
        elif request.form.get('supprimer') == "True": # Si suppression
            supprimer_compte(compte_connecté()) # On supprime le compte auquel on était connecté
            connecte_compte("Non connecté") # On se connecte au compte par défault "Non connecté", qui déconnecte les autres comptes.


    # Retourne dans tous les cas 'page.html'
    return render_template('page.html', title='Traducteur Morse',lien_ampoule_trad="/static/ampoule.png",etat_lum="True", compte=compte_connecté(),
                           lien_volume_trad="/static/Volume.jpeg",etat_son="True",lien_volume_sequence_morse="/static/Volume2.jpg",etat_son_sequence_morse="False")




@app.route("/sequence",methods=["GET", "POST"]) # Envoi sur cette route si on lance l'enregistrement de la séquence (formulaire post)
def sequence():
    
     
    # On rentre toujours dans le if
    if request.method == "POST":
        
        sequence="" # On commence avec une séquence vide
        son_sequence_morse=request.form.get('sonore_sequence') # Récupère l'information pour savoir si le son du buzzer est actif pendant les appuis de la séquence morse au bouton
        # On l'obtient forcément en str

        """ Boucle enregistrement bouton"""
        
        couper=False
        while True:
            
            if son_sequence_morse=="True":
                button.on_press = press_button_avec_son # Se déclenche à l'appui du bouton.
                button.on_release = release_button_bouton_avec_son # Se déclenche quand le bouton n'est pas appuyé.
            else: # son_sequence_morse=="False"
                button.on_press = press_button_sans_son # Se déclenche à l'appui du bouton.
                button.on_release = release_button_bouton_sans_son # Se déclenche quand le bouton n'est pas appuyé.
                
            
            # Si premier bouton appuyé
            if raspi.input(pin_button): 
                sequence,couper=crea_sequence_morse(sequence,couper) # On met à jour la séquence
                
            # Si deuxième bouton appuyé
            elif raspi.input(pin_button2): 
                sequence+=' ' # On rajoute un espace à la séquence
                time.sleep(0.3) # On met un peu de temps de latence pour éviter des problèmes en cas de spam du bouton
            
            
            if couper:
                break
        """                             """     
        
        
        
        traduction=morse_to_texte(sequence)
    
        # On insère les informations de la traduction dans l'historique
        insert_historique(compte_connecté(),sequence,traduction)
        
        
        # On récupère les valeurs de son et lum (en str), qui correspondent aux états des images sous "Morse traduit en texte"
        # Le but est de garder leurs états dans la nouvelle page
        lum=request.form.get('lumineux')
        son=request.form.get('sonore')
        
        if lum=="True":
            lien_ampoule_trad="/static/ampoule.png"
        else:
            lien_ampoule_trad="/static/ampoule2.png"
        
        if son=="True":
            lien_volume_trad="/static/Volume.jpeg";
        else:
            lien_volume_trad="/static/Volume2.jpg"
            
        if son_sequence_morse=="True":
            lien_volume_sequence_morse="/static/Volume.jpeg";
        else:
            lien_volume_sequence_morse="/static/Volume2.jpg"

        
        # Retourne 'page.html'
        return render_template('page.html', title='Traducteur Morse', sequence=sequence,traduction=traduction,lien_ampoule_trad=lien_ampoule_trad,etat_lum=lum, compte=compte_connecté(),
                               lien_volume_trad=lien_volume_trad,etat_son=son,lien_volume_sequence_morse=lien_volume_sequence_morse,etat_son_sequence_morse=son_sequence_morse)
    
    

@app.route("/traduction",methods=["GET", "POST"]) # Envoi sur cette route si on lance la traduction d'un texte en morse (formulaire post)
def traduc():
    
    # On rentre toujours dans le if
    if request.method == "POST":
        
        texte=request.form.get('texte_traduit') # On récupère le texte à traduire
        sequence=texte_to_morse(texte) # On le traduit en morse
        
        # On récupère les valeurs des états des images de notre page
        # Le but est de garder leurs états dans la nouvelle page
        lum=request.form.get('lumineux')
        son=request.form.get('sonore')
        son_sequence_morse=request.form.get('sonore_sequence')
        
        
        
        if lum == "True" or son == "True":
            affiche(sequence,son,lum)
            
        # On insère les informations de la traduction dans l'historique
        insert_historique(compte_connecté(),sequence,texte)
    
        
        if lum=="True":
            lien_ampoule_trad="/static/ampoule.png"
        else:
            lien_ampoule_trad="/static/ampoule2.png"
        
        if son=="True":
            lien_volume_trad="/static/Volume.jpeg";
        else:
            lien_volume_trad="/static/Volume2.jpg"

        if son_sequence_morse=="True":
            lien_volume_sequence_morse="/static/Volume.jpeg";
        else:
            lien_volume_sequence_morse="/static/Volume2.jpg"
            
        
        
        # Retourne 'page.html'
        return render_template('page.html', title='Traducteur Morse', sequence=sequence,traduction=texte,lien_ampoule_trad=lien_ampoule_trad,etat_lum=lum, compte=compte_connecté(),
                               lien_volume_trad=lien_volume_trad,etat_son=son,lien_volume_sequence_morse=lien_volume_sequence_morse,etat_son_sequence_morse=son_sequence_morse)

      
      
    
"""            """
""" Historique """      
"""            """   
      
      
      
@app.route("/historique",methods=["GET", "POST"]) # En cliquant sur "Historique" en haut des page on arrive sur cette route sans requête
def historique():
    
    
    # Si on clique sur "supprimer l'historique" depuis "/historique", on est renvoyé sur la même page avec un formulaire post
    # Donc on rentre dans ce if
    if request.method == "POST":
        reset_hisorique(compte_connecté())
    
    
    # On récupère l'historique du compte auquel on est connecté
    tab=return_histo_selon_id(compte_connecté())
    len_tab=len(tab)
    
    if len_tab==0: # Si l'historique est vide
        tab=[("Vide","Vide","Vide")]
        len_tab=len(tab)    
    
    
    # Retourne 'histo.html'
    return render_template('histo.html', title='Historique',tab=tab,len_tab=len_tab,compte=compte_connecté())
    



"""               """
""" Apprentissage """   
"""               """



@app.route("/apprentissage",methods=["GET", "POST"]) # En cliquant sur "Apprentissage" en haut des page on arrive sur cette route sans requête
def apprentissage():
    
    # Retourne 'apprentissage.html'
    return render_template('apprentissage.html', title='Apprentissage',compte=compte_connecté())



@app.route("/apprentissage/ex_text_to_morse",methods=["GET", "POST"]) # On arrive forcément ici par une requête venant soit de"/apprentissage" (formulaire post)
# soit de "/apprentissage/ex_text_to_morse" ou "/apprentissage/ex_text_to_morse/reponse" (formulaire post) si on clic sur "refaire l'exercice avec les mêmes paramètres"
def ex_morse():
    sequence_joueur=""
    mot=""
    reponse=""
    
    # On rentre toujours ici et on récupère les informations du formulaire sur le choix de la difficulté de l'exercice
    if request.method == "POST":
        v1=request.form.get('val1')
        v2=request.form.get('val2')
        v3=request.form.get('val3')
            
        v1,v2,v3=parametres_to_bool(v1,v2,v3)
        
        # On obtient le mot que l'utilisateur doit traduire en morse
        mot=renvoie_mot(MORSE_DICT,liste_mot,v1,v2,v3)
        
    
    # Retourne 'ex_text_to_morse.html'
    return render_template('ex_text_to_morse.html', title='Exercice morse',mot=mot,sequence_joueur=sequence_joueur,reponse=reponse,v1=v1,v2=v2,v3=v3, compte=compte_connecté())



@app.route("/apprentissage/ex_text_to_morse/reponse",methods=["GET", "POST"]) # On arrive forcément ici par une requête venant de "/apprentissage/ex_text_to_morse" (formulaire post)
def ex_morse_reponse():
    
    sequence_joueur=""
    
    
    # On rentre toujours ici
    if request.method == "POST":
        mot=request.form.get('mot') # On récupère le mot à traduire
        morse_correct=texte_to_morse(mot) # Ainsi que sa traduction morse correcte

        
        """ Boucle enregistrement bouton"""
        couper=False
        while True:
            
            button.on_press = press_button_sans_son
            button.on_release = release_button_bouton_sans_son
            if raspi.input(pin_button):
                sequence_joueur,couper=crea_sequence_morse(sequence_joueur,couper)
            elif raspi.input(pin_button2):
                sequence_joueur+=' '
                time.sleep(0.3)
            if couper:
                break
        """                             """
        
        reponse=""
        
        # La boucle d'enregistrement du bouton stocke la réponse morse du joueur dans la variable sequence_joueur
        if sequence_joueur==morse_correct:
            reponse="Bonne réponse, bien joué !"
        else:
            reponse="Mauvaise réponse !"
        
        
        # On récupère les informations du formulaire sur le choix de la difficulté de l'exercice si l'utilisateur souhaite refaire l'exercice avec les mêmes paramètres
        v1=request.form.get('val1')
        v2=request.form.get('val2')
        v3=request.form.get('val3')
            
            
    # Retourne 'ex_text_to_morse.html'
    return render_template('ex_text_to_morse.html', title='Reponse exercice morse',mot=mot,morse_correct=morse_correct,sequence_joueur=sequence_joueur,
                           reponse=reponse,v1=v1,v2=v2,v3=v3, compte=compte_connecté())



@app.route("/apprentissage/ex_morse_to_texte",methods=["GET", "POST"])# On arrive forcément ici par une requête venant soit de"/apprentissage" (formulaire post)
# soit de "/apprentissage/ex_morse_to_texte", "/apprentissage/ex_morse_to_texte/envoi_morse" ou  "/apprentissage/ex_morse_to_texte/envoi_morse/reponse" (formulaire post)
# si on clic sur "refaire l'exercice avec les mêmes paramètres"
def ex_texte():
    
    # On choisi aléatoirement le type d'envoi du morse
    type_morse,son,lum=choix_type_renvoi_morse()
    
    texte_joueur=""
    reponse=""
    
    # On rentre toujours ici et on récupère les informations du formulaire sur le choix de la difficulté de l'exercice
    if request.method == "POST":
        
        v1=request.form.get('val1')
        v2=request.form.get('val2')
        v3=request.form.get('val3')
         
        v1,v2,v3=parametres_to_bool(v1,v2,v3)
        mot_correct=renvoie_mot(MORSE_DICT,liste_mot,v1,v2,v3) # On récupère le mot correct que doit trouver l'utilisateur
        morse=texte_to_morse(mot_correct) # Ainsi que sa traduction morse
        
        # On rentre dans ce if seulement si l'utilisateur a cliqué sur "refaire l'exercice avec les mêmes paramètres"
        # à partir des routes "/apprentissage/ex_morse_to_texte", "/apprentissage/ex_morse_to_texte/envoi_morse" ou  "/apprentissage/ex_morse_to_texte/envoi_morse/reponse"
        if request.form.get('type_morse') != None:
            
            # On récupère les informations sur le type d'envoi du morse
            son=request.form.get('son')
            lum=request.form.get('lum')
            type_morse=request.form.get('type_morse')
        

        
    # Retourne 'ex_text_to_morse.html'
    return render_template('ex_morse_to_texte.html', title='Exercice texte',morse=morse,type_morse=type_morse,son=son,lum=lum,texte_joueur=texte_joueur,
                           reponse=reponse,classe_rep="invisible",classe_bonne_rep="invisible",classe_valider="show",v1=v1,v2=v2,v3=v3, compte=compte_connecté())





@app.route("/apprentissage/ex_morse_to_texte/envoi_morse",methods=["GET", "POST"])
# On arrive forcément ici par une requête venant de "/apprentissage/ex_morse_to_texte" (formulaire post)
def ex_texte_envoi_morse(): # Cette def et cette route servent à envoyer le morse à l'utilisateur (lumineux, sonore, ou les 2)


    if request.method == "POST":
        
        # Variables servants dans le cas où l'utilisateur relance l'exercice avec les mêmes paramètres
        v1=request.form.get('val1')
        v2=request.form.get('val2')
        v3=request.form.get('val3')
        
        # Variables servants dans le cas où l'utilisateur relance l'exercice avec les mêmes paramètres, et pour envoyer le morse
        son=request.form.get('son')
        lum=request.form.get('lum')
        type_morse=request.form.get('type_morse')
        
        # Variables servants à contenir les informations du morse envoyé, du texte entré par l'utilisateur, et du texte correct
        morse=request.form.get('morse')
        texte_joueur=request.form.get('saisie')
        texte_correct=morse_to_texte(morse)
        
        # Variables servants à afficher le résultat final (définies dans le render template de la def juste avant)
        # Elles sont dans une configuration où le résultat est caché
        reponse=request.form.get('r_texte')
        classe_rep=request.form.get('classe_rep')
        classe_bonne_rep=request.form.get('classe_bonne_rep')
        classe_valider=request.form.get('valid_texte')
        
        # On envoit le morse
        affiche(morse,son,lum)
        
        
    # Retourne 'ex_text_to_morse.html'
    return render_template('ex_morse_to_texte.html', title='Exercice texte',morse=morse,type_morse=type_morse,son=son,lum=lum,texte_joueur=texte_joueur, compte=compte_connecté(),
                           reponse=reponse,classe_rep=classe_rep,classe_bonne_rep=classe_bonne_rep,classe_valider=classe_valider,texte_correct=texte_correct,v1=v1,v2=v2,v3=v3)



@app.route("/apprentissage/ex_morse_to_texte/envoi_morse/reponse",methods=["GET", "POST"])
# On arrive forcément ici par une requête venant de "/apprentissage/ex_morse_to_texte/envoi_morse" (formulaire post)
def ex_texte_envoi_morse_reponse():

    
    if request.method == "POST":
        
        # Variables servants dans le cas où l'utilisateur relance l'exercice avec les mêmes paramètres
        v1=request.form.get('val1')
        v2=request.form.get('val2')
        v3=request.form.get('val3')
        
        # Variables servants dans le cas où l'utilisateur relance l'exercice avec les mêmes paramètres, et pour envoyer le morse
        son=request.form.get('son')
        lum=request.form.get('lum')
        type_morse=request.form.get('type_morse')
        
        # Variables servants à contenir les informations du morse envoyé, du texte entré par l'utilisateur, et du texte correct
        morse=request.form.get('morse')
        texte_joueur=request.form.get('saisie')
        texte_correct=morse_to_texte(morse)
        
        
        
        reponse=""
        
        
        # On regarde si le texte du joueur est égal au texte correct
        if texte_joueur.upper()==texte_correct:
            reponse="Bonne réponse, bien joué !"
            classe_bonne_rep="invisible"
            classe_rep="show green"
        else:
            reponse="Mauvaise réponse !"
            classe_bonne_rep="show"
            classe_rep="show red"
        
        # En fonction de cela on modifie les variables servants à afficher le résultat final
        # Elles passent en même temps dans une configuration où le résultat est montré
        
    
    # Retourne 'ex_text_to_morse.html'
    return render_template('ex_morse_to_texte.html', title='Reponse exercice texte',morse=morse,type_morse=type_morse,son=son,lum=lum,texte_joueur=texte_joueur,reponse=reponse,
                           texte_correct=texte_correct,classe_rep=classe_rep,classe_bonne_rep=classe_bonne_rep,classe_valider="invisible",v1=v1,v2=v2,v3=v3, compte=compte_connecté())




"""        """
""" Profil """   
"""        """


@app.route('/profil',methods=["GET", "POST"]) # On arrive ici en cliquant sur l'image de profil en haut à droite des pages qui dirige par un lien, ou en arrivant de la route '/connexion'
def profil():
    
    # Si on est pas connecté
    if compte_connecté() == "Non connecté":
        return redirect('/connexion') # On est redirigé sur le portail de connexion
    
    # Si on est connecté
    else:

        # On récupère les infos du compte pour les afficher sur la page de profil
        infos=infos_compte(compte_connecté())
        identifiant=infos[0]
        mdp=infos[1]
        email=infos[2]
    
    # Retourne 'profil.html'
    return render_template('profil.html', title='Profil',identifiant=identifiant,email=email,mdp=mdp,compte=compte_connecté())



@app.route('/connexion',methods=["GET", "POST"]) # On arrive ici soit en étant redirigé à partir de la route '/profil', soit en venant d'ici ('/connexion') par une requête (formulaire post)
def connexion():
    
    # Si on connecté
    if compte_connecté() != "Non connecté":
        return redirect('/profil') # On est redirigé sur la page de profil
    
    # Si on est pas connecté
    else:
        classe_erreur="invisible"
        
        # En entrant les informations de connexion, le formulaire nous renvoit sur cette même page
        # On entre donc ici juste après avoir rempli les informations de connexion
        if request.method == "POST":
            
            # On récupère les infos entrées par l'utilisateur
            identifiant=request.form.get('identifiant')
            email=request.form.get('email')
            mdp=request.form.get('mdp')

            # On parcourt les comptes existants et on regarde si toutes les infos de l'utilisateur correspondent à un des comptes
            for comptes in return_table("COMPTES"):
                if comptes[0] == identifiant and comptes[1] == mdp and comptes[2]== email :
                    connecte_compte(comptes[0]) # On connecte alors le compte
                    return redirect('/profil') # Et on est redirigé sur la page de profil
                
            # On arrive ici si on sort de la boucle, seulement si les infos de l'utilisateur ne correspondent pas à un des comptes
            classe_erreur="show" # On affiche alors l'erreur sur la page de connexion, que l'on renvoit ensuite en sortant du if 
        
        # else
        # Si on arrive sur le portail de connexion pour la première fois, avant d'avoir rempli les informations de connexion
        # On renvoit juste la page de connexion
            
            
    # Retourne 'connexion.html'                
    return render_template('connexion.html', title='Connexion',classe_erreur=classe_erreur,compte=compte_connecté())


@app.route('/connexion/creation_compte',methods=["GET", "POST"]) # On arrive ici forcément par le lien de 'connexion.html', du portail de connexion
def creation_compte():
    
    classe_erreur="invisible"
    affichage_avant_validation="show"
    affichage_apres_validation="invisible"
    
    # En entrant les informations de création de compte, le formulaire nous renvoit sur cette même page
    # On entre donc ici juste après avoir rempli les informations de création de compte
    if request.method == "POST":
        identifiant_deja_pris=False
        
        # On récupère les infos entrées par l'utilisateur
        identifiant=request.form.get('identifiant')
        email=request.form.get('email')
        mdp=request.form.get('mdp')
        
        # On parcourt les comptes existants et on regarde si l'identifiant de l'utilisateur pour son nouveau compte est déjà pris ou pas (c'est la validation)
        for comptes in return_table("COMPTES"):
            if comptes[0] == identifiant:
                classe_erreur="show" # Si il est déjà pris, on indique que la page 'creation_compte.html' doit renvoyer une indication d'erreur à cause de ça
                identifiant_deja_pris=True
        
        if identifiant == "": # On n'autorise pas les identifiants vides
            classe_erreur="show"
            identifiant_deja_pris=True
        
        # Une fois qu'on a parcouru les comptes, si l'identifiant n'est pas pris (validation effectuée), on affiche la page avec un nouvel affichage (indiquant la création du compte)
        if identifiant_deja_pris == False: 
            classe_erreur="invisible"
            affichage_avant_validation="invisible"
            affichage_apres_validation="show"
            
            # On insert le compte dans la table des comptes, et on se connecte au nouveau compte
            insert_comptes(identifiant,mdp,email)
            connecte_compte(identifiant)
        
        
           
           
    # else
    # Si on arrive sur le portail de création de compte pour la première fois, avant d'avoir rempli les informations
    # On renvoit juste la page de création de compte

    
    
    # Retourne 'creation_compte.html' 
    return render_template('creation_compte.html', title='Création de compte',classe_erreur=classe_erreur, compte=compte_connecté(),
                           affichage_avant_validation=affichage_avant_validation,affichage_apres_validation=affichage_apres_validation)

if __name__ == "__main__": # Debugger activé
    app.run(debug=True)