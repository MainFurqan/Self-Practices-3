def logs(func):  # Define the decorator
    def wrapper(a, b):
        print("Calling function:", func.__name__)
        result = func(a, b)  # Call the original function and store the result
        print("Result:", result)
        print("Function Executed.")
        return result  # Optionally return result if needed
    return wrapper

@logs  # Apply the decorator
def add(a, b):
    return a + b

add(5, 9)  # Call the function
