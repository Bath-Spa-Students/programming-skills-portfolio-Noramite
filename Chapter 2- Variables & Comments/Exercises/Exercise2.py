Lelouch_quote = "“You can't change the world with pretty words alone."
Lelouch_pre = "Lelouch once said, "

sus = "“and they say chivalry is dead."
sussy_bounce_guy = "Doomfist once said, "

def quotel():
    print(Lelouch_pre + Lelouch_quote)

def quoted():
    print(sus + sussy_bounce_guy)

def ui():
    print("We have two quotes:")
    print("One is from Lelouch and the other from Doomfist")
    ans = input("Which one would you like to view? Lelouch/Doomfist: ")
    if ans.lower() == "lelouch":
        quotel()
    elif ans.lower() == "doomfist":
        quoted()
    else:
        print("Invalid input, try again")

while True:
    quotes = input("Would you like to read some quotes? Y/N: ")
    if quotes.upper() == "Y":
        ui()
        break
    elif quotes.upper() == "N":
        print("Why did you even run this script?")
        break
    else:
        print("Invalid input, try again")
