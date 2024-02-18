def list_main(my_choice):

    if my_choice == 1:
        add_value = input("Enter the number you add: ")
        my_list.append(add_value)
    elif my_choice == 2:
        remove_value = input("Enter the number you want to remove: ")  
        my_list.pop(remove_value)
    elif my_choice == 3: 
        my_list.sort()
    elif my_choice == 4:
        my_list.sort(reverse = True)
    elif my_choice == 5:
        exit()
    else:
        print("Invalid Selection")

my_list = [3, 7, 2, 9, 1]


print("Original list: ", my_list)
print("""
    1. Add a number
    2. Remove a number
    3. Sort the list
    4. Reverse the list
    5. Exit
      """)

my_choice = input("Enter your desired number: ")
list_main(my_choice)


