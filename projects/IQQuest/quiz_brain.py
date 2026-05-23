class QuizBrain:
    total_quizzes = 0
    total_score = 0
    def __init__(self, q_list, max_questions):
        self.question_number = 0
        self.__score = 0
        self.question_list = q_list
        self.max_questions = max_questions
        self.skipped_questions = 0
        self.incorrect_answers = 0
        QuizBrain.total_quizzes += 1

    @property
    def score(self):
        return self.__score
    
    @score.setter
    def score(self, value):
        self.__score = value

    def still_has_questions(self):
        return self.question_number < len(self.question_list) and self.question_number < self.max_questions

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer_choices = current_question.choices
        print(f"Q.{self.question_number}: {current_question.text}")
        for i, choice in enumerate(answer_choices):
            print(f"{i+1}. {choice}")
        while True:
            user_answer = input("Enter your answer (1-4) or leave blank to skip: ")
            if self.check_answer(user_answer, current_question.answer):
                break

    def check_answer(self, user_answer, correct_answer):
        if user_answer == "":
            print("You chose to skip the question.")
            print(f"The correct answer was: {correct_answer}.")
            print(f"Your current score is: {self.score}/{self.question_number}")
            print("\n")
            self.skipped_questions += 1
            return True
        else:
            try:
                user_answer = int(user_answer) - 1  
                if user_answer == self.question_list[self.question_number-1].choices.index(correct_answer):
                    self.score += 1
                    print("You got it right!")
                else:
                    print("That's wrong.")
                    self.incorrect_answers += 1
                print(f"The correct answer was: {correct_answer}.")
                print(f"Your current score is: {self.score}/{self.question_number}")
                print("\n")
                return True
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 4.")
                return False

    def get_total_quizzes(cls):
        return cls.total_quizzes
    
    @classmethod
    def get_average_score(cls):
        return cls.total_score / cls.total_quizzes if cls.total_quizzes else 0
