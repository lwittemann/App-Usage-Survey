import pandas as pd 
import math


def convert_to_ranges(income: int)-> int:
    '''
    Converts a currency in USD to survey ranges
    
    Inputs:
    income -- income converted to USD
    
    Ouputs:
    int -- Which USD range income falls into
    '''
    if (income > 0) & (income <= 10000):
        return 1
    elif income <= 20000:
        return 2
    elif income <= 30000:
        return 3
    elif income <= 50000:
        return 4
    elif income <= 70000:
        return 5
    elif income <= 100000:
        return 6
    elif income <= 150000:
        return 7
    elif income <= 200000:
        return 8
    elif income <= 250000:
        return 9
    elif income <= 350000:
        return 10
    else: 
        return 11


def convert_column(newList: list, oldList: list, ranges: list, conversion: float)-> list:
    '''
    Converts a column of ranges in foriegn currency to ranges in USD
    
    Inputs:
    newList -- Standardized list of currency ranges in USD 
    oldList -- List containing ranges in foreign currency
    ranges -- List of middle values of ranges of foreign currencies
    conversion -- Currency conversion value for foriegn currency
    
    Outputs:
    newList -- Standardized list of currency ranges in USD 
    '''
    for i in range(1,len(oldList)):
        #ignore nan's
        if (math.isnan(oldList[i]) == False) & (oldList[i] < 11):
            #convert to USD
            standard = conversion*ranges[int(oldList[i])-1]
            #convert to USD range and add to list
            newList[i] = convert_to_ranges(standard)
    return newList
    


def standardize_income(fName: str, conversionChart: list, outputFName: str):
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
    #instantiate consolidated income list with USD
    incomesTotal = list(dataset['Q29.12'])
    for i in range(1,len(incomesTotal)):
        if math.isnan(incomesTotal[i]) | (incomesTotal[i] == 12):
            incomesTotal[i] = 'NotAvailable'
    #instantiate mean currency lists
    meanCurrencies = []
        #AUD
    meanCurrencies.append([5000, 15000, 30000, 50000, 70000, 90000, 125000, 175000, 250000, 375000])
        #BRL
    meanCurrencies.append([2500, 7500, 15000, 25000, 35000, 45000, 62500, 87500, 125000, 200000])
        #GBP
    meanCurrencies.append([2500, 7500, 12500, 17500, 25000, 35000, 45000, 62500, 87500, 125000])
        #CAD
    meanCurrencies.append([5000, 15000, 25000, 40000, 60000, 85000, 125000, 175000, 225000, 300000])
        #CNY
    meanCurrencies.append([2500, 7500, 15000, 25000, 35000, 45000, 62500, 87500, 125000, 200000])
        #EUR
    meanCurrencies.append([2500, 7500, 15000, 25000, 35000, 45000, 62500, 87500, 125000, 200000])
        #INR
    meanCurrencies.append([10000, 20000, 50000, 70000, 90000, 125000, 175000, 250000, 350000, 500000])
        #JPY
    meanCurrencies.append([500000, 1500000, 2500000, 3500000, 4500000, 5500000, 7000000, 10000000, 16000000, 25000000])
        #MXN
    meanCurrencies.append([12500, 37500, 62500, 87500, 112500, 137500, 175000, 250000, 400000, 625000])
        #RUB
    meanCurrencies.append([50000, 150000, 250000, 350000, 450000, 550000, 700000, 1000000, 1600000, 2500000])
        #KRW
    meanCurrencies.append([2500000, 7500000, 15000000, 25000000, 35000000, 45000000, 62500000, 87500000, 125000000, 200000000 ])
    #loop through columns for currency conversion
    for i in range(11):
        column = 'Q29.' + str(i+1)
        #print(i)
        incomesTotal = convert_column(incomesTotal, list(dataset[column]), meanCurrencies[i], conversionChart[i])
    #insert title in first row
    incomesTotal[0] = 'Standardized incomes in USD. Ranges: 0 - 10,000 (1) 10,001 - 20,000 (2) 20,001 - 30,000 (3) 30,001 - 50,000 (4) 50,001 - 70,000 (5) 70,001 - 100,000 (6) 100,001 - 150,000 (7) 150,001 - 200,000 (8) 200,001 - 250,000 (9) 250,001 - 350,000 (10) More than 350,000 (11)'
    #insert converted row into dataframe
    dataset.insert(141, 'Q29',incomesTotal)
    #output to excel file
    dataset.to_excel(outputFName)

    #compare invalids 
    #inv1 = 0
    #inv2 = 0
    #test = list(dataset['Q29.12'])
    #for i in range(1,len(incomesTotal)):
    #    if incomesTotal[i] == 'NotAvailable':
    #        inv2 += 1
    #    if math.isnan(test[i]):
    #        inv1 += 1
    #print('Invalids in orignal list :' + str(inv1))
    #print('Invalids in new list :' + str(inv2))

    
    
        

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
#standardize_curreny(dataset1,column1, conversionChart, output1)

dataset2 = 'mobile_app_user_dataset_standardCurrency.xlsx'
output2 = 'mobile_app_user_dataset_standardCurrency2.xlsx'
column2 = 'Q12.2'
#standardize_curreny(dataset2,column2, conversionChart, output2)

output3 = 'mobile_app_user_dataset_standardCurrency3.xlsx'
standardize_income(output2, conversionChart, output3)



