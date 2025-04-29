def greet_user(func):
    def wrapper():
        name = func()  # Call the original function to get user input
        print(f"\nHello {name}!")
        print("How are you?")
    return wrapper

@greet_user
def get_name():
    return input("Enter your name: ")

# Call the decorated function
get_name()
