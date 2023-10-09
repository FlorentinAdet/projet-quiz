# scoring.py

# Fonction pour attribuer des points en fonction de la difficulté
def attribuer_points(difficulte):
    if difficulte == 1:
        return 10
    elif difficulte == 2:
        return 20
    else:
        return 30

# Fonction pour attribuer des points bonus pour les séries de bonnes réponses
def points_bonus_series_consecutives(reponse_correcte):
    global reponses_correctes_consecutives
    if reponse_correcte:
        reponses_correctes_consecutives += 1
        if reponses_correctes_consecutives % 3 == 0:  # Bonus tous les 3 bonnes réponses consécutives
            return 15
    else:
        reponses_correctes_consecutives = 0  # Réinitialisation en cas de mauvaise réponse
    return 0

# Fonction pour attribuer des points bonus pour les réponses rapides
def points_bonus_reponse_rapide(temps_de_reponse):
    if temps_de_reponse < 10:  # Si la réponse est donnée en moins de 10 secondes
        return 1,5
    else:
        return 1

def scoring(temps_de_reponse, reponse_correcte, difficulte):
    A = attribuer_points(difficulte)
    B = points_bonus_reponse_rapide(temps_de_reponse)
    C = points_bonus_series_consecutives(reponse_correcte)
    resultat = (A+B)*C

    return resultat