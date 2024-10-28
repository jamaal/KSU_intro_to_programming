# Program Name: Lab_5.py 
# Course: IT1113/Section W04
# Student Name: Jamaal Hinton
# KSU Email Address: jhinton9@students.kennesaw.edu
# Assignment Lab Number: 5
# Due Date: 11/03/2024
# Purpose: 

def print_menu():
    print("Hello, this is a program to record golf information")
    print("Enter 1 to enter golfer information")
    print("enter 2 to print golfer information")
    print("Enter any other character to quit")
    option = input("Enter selection: ")
    print()
    return option

def calculate_score(score):
    if score == 80:
        return "Made par"
    if score < 80:
        return " Was Under Par"
    if score > 80:
        return " Was Over Par"
    

#initailze variables
golf_file = open("golf.txt", "w")
golfers_list= []

option = print_menu()
flag = option == '1' or option == '2'

heading = "{0:15} {1:15} {2:15} {3:15}\n".format("First_Name","Last_Name","Handicap","Score")
golfers_list.append(heading)
golf_file.write(heading)

while flag:
    if option == '1':
        first_name = input("Enter golfer's first name: ")
        last_name = input("Enter golfer's last name: ")
        handicap = input("Enter golfer's handicap: ")
        score = input("Enter golfer's score: ")

        try:
            par = calculate_score(int(score))
            print("{0} {1} was {2}".format(first_name,last_name,par))
        except:
            print("There was an issue reading the score {0}".format(score))
            print("please re-enter the golfer's information")

        golfer = "{0:15} {1:15} {2:15} {3:15}".format(first_name,last_name,handicap,score)
        golfers_list.append(golfer)
        golf_file.write(golfer)
        option = print_menu()
        flag = option =='1' or option =='2'

    elif option == '2':
        for g in golfers_list:
            print(g)
        option = print_menu()
        flag = option =='1' or option =='2'

golf_file.close()

    

