import pandas as pd
import numpy as np

data= {
    "Name":['Zakir', 'Mariya', 'Irtiqa','Stranger'],
    "Roll NO": [11,26,9, np.nan],
    "City": ['Kupwara', 'Baramulla', 'Srinagar', np.nan]
}

df = pd.DataFrame(data)
#print("Original dataframe \n:",df)

missing_data = df.isnull()
print("MIssinf values : \n", missing_data)

df_dropped= df.dropna() #drops nan data
print("\nDataFrame after dropping mising data :", df_dropped)