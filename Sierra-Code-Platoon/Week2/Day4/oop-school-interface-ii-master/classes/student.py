import csv
import os.path
from classes.person import Person

class Student(Person):

    def __init__(self, name, age, password, role, school_id):
        super().__init__(name, age, password, role)
        self.school_id = school_id

    def get_school_id(self):
        return self.school_id
    
    @classmethod
    def objects(cls):
        students = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/students.csv")
        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            
            for row in reader:
                students.append(Student(**dict(row)))
        return students
    
    '''
    LISA
    ---------------
    age: 25
    id: 13345
    '''

    def __str__(self):
        output = f"\n{self.name}\n"\
                "---------------\n"\
                f"age: {self.age}\n"\
                f"id: {self.school_id}\n"\
                       
        return output