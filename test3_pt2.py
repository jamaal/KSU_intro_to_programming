# Program Name: test3_pt2.py 
# Course: IT1113/Section W04
# Student Name: Jamaal Hinton
# KSU Email Address: jhinton9@students.kennesaw.edu
# Assignment: Test 3 pt. 2
# Due Date: 11/24/2024
# Purpose: This Program is used to convert Kilometers into Miles

#create function to convert Km to M
def convert_km_m(k):
    return k * 0.6214

#funtion to print menu that prompts the user
def print_menu():
    print("\n--Enter [1] to convert Kilometers to miles")
    print("--Enter [Q/q] to quit program\n")
    option = input("Enter choice: ").lower()

    return option

#printing program greeting
print("Hello, this is a program to convert Kilometers to miles")
option = print_menu()

#infinte loop to continue to prompt user until 
#user inputs a 'q/Q'
while True:
    if option == '1':
        km = input("Enter in Kilometers: ")
        print()
        #try block to see if the convert_km_m to execute with
        #input user submitted
        try:
            km = float(km)
            miles = convert_km_m(km)
            print("{0} kilometers is {1} miles".format(km, miles))
        except:
            print("Had trouble turning '{0}' to a number. Please try again".format(km))

        option = print_menu()

    #if user inputs a q/Q, the loop quits the program
    elif option == 'q':
        print("Goodbye")
        break
    else:
        print("Input '{0}' not accepted. Please try again".format(option))
        option = print_menu()