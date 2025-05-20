import re

class ValidationUtils:
    
    @staticmethod
    def is_valid_email(email: str) -> bool:
        """
        Validates an email address.
        """
        email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        return re.match(email_regex, email) is not None

    @staticmethod
    def is_valid_password(password: str) -> bool:
        """
        Validates a password (min 8 characters, must contain a digit and a letter).
        """
        if len(password) < 8:
            return False
        if not any(char.isdigit() for char in password):
            return False
        if not any(char.isalpha() for char in password):
            return False
        return True

    @staticmethod
    def is_valid_username(username: str) -> bool:
        """
        Validates a username (min 3 characters, only letters, numbers, and underscores).
        """
        username_regex = r"^[a-zA-Z0-9_]{3,}$"
        return re.match(username_regex, username) is not None

    @staticmethod
    def is_positive_integer(value: str) -> bool:
        """
        Validates if the value is a positive integer.
        """
        try:
            return int(value) > 0
        except ValueError:
            return False