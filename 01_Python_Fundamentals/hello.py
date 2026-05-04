# String manipulation and user input. 
# This program asks the user for their name, removes any leading or trailing whitespace, converts it to title case, and then greets the user.
name = input("What is your name? ")
name = name.strip().title()
print(f"Hello, {name}!")

# String manipulation and user input. 
#slipting the full name into first and last name.
full_name = input("What is your name? ")
first_name, last_name = full_name.split()
print(f"Hello, {first_name}.")
#String manipulation and user input.
#This program asks the user for their city, converts it to title case, and then comments on the city.   
city = input("What city do you live in? ")
city = city.title()
print(f"{city} is a great place to live!")
# String manipulation and user input.
#This program asks the user for their name, converts it to uppercase and then lowercase, and
name = input("What is your name? ")
name = name.upper().lower()
print(f"Hello, {name}!")