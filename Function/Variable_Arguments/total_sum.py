# Q1: Total Sum Calculator using *args
# Write a function called total_sum that accepts any number of numbers using *args and returns their sum.
# Example:
# total_sum(10, 20, 30) → 60
# total_sum() → 0

# Define the Variable_Argument function
def total_sum(*nums):
    total = 0
    for i in nums:
        total += i
    return total

# Call the function
print(total_sum(56, 34, 99, 11, 90))
print(total_sum())