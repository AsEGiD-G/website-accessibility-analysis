import pandas as pd

df = pd.read_csv("data/accessibility_scores.csv")
df.dropna(inplace=True)  # Remove rows with missing values
# Add more cleaning steps here if needed (e.g., data type conversion)
df.to_csv("data/cleaned_scores.csv", index=False)
print("Data cleaning complete!")