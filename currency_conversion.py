import pandas as pd 

def standardize_curreny(fName: str, columnName: str,  conversionChart: list, outputFName: str):
    '''
    Converts dataset with mixed currency into a dataset with standardized currency in USD
    
    Inputs:
    fName --  name of dataset file
    columnName -- name of column to convert currency in
    conversionChart -- chart of currency conversions to USD
    outputFName -- name of output file
    
    Outputs:
    Outputs data from 'fName' into a file called 'outputFName. Column with name 'columnName' will have financial data 
        extracted and converted to USD. 'Not Available' mean either they did put and answer for the column,
        didn't put an answer for the income currency column, or they put 'other' for the income currency column.
    
    '''
    #check inputs
    assert fName[-5:] == '.xlsx', 'Input filename must refer to an excel spreadsheet'
    assert outputFName[-5:] == '.xlsx', 'Output filename must refer to an excel spreadsheet'
    assert len(conversionChart) == 12, 'Input currency conversion list must have 12 entries:\n\
    1=Australian Dollar (AUD), 2=Brazilian Real (BRL), 3=British Pound (GBP)\n\
    , 4=Canadian Dollar (CAD), 5=Chinese Yuan Renminbi (CNY), 6=Euro\n\
    (EUR) (6), 7=Indian Rupee (INR), 8=Japanese Yen (JPY), 9=Mexican Peso (MXN),\n\
    10=Russian Ruble (RUB), 11=South Korean Won (KRW), 12=US Dollar (USD)'
    #convert file to dataframe
    dataset = pd.read_excel(fName)
    #convert needed columns to lists
    nonStandard = list(dataset[columnName])
    standard = [nonStandard[0]]
    parentCurrencies = list(dataset['Q28'])
    #loop through valid entries. Cross reference income currency with nonstandard currency to convert to USD
    for i in range(1,len(parentCurrencies)): 
        #Discude entries where either income currency or non standardized curreny has 'nan
        if (parentCurrencies[i] != 'nan')& (str(nonStandard[i]) != 'nan'):
            #Disclude non standardized currencies
            if (parentCurrencies[i] < 13) :
                #convert commas to periods for international numbers with decimals
                uncleaned = str(nonStandard[i]).replace(',','.')
                #intantiate cleaned empty string
                cleaned = ''
                #set numFound to false. This is needed to ignore the prescence of two numbers in a string
                numFound = False
                #set decimalFound to false. This is needed to ignore second decimals
                decFound = False
                for j in range(len(uncleaned)):
                    try: 
                        cleaned = cleaned + str(int(uncleaned[j]))
                        numFound = True
                    except ValueError:
                        #only accept decimal string
                        if uncleaned[j] == '.':
                            if decFound == True:
                                break
                            else:
                                cleaned = cleaned + '.'
                                decFound = True
                        elif numFound == True:
                            break    
                #ignore cleaned string if it is empty or just a decimal
                if (cleaned == '') | (cleaned == '.'):
                    standard.append('Not Available')
                else:
                    standard.append(float(cleaned)*conversionChart[parentCurrencies[i]-1])
            #Insert "Not available" if either income currency is not on list
            else:
                standard.append('Not Available')
        #Insert "Not available" if either income currency or non standardized currency is 'nan'
        else:
            standard.append('Not Available')
    #replace column in dataframe with standardized data
    dataset[columnName] = standard
    #output to excel file
    dataset.to_excel(outputFName)




conversionChart = [0.64, 0.17, 1.26, 0.7, 0.14, 1.05, 0.1, 0.0067, 0.05, 0.01, 0.000697, 1]
testConversionChart = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
       
dataset1 = 'mobile_app_user_dataset (1).xlsx'
column1 = 'Q12.1_1_TEXT'
output1 = 'mobile_app_user_dataset_standardCurrency.xlsx'
standardize_curreny(dataset1,column1, conversionChart, output1)

dataset2 = 'mobile_app_user_dataset_standardCurrency.xlsx'
output2 = 'mobile_app_user_dataset_standardCurrency2.xlsx'
column2 = 'Q12.2'
standardize_curreny(dataset2,column2, conversionChart, output2)



