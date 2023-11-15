#list of bread
flavored_bread = ["Italian B.M.T.", "Chicken Teriyaki", "Turkey Breast","pastrami", "Tuna","pastrami", "Meatball Marinara","pastrami", "Subway Melt","Veggie Delight", "Steak & Cheese", "Roast Beef", "Spicy Italian", "Black Forest Ham","Sweet Onion Chicken Teriyaki"]

#this counts 3 pastrami breads and puts it in another list to remove it later
while flavored_bread.count('pastrami') < 3:
    flavored_bread.append('pastrami')

print("Deli has run out of pastrami.")

#this consolidates the list to one variable name that could be used to remove pastrami 
yummy = flavored_bread[:]
doned_bread = []

#this removes pastrami because no more
while 'pastrami' in yummy:
    yummy.remove('pastrami')

#uses a for loop to replace a ton of print statements
for flavored in yummy:
    print(f"I made your {flavored} sandwich.")
    
    #this adds the finished bread with flavor to another new list that can be used in another for loop that shows the finished flavored bread
    doned_bread.append(flavored)

#prints finished breads using the newly made list
print("\nList of Finished Sandwiches:")
for bread in doned_bread:
    print(bread)
