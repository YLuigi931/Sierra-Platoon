
from classes.person import Person
import csv

# student.py
class Student(Person):
    
    def __init__(self, **kwargs):
        super().__init__(kwargs['name'], kwargs['age'], kwargs['role'], kwargs['school_id'], kwargs['password'])
        self.school_id = kwargs['school_id']
        
    @staticmethod
    def all_students():
        bag = []
        try:
            with open('./data/students.csv',newline='') as csv_file:
                lines = csv.DictReader(csv_file, delimiter=',', skipinitialspace=True)
                
                for row in lines:
                    
                    temp1 = Student(**row)
                    bag.append(temp1)
                # print(Student.bag)
                return bag
            
        except Exception as e:
            print('==== Something Failed Here (ALL STUDENT method)====')
            print(e)
  

        
    