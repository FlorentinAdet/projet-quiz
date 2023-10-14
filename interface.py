import tkinter as tk
from tkinter import ttk  # Importer le module ttk pour Progressbar
import threading
import time


class afficher_interface:
    def __init__(self):
        self.temps_total = 20  # Temps total en secondes
        self.temps_restant = self.temps_total
        self.label_leaderboard = None
        self.label_score_final = None
        self.leaderboard = {}

        self.fenetre = tk.Tk()
        self.fenetre.title(" " * 96 + "-- QUIZ --")
        self.fenetre.resizable(False, False)
        self.largeur = 720
        self.hauteur = 480
        self.fenetre.geometry(f"{self.largeur}x{self.hauteur}")

        self.couleur_fond = "#2F2F3F"
        self.couleur_gris_sombre = "#1F0F1F"
        self.couleur_texte_bouton = "white"
        self.fenetre.configure(bg=self.couleur_fond)

        self.int_score = 0
        self.label_score = tk.Label(self.fenetre, text=f"Score : {self.int_score}", fg="white", bg=self.couleur_fond)
        self.label_score.grid(row=0, column=1, sticky="ne", padx=10, pady=10)

        self.label_question = tk.Label(self.fenetre, text="QUESTION", fg="white", bg=self.couleur_fond)
        self.label_question.grid(row=0, column=0, columnspan=2, padx=10, pady=50)

        self.bouton_a = tk.Button(self.fenetre, text="A", width=30, height=2, bg=self.couleur_gris_sombre, fg=self.couleur_texte_bouton)
        self.bouton_b = tk.Button(self.fenetre, text="B", width=30, height=2, bg=self.couleur_gris_sombre, fg=self.couleur_texte_bouton)
        self.bouton_c = tk.Button(self.fenetre, text="C", width=30, height=2, bg=self.couleur_gris_sombre, fg=self.couleur_texte_bouton)
        self.bouton_d = tk.Button(self.fenetre, text="D", width=30, height=2, bg=self.couleur_gris_sombre, fg=self.couleur_texte_bouton)

        self.bouton_a.grid(row=1, column=0, padx=5, pady=(20, 0))
        self.bouton_b.grid(row=1, column=1, padx=60, pady=(20, 0))
        self.bouton_c.grid(row=2, column=0, padx=5, pady=(30, 20))
        self.bouton_d.grid(row=2, column=1, padx=60, pady=(30, 20))

        self.bouton_a.config(command=lambda: self.reaction_bouton("A"))
        self.bouton_b.config(command=lambda: self.reaction_bouton("B"))
        self.bouton_c.config(command=lambda: self.reaction_bouton("C"))
        self.bouton_d.config(command=lambda: self.reaction_bouton("D"))

        self.progress_bar = ttk.Progressbar(self.fenetre, mode="determinate", length=self.largeur)
        self.progress_bar.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        self.label_minuteur = tk.Label(self.fenetre, text=f"Temps restant : {self.temps_restant} s", fg="white", bg=self.couleur_fond)
        self.label_minuteur.grid(row=3, column=0, columnspan=2, padx=10, pady=30)

        self.minuteur_thread = threading.Thread(target=self.mise_a_jour_minuteur)
        self.minuteur_thread.start()

        self.fenetre.grid_rowconfigure(0, weight=1)
        self.fenetre.grid_rowconfigure(4, weight=1)
        self.fenetre.grid_columnconfigure(0, weight=1)
        self.fenetre.grid_columnconfigure(3, weight=1)

    def mise_a_jour_minuteur(self):
        while self.temps_restant >= 0:
            pourcentage_restant = (self.temps_restant / self.temps_total) * 100
            self.progress_bar["value"] = pourcentage_restant
            self.label_minuteur.config(text=f"Temps restant : {self.temps_restant} s")
            time.sleep(1)
            self.temps_restant -= 1

        # Quand le minuteur atteint 0, efface les éléments existants et affiche le score
        self.label_question.destroy()
        self.label_score.destroy()
        self.bouton_a.destroy()
        self.bouton_b.destroy()
        self.bouton_c.destroy()
        self.bouton_d.destroy()
        self.label_minuteur.destroy()
        self.progress_bar.destroy()
        self.afficher_score()

    def reaction_bouton(self, choix):
        print(f"Bouton {choix} pressé")
        self.temps_restant = self.temps_total + 1

    def afficher_score(self):
        # Affiche le score dans la même fenêtre
        self.leaderboard = [
            ["Joueur 1", 457],
            ["Joueur 2", 256],
            ["Joueur 3", 253],
            ["Joueur 4", 224],
            ["Joueur 5", 189],
            ["Joueur 6", 180],
            ["Joueur 7", 176],
            ["Joueur 8", 145],
            ["Joueur 9", 142],
            ["Joueur 10", 130]
        ]

        leaderboard_text = "#•• LEADERBOARD ••#\n\n"
        for joueur, score in self.leaderboard:
            leaderboard_text += f"{joueur} : {score}\n"
        leaderboard_text += "\n#•••••••••••••••••••#"

        self.label_leaderboard = tk.Label(
            self.fenetre,
            text=leaderboard_text,
            fg="white",
            bg=self.couleur_fond
        )

        self.label_score_final = tk.Label(self.fenetre, text=f"Score final : {self.int_score}", fg="white", bg=self.couleur_fond)

        self.entry_nom_joueur = tk.Entry(self.fenetre)
        self.bouton_enregistrer = tk.Button(self.fenetre, text="Enregistrer le score", width=15, height=1,
                                            bg=self.couleur_gris_sombre, fg=self.couleur_texte_bouton)
        self.bouton_recommencer = tk.Button(self.fenetre, text="Recommencer", width=12, height=1,
                                            bg=self.couleur_gris_sombre, fg=self.couleur_texte_bouton)

        self.label_leaderboard.grid(row=1, column=0, padx=300, pady=10, columnspan=1)
        self.label_score_final.grid(row=2, column=0, padx=300, pady=10, columnspan=1)
        self.entry_nom_joueur.grid(row=3, column=0, padx=0, pady=10, columnspan=2)
        self.bouton_enregistrer.grid(row=4, column=0, padx=5, pady=0)
        self.bouton_recommencer.grid(row=5, column=0, padx=5, pady=20)