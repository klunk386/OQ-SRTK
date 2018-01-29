from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

import numpy as np
import matplotlib.pyplot as plt

from openquake.srtk import sitedb
from openquake.srtk import grid3d

H = ['hl','vp','vs','dn','qp','qs']

sites = []

sites.append(sitedb.Site1D(1,0,0))
sites[0].read_model('data/site01.mod', header=H, skip=1, delimiter=' ')


sites.append(sitedb.Site1D(2,10,0))
sites[1].read_model('data/site02.mod', header=H, skip=1, delimiter=' ')


sites.append(sitedb.Site1D(3,0,10))
sites[2].read_model('data/site03.mod', header=H, skip=1, delimiter=' ')


gg = grid3d.GeoGrid()
gg.set_limits([0, 10], [0, 10], 50, 50)
gg.compute_grid()
gg.compute_model(sites)

#plt.pcolor(gg.gx, gg.gy, gg.geo['vs'])
#plt.show(block=False)


fig = plt.figure()
ax = fig.gca(projection='3d')

Htot = 0
for H in gg.geo['hl']:

    Htot += H
    # Plot the surface.
    ax.plot_surface(gg.gx, gg.gy, Htot,
                           linewidth=1, antialiased=False)
    #ax.plot_wireframe(gg.gx, gg.gy, Htot,color=np.random.rand(1,3),
    #                       linewidth=1, antialiased=False)

plt.gca().invert_zaxis()
#ax.zaxis.set_major_locator(LinearLocator(10))
#ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

plt.show(block=False)