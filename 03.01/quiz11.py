import logging
import random

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Question:
    """
    Base class for quiz questions.
    """
    def __init__(self, question_text, answer_choices, correct_answer):
        self.question_text = question_text
        self.answer_choices = answer_choices
        self.correct_answer = correct_answer

    def display_question(self):
        print(self.question_text)
        for i, choice in enumerate(self.answer_choices):
            print(f"{i+1}. {choice}")
        
    def get_user_answer(self):
        while True:
            try:
                user_choice = int(input("Enter your choice: "))
                if user_choice not in range(1, len(self.answer_choices)+1):
                    raise ValueError("Invalid choice. Please enter a valid choice.")
                break
            except ValueError as e:
                logging.error(e)
        return user_choice

    def check_answer(self, user_answer):
        return user_answer == self.correct_answer

class TrueFalseQuestion(Question):
    """
    A child class for quiz questions with true/false answer choices.
    """
    def __init__(self, question_text, correct_answer):
        super().__init__(question_text, ["True", "False"], correct_answer)

class MultipleChoiceQuestion(Question):
    """
    A child class for quiz questions with multiple choice answer choices.
    """
    def __init__(self, question_text, answer_choices, correct_answer):
        super().__init__(question_text, answer_choices, correct_answer)

class Quiz:
    """
    Class for a quiz that contains a list of questions.
    """
    def __init__(self, name, questions):
        self.name = name
        self.questions = questions

    def run_quiz(self):
        # Initialize variables to track the number of correct and incorrect answers
        num_correct = 0
        num_incorrect = 0

        # Shuffle the list of questions to randomize the order
        random.shuffle(self.questions)

        # Display each question and get the user's answer
        for question in self.questions:
            question.display_question()
            user_answer = question.get_user_answer()

            # Check the user's answer and update the number of correct/incorrect answers
            if question.check_answer(user_answer):
                print("Correct!")
                num_correct += 1
            else:
                print("Incorrect.")
                num_incorrect += 1

        # Display the final score
        print(f"\nQuiz complete. You answered {num_correct} out of {len(self.questions)} questions correctly.")

if __name__ == "__main__":
    # Create a quiz with a mix of true/false and multiple choice questions
    questions = [
        TrueFalseQuestion("The capital of France is Paris.", 1),
        MultipleChoiceQuestion("What is the largest planet in our solar system?", ["Venus", "Jupiter", "Saturn", "Mars"], 2),
        MultipleChoiceQuestion("Which of the following is a mammal?", ["Shark", "Octopus", "Gorilla", "Lizard"], 3),
        TrueFalseQuestion("The Great Wall of China is visible from space.", 2),
        MultipleChoiceQuestion("What is the tallest mammal?", ["Giraffe", "Elephant", "Hippopotamus", "Rhinoceros"], 1)
    ]
    my_quiz = Quiz("General Knowledge Quiz", questions)

    # Run the quiz
    logging.info("Starting quiz...")
    my_quiz.run_quiz()
    logging.info("Quiz completed.") 
