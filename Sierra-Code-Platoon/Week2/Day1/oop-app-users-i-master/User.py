# your User class goes here

class User:
    
    def __init__(self, name, email, driver_license, username, password):
        try:
            self.name = name
            self.email = email
            self.diver_license = driver_license
            self.__username = username
            self.__password = password
        except:
            print("An exception occurred")
    
    def set_user(self, user):
        self.__username = user
    
    def get_user(self):
        return self.__username
    
    
    def set_pass(self, password):
        self.__password = password
    
    def get_pass(self):
        return self.__password
    
    def __str__(self):
        return f'\nName: {self.name} \nEmail: {self.email} \n'
    
    
print('\nTest #1')    
test1 = User('Billy', 'billy123@mail.com', 'A123456789', 'billyKing12', '123456')
print(test1)
print(f"Old password: {test1.get_pass()}\n")
print('Changing password... \n')
test1.set_pass('abcdefg')
print(f'New password: {test1.get_pass()}\n')
