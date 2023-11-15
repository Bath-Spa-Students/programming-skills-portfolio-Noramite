def make_shirt(size, message):
    print(f"Shirt size: {size.upper()}, Message: {message}")

#activates function using positional arguments 
make_shirt("medium", "Eriel lost his airpods LOL")

#activates the function using keywords
make_shirt(size="large", message="He found it later in a different room")
