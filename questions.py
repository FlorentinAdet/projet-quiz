import json
import random

def load_questions_from_json(file_path): # Loading the json file
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    return data

def get_random_question(data):
    # Randomly select a theme
    theme = random.choice(list(data.keys()))
    
    # Randomly select a question from the selected theme
    question_id = random.choice(list(data[theme].keys()))
    question_data = data[theme][question_id]

    # Extract question text and options
    question = question_data['question']
    options = question_data['options']
    correct_answer_index = question_data['correct_answer']
    correct_answer = options[correct_answer_index]
    difficulty = question_data['difficulty']

    return theme, question, options, correct_answer, difficulty

# def main():
#    theme, question, _, correct_answer, difficulty = get_random_question(load_questions_from_json('questions.json'))
#    print(f"Theme: {theme}")
#    print(f"Question: {question}")
#    print(f"Correct answer: {correct_answer}")
#    print(f"Difficulty: {difficulty}")

# if __name__ == "__main__":
#    main()

