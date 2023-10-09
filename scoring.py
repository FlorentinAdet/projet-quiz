# scoring.py

# Variables globales
reponses_correctes_consecutives = 0

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
        return 1.5
    else:
        return 1

# Fonction de scoring complète
def scoring(difficulte, reponse_correcte, temps_de_reponse):
    A = attribuer_points(difficulte)
    B = points_bonus_series_consecutives(reponse_correcte)
    C = points_bonus_reponse_rapide(temps_de_reponse)
    resultat = (A + B) * C

    return resultat

def main():
    difficulte = 2  # Niveau de difficulté
    reponse_correcte = True  # Si la réponse est correcte
    temps_de_reponse = 5  # Temps de réponse en secondes

    score = scoring(difficulte, reponse_correcte, temps_de_reponse)
    print("Score final :", score)

if __name__ == "__main__":
    main()
