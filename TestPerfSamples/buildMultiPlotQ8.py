import matplotlib.pyplot as plt

# Exemple de données
tailles = [0, 115527, 202890, 449955, 645593]  # X-axis
labels_x = ["0","~115k", "~203k", "~450k", "~646k"]  # Labels personnalisés
temps_comp = [0,931.459, 1607.584, 3658.55, 5284.37]
temps_decomp = [0,838.253, 1418.139, 3225.621, 4663.974]
fichiers = ["","Blaise_Pascal", "La_morale_\nde_Nietzsche", "Indiens", "Peninsule_des_Balkans"]

# Calcul des différences
diff = [c - d for c, d in zip(temps_comp, temps_decomp)]

fig, axes = plt.subplots(2, 1, figsize=(10,10))  # 2 lignes, 1 colonne

# --- SUBPLOT 1 : Courbes ---
axes[0].plot(tailles, temps_comp, marker=".", label='Compression (ms)')
axes[0].plot(tailles, temps_decomp, marker=".", label='Décompression (ms)')
axes[0].set_xlim(left=0)
axes[0].set_ylim(bottom=0)
axes[0].set_xticks(tailles)
axes[0].set_xticklabels(labels_x)
axes[0].set_xlabel("Nombre total de caractères", labelpad=20)
axes[0].set_ylabel("Temps (ms)")
axes[0].set_title("Analyse des performances question 8")
axes[0].legend()
axes[0].grid(True)

# Ajouter les noms de fichiers (en bas)
for x, f in zip(tailles, fichiers):
    axes[0].text(x, -700, f, ha='center', va='top')

# Ajustement automatique pour éviter chevauchements
plt.subplots_adjust(bottom=0.25, hspace=0.5)

# --- SUBPLOT 2 : Bar chart des différences ---
bars = axes[1].bar(labels_x[1:], diff[1:], color='red')
axes[1].set_title("Différence (Compression - Décompression)")
axes[1].set_xlabel("Nombre total de caractères", labelpad=30)
axes[1].set_ylabel("Différence (ms)")
axes[1].axhline(0, color='black', linewidth=0.8)

# Ajouter les noms de fichiers sous les barres
for i, f in enumerate(fichiers[1:]):
    axes[1].text(i, -80, f, ha='center', va='top', rotation=0)

# Ajouter les valeurs sur les barres
for i, v in enumerate(diff[1:]):
    axes[1].text(i, v + 0.5 , f"{v:.1f}",
                 ha='center', va='bottom' if v>=0 else 'top')

plt.show()