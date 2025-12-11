import matplotlib.pyplot as plt

fichiers = ["Blaise_Pascal", "La_morale_\nde_Nietzsche", "Indiens", "Peninsule_des_Balkans"]
serie1 = [46.26, 45.07, 43.43, 44.16]
serie2 = [(100-46.26), (100-45.07), (100-43.43), (100-44.16)]

# Barres empilées
bars1 = plt.bar(fichiers, serie1, label='5 caractères les plus utilisés')
bars2 = plt.bar(fichiers, serie2, bottom=serie1, label='Tous les autres caractères')

# Ajouter les valeurs de la série 1 sur les barres
for bar, value in zip(bars1, serie1):
    plt.text(
        bar.get_x() + bar.get_width()/2,  # position x : centre de la barre
        value/2,                          # position y : milieu de la barre
        f'{value:.2f}%',                  # texte à afficher
        ha='center', va='center', fontsize=14, color='black'
    )

plt.ylabel("Occupation du texte (%)")
plt.title("Diversité des caractères des textes naturels")
plt.legend()

plt.ylim(0, 120)
# Filtrer les labels y
plt.yticks([tick for tick in plt.yticks()[0] if tick <= 100])

plt.show()