class Score:

    def __init__(self):
        self.reponses_correctes_consecutives = 0

    def attribuer_points(self, difficulte):
        if difficulte == 1:
            return 10
        elif difficulte == 2:
            return 20
        else:
            return 30

    def points_bonus_series_consecutives(self, reponse_correcte, reponses_correctes_consecutives):
        if reponse_correcte:
            reponses_correctes_consecutives += 1
            if reponses_correctes_consecutives % 3 == 0:  
                return 1.5 # Bonus tous les 3 bonnes réponses consécutives
        else:
            reponses_correctes_consecutives = 0 # Réinitialisation en cas de mauvaise réponse
        return 1

    def points_bonus_reponse_rapide(self, temps_de_reponse):
        if temps_de_reponse <= 10:
            return 1.5
        else:
            return 1

# Exemple d'utilisation

score = Score() 

points = score.attribuer_points(difficulte=2) 
bonus = score.points_bonus_series_consecutives(reponse_correcte=True, reponses_correctes_consecutives=score.reponses_correctes_consecutives)
score_total = points * bonus