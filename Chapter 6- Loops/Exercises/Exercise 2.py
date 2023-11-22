while True:
    print("Type 'quit' to leave")

    age_input = input("Enter your age here: ").lower()

    # breaks the loop essentially when user puts Quit on the input
    if age_input == 'quit':
        break

    try:
        age = int(age_input)

        #checks age then prints price
        if age < 3:
            print("The ticket is free.")
        elif 3 <= age < 12:
            print("The ticket costs $10.")
        elif age >= 12:
            print("The ticket costs $15.")
    
    #this is just here incase the user puts some random stuff on the input
    except ValueError:
        print("Cannot identify input, please try again")
