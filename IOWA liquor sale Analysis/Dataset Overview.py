
import pandas as pd 

df = pd.read_csv('Iowa_Liquor_Sales.csv')

# Overview of the raw data
raw_data_str = df.head().to_string()
raw_data_str = raw_data_str.replace('\n', ' |\n')  # Replace line breaks with ' | '

# Count of unique values in each column
unique_values_str = df.nunique().to_string()
unique_values_str = unique_values_str.replace('\n', ' |\n')  # Replace line breaks with ' | '

# Summary statistics for numerical columns
summary_stats_str = df.describe().to_string()
summary_stats_str = summary_stats_str.replace('\n', ' |\n')  # Replace line breaks with ' | '

# Define the file path where you want to save the output
output_file_path = "data_summary.txt"

# Create a separator line
separator_line = '-' * 80  # Adjust the length as needed

# Open the file in write mode and write the data
with open(output_file_path, "w") as f:
    f.write(separator_line + '\n')
    f.write("Overview of the raw data:\n")
    f.write(separator_line + '\n')
    f.write(raw_data_str)
    f.write(separator_line + '\n\n')
    f.write("Count of unique values in each column:\n")
    f.write(separator_line + '\n')
    f.write(unique_values_str)
    f.write(separator_line + '\n\n')
    f.write("Summary statistics for numerical columns:\n")
    f.write(separator_line + '\n')
    f.write(summary_stats_str)

print(f"Data summary saved to {output_file_path}")
