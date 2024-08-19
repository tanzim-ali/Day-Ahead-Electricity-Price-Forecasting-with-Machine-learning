import pandas as pd

# Read the CSV file
file_path = '/Users/alitahseen/Desktop/FYP-2024/Machine_learning/Datafiles/ML_Dataset.csv'
df = pd.read_csv(file_path)

# Filter the required columns
df = df[['Datetime', 'Average_Temp', 'MW']]

# Calculate row indices for splitting
total_rows = len(df)
train_end = int(total_rows * 0.7)
validate_end = train_end + int(total_rows * 0.15)

# Split the DataFrame
train_df = df.iloc[:train_end]
validate_df = df.iloc[train_end:validate_end]
test_df = df.iloc[validate_end:]

# Save the DataFrames to CSV files
train_df.to_csv('/Users/alitahseen/Desktop/FYP-2024/Machine_learning/Datafiles/train.csv', index=False)
validate_df.to_csv('/Users/alitahseen/Desktop/FYP-2024/Machine_learning/Datafiles/validate.csv', index=False)
test_df.to_csv('/Users/alitahseen/Desktop/FYP-2024/Machine_learning/Datafiles/test.csv', index=False)
