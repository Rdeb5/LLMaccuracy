import pandas as pd
import numpy as np


def llm_accuracy(xl):
    df = pd.read_excel(xl)

    df = np.array(df)
    df =df[3:]
    df = df.T
    df =df[len(df)-1]
    return df

    

print(llm_accuracy("C:\\Users\\Raunak\\OneDrive\\Documents\\Python Scripts\\CampoCosmetics-bad.xlsx"))