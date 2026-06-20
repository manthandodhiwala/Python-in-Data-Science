# Square of numbers from 1 to 10

print("Squares of Numbers from 1 to 10")

for i in range(1, 11):
    print(i, "=", i ** 2)

# Count Even Numbers

count = 0

print("\nEnter 5 Numbers:")

for i in range(5):
    num = int(input())

    if num % 2 == 0:
        count += 1

print("Total Even Numbers =", count)
