from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


def quiz():
    question_bank = []
    for q in question_data:
        q_text = q["text"]
        q_answer = q["answer"]
        new_q = Question(q_text, q_answer)
        question_bank.append(new_q)

    quiz_brain = QuizBrain(question_bank)
    while quiz_brain.still_has_questions():
        quiz_brain.next_question()
    print("You've completed the quiz!")
    print(
        f"Your final score was: {quiz_brain.score}/{quiz_brain.question_number}.")


quiz()
