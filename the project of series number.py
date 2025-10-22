# step 1: input the series
def enter_numbers():
    user_numbers = input("please enter a series of positive numbers. "
                         "please enter after each number space. "
                         "please enter at least 3 numbers: ")

    new_numbers = user_numbers.split(" ")
    list_of_numbers = []
    for i in new_numbers:
        try:
            list_of_numbers.append (float (i))
        except:
            return enter_numbers()

    for number in list_of_numbers:
        if number <= 0:
            return enter_numbers()

    if len(list_of_numbers) < 3:
        return enter_numbers()

    return list_of_numbers

the_list = enter_numbers()

#step 2: the menu
def show_menu():
    print ("Series Analyzer - Menu. \n"
    "1. Input a new series. \n"
    "2. Display the series (original order). \n"
    "3. Display the series (reversed order). \n"
    "4. Display the series (sorted low→high). \n"
    "5. Display the Max value. \n"
    "6. Display the Min value. \n"
    "7. Display the Average value. \n"
    "8. Display the Number of elements. \n"
    "9. Display the Sum of the series. \n"
    "0. Exit.")

show_menu()


#step 3: choose an option
def user_choice ():
    user_select = int (input ("please choose one option by his number: "))
    match user_select:
        case 1:
            enter_numbers()
            show_menu()
            user_choice()
        case 2:
            print(the_list)
            show_menu()
            user_choice()
        case 3:
            print(the_list[: : -1])
            show_menu()
            user_choice()
        case 4:
            print(sorted(the_list))
            show_menu()
            user_choice()
        case 5:
            print(max (the_list))
            show_menu()
            user_choice()
        case 6:
            print(min(the_list))
            show_menu()
            user_choice()
        case 7:
            import statistics
            print(statistics.mean(the_list))
            show_menu()
            user_choice()
        case 8:
            print(len (the_list))
            show_menu()
            user_choice()
        case 9:
            print(sum(the_list))
            show_menu()
            user_choice()
        case 0:
            return

user_choice()

#step 5: exit
#didn't need to fo any




