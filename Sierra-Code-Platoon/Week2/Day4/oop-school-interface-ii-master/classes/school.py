from classes.staff import Staff
from classes.student import Student

class School:
    def __init__(self, name):
        self.name = name
        self.staff = Staff.objects()
        self.students = Student.objects()

    def list_students(self):
        counter = 0
        for item in self.students:
            counter += 1
            print(f'{counter}. {item.get_name()} {item.get_school_id()}')
        
    def find_student_by_id(self,student_id):
        for item in self.students:
            if item.get_school_id() == student_id:
                
                return item
        
# test1 = School('Prussing')
# print(test1.list_students())