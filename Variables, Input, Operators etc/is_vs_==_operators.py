a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # Output: True  
# Explanation: "==" compares the **contents/values** of the lists. Both have the same elements.

print(a is b)  # Output: False  
# Explanation: "is" compares the **memory locations (identity)**. 'a' and 'b' are two different list objects.

c = a  # Assigning 'a' to 'c' — now both refer to the **same list object** in memory.

print(a is c)  # Output: True  
print(c is a)  # Output: True  
# Explanation: Both 'a' and 'c' point to the same memory location (same object identity).
