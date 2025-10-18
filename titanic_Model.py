import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

#read data
df= pd.read_csv('titanic.csv') #reading csv file
# print(df)

#data cleaning
df=df.dropna(subset=['Age','Fare']) #removing any rows that have missing (NaN) values in the Age or Fare columns.
x=df[['Age','Fare']] #features for input
y=df['Survived'] #features for output

X_train, X_test, Y_train, Y_test= train_test_split(x,y,test_size=0.3, random_state=42) #random_state=25 ensures the split is the same every time (for reproducibility).
#  print(X_test)

#model
model=LogisticRegression()  #Logistic Regression is a machine learning algorithm used for binary classification
model.fit(X_train, Y_train)

#predict
y_values=model.predict(X_test)
Acc=accuracy_score(Y_test, y_values)
print(Acc)