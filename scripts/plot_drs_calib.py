import matplotlib.pyplot as plt
from astropy.io import fits
import numpy as np

pixel = 102

f = fits.open('drscalib.fits.gz')

raw_data = f[1].data['Data'][0]
calibrated = f[1].data['DataCalibrated'][0]

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

ax1.plot(np.arange(300) / 2, raw_data[pixel * 300:(pixel + 1) * 300])
ax1.set_ylabel(r'$\mathrm{ADC\,Counts}')

ax2.plot(np.arange(300) / 2, calibrated[pixel * 300:(pixel + 1) * 300])
ax2.set_ylabel(r'$V / \si{\milli\volt}$')
ax2.set_xlabel(r'$t / \si{\nano\second}$')

fig.tight_layout(pad=0)
fig.savefig('build/plots/drs_calib.pdf')
