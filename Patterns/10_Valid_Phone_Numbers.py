import re

def validate_phone_number(phone):
    # Check if phone number starts with 6, 7, 8, or 9 and is 10 digits long
    if re.match(r'^[6-9]\d{9}$', phone):
        print("Valid phone number.")
    else:
        print("Invalid phone number. Please enter a valid number that starts with 6, 7, 8, or 9 and contains 10 digits.")

def main():
    # Taking user input for phone number
    phone_number = input("Enter your phone number: ")
    
    validate_phone_number(phone_number)

main()
