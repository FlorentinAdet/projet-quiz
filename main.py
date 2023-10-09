from scoring import Score
from save import ScoreRepository
import random
import time

# Questions, réponses, corrections
questions = ["Quelle est la capitale de la France ?", "Qui a écrit Le Petit Prince ?",
             "Quelle est la racine carrée de 9 ?"]
reponses = [["Paris", "Marseille", "Lyon"], ["Jules Verne", "Antoine de Saint-Exupéry", "Victor Hugo"], ["3", "2", "4"]]
corrections = [0, 1, 0]

# Initialisation du repo
repo = ScoreRepository("scores.json")

# Variable pour cumuler les scores
score_total = 0

# Boucle de jeu
for i in range(3):

    print(questions[i])

    for j, r in enumerate(reponses[i]):
        print(f"{j + 1}. {r}")

    temps_debut = time.time()
    reponse_joueur = input("Votre réponse: ")
    temps_fin = time.time()

    # Vérification réponse
    if int(reponse_joueur) - 1 == corrections[i]:
        print("Bonne réponse !")
        reponse_correcte = True
    else:
        print("Mauvaise réponse !")
        reponse_correcte = False

    # Calcul du score
    score = Score()
    points = score.attribuer_points(i + 1)
    bonus_consec = score.points_bonus_series_consecutives(reponse_correcte, score.reponses_correctes_consecutives)
    bonus_rapidite = score.points_bonus_reponse_rapide(temps_fin - temps_debut)
    score_tour = points * bonus_consec * bonus_rapidite

    print(f"Vous avez gagné {score_tour} points !");

    # Cumul des scores
    score_total += score_tour

# Demande du nom
nom_joueur = input("Entrez votre nom : ")

# Sauvegarde du score total
repo.ajouter_score(score_total, nom_joueur)

print("Scores enregistrés :", repo.obtenir_donnees())