class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        return len(self.question_list) > self.question_number

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {question.text} True/False? ").lower()
        self.check_answer(user_answer, question.answer.lower())

    def check_answer(self, user_answer, answer):
        if user_answer == answer:
            print("You are correct!")
            self.score += 1
        else:
            print("You wrong!")
        print(f"The answer is {answer}! Your score is: {self.score}/{self.question_number} \n")

    def final_score(self):
        print(f"You've completes the quiz, your final score is: {self.score}/{self.question_number}")
