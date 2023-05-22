import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Read the data from the text file
data = pd.read_csv('datos.txt', delimiter=';')

# Step 2: Extract the "VMATRI" column
vamtri_data = data["VMATRI"]

# Step 3: Visualize the data using a histogram or density plot
plt.hist(vamtri_data, bins='auto', density=True)
plt.xlabel('VMATRI')
plt.ylabel('Density')
plt.show()

# Step 4: Overlay different probability distributions
distributions = [stats.norm, stats.expon, stats.gamma, stats.t, stats.chi2, stats.f]

for dist in distributions:
    params = dist.fit(vamtri_data)
    x = np.linspace(min(vamtri_data), max(vamtri_data), 100)
    pdf = dist.pdf(x, *params)
    plt.plot(x, pdf, label=dist.name)

plt.legend()
plt.xlabel('VMATRI')
plt.ylabel('Density')
plt.show()

# Step 5: Perform goodness-of-fit tests and evaluate p-values
best_fit = None
best_pvalue = 0

for dist in distributions:
    params = dist.fit(vamtri_data)
    _, pvalue = stats.kstest(vamtri_data, dist.name, args=params)

    if pvalue > best_pvalue:
        best_fit = dist
        best_pvalue = pvalue

print("Best-fitting distribution:", best_fit.name)
print("P-value:", best_pvalue)
