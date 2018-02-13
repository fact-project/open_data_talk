import json
import gzip
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from fact.instrument.camera import get_pixel_coords
import numpy as np



def get_n_photons(event):
    return sum(len(p) for p in event['PhotonArrivals_500ps'])


f = gzip.open('build/phs.jsonl.gz')
for i in range(323):
    f.readline()


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')

x, y = get_pixel_coords()


event = json.loads(f.readline())

n_photons = get_n_photons(event)
points = np.empty((n_photons, 3))

i = 0
for chid, photons in enumerate(event['PhotonArrivals_500ps']):
    for photon in photons:
        points[i] = x[chid], y[chid], photon / 2
        i += 1

ax.scatter(points[:, 0], points[:, 1], points[:, 2], s=3, alpha=0.2, lw=0)

ax.view_init(30, 30)

ax.set_xlim(-200, 200)
ax.set_ylim(-200, 200)
ax.set_xlabel(r'$x / \si{\milli\meter}$')
ax.set_ylabel(r'$y / \si{\milli\meter}$')
ax.set_zlabel(r'$t / \si{\nano\second}$')

fig.savefig('build/plots/phs.pdf')
