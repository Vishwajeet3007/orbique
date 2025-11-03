# -----------------------------------------------
# Program: Fruit Information Saver
# Author : Vishwajeet Kumar
# Course : B.Tech (4th Year)
# Description:
#   This program stores details about fruits such as
#   name, rate, quantity, cost, and their benefits
#   into a text file using file handling.
# -----------------------------------------------

def save_fruit_info():
    filename = "03_Nov_2025/fruits_info.txt"
    
    print("\n--- Fruit Information Entry ---")
    n = int(input("Enter number of fruits to record: "))

    with open(filename, "a") as file:
        for i in range(1, n + 1):
            print(f"\nEnter details for Fruit {i}:")
            name = input("Fruit Name: ").capitalize()
            rate = float(input("Rate per unit (₹): "))
            qty = int(input("Quantity: "))
            cost = rate * qty
            desc = input("Description / Benefits: ")

            # Format data
            fruit_data = (
                f"Fruit Name : {name}\n"
                f"Rate (₹)    : {rate:.2f}\n"
                f"Quantity    : {qty}\n"
                f"Total Cost  : ₹{cost:.2f}\n"
                f"Benefits    : {desc}\n"
                f"{'-'*40}\n"
            )

            # Write data to file
            file.write(fruit_data)

    print(f"\n✅ All fruit details have been saved to '{filename}' successfully!\n")


def read_fruit_info():
    filename = "03_Nov_2025/fruits_info.txt"
    try:
        print("\n--- Saved Fruit Details ---\n")
        with open(filename, "r") as file:
            data = file.read()
            if data.strip():
                print(data)
            else:
                print("No fruit data found.")
    except FileNotFoundError:
        print("❌ File not found. Please add fruit data first.")


# ----------------------------
# Main Menu
# ----------------------------
while True:
    print("\n====== FRUIT INFORMATION SYSTEM ======")
    print("1. Add Fruit Details")
    print("2. View Saved Fruit Details")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        save_fruit_info()
    elif choice == "2":
        read_fruit_info()
    elif choice == "3":
        print("👋 Exiting... Have a healthy day!")
        break
    else:
        print("❌ Invalid choice! Please try again.")
