import json
import random

def load_questions_from_json(file_path):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    return data

def get_random_question(data):
    # Randomly select a theme
    theme = random.choice(list(data.keys()))
    print(f"Theme: {theme}")
    
    # Randomly select a question from the selected theme
    question_id = random.choice(list(data[theme].keys()))
    question_data = data[theme][question_id]

    # Extract question text and options
    question = question_data['question']
    options = question_data['options']
    correct_answer_index = question_data['correct_answer']
    correct_answer = options[correct_answer_index]

    return theme, question, options, correct_answer

def main():
    theme, question, _, correct_answer = get_random_question(load_questions_from_json('questions.json'))
    print(theme)
    print(question)
    print(correct_answer)

if __name__ == "__main__":
    main()

