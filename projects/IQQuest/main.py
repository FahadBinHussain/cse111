import yaml

from input_service import InputService
from api_service import ApiService
from user_model import User
from quiz_runner import Quiz
from question_model import Question

try:
    # Try to open the existing users.yml file
    with open('users.yml', 'r') as file:
        user_data = yaml.safe_load(file)
except FileNotFoundError:
    # If the file doesn't exist, create an empty user_data dictionary
    user_data = {'users': []}

while True:
    try:
        # Ask the user for their name
        name = InputService.get_name()
        if name.lower() == 'exit':
            break

        # Check if user already exists in the list
        user_exists = False
        for user in user_data['users']:
            if user['name'] == name:
                user_exists = True
                new_user = user
                input("Your information was previously saved in the system. Press any key to continue.")
                break

        if not user_exists:
            # Ask the user for their information
            age = InputService.get_age()
            email = InputService.get_email()
            address = InputService.get_address()
            phone_number = InputService.get_phone_number()
            user_type = InputService.get_user_type()
            question_type = InputService.get_question_type()

            new_user = {
                'name': name,
                'age': age,
                'email': email,
                'address': address,
                'phone_number': phone_number,
                'user_type': user_type,
                'quizzes': []
            }
            user_data['users'].append(new_user)

            # Ask for the category regardless of whether the user is new or existing
            category = InputService.get_category()

        else:
            #access category from the yml file
            new_user = user_data['users'][0]
            age = new_user['age']
            email = new_user['email']
            address = new_user['address']
            phone_number = new_user['phone_number']
            user_type = new_user['user_type']

            # Ask for the category regardless of whether the user is new or existing
            category = InputService.get_category()
            question_type = InputService.get_question_type()

        api_service = ApiService()
        question_data = api_service.fetch_trivia_questions(category, question_type)

        question_data = [Question(q["question"], q["incorrect_answers"] + [q["correct_answer"]], q["correct_answer"]) for q in question_data]
        user = User(name, age, email, address, phone_number, user_type, category)

        quiz = Quiz(user, question_data)
        quiz_result = quiz.run()
        new_user['quizzes'].append(quiz_result)

        # Save the updated user information back to the YAML file
        with open('users.yml', 'w') as file:
            yaml.dump(user_data, file, sort_keys=False)

    except Exception as e:
        print(e)
