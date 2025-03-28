import pandas as pd

def get_trend_w_categorical(x, categories, trend_name, index_map, mapping = None, need_mapping = True):
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

        type_apps = [f'Q15_{i}' for i in range(1, 24)]

        trend = 'Q16'

        index_map = {1 : 'Male', 
                    2 : 'Female'}
        trend_name = 'Gender'

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

        x = df[trend]

        cats = df[type_apps]

        result = get_trend_w_categorical(x,cats,trend_name,index_map, categories)

        print(result, type(result))

        what gets printed:

                            Navigation  Business  Travel  Books  Photo & Video  ...  Weather  Productivity  Music  Other  Count
                Female         693       226     490    762            941  ...     1008           380   1030    172   2721
                Male          1022       472     566    719            903  ...      922           574   1015    209   2645
                Total         1715       698    1056   1481           1844  ...     1930           954   2045    381   5366

            [3 rows x 23 columns] <class 'pandas.core.frame.DataFrame'>
    '''
    assert isinstance(trend_name, str), "trend_name must be a str"
    assert isinstance(index_map, dict), "index_map must be a dict"
    if mapping is not None:
        assert isinstance(mapping, dict), "mapping must be a dict"

    # Apply the mapping for the trend column if needed (e.g., gender)
    if need_mapping:
        x = x.map(index_map)

    # Rename the columns in categories based on the mapping
    categories_renamed = categories.rename(columns=mapping)

    # Convert categories to numeric values (this step depends on your data structure)
    categories_renamed = categories_renamed.apply(pd.to_numeric, errors='coerce').fillna(0).astype(int)

    # Remove rows in x where the value is NaN or missing
    mask = x.notna()
    x_filtered = x[mask]
    categories_filtered = categories_renamed[mask.values]

    # Group by the values in x (e.g., Male and Female) and sum the categories for each group
    grouped = categories_filtered.groupby(x_filtered).sum()

    # Add count of each index_map
    count_series = x_filtered.value_counts().rename("Count")

    # Merge count column into the grouped DataFrame
    grouped = grouped.merge(count_series, left_index=True, right_index=True)

    # Calculate the total row (sum of each column)
    total_row = grouped.sum().to_frame().T
    total_row.index = ["Total"]

    # Append the total row to the bottom of the DataFrame
    grouped = pd.concat([grouped, total_row])

    # Add a name to the index of the grouped DataFrame
    grouped.index.name = trend_name

    # Remove entry directly under column if mapping not needed
    if not need_mapping:
        grouped = grouped[grouped["Count"] > 1]

    return grouped

df = pd.read_excel("app_dataset.xlsx")

type_apps = [f'Q15_{i}' for i in range(1, 24)]

trend = 'Q19'

index_map = {1 : 'American', 
             2 : 'Australian', 
             3 : 'Brazilian', 
             4 : 'British', 
             5 : 'Canadian', 
             6 : 'Chinese', 
             7 : 'French', 
             8 : 'German',
             9 : 'Indian', 
            10 : 'Italian', 
            11 : 'Japanese', 
            12 : 'Mexican', 
            13 : 'Russian', 
            14 : 'South Korean', 
            15 : 'Spanish', 
            16 : 'Other'}

index_map = {0 : '0 - 10,000',
             1 : '10,001 - 20,000', 
             2 : '20,001 - 30,000', 
             3 : '30,001 - 50,000', 
             4 : '50,001 - 70,000', 
             5 : '70,001 - 100,000', 
             6 : '100,001 - 150,000', 
             7 : '150,001 - 200,000', 
             8 : '200,001 - 250,000',
             9 : '250,001 - 300,000', 
            10 : '300,001 - 350,000', 
            11 : 'More than 350,001'}

# values = range(1,100,1)

# index_map = {}
# for i in values:
#     index_map[i] = i

trend_name = 'Income Ranges'


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

x = df[trend]

cats = df[type_apps]

result = get_trend_w_categorical(x,cats,trend_name,index_map, categories, True)

print(result)


