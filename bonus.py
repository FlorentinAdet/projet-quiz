import json
import random
class Question:
    def __init__(self, question, difficulty, options,  theme, correct_answer):
        self.question = question
        self.difficulty = difficulty
        self.theme = theme
        self.options = options
        self.correct_answer = correct_answer

    def formatJSON(self):
        new_question = {
            "question": self.question,
            "difficulty": self.difficulty,
            "theme": self.theme,
            "options": self.options,
            "correct_answer": self.correct_answer,
        }
        return new_question


def create_question():
    # Récupérer les entrées de l'utilisateur du formulaire
    question = input("Entrez la question : ")
    options = [input(f"Entrez la proposition {i + 1} : ") for i in range(4)]
    correct_answer = int(input("Entrez le numéro de la proposition correcte (1-4) : "))
    difficulty = input("Entrez le niveau (facile, normal, difficile) : ")
    theme = input("Entrez la catégorie de la question : ")

    return Question(question, difficulty, options, theme, correct_answer)

def add_question_to_json(question, theme):
    try:
        # Lire le contenu existant du fichier JSON
        with open('questions.json', 'r') as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        data = {}  # Le fichier n'existe pas encore

    questions_in_theme = data[theme]

    last_id = max(int(id) for id in questions_in_theme.keys())
    # Incrémenter l'ID pour la nouvelle question
    new_id = last_id + 1
    # Ajouter la nouvelle question avec le nouvel ID
    print(question.formatJSON())
    data[theme][str(new_id)] = question.formatJSON()

    # Écrire la structure de données mise à jour dans le fichier JSON
    with open('questions.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

def bonus5050(question): #question sous format JSON
    modified_question = question.copy()

    # Identifiez la position de la réponse correcte
    correct_answer_index = modified_question["correct_answer"]

    # Retirez la réponse correcte de la liste des options
    correct_answer = modified_question["options"][correct_answer_index]
    modified_question["options"].pop(correct_answer_index)

    # Choisissez une réponse incorrecte au hasard parmi les options restantes
    random_incorrect_answer = random.choice(modified_question["options"])

    # Créez la liste finale des réponses, en incluant la réponse correcte et une réponse incorrecte
    final_answers = [correct_answer, random_incorrect_answer]

    # Mélangez les réponses pour qu'elles apparaissent dans un ordre aléatoire
    random.shuffle(final_answers)

    # Mettez à jour la question avec les réponses modifiées
    modified_question["options"] = final_answers

    return modified_question


# Affichez la question modifiée au format JSON
# print(json.dumps(modified_question, indent=4))


def main():
    print("\nCréation d'une nouvelle question :")
    new_question = create_question()
    add_question_to_json(new_question, "Geography")
    print("\nQuestion ajoutée avec succès !")

    print(f"\nQuestion : {new_question}")


if __name__ == "__main__":
    main()