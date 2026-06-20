import math

while True:
    try:
        num = input("Enter a number (or 'q' to quit): ")

        if num.lower() == 'q':
            print("Program Ended")
            break

        num = float(num)

        if num < 0:
            print("Square root of a negative number is not possible.")
        else:
            print("Square Root =", math.sqrt(num))

    except ValueError:
        print("Invalid Input! Please enter a valid number.")

