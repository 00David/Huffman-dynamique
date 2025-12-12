import matplotlib.pyplot as plt

# Exemple de données
tailles = [0, 117805, 206395, 459988, 655901]  # X-axis
labels_x = ["0","~118k", "~206k", "~460k", "~656k"]  # Labels personnalisés
temps_comp = [0,950.583, 1662.918, 3874.427, 5557.657]
temps_decomp = [0,881.901, 1515.107, 3417.671, 4855.011]
fichiers = ["","Blaise_Pascal", "La_morale_\nde_Nietzsche", "Indiens", "Peninsule_des_Balkans"]

plt.figure(figsize=(10,6))

# Tracer les courbes
plt.plot(tailles, temps_comp, marker=".", label='Temps de compression (ms)', color='blue')
plt.plot(tailles, temps_decomp, marker=".", label='Temps de décompression (ms)', color='red')

# Axes qui commencent à 0
plt.xlim(left=0)
plt.ylim(bottom=0)

# Labels et titre
plt.xlabel("Nombre total de caractères", labelpad=30)
plt.ylabel("Temps (ms)")
plt.title("Analyse des performances question 8", pad=20)
plt.legend()
plt.grid(True)

# Mettre les labels personnalisés sur l'axe des x
plt.xticks(tailles, labels_x)

# Ajuster la marge inférieure pour laisser de la place aux labels
plt.subplots_adjust(bottom=0.2)

# Ajouter les noms de fichiers sous chaque point, tournés à 90° vers la droite
for x, f in zip(tailles, fichiers):
    plt.text(x+5000, -700, f, rotation=0, ha='center', va='top')  # position verticale ajustable

plt.show()