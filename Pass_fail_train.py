import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
df= pd.read_csv("Pass.csv")
print(df)
# df= pd.read_csv("Pass.csv", nrows=6) #nrows will read only those rows with index 0-6
'''print (df.columns) #shows name ofcolumns
print (df.head()) #first five rows
print(df.tail()) #last five rows
print(df.info()) #data typpes, memory usage, enteries
print(df.describe()) #describes data e,g mean, count,min etc
print(df.shape) #shows no.of rows and columns
print(df['Tution_Monthly']) #particular column
print(df[['Tution_Monthly','Pass_Or_Fail']]) #two columns
print(df.loc[2]) #shows particular row
print(df.iloc[1:4])  #shows selected rows
'''
X= df[['Self_Study_Daily','Tution_Monthly']]
Y= df['Pass_Or_Fail']
X_train, X_test, Y_train, Y_test= train_test_split(X,Y,test_size=0.4,random_state=42)
# print(X_test)
model = LogisticRegression()
model.fit(X_train, Y_train)
y_values= model.predict(X_test)
Acc= accuracy_score(Y_test, y_values)
print(Acc)