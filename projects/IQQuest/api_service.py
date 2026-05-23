import requests
from requests.adapters import HTTPAdapter
from requests.exceptions import RequestException
from urllib3.util.retry import Retry

class ApiService:
    def __init__(self):
        self.session = self.create_session_with_retry()
        self.token = self.fetch_token()

    @staticmethod
    def create_session_with_retry(retries=3, backoff_factor=0.3, status_forcelist=(500, 502, 504)):
        session = requests.Session()
        retry = Retry(
            total=retries,
            backoff_factor=backoff_factor,
            status_forcelist=status_forcelist
        )
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        return session

    def fetch_token(self):
        try:
            response = self.session.get('https://opentdb.com/api_token.php?command=request', timeout=5)
        except RequestException as err:
            print ("Something went wrong:",err)
            return None
        return response.json()["token"]

    def fetch_trivia_questions(self, category, question_type):
        category_ids = {
            'cse': '18',
            'book': '10',
            'film': '11',
            'music': '12',
            'games': '15'
        }
        category_id = category_ids.get(category.lower())
        if not category_id:
            raise ValueError(f"Invalid category: {category}")

        api_url = f'https://opentdb.com/api.php?amount=10&category={category_id}&type={question_type}&token={self.token}'

        response = self.session.get(api_url)

        response.raise_for_status()  # Raise an exception if request fails

        response_code = response.json()["response_code"]
        if response_code == 0:  # Success
            question_data = response.json()["results"]
            return question_data
        elif response_code == 3:  # Token Not Found
            self.token = self.fetch_token()  # Fetch a new token
            return self.fetch_trivia_questions(category)  # Retry fetching trivia questions
        elif response_code == 4:  # Token Empty
            response = self.session.get(f'https://opentdb.com/api_token.php?command=reset&token={self.token}')  # Reset the token using session
            response.raise_for_status()  # Raise an exception if request fails
            return self.fetch_trivia_questions(category)  # Retry fetching trivia questions
        else:  # Other errors
            raise Exception(f'Failed to fetch trivia questions. Response code: {response_code}')

    @staticmethod
    def fetch_categories(self):
        response = self.session.get('https://opentdb.com/api_category.php')  # Use session instead of requests
        response.raise_for_status()  # Raise an exception if request fails
        return response.json()["trivia_categories"]
