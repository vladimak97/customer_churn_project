import pandas as pd
import json
import matplotlib.pyplot as plt

# Load JSON data
file_path = r'C:\Users\vladi\Desktop\va_pension.json'
with open(file_path, 'r') as file:
    json_data = json.load(file)

# Extract the data from the nested structure
data_rows = json_data['data']
columns = [col['fieldName'] for col in json_data['meta']['view']['columns'] if 'fieldName' in col]
pension_data = pd.DataFrame(data_rows, columns=columns)

# Convert data types
pension_data['total_pension_recipients'] = pd.to_numeric(pension_data['total_pension_recipients'], errors='coerce')

# Define future behaviour for downcasting
pd.set_option('future.no_silent_downcasting', True)

# Filling missing values
pension_data.fillna(0, inplace=True)

# Convert data to excel and csv
excel_path = r'C:\Users\vladi\Desktop\va_pension.xlsx'
csv_path = r'C:\Users\vladi\Desktop\va_pension.csv'
pension_data.to_excel(excel_path, index=False)
pension_data.to_csv(csv_path, index=False)

# Statistical summary
print("\nStatistical summary:")
print(pension_data.describe())

# Bar chart
plt.figure(figsize=(12, 8))
plt.bar(pension_data['state'], pension_data['total_pension_recipients'], color='skyblue')
plt.xlabel('State')
plt.ylabel('Number of Pension Recipients')
plt.title('Pension Recipients by State - FY 2023')
plt.xticks(rotation=90)
plt.show()

# Pie chart
plt.figure(figsize=(10, 8))
plt.pie(pension_data['total_pension_recipients'], labels=pension_data['state'], autopct='%1.1f%%')
plt.title('Distribution of Pension Recipients by State - FY 2023')
plt.axis('equal')
plt.show()

# Top five states with the highest number of pension recipients
top_states = pension_data.sort_values(by='total_pension_recipients', ascending=False).head(5)
print("\nTop 5 states with the highest number of pension recipients:")
print(top_states[['state', 'total_pension_recipients']])
