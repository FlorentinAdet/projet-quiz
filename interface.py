import tkinter as tk
from tkinter import ttk
import threading
import time
import json
from questions import load_questions_from_json, get_random_question
from scoring import Score
from save import ScoreRepository

class afficher_interface:
    def __init__(self):
        theme, question, options, correct_answer, difficulty = get_random_question(load_questions_from_json('questions.json'))

        self.temps_total = 10  # Temps total en secondes
        self.temps_restant = self.temps_total
        self.label_leaderboard = None
        self.label_score_final = None
        self.leaderboard = {}
        self.int_vie = 3

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
        self.label_score = tk.Label(self.fenetre, text=f"Vie : {self.int_vie} | Score : {self.int_score}", fg="white", bg=self.couleur_fond)
        self.label_score.grid(row=0, column=1, sticky="ne", padx=10, pady=10)

        self.label_question = tk.Label(self.fenetre, text=f"{question}\n\nDifficulty : {difficulty}/3", fg="white", bg=self.couleur_fond)
        self.label_question.grid(row=0, column=0, columnspan=2, padx=10, pady=50)

        self.bouton_a = tk.Button(self.fenetre, text=f"A) {options[0]}", width=30, height=2, bg=self.couleur_gris_sombre, fg=self.couleur_texte_bouton)
        self.bouton_b = tk.Button(self.fenetre, text=f"B) {options[1]}", width=30, height=2, bg=self.couleur_gris_sombre, fg=self.couleur_texte_bouton)
        self.bouton_c = tk.Button(self.fenetre, text=f"C) {options[2]}", width=30, height=2, bg=self.couleur_gris_sombre, fg=self.couleur_texte_bouton)
        self.bouton_d = tk.Button(self.fenetre, text=f"D) {options[3]}", width=30, height=2, bg=self.couleur_gris_sombre, fg=self.couleur_texte_bouton)

        self.correct_answer = correct_answer
        self.difficulty = difficulty

        self.bouton_a.grid(row=1, column=0, padx=5, pady=(20, 0))
        self.bouton_b.grid(row=1, column=1, padx=60, pady=(20, 0))
        self.bouton_c.grid(row=2, column=0, padx=5, pady=(30, 20))
        self.bouton_d.grid(row=2, column=1, padx=60, pady=(30, 20))

        self.bouton_a.config(command=lambda: self.reaction_bouton(f"{options[0]}"))
        self.bouton_b.config(command=lambda: self.reaction_bouton(f"{options[1]}"))
        self.bouton_c.config(command=lambda: self.reaction_bouton(f"{options[2]}"))
        self.bouton_d.config(command=lambda: self.reaction_bouton(f"{options[3]}"))

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
        self.score = Score()
        self.correct_answer = None
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
        if choix == self.correct_answer:
            points = self.score.attribuer_points(self.difficulty)
            bonus_series = self.score.points_bonus_series_consecutives(True,self.score.reponses_correctes_consecutives)
            self.int_score += points * bonus_series
            self.label_score.config(text=f"Score : {self.int_score}")
            self.score.reponses_correctes_consecutives += 1
        else:
            self.int_vie -= 1
            self.score.reponses_correctes_consecutives = 0  # Réinitialise la série de bonnes réponses en cas de mauvaise réponse
            if self.int_vie == 0:
                self.temps_restant = 0

        self.temps_restant = self.temps_total + 1
        if self.int_vie == 0:
            self.temps_restant = 0
        self.label_score.config(text=f"Vie : {self.int_vie}  |  Score : {self.int_score}")

        theme, question, options, correct_answer, difficulty = get_random_question(load_questions_from_json('questions.json'))

        self.label_question.config(text=f"{question}\n\nDifficulty : {difficulty}/3")
        self.bouton_a.config(text=f"A) {options[0]}")
        self.bouton_b.config(text=f"B) {options[1]}")
        self.bouton_c.config(text=f"C) {options[2]}")
        self.bouton_d.config(text=f"D) {options[3]}")

        self.bouton_a.config(command=lambda: self.reaction_bouton(f"{options[0]}"))
        self.bouton_b.config(command=lambda: self.reaction_bouton(f"{options[1]}"))
        self.bouton_c.config(command=lambda: self.reaction_bouton(f"{options[2]}"))
        self.bouton_d.config(command=lambda: self.reaction_bouton(f"{options[3]}"))

        self.correct_answer = correct_answer
    def afficher_score(self):
        # Charger les scores depuis le fichier JSON
        try:
            with open('scores.json', 'r') as scores_file:
                scores_data = json.load(scores_file)
        except FileNotFoundError:
            scores_data = {"scores": []}

        # Trier les scores par ordre décroissant
        scores_data["scores"].sort(key=lambda x: x["score"], reverse=True)

        # Prendre les 5 meilleurs scores
        top_scores = scores_data["scores"][:5]

        # Créer une chaîne de texte avec les meilleurs scores
        leaderboard_text = "#•• LEADERBOARD ••#\n\n"
        for entry in top_scores:
            leaderboard_text += f"{entry['pseudo']} : {entry['score']}\n"
        leaderboard_text += "\n#•••••••••••••••••••#"

        # Afficher le leaderboard dans la fenêtre
        if self.label_leaderboard:
            self.label_leaderboard.destroy()

        self.label_leaderboard = tk.Label(
            self.fenetre,
            text=leaderboard_text,
            fg="white",
            bg=self.couleur_fond
        )
        self.label_leaderboard.grid(row=1, column=0, padx=300, pady=10, columnspan=1)
        # Créer une entrée de texte pour le nom du joueur
        self.entry_nom_joueur = tk.Entry(self.fenetre)
        self.entry_nom_joueur.grid(row=3, column=0, padx=0, pady=10, columnspan=2)

        # Créer un bouton pour sauvegarder le score
        self.bouton_enregistrer = tk.Button(
            self.fenetre,
            text="Sauvegarder le score",
            width=15,
            height=1,
            bg=self.couleur_gris_sombre,
            fg=self.couleur_texte_bouton,
            command=self.sauvegarder_score
        )
        self.bouton_enregistrer.grid(row=4, column=0, padx=5, pady=0)

    def sauvegarder_score(self):
        pseudo_joueur = self.entry_nom_joueur.get()
        if not pseudo_joueur:
            pseudo_joueur = "Joueur Anonyme"  # Utilisateur anonyme si le champ est vide

        # Enregistrer le score en utilisant la classe ScoreRepository
        score_repo = ScoreRepository("scores.json")
        score_repo.ajouter_score(self.int_score, pseudo_joueur)

        # Afficher un message pour indiquer que le score a été enregistré
        self.label_leaderboard.config(text=f"Score enregistré\n pour {pseudo_joueur} !")

        # Désactiver le bouton "Sauvegarder le score" après l'enregistrement
        self.bouton_enregistrer.config(state="disabled")
