import matplotlib.pyplot as plt
import numpy as np

# -------------------------------
# Données du duel demandé
# -------------------------------

data = {
    "large_sample2.json": {
        "hauteur": 15,
        "longueur moyenne des codes": 3.09,
        "compression": 107.57,
        "decompression": 91.871,
        "taux": 0.39004,
        "top5_total": 73.13   # en pourcentage
    },
    "large_sample1.csv": {
        "hauteur": 11,
        "longueur moyenne des codes": 5.00,
        "compression": 218.751,
        "decompression": 201.055,
        "taux": 0.62813,
        "top5_total": 34.94   # en pourcentage
    }
}

file1 = "large_sample2.json"
file2 = "large_sample1.csv"

# -------------------------------
# Fonction qui trace le duel
# -------------------------------

def plot_duel(file1, file2):

    fig, axes = plt.subplots(2, 2, figsize=(10, 10))
    fig.suptitle(f"Duel : {file1} vs {file2}", fontsize=16)

    width = 0.35  # Largeur des barres

    # ----- 1) Hauteur + Longueur moyenne -----
    ax = axes[0][0]
    ax.bar([0], data[file1]["hauteur"], width, label=file1, color="green")
    ax.bar([0 + width], data[file2]["hauteur"], width, label=file2, color="yellow")
    ax.bar([1], data[file1]["longueur moyenne des codes"], width, color="green")
    ax.bar([1 + width], data[file2]["longueur moyenne des codes"], width, color="yellow")

    ax.set_xticks([0.2, 1.2])
    ax.set_xticklabels(["hauteur", "long. moy.\ncodes"])
    ax.set_title("Hauteur & Longueur moyenne des codes")
    ax.tick_params(axis='x', which='both', length=0)
    ax.set_ylim(0, 20)
    ax.set_yticks(range(0, 21, 2))
    ax.legend()

    # ----- 2) Temps compression + décompression -----
    ax = axes[0][1]
    ax.bar([0], data[file1]["compression"], width, label=file1, color="green")
    ax.bar([0 + width], data[file2]["compression"], width, label=file2, color="yellow")
    ax.bar([1], data[file1]["decompression"], width, color="green")
    ax.bar([1 + width], data[file2]["decompression"], width, color="yellow")

    ax.set_xticks([0.2, 1.2])
    ax.set_xticklabels(["compression", "décompression"])
    ax.set_title("Temps compression / décompression (ms)")
    ax.tick_params(axis='x', which='both', length=0)
    ax.set_ylim(0, 250)
    ax.legend()

    # ----- 3) Taux de compression -----
    ax = axes[1][0]
    ax.bar([0], data[file1]["taux"], width, label=file1, color="green")
    ax.bar([0 + width], data[file2]["taux"], width, label=file2, color="yellow")

    ax.set_xticks([0.175])
    ax.set_xticklabels(["taux"])
    ax.set_title("Taux de compression")
    ax.tick_params(axis='x', which='both', length=0)
    ax.set_ylim(0, 1)
    ax.legend()

    # ----- 4) Somme du Top 5 des caractères les plus présents -----
    ax = axes[1][1]
    ax.bar([0], data[file1]["top5_total"], width, label=file1, color="green")
    ax.bar([0 + width], data[file2]["top5_total"], width, label=file2, color="yellow")

    ax.set_xticks([0.175])
    ax.set_xticklabels(["Top 5 (%)"])
    ax.set_title("Somme des 5 caractères les + fréquents")
    ax.tick_params(axis='x', which='both', length=0)
    ax.set_ylim(0, 100)
    ax.set_yticks(range(0, 101, 10))
    ax.legend()

    plt.tight_layout()
    plt.show()


# -------------------------------
# Exécuter le duel
# -------------------------------
plot_duel(file1, file2)