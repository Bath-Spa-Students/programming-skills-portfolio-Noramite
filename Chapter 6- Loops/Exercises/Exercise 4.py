#list of bread
flavored_bread = ["Italian B.M.T.","Chicken Teriyaki","Turkey Breast","Tuna","Meatball Marinara","Subway Melt","Veggie Delight","Steak & Cheese","Roast Beef","Spicy Italian","Black Forest Ham","Sweet Onion Chicken Teriyaki"]
finished_flavored_bread = []

#uses a for loop to replace a ton of print statements
for flavored in flavored_bread:
    print(f"I made your {flavored} sandwich.")
    
    #this adds the finished bread with flavor to another new list that can be used in another for loop that shows the finished flavored bread
    finished_flavored_bread.append(flavored)

#prints finished breads using the newly made list
print("\nList of Finished Sandwiches:")
for bread in finished_flavored_bread:
    print(bread)
