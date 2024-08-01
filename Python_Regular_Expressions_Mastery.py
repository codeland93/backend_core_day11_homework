import re

def verify_names(names):
    # Define the regex pattern for a valid name
    pattern = r'^[A-Z][a-z]*\s(?:[A-Z][a-z]*\s)*[A-Z][a-z]*$'
    
    for name in names:
        if re.match(pattern, name):
            print(name)
        else:
            print("Invalid name")

# Test the function with the given list of names
names = ["Abraham Lincoln", "Andrew P Garfield", "peter pan", 
         "Connor Milliken", "Jordan Alexander Williams", "Madonna", "programming is cool"]

verify_names(names)
