import pandas as pd
import numpy as np
#data=pd.read_csv('C:\\Users\\THINK PAD\\GreyAtom\\Python coding\\mall_data.txt')

def IQR_Val(array):
    a=np.nanpercentile(array,25)
    b=np.nanpercentile(array,75)
    iqr=b-a
    upper_bound=b+(1.5*iqr)
    lower_bound=a-(1.5*iqr)
    return([i for i in array if i>upper_bound or i<lower_bound])
    
def basic_exploration(df):
    #df.shape
    print("Rows:{}, Columns:{} ".format(str(df.shape[0]), str(df.shape[1])))
    print(df.info())
    Print("="*100)
    print("Descriptive stats", df.describe(include="object"))
    print("Non null columns and counts")
    nul_col=pd.DataFrame(df.isnull().sum()) #we are creating a subset of DF which gives index and sum
    nul_col.columns=["Counts"] #we are naming the column Counts
    # we want to return the column which has count >0
    #print(nul_col["Counts"]>0) This will give a boolean output with all the column value
    print(nul_col[nul_col['Counts']>0])
    #Select all the columns with numeric values
    df_num=df.select_dtypes(exclude='object')
    num_cols=df_num.columns
    for i in num_cols:
        #vals=data[i]
        print(i)
        print(IQR_Val(df[i]))

if __name__ == "__main__":
    data=pd.read_csv('mall_data.txt')
    basic_exploration(data)