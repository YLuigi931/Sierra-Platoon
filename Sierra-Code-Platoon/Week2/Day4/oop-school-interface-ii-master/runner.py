from classes.school import School

school = School('Ridgemont High')


# print(school.staff)
# print(school.students)
query = "\nWhat would you like to do?\n"\
        "Options:\n"\
        "   1. List All Students\n"\
        "   2. View Individual Student\n"\
        "   <student_id>\n"\
        "   3. Add a Student\n"\
        "   4. Remove a Student <student_id>\n"\
        "   5. Quit\n"\

mode = input(query)

# print(mode)
while(mode != 5):
    
    if mode == '1':
        school.list_students()
    elif mode == '2':
        student_id = input('Enter student id:')
        student = school.find_student_by_id(student_id)
        print(str(student))
    elif mode == '5':
        
        break
    else:
        pass
    mode = input(query)



