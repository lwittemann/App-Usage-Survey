import pandas as pd

def get_overall_apps(x,mapping):
    '''
    takes in pd.dataframe and sums every column in dataframe to set up count for each column in dataframe

    params:
        x: (pd.dataframe) takes in column(s) to be summed
        mapping: (dict) mapping for column name to categorical name
    
    returns:
        pd.dataframe of counts for each column given

    example usage:

        df = pd.read_excel("mobile_app_data_usage.xlsx")

        categories = {
            'Q15_1'  : 'Navigation',
            'Q15_2'  : 'Business',
            'Q15_3'  : 'Catalogues',
            'Q15_4'  : 'Travel',
            'Q15_5'  : 'Books',
            'Q15_6'  : 'Photo & Video',
            'Q15_7'  : 'Lifestyle',
            'Q15_8'  : 'Entertainment',
            'Q15_9'  : 'Finance',
            'Q15_10' : 'News',
            'Q15_11' : 'Health & Fitness',
            'Q15_12' : 'Games',
            'Q15_13' : 'Food & Drink',
            'Q15_14' : 'Education',
            'Q15_15' : 'Medical',
            'Q15_16' : 'Social Networking',
            'Q15_17' : 'Reference',
            'Q15_18' : 'Sports',
            'Q15_19' : 'Utilities',
            'Q15_20' : 'Weather',
            'Q15_21' : 'Productivity',
            'Q15_22' : 'Music',
            'Q15_23' : 'Other'
        }

        type_apps = [f'Q15_{i}' for i in range(1, 24)]

        x = df[type_apps]

        count = get_overall_apps(x,categories)

        print(count)

        what gets printed:
                            Count   Percentage
        Navigation          1724.0    5.835957
        Business             703.0    2.379743
        Travel              1059.0    3.584848
        Books               1488.0    5.037067
        Photo & Video       1855.0    6.279408
        Lifestyle           1133.0    3.835347
        Entertainment       1537.0    5.202938
        Finance              724.0    2.450831
        News                1392.0    4.712095
        Health & Fitness    1045.0    3.537456
        Games               2999.0   10.151992
        Food & Drink         917.0    3.104160
        Education            972.0    3.290342
        Medical              494.0    1.672252
        Social Networking   2734.0    9.254934
        Reference            511.0    1.729799
        Sports               882.0    2.985681
        Utilities           2026.0    6.858265
        Weather             1945.0    6.584070
        Productivity         960.0    3.249721
        Music               2058.0    6.966589
        Other                383.0    1.296503
        Total              29541.0  100.000000

    '''
    assert isinstance(mapping, dict), "mapping must be a dict"

    # converts each column to numeric values instead of str, set at ints
    x = x.apply(pd.to_numeric, errors='coerce').fillna(0).astype(int)

    # Sum each column
    column_sums = x.sum()

    # Compute total sum of all columns
    total_sum = column_sums.sum()

    # Calculate percentage of total for each column
    percentages = (column_sums / total_sum) * 100

    # Create DataFrame with sums and percentages
    categorical_df = pd.DataFrame({'Count': column_sums, 'Percentage': percentages})

    # Map the column names to their custom labels using the column_mapping
    categorical_df.index = categorical_df.index.map(mapping)

    # Append a total row at the bottom
    categorical_df.loc['Total'] = [total_sum, 100.0]  # Total sum, 100% of total

    return categorical_df

df = pd.read_excel("mobile_app_data_usage.xlsx")

categories = {'Q15_1'  : 'Navigation',
            'Q15_2'  : 'Business',
            'Q15_3'  : 'Catalogues',
            'Q15_4'  : 'Travel',
            'Q15_5'  : 'Books',
            'Q15_6'  : 'Photo & Video',
            'Q15_7'  : 'Lifestyle',
            'Q15_8'  : 'Entertainment',
            'Q15_9'  : 'Finance',
            'Q15_10' : 'News',
            'Q15_11' : 'Health & Fitness',
            'Q15_12' : 'Games',
            'Q15_13' : 'Food & Drink',
            'Q15_14' : 'Education',
            'Q15_15' : 'Medical',
            'Q15_16' : 'Social Networking',
            'Q15_17' : 'Reference',
            'Q15_18' : 'Sports',
            'Q15_19' : 'Utilities',
            'Q15_20' : 'Weather',
            'Q15_21' : 'Productivity',
            'Q15_22' : 'Music',
            'Q15_23' : 'Other'
        }

type_apps = [f'Q15_{i}' for i in range(1, 24)]

x = df[type_apps]

count = get_overall_apps(x,categories)

print(count)

print(type(count))