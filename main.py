import os

print("Running Website Accessibility Analysis...")

os.system("python scripts/collect_data.py")
os.system("python scripts/clean_data.py")
os.system("python scripts/visualize_data.py")

print("Analysis complete! Check the data/ and images/ folders.")