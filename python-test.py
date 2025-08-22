import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("housing.csv")
print(df.head())



sns.pairplot(df)
plt.show()

print(plt.show())

