class Question:
    def __init__(self, question: str, correct_answer: str, choices: list, category: str):
        self.question_text = question
        self.correct_answer = correct_answer
        self.choices = choices
        self.category = category
