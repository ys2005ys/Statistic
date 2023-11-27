import numpy as np
import scipy.stats as stats

h_daughters = [175, 167, 154, 174, 178, 148, 160, 167, 169, 170]
h_mothers = [178, 165, 165, 173, 168, 155, 160, 164, 178, 175]

mean_daughters = np.mean(h_daughters)
mean_mothers = np.mean(h_mothers)
delta = mean_mothers - mean_daughters

D_daughters = np.var(h_daughters, ddof=1)
D_mothers = np.var(h_mothers, ddof=1)
D = (D_daughters + D_mothers)/2

n_daughters = len(h_daughters)
n_mothers = len(h_mothers)

se = np.sqrt((D / n_daughters) + (D / n_mothers))

df = n_daughters + n_mothers - 2

t = stats.t.ppf(0.975, df)

print("Доверительный интервал для разности среднего роста родителей и детей:")
print(delta - t * se, delta + t * se)
