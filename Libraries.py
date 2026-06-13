#pandas help to read daa from files such as MS Excel , csv, sql, JSON.
#Matplotlib used to create static 


import pandas as pd
file = r"C:\Users\RichardMusime\Downloads\KIREHE_FILTERED_DATA_2026-06-06 (5).xlsx"
df = pd.read_excel(file)
print(df)  #will display all rows
print("*******************")
print(df.head()) #will display 5 top rows
print("*******************")
print(df.tail()) #will display 5 last rows