# Ask to user enter '7 multiple'
multiple = int(input("Enter '7 multiple': "))

# Identify whether given number is 'multiple of 7'
if(multiple%7==0):
    print(f"{multiple} is multiple of '7'")
else:
    print(f"{multiple} is not multiple of '7'")  