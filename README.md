# App Usage Survey
 Final Project for ECE 143 - WI25 - Group 15. Analysis of app usage dataset to ascertain trends. Could find use cases such as marketing or psychological research.

 Files:
 
    currency_conversion:
        Author: 
            Luke Wittemann
        Purpose and Usage:
            Converts currency and currency ranges in multiple different foriegn currencies into USD. Functions standardize_income and standardize_currency are provided with the dataset filename, a chart of currency conversions to USD, and an output filename. For standardize_currency, a column from which to standarize is also provided and this column is replaced and a new file is created. For standardize_income, the standardized income ranges in USD are inserted as a new column

    get_income_w_categories:
        Author: 
            Trevor Kam
        Purpose and Usage:
            Takes in standardized currency column from Luke Whittemann's currency conversion and gets corresponding categorical responses from the survey to graph against and see trends

    get_overall_apps:
        Author: 
            Trevor Kam
        Purpose and Usage:
            Takes in all the app categories and sums up the totals for each category to analyze overall downloaded apps.

    get_trend_w_categorical:
        Author: 
            Trevor Kam
        Purpose and Usage:
            Takes in any single datasheet column and gets corresponding categorical responses from the survey to graph against and see trends

    personality_vs_app_downloading:
        Author: 
            Zihao Yang
        Purpose and Usage: 
        (1)Transformed the original 7-point scale into three categories (disagree, neutral, agree) to simplify personality data.
        (2)Calculated the average download rates for 23 different app categories based on these personality groups.
        (3)Created heatmaps to compare how different personality traits correlate with various app download behaviors. 
        

    ProjectPlotting: 
        Author(s):
            Lingxiao Li, Mayank Kumar, Zihao Yang
        Purpose and Usage:
            Simply a Jupyter notebook containg the visualization scripts(2d_plotting, 3D_Plots, and PlotHeatmaps)

    2d_plotting:
        Author: 
            Lingxiao Li
        Purpose and Usage:

    3D_Plots:
        Author: 
            Mayank Kumar
        Purpose and Usage:
            Simple python notebook to try out a 3Dplot of the given data 

    PlotHeatmaps:
        Author: 
            Mayank Kumar, Zihao Yang
        Purpose and Usage: 
        Heatmaps serve as a visualization of display the aggregated mean download rates of various app categories across different personality groups.

Third Party Modules:

    1. Pandas

    2. Matplotlib



