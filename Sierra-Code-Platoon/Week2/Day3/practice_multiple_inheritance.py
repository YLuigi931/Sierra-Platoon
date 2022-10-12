import math

class Person:
    def __init__(self, name, job):
        self.name = name
        self.job = job
    def work(self):
        print(f"{self.name} is working hard as a {self.job}.")
    
class Computer:
    def __init__(self, number_of_cores):
        self.number_of_cores = number_of_cores

    def compute(self):
        print(round(math.pi, self.number_of_cores))
        
class Cyborg(Person, Computer):
    def __init__(self, name, job, number_of_cores):
        # Person.__init__(self, name, job)
        # Computer.__init__(self, number_of_cores)
        # or
        super().__init__(name, job)
        super(Person, self).__init__(number_of_cores)



robot = Cyborg('Charlie', 'Coder', '8')