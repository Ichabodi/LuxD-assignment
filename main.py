import pandas as pd
import numpy as np
data = pd.read_csv('Salary.csv')
print(data.info)
print(data.shape)
print(data.set_option('display.max_columns',23))
print(data.set_option('display.max_rows',23))
figure=pd.read_csv('data/Salary.cvs')
print(figure)