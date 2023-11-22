def make_shirt(size="large", message="I love Python"):
    print(f"Shirt size: {size.capitalize()}, Message: {message}")

#activates function using positional arguments
make_shirt("medium", "Eriel lost his AirPods LOL")

#activates the function using keywords
make_shirt(size="large", message="He found it later in a different room")
