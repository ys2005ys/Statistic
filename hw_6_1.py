from scipy import stats

x = 80
n = 256
s = 16
z_tabl = stats.norm.ppf(0.975)
print("Д_интервал", x - z_tabl * s / n ** 0.5, x + z_tabl * s / n ** 0.5, )
