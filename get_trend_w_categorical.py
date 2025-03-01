import pandas as pd

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colormaps 

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
    assert isinstance(mapping, dict), "mapping must be a dict"

    # Apply the mapping for the trend column (e.g., gender)
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

    # Add a name to the index of the grouped DataFrame
    grouped.index.name = trend_name

    # Calculate the total row (sum of each column)
    total_row = grouped.sum().to_frame().T
    total_row.index = ["Total"]

    # Append the total row to the bottom of the DataFrame
    grouped = pd.concat([grouped, total_row])

    return grouped

df = pd.read_excel(r"D:\UCSD Stuff\WI25\ECE 143\project\App-Usage-Survey\mobile_app_user_dataset.xlsx")

type_apps = [f'Q15_{i}' for i in range(1, 24)]

trend = 'Q19'

index_map = {1 : 'American', 
             2 : 'Australian', 
             3 : 'Brazillian', 
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

trend_name = 'Nationality'

# trend = 'Q16'

# index_map = {1 : 'Male', 
#             2 : 'Female'}
# trend_name = 'Gender'

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
# print(result, type(result))

def plt_3d_bar():
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    xticks = result.index.values.tolist()[:-1]
    yticks = result.columns.values.tolist()[:-1]

    # fake data
    _x = np.arange(len(xticks))
    _y = np.arange(len(yticks))
    _xx, _yy = np.meshgrid(_x, _y)
    x, y = _xx.ravel(), _yy.ravel()

    top = []
    for i in range(len(xticks) * len(yticks)):
        top.append(result.iloc[i//len(yticks) , i % len(yticks)])

    bottom = np.zeros_like(top)
    width = depth = 0.75

    cls_ls = []
    # # To have different colors for each bar
    # for x_t in range(len(xticks)):
    #     cls = colormaps[list(colormaps)[x_t]].resampled(len(yticks))
    #     cls_ls_t = [cls(i) for i in range(len(yticks))]
    #     cls_ls.extend(cls_ls_t)

    # To have heatmap colors for each bar
    max_val = max(top)
    cls = colormaps['brg'].resampled(max_val)
    cls_ls = [cls(x) for x in top]

    ax.bar3d(x + 0.25, y + 0.25, bottom, width, depth, top, color=cls_ls, shade=True)
    ax.set_title('Plot')


    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    ax.set_xticks(_x+1, xticks)
    ax.set_yticks(_y+1, yticks)

    figManager = plt.get_current_fig_manager()
    figManager.window.showMaximized()

    plt.show()


def plot_heatmap():
    xticks = result.index.values.tolist()[:-1]
    yticks = result.columns.values.tolist()[:-1]

    data_tb = []
    for i in range(len(xticks)):
        dat = []
        for j in range(len(yticks)):
            dat.append(result.iloc[i , j])
        data_tb.append(dat)

    _x = np.arange(len(xticks))
    _y = np.arange(len(yticks))

    fig = plt.figure()
    ax = fig.add_subplot()


    ax.imshow( data_tb, cmap='autumn') 
    ax.set_yticks(_x, xticks)
    ax.set_xticks(_y, yticks, rotation=90, ha='right')

    for i in range(len(xticks)):
        for j in range(len(yticks)):
            text = ax.text(j, i, data_tb[i][j],
                                ha="center", va="center", color="w")

    ax.set_title( "2-D Heat Map" ) 
    plt.show() 


# Uncomment any one of these two functions to plot the relevant things 
plt_3d_bar()
# plot_heatmap()