import pandas as pd
data = {
    "Name" : ["Zakir","Mariya","Irtiqa"],
    "Roll_No" : [11,26,9],
    "city" : ["Kupwara", "Baramulla", "Srinagar"]
}

df= pd.DataFrame(data)
# print(df)

df.to_csv('Trio.csv', index = False)#to.save is saving at mentioned extension an index False will not show index in csv file

df=pd.read_csv('Trio.csv')
print(df)
print(df.head(2)) #head(2) shows only first two rows
print(df.tail(2)) #tail(2) shows only last two rows
print(df.info()) #shows num of rows, colums,index, memory usage, datatypes 
print(df.describe()) #describes the data
print(df.min()) #shows minimum values
print(df.max())
print(df.columns) #shows nameof columns or we can say structure of dataset
print(df[['Name','city']]) #shows two columns, for accessing more than one colmn we use two sq braces
print(df.shape) #tells num of rows and columns or we can say size of dataset
print(df.loc[1]) #shows specific row
print(df.iloc[0:2]) #shows rows of index o and 1
print(df["Roll_No"]>10)#filter only ROllNos greater than 10 but gives output in boolean
print(df[(df["Roll_No"] > 10) & (df["Roll_No"] < 20)]) #follows condition

#https://youtu.be/qrMnoY8qBJM?si=t6d984-KXNQPuSu2