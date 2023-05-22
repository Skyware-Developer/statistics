import pandas as pd
import numpy as np
from scipy.stats import pearsonr

# Read the data from the text file
data = pd.read_csv('datos.txt', delimiter=';')

# Assuming you have a DataFrame named 'data' with columns 'TIEMPO' and 'PROM'
horas = data['HORAS']
prom = data['PROM']

# Calculate the correlation coefficient and p-value
correlation, p_value = pearsonr(horas, prom)

print("Correlation coefficient:", correlation)
print("P-value:", p_value)
