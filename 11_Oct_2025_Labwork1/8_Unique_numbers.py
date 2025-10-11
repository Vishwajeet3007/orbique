def unique_numbers(number):
    unique = []
    for num in number:
        if num not in unique:
            unique.append(num)
    return unique
numbers = [1,2,3,3,4,4,5,5,5,6,7,8,9,10,11]
print(unique_numbers(numbers))