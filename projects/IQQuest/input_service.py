from validator import Validator

class InputService:
    @staticmethod
    def get_name(prompt="Enter your name: "):
        while True:
            name = input(prompt)
            try:
                Validator.validate_name(name)
                return name
            except ValueError as e:
                print(e)

    @staticmethod
    def get_age():
        while True:
            age = input("Enter your age: (eg. 21) ")
            try:
                Validator.validate_age(age)
                return age
            except ValueError as e:
                print(e)

    @staticmethod
    def get_email():
        while True:
            email = input("Enter your email: (eg. human@gmail.com) ")
            try:
                Validator.validate_email(email)
                return email
            except ValueError as e:
                print(e)

    @staticmethod
    def get_address():
        while True:
            address = input("Enter your address: (eg. 123, Main St) ")
            try:
                Validator.validate_address(address)
                return address
            except ValueError as e:
                print(e)

    @staticmethod
    def get_phone_number():
        while True:
            phone_number = input("Enter your phone number: (eg. +919876543210) ")
            try:
                Validator.validate_phone_number(phone_number)
                return phone_number
            except ValueError as e:
                print(e)
    
    @staticmethod
    def get_user_type():
        while True:
            user_type = input("Enter your user type: (eg. school, college, university) ")
            try:
                Validator.validate_user_type(user_type)
                return user_type
            except ValueError as e:
                print(e)

    @staticmethod
    def get_category():
        while True:
            category = input("Enter your category: (eg. cse, book, film, music, games) ")
            try:
                Validator.validate_category(category)
                return category
            except ValueError as e:
                print(e)
    
    @staticmethod
    def get_question_type():
        while True:
            question_type = input("Enter your preferred question type (multiple/boolean): ")
            try:
                Validator.validate_question_type(question_type)
                return question_type
            except ValueError as e:
                print(e)
