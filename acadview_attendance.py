print "Acadview's Attendance Management System"
teacher_name = raw_input("Enter Teacher's Name : ")
flag = True
students_name_list = []
while flag:
    print "Select : \n1. Mark attendance \n2. Quit"
    teacher_choice = raw_input("Enter your choice : ")
    if teacher_choice == "1":
        students_count = int(raw_input("Enter the number of students : "))
        while len(students_name_list) < students_count:
            student_name = raw_input("Enter student name : ")
            if student_name in students_name_list:
                check_status = raw_input('The name already exist. Are you sure? y/n : ')
                if check_status == "y":
                    students_name_list.append(student_name)
                else:
                    continue
            else:
                students_name_list.append(student_name)
        for name in students_name_list:
            print name
    elif teacher_choice == "2":
        flag = False
        print "Bye!"
