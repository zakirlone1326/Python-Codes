# #giving letters elements in list

# import pandas as pd
# data= [10,20,30,40,50]
# series= pd.Series(data, index=['a','b','c','d','e'])
# print("pandas series \n" , series)


#  #creatng dataframe
# import pandas as pd
# data= {
#     "Name":['Zakir', 'Mariya', 'Irtiqa'],
#     "Roll NO": [11,26,9],
#     "City": ['Kupwara', 'Baramulla', 'Srinagar']
# }
# df = pd.DataFrame(data)
# print(df)
 
 #missing values in datframe and filling them
import pandas as pd
import numpy as np
data= {
    "Name":['Zakir', 'Mariya', 'Irtiqa','Stranger'],
    "Roll NO": [11,26,9, np.nan],
    "City": ['Kupwara', 'Baramulla', 'Srinagar', np.nan]
}
df = pd.DataFrame(data)
#print("Original DataFrame : ", df)

df_filled = df.fillna({"Roll NO":23, "City": 'Jungle'}) #filled roll no and city to stranger
print("After updating values :" , df_filled)

 #removing dup[licates]
import pandas as pd
import numpy as np
data= {
    "Name":['Zakir', 'Mariya', 'Zakir',],
    "Roll NO": [11,26,11],
    "City": ['Kupwara', 'Baramulla', 'Kupwara']
}
df = pd.DataFrame(data)
#print("Original DataFrame : ", df)

df_duplicates = df.drop_duplicates()
print("After removing dups values :" , df_duplicates)