# import pandas as pd

# # Sample DataFrames
# df_A = pd.DataFrame({'value': ['a', 'b', 'c'], 'number': [1, 2, 3]})
# df_B = pd.DataFrame({'value': ['a', 'c', 'd']})

# # Merge the DataFrames on the 'value' column
# merged_df = df_A.merge(df_B, on='value', how='outer')

# # Increment the 'number' column where the merge was successful
# merged_df['number'] = merged_df['number'].fillna(0).astype(int) + 1

# # Update df_A and create 'number' column in df_B
# df_A = merged_df[['value', 'number']].drop_duplicates()
# df_B['number'] = merged_df['number']

# print(df_A)
# print(df_B)

import pandas as pd

# Sample DataFrame
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)

# Check if column 'X' exists
if 'X' not in df.columns:
    # Create the 'X' column with default value 0
    df['X'] = 0

print(df)