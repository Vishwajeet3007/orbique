def generate(series_length):
    series = ""
    total = 0
    for i in range(1,series_length):
        series += f"{i}/{i+1}"
        total += i/(i+1)
        if i < series_length:
            series += "+"
 # Display neatly
    print("Generated Series:")
    print(series)
    print("\n-------------------------")
    print(f"Sum of the Series = {total:.4f}")
    print("-------------------------")

# Input from user
n = int(input("Enter the number of terms: "))
generate(n)