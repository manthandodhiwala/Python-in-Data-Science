# Swapping two elements in a list

def swap_elements(lst, pos1, pos2):
    lst[pos1], lst[pos2] = lst[pos2], lst[pos1]
    return lst

numbers = [10, 20, 30, 40, 50]

print("Original List:", numbers)

swap_elements(numbers, 1, 3)

print("Updated List:", numbers)
