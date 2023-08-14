# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 14:54:29 2023

@author: vaish
"""

import pandas as pd

# file_name = pd.read_csv('file.csv')<___format of read_csv 

data = pd.read_csv('transaction2.csv')

data = pd.read_csv('transaction2.csv',sep=";")

# summary of the data

data.info()

costperitem = 11.73
sellingperitem = 21.11
NumberOfItemsPurchased= 6

costpertransaction = 11.73*6
sellingpertransaction = 21.11*6

#cost per transaction column summary
#variable=dataframe['column_name']

costperitem = data['CostPerItem']
NumberOfItemsPurchased=data['NumberOfItemsPurchased']
costpertransaction=costperitem*NumberOfItemsPurchased

#adding a new column in data
data['costpertransaction'] = costpertransaction

#salespertransaction
data['salespertransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

#profit calculation
data['profitpertransaction']= data['salespertransaction']-data['costpertransaction']

#markup calculation
data['markuppertransaction']=data['profitpertransaction']/data['costpertransaction']

#round marking up
roundmarkup=round(data['markuppertransaction'],2)

#combining data fields

my_date='Day'+'-'+'month''-''year'

#change column type (toconvert datatypes)

day =data['Day'].astype(str)
year=data['Year'].astype(str)
print(day.dtype)



my_date= day + '-'+'Month'+'-'+year
my_date= data['date']

data['date']=my_date

#using iloc to view specific columns/rows
data.iloc[0:3] #first three rows
data.iloc[-5:]#last five rows
data.iloc[5]#first five rows
data.iloc[:,2]#brimg 2 rows in every columns
data.iloc[4,2]#brings 4 rows 2 column

#using split to split the client_keyword field
#new_var=column.str.split('sep' , expand=true)

split_col=data['ClientKeywords'].str.split(',' , expand = True)

data['clientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthofContract'] = split_col[2]

#using the replace fumction
data['clientAge'] =data['clientAge'].str.replace('[','')
data['LengthofContract'] =data['LengthofContract'].str.replace(']','')

#using the lower function to change item to lowercase
data['ItemDescription'] =data['ItemDescription'].str.lower()

#how to merge files

#bringing in a new dataset
seasons = pd.read_csv('value_inc_seasons.csv', sep=';')

#merging of files; merge_df = pd.merge(df_old ,df_new, on = 'key')

data =pd.merge(data,seasons, on='Month')

#dropping columns

#df = df.drop('column name' , axis=1)

data=data.drop('ClientKeywords' , axis=1) 
data=data.drop(['Day','Year','Month'] , axis=1)

#Export into CSV
data.to_csv('valueinc_Cleaned.csv',index=False)


