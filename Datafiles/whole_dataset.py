import pandas as pd

# Input CSV file
input_csv_file = '/Users/alitahseen/Desktop/FYP-2024/Machine_learning/Datafiles/ML_Dataset.csv'

# Read the input CSV file into a pandas dataframe
df = pd.read_csv(input_csv_file)

# Columns to drop
columns_to_drop = ['local_time', 'PNODE_RESMRID', 'GRP_TYPE', 'POS', 'GROUP']  

df = df.drop(columns=columns_to_drop)

# Define the columns for the new CSV file
new_column_order = ['Datetime', 'Average_Temp', 'MW']  

# Rearrange columns in dataframe
df = df[new_column_order]

# Output CSV file
output_csv_file = '/Users/alitahseen/Desktop/FYP-2024/Machine_learning/Datafiles/Whole_Dataset.csv'

# Save new CSV file
df.to_csv(output_csv_file, index=False)
