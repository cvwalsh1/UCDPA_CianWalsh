# Cian Walsh, cvwalsh1@gmail.com

import csv

import pandas as pd

# Importing CSV file into a Pandas DataFrame
data=pd.read_csv("PPR-2020(2).csv", encoding='latin-1')
print(data)

# Retrieve data from online APIs
import requests
request=requests.get('https://www.kaggle.com/datajmcn/residential-property-prices-2020')
print(request.status_code)
print(request.text)


## code inserted to expand number of columns shown
desired_width = 50000
width = pd.set_option('display.width', desired_width)
size = pd.set_option('display.max_columns', 20)

df = pd.DataFrame(data)
price = ['Price (EUR)']
address_index = (df.sort_values(by=(price)).set_index('Address')['Price (EUR)']) # indexing
price_sort = (df.sort_values(by=['Price (EUR)'])) #sorting by price ascending
print(price_sort, width, size)
print(address_index, width, size)

# dropping duplicate dates

dup_data = data.drop_duplicates(subset=['Date of Sale (dd/mm/yyyy)'])
print(dup_data)

## to show data on missing rows

print(data.isnull().sum())



## as information for postcode would be in Sting format, we leave a commnet in order to deal with missing values
cleaned_data = data.fillna("information not currently available")
print(cleaned_data)

## missing data is then removed
print(cleaned_data.isnull().sum())

## grouping mean price by county
print(cleaned_data.groupby("County")["Price (EUR)"].mean())

## for loop

head = (cleaned_data.head(5))
for columnName in head: #for loop to gather column names
    print(columnName)

for k,v in head.iterrows(): # iterrows
    print(k)
    print(v)


## merging

data2=pd.read_csv('Property_Price_Register_Ireland-28-05-2021(3).csv', encoding='latin-1')

#importing second dataframe for merging
merge_data = pd.merge_ordered(cleaned_data, data2, on='Date of Sale (dd/mm/yyyy)', suffixes=('_data1','_data2'), fill_method='ffill')
print(merge_data)

import numpy as np
import numpy_financial as npf
# using numpy and custom function to find future value of an array

current_housing_value = np.array([300000,10000,-15000,20000,2000])
print("With an initial investment of 300000, this house will be worth:",npf.npv(rate=0.05, values= current_housing_value),"in four years")

# printing additional CSV file containing quarterly house prices nationally and regionally from 1997 - 2016
qtr_house_price = pd.read_csv('form_41h-price-sh-house-area-by-qtr_1.csv', encoding='latin-1')
print(qtr_house_price)


# Using Python Dictionary to print 1st row and corresponding column values as an array
reader = csv.DictReader(open('form_41h-price-sh-house-area-by-qtr_1.csv', encoding='latin-1'))
dict_row = next(reader)
print(dict_row)


import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt



qtr_house_price = pd.read_csv('form_41h-price-sh-house-area-by-qtr_1.csv',encoding='latin-1')
print(qtr_house_price.describe())
print(cleaned_data.describe(include='all')) # include 'all' selected here in order for every column to be counted

# Chart 1
plt.rcParams["figure.figsize"] = [16,9]
fig, ax = plt.subplots()
#figure(figsize=(15, 15), dpi=80)
ax.scatter(qtr_house_price["Year/Qrt"], qtr_house_price["National"])
ax.set_xlabel("Quarterly Year")
ax.set_ylabel("Price (EUR)")
plt.title("Average Second Hand Housing Prices in Ireland 1997-2016")
ax.xaxis.set_major_locator(plt.MaxNLocator(42))
plt.xticks(fontsize=7, rotation=90)
plt.show()

# Chart 2
plt.rcParams["figure.figsize"] = [16,9]
#figure(figsize=(15, 7), dpi=80)
plt.plot(qtr_house_price['Year/Qrt'], qtr_house_price['Waterford'], color='g', label='Waterford')
plt.plot(qtr_house_price['Year/Qrt'], qtr_house_price['Galway'], color='r', label='Galway')
plt.plot(qtr_house_price['Year/Qrt'], qtr_house_price['Limerick'], color='hotpink', label='Limerick')
plt.plot(qtr_house_price['Year/Qrt'], qtr_house_price['Dublin'], color='b', label='Dublin')
plt.xticks(fontsize=7, rotation=90)
plt.xlabel("Quarterly Year")
plt.ylabel("Housing Prices(EUR)")
plt.title("Selected Regional Second Hand Housing Prices per Quarter 1997-2016 (EUR)")
ax.xaxis.set_major_locator(plt.MaxNLocator(42))
#figure(num=1, figsize=(20, 20))
plt.legend()
plt.show()

# Chart 3
fig, ax = plt.subplots()
ax.plot(qtr_house_price['Year/Qrt'], qtr_house_price["Dublin"], color='b', label='Dublin')
ax.plot(qtr_house_price['Year/Qrt'], qtr_house_price["National"], color='g', label='National')
ax.set_xlabel('Quarterly Year')
ax.set_ylabel('Housing Prices (EUR)')
plt.xticks(fontsize=7, rotation=90)
plt.title("Dublin v National Second Hand Housing Prices per Quarter 1997-2016 (EUR)")
plt.legend()
ax.xaxis.set_major_locator(plt.MaxNLocator(42))
plt.text('2005Q3', 600000, r'$Dublin\ Peak$',fontdict={'size':8,'color':'b'})
plt.show()


# Insights into graphs:

# 1. As seen in graphh National Housing Prices in Ireland 1997-2016, Ireland's housing prices have fluctuated within this time period.
#    This scatter plot shows us that housing prices rapidly grew between 1997 until the 1st quarter of 2007. This was due to the growing 'Celtic Tiger' economy

# 2. According to line graph Selected Regional Housing Prices per Quarter 1997-2016 (EUR), housing prices in Dublin have remained higher than other regios.
#    House prices in Dublin never fell below prices in the selected other regions all throughout this 20 year data base

# 3. Between Q4 2009 until 2016, housing prices in the other regions continued to fall while Dublin prices rose.
#    This may have been due many rural people moving to the capital in order to find work, thereby increasing demand in housing in Dublin

# 4. According to Dublin v National Housing Prices per Quarter 1997-2016 (EUR), there was a significant difference in average housing prices between Dublin and the national average.
#    In Q3 2006, there was a difference of EUR200,000 between Dublin and national level housing prices. This would suggest great inequality between Dublin and the rest of the country at that time.

# 5. According to Dublin v National Housing Prices per Quarter 1997-2016 (EUR), housing prices within Dublin compared to the national average were very similar circa Q2 2010.
#    This was due to the impact that the housing crisis and Recession had on outwards migration (thereby lowering housing prices)