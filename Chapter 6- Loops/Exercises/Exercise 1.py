#pizza time loop
while True:
    pizza = input("We are making a pizza, what would you like on it? ")
    if pizza.upper() == 'QUIT':
        print("You decided to stop making the pizza. Now the pizza is sad.")
        break
    else:
        print(f"You added {pizza} to the pizza.")
