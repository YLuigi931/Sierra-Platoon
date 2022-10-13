# your improved User class goes here

from getpass import getuser


class User:
    
    user_lst = []
    message_lst = []
    
    def __init__(self, name, email, driver_license, username, password):
        try:
            self.name = name
            self.email = email
            self.diver_license = driver_license
            self._username = username
            self._password = password
            User.user_lst.append(self)
            User.message()
        except:
            print("An exception occurred")
    
    @property
    def user(self):
        return self._username
    
    @user.setter
    def user(self, user):
        self._username = user
    
    @property
    def gpass(self):
        return self._password
    
    @gpass.setter
    def gpass(self, password):
        self._password = password
    
    def __str__(self):
        return f'\nName: {self.name} \nEmail: {self.email} \n'
    
    def add_user(self):
        pass
    
    def get_msg_lst(self):
        
        for item in User.message_lst:
            print(f"{item}")
            
        return
        
    
    def message(self):
        
        ask = input("Tell me your thoughts: \n")
        mail = f"{self._username}: {ask}"
        User.message_lst.append(mail)
    
    
print('\nTest #1')
    
test1 = User('Billy', 'billy123@mail.com', 'A123456789', 'billyKing12', '123456')
test2 = User('Obiwon','DarthVaderCanSuckIt@SW.com','A234564321', 'OB1_CanOB','111111')

print(test1)

print(f"Old password: {test1.gpass}\n")
print('Changing password... \n')
# test1.gpass('abcdefg')
print(f'New password: {test1.gpass()}\n')
test1.message()
test1.get_msg_lst()
test1.message()
test1.get_msg_lst()
test2.message()
test2.get_msg_lst()
print("( ͡❛ ͜ʖ ͡❛)")
