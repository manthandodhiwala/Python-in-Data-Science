# Import pandas library
import pandas as pd

# Create a Pandas Series
numbers = pd.Series([10, 25, 30, 45, 50, 15])

# Display original Series
print("Original Series:")
print(numbers)

# Filter values greater than 25 using Boolean array
filtered = numbers[numbers > 25]

# Display filtered Series
print("\nFiltered Series (Values > 25):")
print(filtered)
