import numpy as np
from scipy import stats

x = [6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1]
X = np.mean(x)
std = np.std(x, ddof=1)
n = len(x)
alpha = 0.05

t = stats.t.ppf(1 - alpha/2, df=n-1)
print("Д_интервал:", X - t * std / n ** 0.5, X + t * std / n ** 0.5)
