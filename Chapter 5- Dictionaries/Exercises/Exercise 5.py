Eriek = {'kind': 'snake', 'owner': 'Eriel'}
jr = {'kind': 'dog', 'owner': 'John'}
bengel = {'kind': 'cat', 'owner': 'Angel'}
barsim = {'kind': 'bird', 'owner': 'Basim'}

pets = [Eriek, jr, bengel, barsim]

for pet in pets:
    print(f"{pet['owner']}'s pet is very amazing, because it's a {pet['kind']}")
