persons = ["Mom", "Dad", "Grandpa", "Grandma"]
pre = "I would like to invite my"
post = "to my dinner party"

backup = ["Uncle", "Auntie", "Cousin"]
na = "would not be able to attend"

for person in persons:
    print(pre, person, post)

print ("Dad cannot attend the dinner party")

remove = "Dad"
if remove in persons:
    persons.remove(remove)

for person in persons:
    print(pre, person, post)
print(pre, backup[1], post)
