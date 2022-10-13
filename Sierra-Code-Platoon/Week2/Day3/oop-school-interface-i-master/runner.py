from classes.school import School
from classes.student import Student
from classes.staff import Staff



school = School('Ridgemont High') 

student_info = {'name' : 'Diana', 'password' : 'password', 'school_id' : 12345, 'age' : 17, 'role' : 'Student'}
staff_info = {'name' : 'Steve', 'password' : 'password', 'employee_id' : 12345, 'age' : 17, 'role' : 'Teacher'}


steve = Staff('Steve','password',12345,28,'Teacher')
bag_of_staff = steve.all_staff()
print(bag_of_staff)

# diane = Student(**student_info)
bag_students = Student.all_students()
print(bag_students)


print(school.name)
