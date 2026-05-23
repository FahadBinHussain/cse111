class Person:
    def __init__(self, name, age, email, address, phone_number):
        self.name = name
        self.age = age
        self.email = email
        self.address = address
        self.phone_number = phone_number
        
class User(Person):
    ALLOWED_USER_TYPES = ['school', 'college', 'university']
    total_users = 0

    def __init__(self, name, age, email, address, phone_number, user_type, category):
        super().__init__(name, age, email, address, phone_number)
        self.user_type = user_type
        self.category = category
        self.quizzes_taken = 0
        self.total_score = 0
        self.highest_score = 0
        User.total_users += 1

    @classmethod
    def get_total_users(cls):
        return cls.total_users
    
    def update_user_type(self, user_type):
        User.validate_user_type(user_type)
        self.user_type = user_type

    def increment_quizzes_taken(self):
        self.quizzes_taken += 1

    def update_total_score(self, score):
        self.total_score += score

        if score > self.highest_score:
            self.highest_score = score

    def calculate_average_score(self):
        if self.quizzes_taken > 0:
            return self.total_score / self.quizzes_taken
        else:
            return 0
        