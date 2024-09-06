
#Creating empty list to hold items
item_list=[]

#Using a loop to prompt the user 8 times
for i in range(8):
    #variables for the item name and price
    item_name = input("[{row_num}] Please give the item name: ".format(row_num=i+1))
    item_price = str(input("[{row_num}] please give the item price: ".format(row_num=i+1)))

    #Saving the formatted item name and price as a String
    item = "{name:15} {price}".format(name=item_name, price=item_price)

    #Adding the formatted String to the list
    item_list.append(item)

#Looping through list to print off items
for i in item_list:
    print(i)
    print()
