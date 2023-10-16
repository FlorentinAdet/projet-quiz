import json
import random
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from interface import afficher_interface

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

def lancerPartie():
    app = afficher_interface()
    app.fenetre.mainloop()

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

def create_question_window():
    def submit_question():
        # Récupérez les valeurs des éléments du formulaire
        theme = theme_var.get()
        question = question_text.get("1.0",
                                     "end-1c")  # Obtenez le texte de la zone de texte (1.0 signifie ligne 1, caractère 0)
        num_options = int(num_options_var.get())
        answers = [answer_textboxes[i].get() for i in range(4)]
        correct_answer_index = correct_answer_var.get()

        # Créez un dictionnaire avec les données de la question
        question_data = {
            "question": question,
            "difficulty": num_options,
            "theme": theme,
            "options": answers,
            "correct_answer": correct_answer_index
        }

        new_question = Question(question, num_options, answers, theme, correct_answer_index)
        add_question_to_json(new_question, theme)

        messagebox.showinfo("Question ajoutée", "La question a été ajoutée avec succès!")

        # Réinitialisez le formulaire
        theme_var.set("")
        question_text.delete("1.0", tk.END)
        num_options_var.set("")
        for i in range(4):
            answer_textboxes[i].delete(0, tk.END)
        correct_answer_var.set(0)

    question_window = tk.Toplevel(main_window)
    question_window.title("Créer une question")
    question_window.geometry("720x480")

    # Liste déroulante pour le thème
    theme_label = tk.Label(question_window, text="Thème:")
    theme_label.pack()
    themes = ["Geography", "Science", "History", "Entertainment"]
    theme_var = tk.StringVar()
    theme_dropdown = ttk.Combobox(question_window, textvariable=theme_var, values=themes)
    theme_dropdown.pack()

    # Zone de texte pour la question
    question_label = tk.Label(question_window, text="Question :")
    question_label.pack()
    question_text = tk.Text(question_window, height=5, width=50)
    question_text.pack()

    # Liste déroulante pour la difficulté
    num_options_label = tk.Label(question_window, text="Difficulté :")
    num_options_label.pack()
    num_options = [1, 2, 3]
    num_options_var = tk.StringVar()
    num_options_dropdown = ttk.Combobox(question_window, textvariable=num_options_var, values=num_options)
    num_options_dropdown.pack()

    # Zones de texte pour les réponses
    answer_labels = []
    answer_textboxes = []
    for i in range(4):
        answer_label = tk.Label(question_window, text=f"Réponse {i + 1}:")
        answer_label.pack()
        answer_labels.append(answer_label)
        answer_text = tk.Entry(question_window)
        answer_text.pack()
        answer_textboxes.append(answer_text)

    # Boutons radio pour sélectionner la bonne réponse
    correct_answer_var = tk.IntVar()
    correct_answer_var.set(0)  # Par défaut, la première réponse est sélectionnée
    correct_answer_labels = []
    for i in range(4):
        correct_answer = tk.Radiobutton(question_window, text=f"Réponse {i + 1}", variable=correct_answer_var, value=i)
        correct_answer.pack()
        correct_answer_labels.append(correct_answer)

    # Bouton pour valider la question
    submit_button = tk.Button(question_window, text="Valider", command=submit_question)
    submit_button.pack()

main_window = tk.Tk()
main_window.title("Quiz Game")
main_window.geometry("720x480")

launch_button = tk.Button(main_window, text="Lancer une partie")
launch_button.config(command=lambda:lancerPartie())
launch_button.pack()

create_question_button = tk.Button(main_window, text="Créer une question", command=create_question_window)
create_question_button.pack()

main_window.mainloop()

