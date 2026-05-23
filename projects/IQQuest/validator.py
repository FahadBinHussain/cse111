import re
import phonenumbers
from user_model import User

class Validator:
    @staticmethod
    def validate_name(name):
        regex = re.compile(r"^[a-zA-ZàáâäãåąčćęèéêëėįìíîïłńòóôöõøùúûüųūÿýżźñçčšžÀÁÂÄÃÅĄĆČĖĘÈÉÊËÌÍÎÏĮŁŃÒÓÔÖÕØÙÚÛÜŲŪŸÝŻŹÑßÇŒÆČŠŽ∂ð ,.'-]+$")
        if not re.fullmatch(regex, name):
            raise ValueError("Invalid name. Please enter a valid name.")
        return name
    
    @staticmethod
    def validate_user_type(user_type):
        user_type = user_type.lower()
        if user_type not in User.ALLOWED_USER_TYPES:
            allowed_values = ', '.join(User.ALLOWED_USER_TYPES)
            raise ValueError(f"Invalid user_type. Allowed values are {allowed_values}.")

    @staticmethod
    def validate_category(category):
        category = category.lower()
        valid_categories = ['cse', 'book', 'film', 'music', 'games']
        if category not in valid_categories:
            allowed_values = ', '.join(valid_categories)
            raise ValueError(f"Invalid category. Allowed values are {allowed_values}.")

    @staticmethod
    def validate_age(age):
        try:
            age = int(age)
        except ValueError:
            raise ValueError("Invalid age. Age must be a number.")
        if age < 0:
            raise ValueError("Invalid age. Age cannot be negative.")
        if age > 100:
            raise ValueError("Invalid age. Age cannot be more than 100.")
        return age
    
    @staticmethod
    def validate_email(email): 
        regex = re.compile(r"(^[\w][\w_.+-]+){1,}@[\w_.-]+\.[\w]{2,}$")
        if not re.fullmatch(regex, email):
            raise ValueError("Invalid email. Please enter a valid email address.")
        if re.search("@gm(ia|a|i)l.com$", email):
            raise ValueError("Maybe you meant @gmail.com?")
        return email

    @staticmethod
    def validate_address(address):
        if not address:
            raise ValueError("Address cannot be empty")
            
        # Split the address into components
        components = address.split(',')
        
        # Check if the address has at least 2 components (e.g., street and city)
        if len(components) < 2:
            raise ValueError("Invalid address")
            
        # Remove leading/trailing white space from each component
        components = [component.strip() for component in components]
        
        # Check if the first component (the street) and second component (the city) are not empty
        if not components[0] or not components[1]:
            raise ValueError("Invalid address")

        return address
    
    @staticmethod
    def validate_phone_number(phone_number):
        if not phone_number:
            raise ValueError("Phone number cannot be empty")
            
        try:
            parsed_number = phonenumbers.parse(phone_number)
        except phonenumbers.phonenumberutil.NumberParseException:
            raise ValueError("Invalid phone number")
        
        if not phonenumbers.is_valid_number(parsed_number):
            raise ValueError("Invalid phone number")
        
        return phone_number
    
    @staticmethod
    def validate_question_type(question_type):
        question_type = question_type.lower()
        valid_types = ['multiple', 'boolean']
        if question_type not in valid_types:
            allowed_values = ', '.join(valid_types)
            raise ValueError(f"Invalid question type. Allowed values are {allowed_values}.")
