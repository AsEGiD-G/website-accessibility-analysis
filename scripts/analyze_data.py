import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/cleaned_scores.csv")

plt.figure(figsize=(10, 6))
plt.bar(df["Website"], df["Accessibility Score"], color="skyblue") # Changed color for visibility
plt.xticks(rotation=45, ha="right")
plt.xlabel("Website")
plt.ylabel("Accessibility Score")
plt.title("Website Accessibility Scores")
plt.tight_layout() # Adjust layout to prevent labels from overlapping
plt.savefig("images/accessibility_scores.png") # Save the image to the images/ folder
plt.show()

print("Visualization complete!")