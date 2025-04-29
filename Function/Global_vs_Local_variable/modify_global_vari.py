counter = 0
def increment(num):
    global counter      # relate with "call by value" and "call by reference"
    counter = num
    return counter

print(increment(5))
print(counter)

