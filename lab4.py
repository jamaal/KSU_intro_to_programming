# Program Name: Lab_4.py 
# Course: IT1113/Section W04
# Student Name: Jamaal Hinton
# KSU Email Address: jhinton9@students.kennesaw.edu
# Assignment Lab Number: 4
# Due Date: 10/13/2024
# Purpose: This program prompts the user enter a student's grade or print the list
#of students who's grades are already entered. It will continue to prompt the user
#for input until the user enters anything other than a 1 or 2

#function to calculate the average of the student's grades
def calc_average(grades):
    return int(sum(grades)/len(grades))

# function to calculate the letter equivalent of a grade
def determine_grade(grade):
    if 0 <= grade < 60:
        return 'F'
    elif 60 <= grade <= 69:
        return 'D'
    elif 70 <= grade <= 79:
        return 'C'
    elif 80 <= grade <= 89:
        return 'B'
    elif 90 <= grade:
        return 'A'
    
#prints out menu for the user
def print_menu():
    print("Hello, this is a program to record student grades")
    print("Enter 1 to add student grades")
    print("enter 2 to print current grades")
    print("Enter any other character to quit")
    option = input("Enter selection: ")
    print()
    return option

#create variables
all_students = []
option = print_menu()
flag = option == '1' or option == '2'

#loop while flag is a 1 or a 2
while flag:
    #print students entered so far
    if option =='2':
        print("List of current grades recorded")
        for student in all_students:
            print(student)
        print()

    #option to input another student
    elif option == '1':
        student_name = input("Enter student name: ")
        temp_grade_list = []
        grade_num = 1
        is_num_flag = True
        #loop ot enter in 8 grades for a student
        while grade_num <= 8:
            grade_str = input("enter in grade {num}: ".format(num=grade_num))
            try:
                grade = int(grade_str)
                temp_grade_list.append(int(grade))
                
                letter_grade = determine_grade(grade)
                print("Letter grade for {g} is {lg}".format(g=grade, lg=letter_grade))
                print("grade avgerage is {avg}".format(avg=calc_average(temp_grade_list)))
                print()
                grade_num = grade_num + 1
            except:
                print("had issue adding grade {g}. Please re-enter grade".format(g=grade_str))
                print()
        
        #calculate final average for student and save in student list
        final_avg = calc_average(temp_grade_list)
        final_letter_grade = determine_grade(final_avg)
        student = "Name: {name:15} Grade: {lg}".format(name=student_name, lg=final_letter_grade)
        all_students.append(student)

    #prints menu to prompt user for input again. 
    option = print_menu()
    flag = option == '1' or option == '2'






