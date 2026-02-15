class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def is_valid_password(self):
        if len(self.password) < 8:
            return False
        
        has_digit = False
        has_upper = False
        
        for char in self.password:
            if char.isdigit():
                has_digit = True
            if char.isupper():
                has_upper = True
        
        return has_digit and has_upper


user1 = User("rico", "Password1")
print(user1.is_valid_password())   

user2 = User("rico", "pass")
print(user2.is_valid_password())   
