# IQQuest

<img src="https://wakapi-qt1b.onrender.com/api/badge/fahad/interval:any/project:IQQuest" 
     alt="Wakapi Time Tracking" 
     title="Spent more than that amount of time spent on this project">

[![Clone this repo](https://img.shields.io/badge/Clone-this_repo-brightgreen.svg)](https://github.com/FahadBinHussain/IQQuest)

This Python application interacts with users to get their information, fetch trivia questions from an API based on their preferences, run a quiz for them, and store their information including quiz results in a YAML file.

# Dependencies

* requests
* PyYAML
* phonenumbers

# How to Use

## Critical prerequisites to install

* run ```pip3 install -r requirements.txt```

You're all set.

## Run the script on the desktop

1. Open a terminal or command prompt

2. Navigate to the directory where you cloned the repository

3. Run `python3 main.py` to start the Quest!

## Usage
After running the program, follow the prompts in the terminal to input your information and answer trivia questions.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)

## How the Quiz Game Works

The quiz game is an interactive Python application that allows users to participate in trivia quizzes. The quizzes are generated based on the user's preferences and fetched from the Open Trivia Database API. The application validates user inputs, keeps track of user scores, and stores user information and quiz results in a YAML file.

### User Interaction

When a user starts the game, they are asked to enter their personal information and preferences for the trivia quiz. If the user's information has been saved from a previous game, they can continue with the saved information. Otherwise, new users are asked to input their name, age, email, address, phone number, user type, and preferred category and type of questions for the quiz. The `InputService` class handles user inputs and the `Validator` class validates these inputs.

### Validation Process

The `Validator` class validates user inputs. It checks if the user's name, age, email, address, phone number, user type, category, and question type are in the correct format and within the allowed values. 

### Quiz Generation

The application fetches trivia questions from the Open Trivia Database API based on the user's preferred category and question type. These questions are represented by the `Question` class, which includes the question text, answer choices, and the correct answer. 

### Running the Quiz

Once all user inputs are validated and the questions are fetched, a `QuizBrain` object is created. The `QuizBrain` class handles the logic of the quiz game, such as displaying the next question, checking the user's answer, and updating the user's score. The quiz is run until all questions are answered or skipped.

### User Scoring

After the quiz is finished, the user's total score and the number of quizzes they have taken are updated. The `User` class, which represents a user of the quiz game, keeps track of these statistics.

### Quiz Results

The results of the quiz are returned as a dictionary, which includes the date and time the quiz was taken, the total number of questions, the number of correct and incorrect answers, the number of unanswered questions, and the category of the quiz.

### Data Storage

The user's information and quiz results are then saved back to a YAML file for future reference. 

### Error Handling

The application uses a session with a retry mechanism for making requests to the API, which means it will retry failed requests a certain number of times. This is useful in cases where the API might be temporarily unavailable or responding with error status codes.

The quiz game provides a fun and interactive way for users to test their trivia knowledge. It offers flexibility in terms of the type and category of questions, and it ensures a smooth user experience by validating user inputs and handling errors effectively.
