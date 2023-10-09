import tkinter as tk
from tkinter import ttk  # Importer le module ttk pour Progressbar
import threading
import time


def afficher_interface():
    #################################
    #   PARAMETRES DE LA FENETRE    #
    #################################

    fenetre = tk.Tk()
    fenetre.title(" " * 98 + "-- QUIZ --")
    fenetre.resizable(False, False)
    largeur = 720
    hauteur = 480
    fenetre.geometry(f"{largeur}x{hauteur}")

    # Couleurs Personnalisées
    couleur_fond = "#3F2F3F"
    couleur_gris_sombre = "#0F0F0F"
    couleur_texte_bouton = "white"
    fenetre.configure(bg=couleur_fond)

    #############################
    #   CONTENU DE LA FENETRE   #
    #############################

    # Score
    label_score = tk.Label(fenetre, text="Score : 0", fg="white", bg=couleur_fond)
    label_score.grid(row=0, column=1, sticky="ne", padx=10, pady=10)  # Placer le label en haut à droite

    # Question
    label_question = tk.Label(fenetre, text="QUESTION", fg="white", bg=couleur_fond)
    label_question.grid(row=0, column=0, columnspan=2, padx=10, pady=10)  # Placer le label au milieu

    # Boutons "A", "B", "C" et "D"
    boutons_width = 30
    bouton_a = tk.Button(fenetre, text="A", width=boutons_width, height=2, bg=couleur_gris_sombre,
                         fg=couleur_texte_bouton)
    bouton_b = tk.Button(fenetre, text="B", width=boutons_width, height=2, bg=couleur_gris_sombre,
                         fg=couleur_texte_bouton)
    bouton_c = tk.Button(fenetre, text="C", width=boutons_width, height=2, bg=couleur_gris_sombre,
                         fg=couleur_texte_bouton)
    bouton_d = tk.Button(fenetre, text="D", width=boutons_width, height=2, bg=couleur_gris_sombre,
                         fg=couleur_texte_bouton)

    bouton_a.grid(row=1, column=0, padx=5, pady=(20, 0))
    bouton_b.grid(row=1, column=1, padx=60, pady=(20, 0))
    bouton_c.grid(row=2, column=0, padx=5, pady=(0, 20))
    bouton_d.grid(row=2, column=1, padx=60, pady=(0, 20))

    # Barre de chargement
    progress_bar = ttk.Progressbar(fenetre, mode="determinate", length=largeur)
    progress_bar.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    # Minuteur
    def mise_a_jour_minuteur():
        temps_total = 20  # Temps total en secondes (par exemple, 60 secondes)
        temps_restant = temps_total
        while temps_restant >= 0:
            pourcentage_restant = (temps_restant / temps_total) * 100
            progress_bar["value"] = pourcentage_restant
            time.sleep(1)
            temps_restant -= 1


    minuteur_thread = threading.Thread(target=mise_a_jour_minuteur)
    minuteur_thread.start()

    # Configure la grille pour centrer le contenu
    fenetre.grid_rowconfigure(0, weight=1)
    fenetre.grid_rowconfigure(5, weight=1)
    fenetre.grid_columnconfigure(0, weight=1)
    fenetre.grid_columnconfigure(3, weight=1)

    fenetre.mainloop()


afficher_interface()