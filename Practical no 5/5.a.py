# Import pandas library
import pandas as pd

# Create a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [22, 24, 23],
    'City': ['New York', 'London', 'Paris']
}

# Create DataFrame
df = pd.DataFrame(data)

# Display DataFrame
print("DataFrame:")
print(df)
