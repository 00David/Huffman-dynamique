import matplotlib.pyplot as plt
import numpy as np

# -------------------------------
# Données
# -------------------------------

data = {
    "fr1.txt": {
        "hauteur": 10, "longueur moyenne des codes": 6.86,
        "compression": 33.736, "decompression": 31.5,
        "taux": 0.85275
    },
    "fr2.txt": {
        "hauteur": 11, "longueur moyenne des codes": 6.60,
        "compression": 26.069, "decompression": 25.881,
        "taux": 0.8169
    },
    "fr4.txt": {
        "hauteur": 8, "longueur moyenne des codes": 6.93,
        "compression": 323.046, "decompression": 315.109,
        "taux": 0.73795
    },
    "fr5.txt": {
        "hauteur": 15, "longueur moyenne des codes": 6.65,
        "compression": 254.709, "decompression": 252.225,
        "taux": 0.72312
    },
    "latin1.txt": {
        "hauteur": 14, "longueur moyenne des codes": 10.20,
        "compression": 2477.456, "decompression": 2440.224,
        "taux": 0.64159
    },
    "latin2.txt": {
        "hauteur": 14, "longueur moyenne des codes": 9.92,
        "compression": 2016.517, "decompression": 1998.54,
        "taux": 0.61683
    }
}

duels = [
    ("fr1.txt", "fr2.txt"),
    ("fr4.txt", "fr5.txt"),
    ("latin1.txt", "latin2.txt"),
]

# -------------------------------
# Fonction pour tracer un duel
# -------------------------------

def plot_duel(file1, file2):

    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    fig.suptitle(f"Duel : {file1} vs {file2}", fontsize=16)

    # Largeur des barres
    width = 0.35  
    x = np.arange(2)  # toujours 2 fichiers

    # ----- 1) Hauteur + Longueur -----
    ax = axes[0]
    ax.bar([0], data[file1]["hauteur"], width, label=file1, color="blue")
    ax.bar([0 + width], data[file2]["hauteur"], width, label=file2, color="red")
    ax.bar([1], data[file1]["longueur moyenne des codes"], width, color="blue")
    ax.bar([1 + width], data[file2]["longueur moyenne des codes"], width, color="red")

    ax.set_xticks([0.2, 1.2])
    ax.set_xticklabels(["hauteur", "long. moy. des codes"])
    ax.set_title("Hauteur & Longueur moyenne des codes")
    ax.tick_params(axis='x', which='both', length=0)
    ax.set_ylim(0, 20)
    ax.set_yticks(range(0, 20+1, 2))
    ax.legend()

    # ----- 2) Compression + Décompression -----
    ax = axes[1]
    ax.bar([0], data[file1]["compression"], width, label=file1, color="blue")
    ax.bar([0 + width], data[file2]["compression"], width, label=file2, color="red")
    ax.bar([1], data[file1]["decompression"], width, color="blue")
    ax.bar([1 + width], data[file2]["decompression"], width, color="red")

    ax.set_xticks([0.2, 1.2])
    ax.set_xticklabels(["compression", "décompression"])
    ax.set_title("Temps compression / décompression (ms)")
    ax.tick_params(axis='x', which='both', length=0)
    ax.legend()

    # ----- 3) Taux de compression -----
    ax = axes[2]
    ax.bar([0], data[file1]["taux"], width, label=file1, color="blue")
    ax.bar([0 + width], data[file2]["taux"], width, label=file2, color="red")

    ax.set_xticks([0.175])
    ax.set_xticklabels(["taux"])
    ax.set_title("Taux de compression")
    ax.tick_params(axis='x', which='both', length=0)
    ax.set_ylim(0, 1)
    ax.legend()

    plt.tight_layout()
    plt.show()


# -------------------------------
# Exécute les 3 duels
# -------------------------------
for f1, f2 in duels:
    plot_duel(f1, f2)