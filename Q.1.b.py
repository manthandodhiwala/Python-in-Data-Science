numbers = []

n = int(input("Enter the number of elements: "))

for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

total = sum(numbers)

print("List of numbers:", numbers)
print("Total Sum =", total)
