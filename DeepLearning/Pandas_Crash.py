import numpy as np
import pandas as pd

labels=['a','b','c']

mylist=[10,20,30]

arr=np.array([10,20,30])

d={'a':10,'b':20,'c':30}

# print(pd.Series(mylist))

# print(pd.Series(arr,index=labels))

# print(pd.Series(d))

# series=pd.Series(d)
#
# print(pd.Series(d))
#
# print(series[0])
#
# print(series['a'])

# ----------------------------
# Working with Pandas

columns = ['W','X','Y','Z']
index = ['A','B','C','D','E']
from numpy.random import randint
np.random.seed(42)
data=randint(-100,100,(5,4))

# print(data)

df=pd.DataFrame(data,index,columns)

# print(df)

# print(df['W'])
#
# print(type(df['W']))
#
# print(df[['W','Z']])
#
# df['new']=df['W']+df['Z']
#
# print(df)
#
# df=df.drop('new',axis=1)
#
# print(df)

# Accessing on Rows

# print(df.loc['A'])
#
# print(df.loc[['A','B']])
#
# # incase you want to access it on index
#
# print(df.iloc[0])
#
# print(df.iloc[-1])
#
# print(df.iloc[0:3])
#
# print(df.loc[['A','C'],['W','Y']])

# print(df.iloc[0:2,0:2])


# Conditional operations on Dataframe

# print(df['X']>0)

# print(df[df['X']>0])

# print(df[df['X']>0]['W'])

# print((df['W']>0)|(df['Y']>1))

# print(df[(df['W']>0)|(df['Y']>1)])

# print(df[(df['W']>0)&(df['Y']>1)])
#
# df=df.reset_index()
# print(df)
#
# new_index_list=['CA','NY','WY','OR','CO']
# df['states']=new_index_list
# df = df.set_index('states')
#
# print(df)
