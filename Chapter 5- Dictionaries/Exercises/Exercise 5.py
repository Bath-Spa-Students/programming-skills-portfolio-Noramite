#list of some of my friends and some random animals they may or may not like
Eriek = {'kind': 'snake', 'owner': 'Eriel'}
jr = {'kind': 'dog', 'owner': 'John'}
bengel = {'kind': 'cat', 'owner': 'Angel'}
barsim = {'kind': 'bird', 'owner': 'Basim'}

#this part just organizes the whole process
pets = [Eriek, jr, bengel, barsim]


for pet in pets:
    print(f"{pet['owner']}'s pet is very amazing, because it's a {pet['kind']}")
