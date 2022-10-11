
class Animal:
    
    def __init__(self, name, breed, color, sound):
        self.name = name
        self.__breed = breed
        self.color = color
        self.sound = sound
        
    
    def speak(self):
        print(f'>> {self.sound}')
    
    def fetch(self, item):
        print(f'>> {self.name} is fetching {item}')
    
    def __str__(self):
        return f'name: {self.name}'
        
    def __add__(self, other):
        return f'{self.name}, {other.name}'
        
    def breed_set(self, breed):
        self.breed = breed
        
    def breed_get(self):
        return self.breed 
        
bibo = Animal('bibo', 'wolf', 'grey', 'woof')
bibo.speak()
print(bibo)

fifi = Animal('fifi', 'Bird', 'Red', 'tweet tweet')
fifi.speak()
        
    