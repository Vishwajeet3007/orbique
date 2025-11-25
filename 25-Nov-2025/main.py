from student import (
    get_name, get_score, get_performance,
    add_name, add_score, add_performance
)

while True:
    print("\n===== STUDENT MENU =====")
    print("1. Show Student Details")
    print("2. Add Student")
    print("3. Exit")

    choice = int(input("Enter choice: "))

    # Show student details
    if choice == 1:
        roll = int(input("Enter roll number: "))
        print("\n--- STUDENT DETAILS ---")
        print("Name       :", get_name(roll))
        print("Score      :", get_score(roll))
        print("Performance:", get_performance(roll))

    # Add a student
    elif choice == 2:
        roll = int(input("Enter new roll number: "))
        name = input("Enter student name: ")
        score = int(input("Enter score: "))
        performance = input("Enter performance: ")

        add_name(roll, name)
        add_score(roll, score)
        add_performance(roll, performance)

        print("\nStudent added successfully!")

    elif choice == 3:
        print("Exiting...")
        break

    else:
        print("Invalid option, try again!")
