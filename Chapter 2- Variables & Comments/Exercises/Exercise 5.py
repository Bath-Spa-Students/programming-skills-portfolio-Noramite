print("This is a calculator for calculating how many USB sticks you can get for the amount of money you have.")
print("USB Stick - €6")

while True:
    usb = 6
    money = input("How much money do you have? ")
    #this part detects if no digit is present and instantly repeats the question
    if any(char.isdigit() for char in money):
        break

#this part filters out any symbol/letter if a number is detected so that the numbers can be used in a math equation
money = int(''.join([char for char in money if char.isdigit()]))

ans = (money//usb)
change = (ans*usb)
change2 = (money-change)

print("You can get", ans, "USB sticks with that much money")
print("And you will be left with", "€" + str(change2))
