import pandas as pd

# List of file paths for the CSV files
file_paths = [
  "E:\\Great learning All Data Analytise Material\\final live project\\Comedy_youtube_data.csv",
  "E:\\Great learning All Data Analytise Material\\final live project\\Films_youtube_data.csv",
  "E:\\Great learning All Data Analytise Material\\final live project\\Finance_youtube_data.csv",
  "E:\\Great learning All Data Analytise Material\\final live project\\Shopping_youtube_data.csv",
  "E:\\Great learning All Data Analytise Material\\final live project\\Gaming_youtube_data.csv"
]

# Read each CSV file and store them in a list of dataframes
dfs = []
for file_path in file_paths:
    df = pd.read_csv(file_path)
    dfs.append(df)

# Concatenate all dataframes into a single dataframe
concatenated_df = pd.concat(dfs, ignore_index=True)

# Write the concatenated dataframe to a new CSV file
output_file_path = 'merged_file2.csv'
concatenated_df.to_csv(output_file_path, index=False)

print("Merged CSV file has been created successfully at:", output_file_path)
