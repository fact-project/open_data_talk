import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('build/runs.csv')


plt.hist(df.zenith, weights=df.ontime / 3600, bins=20, range=[0, 30])
plt.xlabel(r'$\theta / \si{\degree}$')
plt.ylabel(r'$\text{Observation Time} / \si{\hour}$')

plt.tight_layout(pad=0)
plt.savefig('build/plots/zenith.pdf')
