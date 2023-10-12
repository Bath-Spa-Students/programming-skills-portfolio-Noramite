import time

favnum = (77)
Ending = ("the giant's favorite number was " + str(favnum) + " all along")
dilema = ("I hope i can get out of this place soon...")
trollface = ("""⢿⣿⣿⣿⣭⠹⠛⠛⠛⢿⣿⣿⣿⣿⡿⣿⠷⠶⠿⢻⣿⣛⣦⣙⠻⣿
⣿⣿⢿⣿⠏⠀⠀⡀⠀⠈⣿⢛⣽⣜⠯⣽⠀⠀⠀⠀⠙⢿⣷⣻⡀⢿
⠐⠛⢿⣾⣖⣤⡀⠀⢀⡰⠿⢷⣶⣿⡇⠻⣖⣒⣒⣶⣿⣿⡟⢙⣶⣮
⣤⠀⠀⠛⠻⠗⠿⠿⣯⡆⣿⣛⣿⡿⠿⠮⡶⠼⠟⠙⠊⠁⠀⠸⢣⣿
⣿⣷⡀⠀⠀⠀⠀⠠⠭⣍⡉⢩⣥⡤⠥⣤⡶⣒⠀⠀⠀⠀⠀⢰⣿⣿
⣿⣿⡽⡄⠀⠀⠀⢿⣿⣆⣿⣧⢡⣾⣿⡇⣾⣿⡇⠀⠀⠀⠀⣿⡇⠃
⣿⣿⣷⣻⣆⢄⠀⠈⠉⠉⠛⠛⠘⠛⠛⠛⠙⠛⠁⠀⠀⠀⠀⣿⡇⢸
⢞⣿⣿⣷⣝⣷⣝⠦⡀⠀⠀⠀⠀⠀⠀⠀⡀⢀⠀⠀⠀⠀⠀⠛⣿⠈
⣦⡑⠛⣟⢿⡿⣿⣷⣝⢧⡀⠀⠀⣶⣸⡇⣿⢸⣧⠀⠀⠀⠀⢸⡿⡆
⣿⣿⣷⣮⣭⣍⡛⠻⢿⣷⠿⣶⣶⣬⣬⣁⣉⣀⣀⣁⡤⢴⣺⣾⣽⡇
""")
print("welcome to the Giant's house")
time.sleep (0.5)
print("can you find his favourite number in strange place?")
time.sleep (0.5)

#these are functions that make my life easier by seperating the events by module
def start():
    print("Type up, down, left, or right to move")
    time.sleep (0.5)
    direction = input("You stumble upon a giant house, where will you go?: ")
    if direction.upper() == "UP":
        up()
    else:
        print("Your lungs start to fill with water and you collapsed")

def up():
    direction2 = input("""You went UP the house instead of going through the door, 
you find yourself in front of a ladder that goes to the attic. 
Where do you go?: """)
    if direction2.upper() == "UP":
        attic()
    else:
        print("something grabbed your foot...")

def attic():
    direction3 = input("""You climbed the ladder and got yourself into the giant house,
you are here to find the giant's favorite number.
Where do you start looking?: """)
    if direction3.upper() == "LEFT":
        hide()
    else:
        print("You start to feel tired")
        time.sleep (0.5)
        print("You collapsed")

def hide():
    direction4 = input("*You hear him*. Where do you H I D E?: ")
    if direction4.upper() == "DOWN":
        paper()
    else:
        print(trollface)

def paper():
    direction5 = input("You notice a piece of paper sticking out of the drawers in your hiding place. Where is it?: ")
    if direction5.upper() == "RIGHT":
        print(Ending)
        time.sleep (0.5)
        print(dilema)
    else:
        print(trollface)

#this is the script itself that runs the functions
while True:
    intro = input("would you like to read the map? {Y/N} ")
    if intro.upper() == "Y":
        print("The map says:")
        time.sleep (0.5)
        print("""
<you must go up, up, left, down, and right>
    <If you enter the wrong direction>
            <you might die>
              """)
        start()
        break
    elif intro.upper() == "N":
        print("suit yourself...")
        start()
        break
    else:
        print("Invalid input. Try again.")