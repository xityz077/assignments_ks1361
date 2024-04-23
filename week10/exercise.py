# Ask user to enter string
search_string = input("Enter a string:").lower()

# Ask user to enter a single letter
search_char = input("Enter a single letter:").lower()

# Counter
count = 0

# Count the number of times the letter appears in the string
for searching in search_string:
    print(f'searching = {searching}, search_char = {search_char} count = {count}')
    if search_char in searching:
        count = count + 1

# Display the number to the user
print(f"{search_char} appeared {count} times in {search_string}")
