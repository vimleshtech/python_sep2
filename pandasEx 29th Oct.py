'''
pip install pandas 
pip install matplotlib
'''

import pandas as pd 
import matplotlib.pyplot as plt

df = pd.DataFrame()
print(df)


#create dataframe from list 
name=["raman","jatin","gaurav","ayush","monika"]
gender=["male","male","male","male","female"]
sal=[11111,2222,3333,4444,555555]
df = pd.DataFrame(data={'name':name,'gender':gender,'sal':sal})
print(df)

#show list of columns
print(df.columns)

#shwo top given rows 
print(df.head(2))

#show buttom given rows 
print(df.tail(3))

#show selected columns 
print(df['name'])


#print selected rows 
print(df[1:3])

##group by / summarize data 
print(df.groupby('gender').size())
print(df.groupby('gender').sum())
print(df.groupby('gender').max())
print(df.groupby('gender').min())

print(df.groupby('gender').max()['sal'])

##sort or order by
print(df.sort_values('name',ascending=True))
print(df.sort_values('name',ascending=False))

print(df.sort_values('sal',ascending=False))

##show stats 
#count
#std dev
#mean
#min
#25%
#50%
#75%
#max 

print(df.describe())

### reaed data from csv 
df = pd.read_csv(r'C:\Users\vkumar15\Desktop\Weekend\color-anova-example.csv')
print(df.shape)  # row,col

print(df.describe())


df.plot(kind='bar')
plt.show()




