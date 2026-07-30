# Import pandas library
import pandas as pd

# Create dictionary
data = {
    'Math': 95,
    'Science': 88,
    'English': 92
}

# Create Series
series = pd.Series(data)

# Display Series
print("Pandas Series:")
print(series)
