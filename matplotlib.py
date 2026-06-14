import pandas as pd
import matplotlib.pyplot as plt
file = r"C:\Users\RichardMusime\Downloads\KIREHE_FILTERED_DATA_2026-06-06 (5).xlsx"
df = pd.read_excel(file)
plt.scatter(df.index,df["Gender"])
plt.ylabel("GENDER")
plt.xlabel("INDEX")


plt.bar(df.index,df["CAT"].values)
plt.show()



#General Formula
#1. Library           -> import pandas as pd
#2. Path/File         -> variablefile = r"C:\users"
#3. Read              -> variable2 = pd.read_csv(variablefile)
#4. Display           -> print(variable2)