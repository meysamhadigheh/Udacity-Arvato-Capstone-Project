import time

import pandas as pd
import pip
from py import process

print(pd.__version__)

#attributes = pd.read_excel('DIAS Attributes - Values 2017.xlsx', index_col = 1)
#customers = pd.read_csv('data/customers.csv')
#customers_clean = customers.drop(['PRODUCT_GROUP', 'CUSTOMER_GROUP', 'ONLINE_PURCHASE'], axis = 1, inplace = True)
#customers_clean = customers.drop(['CUSTOMER_GROUP'], axis = 1, inplace = True)

# azdias = pd.read_csv('../../data/Term2/capstone/arvato_data/Udacity_AZDIAS_052018.csv', sep=';')
# customers = pd.read_csv('../../data/Term2/capstone/arvato_data/Udacity_CUSTOMERS_052018.csv', sep=';')


df = pd.read_csv('data/my.csv')
print(df.head())
print("df..................................")
df.drop('Place',axis=1,inplace=True)
print(df.head())
print("df drop..................................")
# customers = pd.read_csv('data/customers.csv', sep=';')
customers = pd.read_csv('data/customers.csv', sep=';', error_bad_lines=False, index_col=False, dtype='unicode')
customers_clean = customers.drop(['PRODUCT_GROUP', 'CUSTOMER_GROUP', 'ONLINE_PURCHASE'], axis = 1, inplace = True)
print(customers.head())
print("customers head ..................................")
print(customers)
print("customers ..................................")
import datetime
print(datetime.datetime.now().time())
chunksize = 10 ** 6
with pd.read_csv('data/azdias.csv', sep=';', error_bad_lines=False, index_col=False, dtype='unicode', chunksize=chunksize) as reader:
    for chunk in reader:
        process(chunk)
print(datetime.datetime.now().time())
print("azdias chunk ..................................")
print(datetime.datetime.now().time())

azdias = pd.read_csv('data/azdias.csv', sep=';', error_bad_lines=False, index_col=False, dtype='unicode')
print(azdias)
print(datetime.datetime.now().time())

print("azdias ..................................")
print(azdias.head())
print("azdias head..................................")
attributes = pd.read_excel('data/attributes.xlsx', index_col = 1, engine='openpyxl')
print(attributes)
print("attributes ..................................")

print(attributes.head())
print("attributes head ..................................")


