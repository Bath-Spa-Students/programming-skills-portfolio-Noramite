while True:
    print("Type 'quit' to leave")

    age_input = input("Enter your age here: ").lower()

    if age_input == 'quit':
        break

    try:
        age = int(age_input)

        if age < 3:
            print("The ticket is free.")
        elif 3 <= age < 12:
            print("The ticket costs $10.")
        elif age >= 12:
            print("The ticket costs $15.")
    except ValueError:
        print("cannot identify input, please try again")
