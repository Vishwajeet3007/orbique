import math

def cube_root(num):
    # Check if the number is a whole number
    if num < 0:
        print("Please enter a non-negative number.")
        return

    # Calculate the cube root
    cube_root_value = round(num ** (1 / 3), 4)  # Rounded to 4 decimal places
    print(f"The cube root of {num} is {cube_root_value}")

def main():
    try:
        # Taking user input
        num = float(input("Enter a number to find its cube root: "))

        # Validate if the number is a whole number
        if num.is_integer():
            cube_root(int(num))  # Pass the integer value to cube_root function
        else:
            print("Please enter a whole number (integer).")

    except ValueError:
        print("Invalid input! Please enter a valid number.")

# Run the main function
main()
