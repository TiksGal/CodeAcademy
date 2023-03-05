import random

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

class MultipleChoiceQuestion(Question):
    def __init__(self, prompt, answer, choices):
        super().__init__(prompt, answer)
        self.choices = choices

    def get_choices(self):
        return self.choices

class TrueFalseQuestion(Question):
    def __init__(self, prompt, answer):
        super().__init__(prompt, answer)

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def take_quiz(self):
        random.shuffle(self.questions)
        for question in self.questions:
            print(question.prompt)
            user_answer = input().lower()
            if user_answer == str(question.answer).lower():
                print("Correct!")
                self.score += 1
            else:
                print("Incorrect.")
            print()
        print("Quiz complete. You scored {}/{}.".format(self.score, len(self.questions)))

# example questions
q1 = Question("What is the capital of France?", "Paris")
q2 = MultipleChoiceQuestion("What is the largest planet in the solar system?",
                            "Jupiter",
                            ["Mars", "Jupiter", "Venus", "Neptune"])
q3 = TrueFalseQuestion("The sun is a star. (True/False)", True)
q4 = TrueFalseQuestion("The earth is flat. (True/False)", False)
q5 = MultipleChoiceQuestion("What is the smallest country in the world?",
                            "Vatican City",
                            ["Monaco", "San Marino", "Andorra", "Vatican City"])

# create a quiz and add the questions
my_quiz = Quiz([q1, q2, q3, q4, q5])

# take the quiz
my_quiz.take_quiz()
