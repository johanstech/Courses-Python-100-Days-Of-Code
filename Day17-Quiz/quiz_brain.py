class QuizBrain:
    def __init__(self, questions) -> None:
        self.questions_list = questions
        self.question_number = 0
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def next_question(self):
        question = self.questions_list[self.question_number]
        self.question_number += 1
        answer = input(
            f"Q.{self.question_number}: {question.text}. (true/false)?\n")
        self.check_answer(answer, question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"Your current score is: {self.score}/{self.question_number}.\n")
