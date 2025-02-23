import pandas as pd

def get_trend_w_categorical(x, categories, trend_name, index_map, mapping):
    '''
    takes in column to get trend (ie gender, Q16), and categorical columns (ie Q15_i). counts up the total categories
    per trend and gives them as pd.dataframe

    params:
        x: (pd.series) column you want to see a trend for
        categories: (pd.dataframe) columns to be checked against
        trend_name: (str) name of trend to be index name
        index_map: (dict) mapping of numerical values to str representation
        mapping: (dict) mapping for column name to categorical name

    returns:
        pd.dataframe with trend and categorical columns to see how trend could affect choice in categories

    example usage:

        df = pd.read_excel("mobile_app_data_usage.xlsx")

        type_apps = [f'Q15_{i}' for i in range(1, 24) if i != 3]

        trend = 'Q16'

        index_map = {1 : 'Male', 
                    2 : 'Female'}
        trend_name = 'Gender'

        categories = {
                    'Q15_1'  : 'Navigation',
                    'Q15_2'  : 'Business',
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

        x = df[trend]

        cats = df[type_apps]

        result = get_trend_w_categorical(x,cats,trend_name,index_map, categories)

        print(result, type(result))

        what gets printed:

                            Navigation  Business  Travel  Books  ...  Weather  Productivity  Music  Other
            Gender                                       ...                                     
            Female         693       226     490    762  ...     1008           380   1030    172
            Male          1022       472     566    719  ...      922           574   1015    209

            [2 rows x 22 columns] <class 'pandas.core.frame.DataFrame'>
    '''
    assert isinstance(trend_name, str), "trend_name must be a str"
    assert isinstance(index_map, dict), "index_map must be a dict"
    assert isinstance(mapping, dict), "mapping must be a dict"

    # Apply the mapping for the trend column (e.g., gender)
    x = x.map(index_map)

    # Rename the columns in categories based on the mapping
    categories_renamed = categories.rename(columns=mapping)

    # Convert categories to numeric values (this step depends on your data structure)
    categories_renamed = categories_renamed.apply(pd.to_numeric, errors='coerce').fillna(0).astype(int)

    # Remove rows in x where the value is NaN or missing
    mask = x.notna()  # True for non-NaN values in x
    x_filtered = x[mask]
    categories_filtered = categories_renamed[mask.values]

    # Group by the values in x (Male and Female) and sum the categories for each group
    grouped = categories_filtered.groupby(x_filtered).sum()

    # Add a name to the index of the grouped DataFrame
    grouped.index.name = trend_name

    return grouped

# df = pd.read_excel("mobile_app_data_usage.xlsx")

# type_apps = [f'Q15_{i}' for i in range(1, 24) if i != 3]

# trend = 'Q16'

# index_map = {1 : 'Male', 
#              2 : 'Female'}
# trend_name = 'Gender'

# categories = {
#             'Q15_1'  : 'Navigation',
#             'Q15_2'  : 'Business',
#             'Q15_4'  : 'Travel',
#             'Q15_5'  : 'Books',
#             'Q15_6'  : 'Photo & Video',
#             'Q15_7'  : 'Lifestyle',
#             'Q15_8'  : 'Entertainment',
#             'Q15_9'  : 'Finance',
#             'Q15_10' : 'News',
#             'Q15_11' : 'Health & Fitness',
#             'Q15_12' : 'Games',
#             'Q15_13' : 'Food & Drink',
#             'Q15_14' : 'Education',
#             'Q15_15' : 'Medical',
#             'Q15_16' : 'Social Networking',
#             'Q15_17' : 'Reference',
#             'Q15_18' : 'Sports',
#             'Q15_19' : 'Utilities',
#             'Q15_20' : 'Weather',
#             'Q15_21' : 'Productivity',
#             'Q15_22' : 'Music',
#             'Q15_23' : 'Other'
#         }

# x = df[trend]

# cats = df[type_apps]

# result = get_trend_w_categorical(x,cats,trend_name,index_map, categories)

# print(result, type(result))

