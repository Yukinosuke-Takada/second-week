import pandas as pd

ecom = pd.read_csv("Ecommerce Purchases")

# head

print(ecom.head())

# how many rows and columns are there

print(ecom.info())

# how many people have purched during AM and PM

print(ecom['AM or PM'].value_counts())

# what is the avearage purchase price?

print(ecom['Purchase Price'].mean())

print(ecom['Purchase Price'].max())

print(ecom['Purchase Price'].min())

# how many peoplw have English as their choice

print(ecom[ecom['Language'] == 'en'].count())
print(ecom[ecom['Language'] == 'en'].count()['Language'])

print(ecom[ecom['Job'] == 'Lawyer'].info())

# what are the 5 most common jobs

print(ecom['Job'].value_counts().head(20))

# whos the one purfklhas[fouwygk'bawlg

print(ecom[ecom['Lot'] == '90 WT'])

# what is his email

print(ecom[ecom['Credit Card'] == 4926535242672853]['Email'])

# hoe many people uses american express

print(ecom[(ecom['CC Provider'] == 'American Express') & (ecom['Purchase Price'] > 95)].count())

# how many people will card expire in 2025

print(sum(ecom['CC Exp Date'].apply(lambda x: x[3:]) == '25'))

# how to split 

print(ecom['Email'].apply(lambda x: x.split('@')[1]))