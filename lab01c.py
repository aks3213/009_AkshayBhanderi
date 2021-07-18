import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from google.colab import drive
drive.mount('/content/drive')

data=pd.read_csv('/content/drive/MyDrive/Study/ML/Lab1/mtcars.csv')
d=pd.crosstab(index=data['cyl'],columns="count",dropna=True)
print(d)

print(data.info())

print("Total Null Data:",data.isnull().sum())

plt.hist(data['mpg'],bins=5)
plt.show()

plt.scatter(data['mpg'],data['wt'])
plt.show()

df=pd.DataFrame(data,columns=['gear'])
print("Count How Many values:\n",df['gear'].value_counts())