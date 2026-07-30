import numpy as np

np.random.seed(42)
arr = np.random.randint(200,2000,size=30)

mask = arr > 1500

sales_upto_mark = arr[mask]

print(len(sales_upto_mark)/ 30 * 100)