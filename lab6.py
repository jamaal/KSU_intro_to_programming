# Program Name: Lab_6.py 
# Course: IT1113/Section W04
# Student Name: Jamaal Hinton
# KSU Email Address: jhinton9@students.kennesaw.edu
# Assignment Lab Number: 6
# Due Date: 11/17/2024
# Purpose: This program allows the user to keep track of rain fall information. 
# After data is entered, the user can view the records created during the session,
# and they can also save the data to a file and read whats been written to the file.


import pickle

#list of months and rainfall for initization
months_list = [("January","7.9"), ("February","10.1"), ("March","3.4"),
                ("April","6.7"), ("May","8.9"), ("June","9.4"), 
          ("July","5.9"), ("August","4.1"), ("September","3.7"),
            ("October","5.1"), ("November","7.2"), ("December","8.3")]

#function to initialize rain fall data
def init_rainfall_list(rainfall_list):
    if len(rainfall_list) == 12:
        print("Cannot complete action. List alread has values")
        return rainfall_list
    else:
        for t in months_list:
            record_str = "{0:15} {1} inches".format(t[0],t[1])
            rainfall_list.append(record_str)
        print("Rain fall Data initialized")
        return rainfall_list

#function to manually add rain fall data
def add_month(rainfall_list):
    if len(rainfall_list) == 12:
        print("Cannot complete action, list is already full")
    else:
        for i in months_list:
            while True:
                rainfall = input("Enter Rainfall for month {m}: ".format(m=i[0]))
                try:
                    rainfall_float = float(rainfall)
                    rainfall_str = "{0:15} {1} inches".format(i[0],rainfall)
                    rainfall_list.append(rainfall_str)
                except:
                    print("Had issue turning {r} into float. Please try again".format(r=rainfall))
                    continue
                
                break
        print("Rainfall list created")
        return rainfall_list
    return rainfall_list

#function to write rain fall data to a file
def write_to_file(file, raindata, header):
    tmp_list = []
    if raindata == []:
        print("No data has been entered")
    else:
        tmp_list.append(header)
        tmp_list.extend(raindata)
        f = open(file, "wb")
        pickle.dump(tmp_list, f)
        f.close()
        print("Data written to file: {f_name}".format(f_name=file))

#function to read rain fall data from a file
def read_from_file(file):
    try:
        f = open(file,'rb')
        data = pickle.load(f)
        print("Data from file: {0}\n".format(file))
        for i in data:
            print(i)
        print()
        f.close()
    except:
        print("Something went wrong trying to read from file {f}".format(f=file))

#function to print the Avg, Min, Max and Total for the rainfall values stored
def calc_agg_data(rain_list):
    rainfall_values = []
    del rain_list[0] #deletes the header
    for i in rain_list:
        tmp_values = i.split()
        rainfall_values.append(float(tmp_values[1]))
    total_rainfall = sum(rainfall_values)
    max_rainfall = max(rainfall_values)
    min_rainfall = min(rainfall_values)
    rain_avg = sum(rainfall_values) / len(rainfall_values)

    agg_str = """
    The total rainfall for the year is: {0} \n
    The highest rainfall for the year is: {1}\n
    The lowest rainfall for the year is: {2}\n
    The avergae fainfall for the year is: {3}\n
       """.format(total_rainfall,max_rainfall,min_rainfall,rain_avg)
    print(agg_str)

#function to print the user menu
def print_menu():
    print("\nMenu Options:")
    print("Enter [0] to initialize list")
    print("Enter [1] to manully enter rainfall for the month")
    print("Enter [2] to print current rainfall information")
    print("Enter [3] to write rainfall information to file")
    print("Enter [4] to print rainfall information from file")
    print("Enter [5] to read from previous rainfall record file")
    print("Enter [6] to display Total, Avg, Highest and Lowest rainfall of the year")
    print("Enter [7] to remove data from list")
    print("Enter [Q/q] to quit\n")
    option = input("Enter selection: ")
    print()
    return option.lower()


#init variables
rainfall_list = []
rainfall_list_fin = []
rainfall_file_name = "rainfall.pkl"
rainfall_file = open(rainfall_file_name,"wb")

print("Hello, this is an application to record rainfall for the year")
option = print_menu()

#create header in file
heading = "{0:15} {1}".format("Month","Rainfall")

#Inifite loop  to continue to prompt the user
while True:
    #option to initialize the rain fall file
    if option == '0':
        rainfall_list_fin = init_rainfall_list(rainfall_list)
        option = print_menu()

    #option to add in rain fall data manually
    elif option == '1':
        rainfall_list_fin = add_month(rainfall_list)
        option = print_menu()

    #option to print rainfall data
    elif option == '2':
        if rainfall_list_fin == []:
            print("Rainfall data list is empty")
        else:
            print(heading)
            for r in rainfall_list_fin:
                print(r)
        option = print_menu()

    #option to write data to a pickle file
    elif option == '3':
        write_to_file(rainfall_file_name,rainfall_list_fin,heading)
        option = print_menu()

    #option to read data from pickle file
    elif option == '4':
        read_from_file(rainfall_file_name)
        option = print_menu()

    #option to read from another pickle file
    elif option == '5':
        user_file = input("Enter in file name: ")
        #Throws an error if the file cannot be found
        try:
            read_from_file(user_file)
        except:
            print("There was an error finding file {file}, or could not find {file}".format(file=user_file))
            print()
        option = print_menu()

    #option to print aggergated data from rainfall file
    elif option == '6':
        if rainfall_list_fin == []:
            print("Rainfall data list is empty")
        else:
            calc_agg_data(rainfall_list_fin)
        option = print_menu()

    #option to delete recorded data        
    elif option == '7':
        rainfall_list = []
        rainfall_list_fin = []
        print("Rain data has been cleared")
        option = print_menu()

    #option to quit the program
    elif option == 'q':
        break

    #user gets re-prompted if they enter invalid option.
    else:
        print("{0} is not a recognizable option. Please try to enter input again".format(option))
        option = print_menu()
rainfall_file.close()

