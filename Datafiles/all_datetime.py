import pandas as pd
from datetime import datetime, timedelta

# Read the CSV file
file_path = '/Users/alitahseen/Desktop/FYP-2024/Machine_learning/Datafiles/Total_Dataset.csv'  
df = pd.read_csv(file_path)

# Generate the Datetime column
start_date = datetime(2021, 1, 1, 0, 0, 0)
end_date = datetime(2023, 12, 31, 23, 0, 0)
delta = timedelta(hours=1)
dates = []
current_date = start_date
while current_date <= end_date:
    dates.append(current_date)
    current_date += delta

# Add the column to the DataFrame
df['Datetime'] = pd.Series(dates[:len(df)])

# Save the updated DataFrame
output_file_path = '/Users/alitahseen/Desktop/FYP-2024/Machine_learning/Datafiles/ML_Dataset.csv' 
df.to_csv(output_file_path, index=False)
