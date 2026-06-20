# List Operations

numbers = [12, 45, 67, 23, 89, 10, 34, 78, 56, 90]

print("List:", numbers)

print("Maximum =", max(numbers))
print("Minimum =", min(numbers))
print("Average =", sum(numbers) / len(numbers))

print("Ascending Order =", sorted(numbers))
print("Descending Order =", sorted(numbers, reverse=True))

new_num = int(input("Enter a new number: "))
numbers.append(new_num)

numbers.pop(0)

print("Updated List =", numbers)
