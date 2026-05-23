import random
from question_model import Question
from quiz_brain import QuizBrain
import datetime
import uuid

class Quiz:
    def __init__(self, user, question_data):
        self.user = user
        self.quiz_brain = QuizBrain(question_data, max_questions=10)

    def run(self):
        question_bank = self.quiz_brain.question_list
        random.shuffle(question_bank)

        while self.quiz_brain.still_has_questions():
            self.quiz_brain.next_question()

        self.user.update_total_score(self.quiz_brain.score)

        print("You've completed the quiz")

        quiz_result = {
            'quiz_id': str(uuid.uuid4()),
            'date_and_time': datetime.datetime.now().isoformat(),
            'total_questions': self.quiz_brain.question_number,
            'correct_answers': self.quiz_brain.score,
            'incorrect_answers': self.quiz_brain.question_number - self.quiz_brain.score,
            'unanswered_questions': self.quiz_brain.skipped_questions,
            'quiz_category': self.user.category
        }

        print(f"Your final score was: {quiz_result['correct_answers']}/{quiz_result['total_questions']}")
        
        return quiz_result
