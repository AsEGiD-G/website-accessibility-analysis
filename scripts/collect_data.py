import json
import subprocess
import pandas as pd

websites = ["https://www.example.com", "https://www.google.com"] # Add your target websites

results = []
for url in websites:
    try:
        cmd = f"lighthouse {url} --quiet --output=json --chrome-flags='--headless'"
        output = subprocess.run(cmd, shell=True, capture_output=True, text=True, check=True) # check=True for errors
        report = json.loads(output.stdout)
        score = report["categories"]["accessibility"]["score"] * 100
        results.append({"Website": url, "Accessibility Score": score})
    except subprocess.CalledProcessError as e:
        print(f"Error running Lighthouse on {url}: {e}")
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON for {url}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred for {url}: {e}")

df = pd.DataFrame(results)
df.to_csv("data/accessibility_scores.csv", index=False)
print("Data collection complete!")