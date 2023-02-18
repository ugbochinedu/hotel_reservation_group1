class Customer:
    def __init__(self, first_name, last_name, email):
        self._first_name = first_name
        self._last_name = last_name
        self._email = email

    def set_first_name(self, first_name):
        self._first_name = first_name

    def get_first_name(self):
        return self._first_name

    def set_last_name(self, last_name):
        self._last_name = last_name

    def get_last_name(self):
        return self._last_name

    def set_gmail(self, email):
        self._email = email

    def get_email(self):
        return self._email

    def __str__(self):
        return f"""
        first_name: {self._first_name} 
        last_name: {self._last_name} 
        email: {self._email} 
        """

    def __repr__(self):
        return f"""
                first_name: {self._first_name} 
                last_name: {self._last_name} 
                email: {self._email} 
                """
