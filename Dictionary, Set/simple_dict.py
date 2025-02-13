# Define a dictionary to store word meanings
word_meanings = {
    "table": ["A piece of furniture.", "A list of facts and figures."],
    "cat": "A small animal"
}

# Retrieve and print the meaning of the word "table"
table_meanings = word_meanings.get("table")
print(table_meanings)
