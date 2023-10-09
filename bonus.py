import json
class Question:
    def __init__(self, question, options, correct_option, level, category):
        self.question = question
        self.options = options
        self.correct_option = correct_option
        self.level = level
        self.category = category

    def __str__(self):
        return f"Question: {self.question}\nOptions: {', '.join(self.options)}\nCorrect Option: {self.correct_option}\nLevel: {self.level}\nCategory: {self.category}"


def create_question():
    question = input("Entrez la question : ")
    options = [input(f"Entrez la proposition {i + 1} : ") for i in range(4)]
    correct_option = int(input("Entrez le numéro de la proposition correcte (1-4) : "))
    level = input("Entrez le niveau (facile, normal, difficile) : ")
    category = input("Entrez la catégorie de la question : ")

    return Question(question, options, correct_option, level, category)


def main():
    questions = []
    while True:
        print("\nCréation d'une nouvelle question :")
        new_question = create_question()
        questions.append(new_question)
        print("\nQuestion ajoutée avec succès !")

        another = input("Voulez-vous ajouter une autre question ? (Oui/Non) : ")
        if another.lower() != "oui":
            break

    print("\nQuestions créées :")
    for i, question in enumerate(questions, start=1):
        print(f"\nQuestion {i}:\n{question}")

    # Enregistrement des questions dans un fichier JSON
    with open('questions.json', 'w') as json_file:
        json.dump([vars(q) for q in questions], json_file, indent=4)

if __name__ == "__main__":
    main()