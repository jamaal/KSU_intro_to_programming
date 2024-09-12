
# Program Name: Lab_2.py 
# Course: IT1113/Section W04
# Student Name: Jamaal Hinton
# KSU Email Address: jhinton9@students.kennesaw.edu
# Assignment Lab Number: 2
# Due Date: 09/08/2024
# Purpose: This program reads in the names and the number of books sold to customers for the month
# and calculates the number of points the bookstore earned for it's sales. In the end, the program
# prints the customer names and total points earned

#Create variables for program
item_list = []
points_sum = 0
points = 0

#Creating a loop to receive input for every customer
for i in range(10):
    name = input("Please enter your name: ")
    num_of_books = int(input("Please enter the number of book purchased this month: "))

    #Logic for choosing how many points the store gets
    if num_of_books <= 0:
        points = 0
    elif 1 <= num_of_books <= 2:
        points = 3
    elif 3 <= num_of_books <= 4:
        points = 12
    elif 5 <= num_of_books <= 6:
        points = 20
    elif 7 <= num_of_books <= 9:
        points = 30
    elif num_of_books >= 10:
        points = 50
    
    #Printing statement for individual customer
    points_sum = points_sum + points
    item = "Name: {name:15} Points earned: {points}".format(name=name, points=points)
    #Appending customer and book points to the list
    item_list.append(item)
    print(item)

    #Printing running total for the pionts earned
    print("Total Points for Bookstore: " + str(points_sum))
    print()

#Printing the list of customers
for i in item_list:
    print(i)
print("Total points this month for the Bookstore: " + str(points_sum))