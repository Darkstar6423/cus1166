import mymodule

s1 = mymodule.student("george", 90)
s1.print_student_info()
s2= mymodule.student("connor", 85)
s2.print_student_info()
s3= mymodule.student("nick", 99)
s3.print_student_info()
s4= mymodule.student("jeorge", 99)
s4.print_student_info()
s5= mymodule.student("adam", 99)
s5.print_student_info()
s6= mymodule.student("nick", 99)
s6.print_student_info()
s7= mymodule.student("nick", 60)
s7.print_student_info()
s8= mymodule.student("nick", 80)
s8.print_student_info()
s9= mymodule.student("nick", 90)
s9.print_student_info()
s10= mymodule.student("nick", 75)
s10.print_student_info()


student_list = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10]
print("the average is: %s"%mymodule.average_grade(student_list))
