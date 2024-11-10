# Program Name: Lab_5.py 
# Course: IT1113/Section W04
# Student Name: Jamaal Hinton
# KSU Email Address: jhinton9@students.kennesaw.edu
# Assignment Lab Number: 5
# Due Date: 11/03/2024
# Purpose: This program allows the user to keep track of golfer information. 
# After data is entered, the user can view the records created during the session,
# and they can also save the data to a file and read whats been written to the file.

import pickle

#function to print menu
def print_menu():
    print("Enter [1] to enter golfer information")
    print("Enter [2] to print current golfer information")
    print("Enter [3] to write golfer information to file")
    print("Enter [4] to print golfer information from file")
    print("ENter [5] to read from previous golfer record file")
    print("Enter [Q/q] to quit")
    print()
    option = input("Enter selection: ")
    print()
    return option.lower()

#function to calculate golf score
def calculate_score(score):
    if score == 80:
        return "Made par"
    if score < 80:
        return " Was Under Par"
    if score > 80:
        return " Was Over Par"
    
#function to read gold data from file
def read_from_file(file):
    f = open(file,'+rb')
    data = pickle.load(f)
    for i in data:
        print(i)
    print()
    f.close()
    return data

#function to write golf data out to a file
def write_to_file(file,golf_data):
    f = open(file,"wb")
    pickle.dump(golf_data, f)
    f.close()
    print("Golfers saved to file: {f}\n".format(f=file))
    return
    

#initailze variables
golf_file_name = "golf.pkl"
golf_file = open(golf_file_name, "wb")
golfers_list= []

#First menu prompt for the user
print("Hello, this is a program to record golf information")
option = print_menu()

#creating header for the golfer list file
heading = "{0:15} {1:15} {2:15} {3:15}".format("First_Name","Last_Name","Handicap","Score")
golfers_list.append(heading)

#loop to continue to prompt user
while True:
    #option to enter in golfer infomation
    if option == '1':
        first_name = input("Enter golfer's first name: ")
        last_name = input("Enter golfer's last name: ")
        handicap = input("Enter golfer's handicap: ")
        score = input("Enter golfer's score: ")
        #throw error if score can't be converted into integer
        try:
            par = calculate_score(int(score))
            print("{0} {1} was {2}".format(first_name,last_name,par))
            print()
            golfer = "{0:15} {1:15} {2:15} {3:15}".format(first_name,last_name,handicap,score)
            golfers_list.append(golfer)
            option = print_menu()
        except:
            print("There was an issue reading the score {0}".format(score))
            print("please re-enter the golfer's information")
            print()

    elif option == '2': #print golfers who are currently in list
        for g in golfers_list:
            print(g)
        print()
        option = print_menu()

    elif option == '3': #Write golfers to golf.txt file
        write_to_file(golf_file_name,golfers_list)
        option = print_menu()

    elif option == '4': #Read golfers that are in golf.txt file
        read_from_file(golf_file_name)
        option = print_menu()
    #read in information from another golf file
    elif option == '5':
        user_file = input("Enter in file name: ")
        #Throws an error if the file cannot be found
        try:
            read_from_file(user_file)
        except:
            print("There was an error finding file {file}, or could not find {file}".format(file=user_file))
            print()
        option = print_menu()

    #option to quit program
    elif option == 'q':
        break
    #re-prompt user if invalid input is received. 
    else:
        print("Sorry, an invalid input was recieved. Please try again.")
        option = print_menu()

#close golf file 
golf_file.close()

    

