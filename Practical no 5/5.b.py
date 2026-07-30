# Import pandas library
import pandas as pd

# Create DataFrame
data = {
    'Marks': [80, 75, 90, 85, 95]
}

df = pd.DataFrame(data)

# Display DataFrame
print("Dataset:")
print(df)

# Show statistical information
print("\nStatistical Information:")
print(df.describe())
