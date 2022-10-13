from classes.person import Person
import csv

#staff.py
class Staff(Person):
    
    
    def __init__(self, name, age, role, employee_id, password):
        super().__init__(name, age, role, employee_id, password)
        self.employee_id = employee_id
    
    # def __init__(self, name, age, role, employee_id ,password, ):
    #     super().__init__(self, name, age, role, password)
    #     self.employeed_id = employee_id
        
    @staticmethod
    def all_staff():
            bag = []
            try:
                with open('./data/staff.csv',newline='') as csv_file:
                    lines = csv.DictReader(csv_file, delimiter=',', skipinitialspace=True)
                    
                    for row in lines:
                        bag.append(Staff(row['name'],row['age'],row['role'],row['employee_id'],row['password']))
                return bag
            except Exception as e:
                print('==== Something Failed Here (ALL STAFF method)====')
                print(e)
            
            
# student_info = {'name' : 'Diana', 'password' : 'password', 'school_id' : 12345, 'age' : 17, 'role' : 'Student'}
# Staff(**student_info)
# kay = Staff('Kay','25','Teacher','Kaykay123','pass1234')