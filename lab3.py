
# Program Name: Lab_3.py 
# Course: IT1113/Section W04
# Student Name: Jamaal Hinton
# KSU Email Address: jhinton9@students.kennesaw.edu
# Assignment Lab Number: 3
# Due Date: 09/29/2024
# Purpose: This program can calculate the price of college tuition for a future date.

rate = .0375
semester_cost = 6750

keep_looping = True
flag = input("Press any key if you would like to calculate future tution rates. Enter Q/q to quit: ")
if flag == "Q" or flag == "q":
    keep_looping = False
while keep_looping:
    n = int(input("How many years in the future would you like to calculate?: "))
    rate = .0375
    semester_cost = 6750

    for i in range(n): 

        cost_increase = rate * semester_cost
        semester_cost = cost_increase + semester_cost
        print("Semester cost for "+ str(2024 + i+1) + " will be: " + str(semester_cost))
        print("Cost increase from last year is: " + str(cost_increase))
        print()
    
    flag = input("Press any key if you would like to calculate future tution rates. Enter Q/q to quit: ")
    if flag == "Q" or flag == "q":
        keep_looping = False