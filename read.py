import pandas as pd
df = pd.read_csv('save_data.csv')
df = df[['Product_name','Brand','Item_id']]
print(df[df == 'nan'])