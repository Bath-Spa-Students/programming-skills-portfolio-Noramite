money = float(input("How much in sales did you make this year?: "))
broke = "You earned nothing lol"

percent = 0.10
bonus = money * percent

if money > 4500:
    print("Your bonus is: $" + str(bonus))
else:
    print(broke)
