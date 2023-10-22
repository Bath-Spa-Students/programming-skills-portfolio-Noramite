places = ["Texas", "Tokyo", "Europe", "Burj Khalifa", "Germany"]

print("Original:", places)
print("alphabetical order:", sorted(places))
print("reversed alphabetical order:", sorted(places, reverse=True))

places.reverse()
print("Reversed:", places)

places.reverse()
print("reversed then back to original:", places)

places.sort()
print("alphabetical order (modified):", places)

places.sort(reverse=True)
print("reversed alphabetical  (modified):", places)
