#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel('mobile_app_user_dataset.xlsx', sheet_name='Sheet1')

print("Columns:", df.columns.tolist())
print("Shape of dataset (rows, cols):", df.shape)


# Q15 AND Q30
#    Q15: Types of apps downloaded
#    Q30: Personality

q15_cols = [f'Q15_{i}' for i in range(1, 24)]   # Q15_1 to Q15_23
q30_cols = [f'Q30_{i}' for i in range(1, 11)]   # Q30_1 to Q30_10

print(df['Q15_1'].head(10))
print(df['Q30_1'].head(210))


# 4. FILL MISSING VALUES
df[q15_cols] = df[q15_cols].fillna(0)
df[q30_cols] = df[q30_cols].fillna(4)

# to numerical 
df[q15_cols] = df[q15_cols].apply(pd.to_numeric, errors='coerce')
df[q30_cols] = df[q30_cols].apply(pd.to_numeric, errors='coerce')


def recode_q30(val):
    if val == 4: # nutrual 
        return 1
    elif val in [1, 2, 3]: # more disagree to personality 
        return 0
    elif val in [5, 6, 7]: # more agree to the perosnality 
        return 2
    else:
        return -1  #the epople who did not respond

# Create new recoded columns for each Q30 item
for original_column in q30_cols:
    new_column_name = f"{original_column}_new"
    df[new_column_name] = df[original_column].apply(recode_q30)




# vidualizaiton: 
for col in q30_cols:
    new_col = col + '_new'
    unique_vals = df[new_col].unique()
    grouped = df.groupby(new_col)[q15_cols].mean()
    if not grouped.empty and grouped.shape[0] > 0:
        plt.figure(figsize=(15, 5))
        sns.heatmap(grouped, annot=True, cmap='Blues', fmt=".3f")
        plt.title(f"Q15 Download Rates by {new_col} (1=Neutral, 0=Disagree, 2=Agree)")
        plt.xlabel("App Categories (Q15)")
        plt.ylabel(f"{new_col} Category")
        plt.tight_layout()
        plt.show()
    else:
        print(f"No data available for {new_col}. Skipping plot.")




# In[ ]:




