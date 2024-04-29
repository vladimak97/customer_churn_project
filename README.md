**Analyzing Pension Recipients by State**

**Overview**

This work focuses on investigating and analyzing the distribution of pension beneficiaries in various US states for the fiscal year 2023. The data includes information about the total number of pension beneficiaries in each state.

**1. Load the JSON data into Pandas and check for any missing or inconsistent entries.**

```python
import pandas as pd
import json
import matplotlib.pyplot as plt
```
```python
# Load JSON data
file_path = r'C:\Users\vladi\Desktop\va_pension.json'
with open(file_path, 'r') as file:
    json_data = json.load(file)
```
```python
# Extract the data from the nested structure
data_rows = json_data['data']
columns = [col['fieldName'] for col in json_data['meta']['view']['columns'] if 'fieldName' in col]
pension_data = pd.DataFrame(data_rows, columns=columns)
```
```python
# Convert data types
pension_data['total_pension_recipients'] = pd.to_numeric(pension_data['total_pension_recipients'], errors='coerce')
```
```python
# Define future behaviour for downcasting
pd.set_option('future.no_silent_downcasting', True)
```
```python
# Filling missing values
pension_data.fillna(0, inplace=True)
```

**2. Convert and save the data into Excel and CSV formats.**

```python
# Convert data to excel and csv
excel_path = r'C:\Users\yourname\Desktop\va_pension.xlsx'
csv_path = r'C:\Users\yourname\Desktop\va_pension.csv'
pension_data.to_excel(excel_path, index=False)
pension_data.to_csv(csv_path, index=False)
```

**3. Generate statistical summary and create a bar chart.**

```python
# Statistical summary
print("\nStatistical summary:")
print(pension_data.describe())
```

![](https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F17427131%2F529785be3c66ac4cf525454f0f79f8c1%2FStatistical%20Summary.png?generation=1714388928180585&alt=media)

```python
# Bar chart
plt.figure(figsize=(12, 8))
plt.bar(pension_data['state'], pension_data['total_pension_recipients'], color='skyblue')
plt.xlabel('State')
plt.ylabel('Number of Pension Recipients')
plt.title('Pension Recipients by State - FY 2023')
plt.xticks(rotation=90)
plt.show()
```

![](https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F17427131%2Fe02d660716016daaf24119e0836531ff%2FBar%20Chart.png?generation=1714388962664213&alt=media)

**4. Construct a pie chart to show the proportion of pension recipients by state.**

```python
# Pie chart
plt.figure(figsize=(10, 8))
plt.pie(pension_data['total_pension_recipients'], labels=pension_data['state'], autopct='%1.1f%%')
plt.title('Distribution of Pension Recipients by State - FY 2023')
plt.axis('equal')
plt.show()
```

![](https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F17427131%2Fec9ad8b2be4fe3035cbd68c8434e90ef%2FPie%20Chart.png?generation=1714388980451818&alt=media)

**5. Identify the top 5 states with the highest number of pension recipients.**

```python
# Top five states with the highest number of pension recipients
top_states = pension_data.sort_values(by='total_pension_recipients', ascending=False).head(5)
print("\nTop 5 states with the highest number of pension recipients:")
print(top_states[['state', 'total_pension_recipients']])
```

![](https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F17427131%2F5c06766297ccd2c68fee58c63d05f3f0%2Fimage_2024-04-29_131023211.png?generation=1714389022902430&alt=media)
