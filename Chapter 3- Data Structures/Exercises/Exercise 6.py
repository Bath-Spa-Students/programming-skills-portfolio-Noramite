persons = ["Mom", "Dad", "Grandpa", "Grandma"]
pre = "I would like to invite my"
post = "to my dinner party"

backup = ["Uncle", "Auntie", "Cousin"]
na = "would not be able to attend"

for person in persons:
    print(pre, person, post)

#this sections basically just removes the dad from the party since hes absent
print ("Dad cannot attend the dinner party")

remove = "Dad"
if remove in persons:
    persons.remove(remove)

for person in persons:
    print(pre, person, post)

#this is my solution on replacing the people who wasnt able to attend
print(pre, backup[1], post)

print("I can invite only two people for dinner.")

while len(persons) > 2:
    removed_person = persons.pop()
    print(f"Sorry, {removed_person}, I can't invite you to dinner.")

#this just says sorry to everyone who was uninvited
for not_invited in persons:
    print(f"Sorry, {not_invited}, I can't invite you to dinner.")

for person in persons:
    print(f"{pre} {person} {post}")

del persons[:]

#this shows the list to be empty afterwards
print(persons)