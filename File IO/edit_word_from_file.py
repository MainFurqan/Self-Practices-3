# Replace the 'java' word with 'python' in " practice.txt " file

# Open the file in read mode
with open("practice.txt", "r") as f:
    data = f.read()

# replace the word "java" with "python"
update_data = data.replace("java", "Python")
print(update_data)

# write the update_data in file
with open("practice.txt", "w") as fw:
    fw.write(update_data)