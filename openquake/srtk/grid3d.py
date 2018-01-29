# =============================================================================
#
# Copyright (C) 2010-2017 GEM Foundation
#
# This file is part of the OpenQuake's Site Response Toolkit (OQ-SRTK)
#
# OQ-SRTK is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License,
# or (at your option) any later version.
#
# OQ-SRTK is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# with this download. If not, see <http://www.gnu.org/licenses/>
#
# Author: Valerio Poggi
#
# =============================================================================
"""

"""

import numpy as _np
from scipy.interpolate import griddata as _griddata

from openquake.srtk.sitedb import GEO_KEYS

# =============================================================================

class GeoGrid(object):
    """
    """

    # -------------------------------------------------------------------------

    def __init__(self, ):

        self.x = 0
        self.y = 0
        self.gx = 0
        self.gy = 0

    # -------------------------------------------------------------------------

    def set_limits(self, xlim, ylim, xnum, ynum):
        """
        """

        self.x = _np.linspace(xlim[0], xlim[1], xnum)
        self.y = _np.linspace(ylim[0], ylim[1], ynum)

    # -------------------------------------------------------------------------

    def compute_grid(self):
        """
        """

        self.gx, self.gy = _np.meshgrid(self.x, self.y)

    # -------------------------------------------------------------------------

    def compute_model(self, site_list, method='linear'):
        """
        """

        self.geo = {}

        for gk in GEO_KEYS:
            point = []
            model = []
            for site in site_list:
                point.append((site.head['x'], site.head['y']))
                model.append(site.mean.geo[gk][0])
            model = _np.array(model)

            self.geo[gk] = []

            for layer in model.T:
                data = _griddata(point,
                                 layer,
                                 (self.gx, self.gy),
                                 method=method, rescale=True)
                self.geo[gk].append(data)



