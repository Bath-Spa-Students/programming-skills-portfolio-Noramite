#list of bread
flavored_bread = ["Italian B.M.T.","Chicken Teriyaki","Turkey Breast","Tuna","Meatball Marinara","Subway Melt","Veggie Delight","Steak & Cheese","Roast Beef","Spicy Italian","Black Forest Ham","Sweet Onion Chicken Teriyaki"]
finished_flavored_bread = []

#uses a for loop to replace a ton of print statements
for flavored in flavored_bread:
    print(f"I made your {flavored} sandwich.")
    finished_flavored_bread.append(flavored)

print("\nList of Finished Sandwiches:")
for bread in finished_flavored_bread:
    print(bread)
