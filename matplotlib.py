import pandas as pd
import matplotlib.pyplot as plt
file = r"C:\Users\RichardMusime\Downloads\KIREHE_FILTERED_DATA_2026-06-06 (5).xlsx"
df = pd.read_excel(file)
plt.scatter(df.index,df["Gender"])
plt.ylabel("GENDER")
plt.xlabel("INDEX")
plt.show()