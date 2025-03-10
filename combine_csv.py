import pandas as pd
import glob

csv_files = glob.glob('bikeshare-ridership-2023/*.csv')

df_list = []
for file in csv_files:
    try:
        df = pd.read_csv(file, encoding='utf-8')
    except UnicodeDecodeError:
        df = pd.read_csv(file, encoding='cp1252')  # Common Windows encoding
    df_list.append(df)

combined_df = pd.concat(df_list, ignore_index=True)
print(combined_df.head())
combined_df.to_csv('combined_data.csv', index=False)