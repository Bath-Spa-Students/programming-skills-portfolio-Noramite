#this is justa generic list of places
rivers_and_countries = {'nile': 'Egypt', 'amazon': 'Brazil', 'yangtze': 'China'}


#this whole area just prints everything in a for loop
for river, country in rivers_and_countries.items():
    print(f"\nThe {river.capitalize()} runs through {country}.")

print("\n\nRivers\n")
for river in rivers_and_countries.keys():
    print(river.capitalize())

print("\n\nCountries\n")
for country in rivers_and_countries.values():
    print(country)
