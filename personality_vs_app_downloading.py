#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# df = pd.read_excel('mobile_app_user_dataset.xlsx', sheet_name='Sheet1')
df = pd.read_excel(r"D:\UCSD Stuff\WI25\ECE 143\project\App-Usage-Survey\mobile_app_user_dataset.xlsx")

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


q30_mapping_ls = [
	"Extroverted, enthusiastic",
	"Critical, quarrelsome",
	"Dependable, self-disciplined",
	"Anxious, easily upset",
	"Open to new experiences, complex",
	"Reserved, quiet",
	"Sympathetic, warm",
	"Disorganized, careless",
	"Calm, emotionally stable",
	"Conventional, uncreative"
]

q30_mapping = {}
for k,v in zip(q30_cols, q30_mapping_ls):
    q30_mapping[k] = v
df = df.rename(columns=q30_mapping)

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
for original_column in q30_mapping_ls:
    df[original_column] = df[original_column].apply(recode_q30)



q15_mapping = {
    'Q15_1': 'Navigation', 'Q15_2': 'Business', 'Q15_3': 'Catalogues', 'Q15_4': 'Travel',
    'Q15_5': 'Books', 'Q15_6': 'Photo & Video', 'Q15_7': 'Lifestyle', 'Q15_8': 'Entertainment',
    'Q15_9': 'Finance', 'Q15_10': 'News', 'Q15_11': 'Health & Fitness', 'Q15_12': 'Games',
    'Q15_13': 'Food & Drink', 'Q15_14': 'Education', 'Q15_15': 'Medical', 'Q15_16': 'Social Networking',
    'Q15_17': 'Reference', 'Q15_18': 'Sports', 'Q15_19': 'Utilities', 'Q15_20': 'Weather',
    'Q15_21': 'Productivity', 'Q15_22': 'Music', 'Q15_23': 'Other'
}

df = df.rename(columns=q15_mapping)

# visualizaiton: 
for col in q30_mapping_ls:
    new_col = col
    unique_vals = df[new_col].unique()[1:]
    grouped = df.groupby(new_col)[list(q15_mapping.values())].mean()[1:]
    if not grouped.empty and grouped.shape[0] > 0:
        plt.figure(figsize=(15, 5))
        sns.heatmap(grouped, annot=True, cmap='Blues', fmt=".3f")
        plt.title(f"Download Rates of each App Category by \"{new_col}\" (1=Neutral, 0=Disagree, 2=Agree)")
        plt.xlabel("App Categories")
        plt.ylabel(f"\"{new_col}\" Category")
        plt.xticks(rotation=45, ha='right', rotation_mode="anchor")
        plt.tight_layout()
        plt.show()
    else:
        print(f"No data available for {new_col}. Skipping plot.")




# In[ ]:




