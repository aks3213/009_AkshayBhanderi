import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from google.colab import drive
drive.mount('/content/drive')

data=pd.read_csv('/content/drive/My Drive/Colab Notebooks/ML-Lab/L1/mtcars.csv') 
d=pd.crosstab(index=data['cyl'],columns="count",dropna=True ) 
print(d)

