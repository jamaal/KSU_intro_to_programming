'''If a customer purchases 0 books, he/she earns 0 points.
If a customer purchases 1-2 books, he/she earns 3 points.
If a customer purchases 3-4 books, he/she earns 12 points.
If a customer purchases 5-6 books, he/she earns 20 points.
If a customer purchases 7-9 books, he/she earns 30 points.
If a customer purchases 10 or more books, he/she earns 50 points. '''

item_list = []
points_sum = 0
points = 0

for i in range(1):
    name = input("Please enter your name: ")
    num_of_books = int(input("Please enter the number of book purchased this month: "))

    #if num_of_books in range(1,3):
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
    

    points_sum = points_sum + points
    item = "{name:15} {points}".format(name=name, points=points)
    item_list.append(item)

print(item_list)
print(points_sum)