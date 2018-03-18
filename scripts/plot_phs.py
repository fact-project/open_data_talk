import json
import gzip
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from fact.instrument.camera import get_pixel_coords
import numpy as np

plt.rcParams['text.color'] = 'white'
plt.rcParams['axes.edgecolor'] = 'lightgray'
plt.rcParams['axes.labelcolor'] = 'lightgray'
plt.rcParams['xtick.color'] = 'lightgray'
plt.rcParams['ytick.color'] = 'lightgray'



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

ax.set_facecolor('k')
fig.set_facecolor('k')

ax.scatter(
    points[:, 0],
    points[:, 1],
    points[:, 2],
    s=1,
    alpha=0.3,
    lw=0,
    color='cyan'
)

ax.view_init(30, 30)


mask = (points[:, 2] > 35) & (points[:, 2] < 65)
image, xedges, yedges = np.histogram2d(
    points[mask, 0],
    points[mask, 1],
    range=[[-200, 200], [-200, 200]],
    bins=50,
)

x_center = 0.5 * (xedges[:-1] + xedges[1:])
y_center = 0.5 * (yedges[:-1] + yedges[1:])


ax.contourf(
    x_center,
    y_center,
    image.T,
    offset=0,
    cmap='inferno',
)

ax.set_xlim(-200, 200)
ax.set_ylim(-200, 200)
ax.set_zlim(0, 75)
ax.set_xlabel(r'$x / \si{\milli\meter}$')
ax.set_ylabel(r'$y / \si{\milli\meter}$')
ax.set_zlabel(r'$t / \si{\nano\second}$')

fig.savefig('build/plots/phs.pdf', facecolor=fig.get_facecolor())
