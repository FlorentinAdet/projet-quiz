from interface import afficher_interface
from bonus import Question
from scoring import Score
from save import ScoreRepository
import json
import threading
import time


def charger_questions(theme):
    try:
        with open('questions.json', 'r') as json_file:
            data = json.load(json_file)
            return data.get(theme, {})
    except FileNotFoundError:
        return {}


def effectuer_quiz(theme):
    questions_theme = charger_questions(theme)
    app = afficher_interface()
    score = Score()
    score_total = 0

    def mise_a_jour_interface():
        if not questions_theme:
            app.afficher_score_final(score_total)
            pseudo = input("Entrez votre pseudo : ")
            repo = ScoreRepository("scores.json")
            donnees = repo.ajouter_score(score_total, pseudo)
            print("Nouveau score ajouté !")
            print(donnees)
        else:
            question_id, question_data = questions_theme.popitem()
            question = question_data["question"]
            options = question_data["options"]
            reponse_correcte = question_data["correct_answer"]
            difficulte = question_data["difficulty"]
            app.mise_a_jour_question(question, options, difficulte, reponse_correcte)
            app.reponse = None
            app.temps_restant = 20
            t = threading.Thread(target=verifier_reponse, args=(question_data,))
            t.start()

    def verifier_reponse(question_data):
        while app.temps_restant > 0:
            time.sleep(1)
            app.temps_restant -= 1
            app.mise_a_jour_minuteur(app.temps_restant)

        if app.reponse is not None:
            nonlocal score_total
            if app.reponse == question_data["correct_answer"]:
                points = score.attribuer_points(question_data["difficulty"])
                bonus_series = score.points_bonus_series_consecutives(True, score.reponses_correctes_consecutives)
                score_total += points * bonus_series
            app.reinitialiser_interface()
            mise_a_jour_interface()

    mise_a_jour_interface()
    app.fenetre.mainloop()


def main():
    print("Bienvenue dans le Quiz !")
    theme = input("Choisissez un thème (Geography, Science, History, Entertainment) : ")

    if theme not in ["Geography", "Science", "History", "Entertainment"]:
        print("Thème invalide. Choisissez parmi les thèmes disponibles.")
        return

    effectuer_quiz(theme)


if __name__ == "__main__":
    main()
