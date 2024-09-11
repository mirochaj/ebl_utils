import os
import numpy as np
from math import sqrt

try:
    from astropy.io import fits
    has_astropy = True
except IndexError:
    has_astropy = False

_input = os.environ.get('HOME') + '/.ebl_utils'

name = 'Driver et al. (2016)'
name_short = 'D16'
link = 'https://ui.adsabs.harvard.edu/abs/2016ApJ...827..108D/abstract'
link_data = 'https://content.cld.iop.org/journals/0004-637X/827/2/108/revision1/apjaa28a0_table3.tar.gz'
style = \
{
 'color': 'r',
 'edgecolor': 'r',
 'facecolor': 'none',
 'hatch': '\\',
 'label': name,
}

bibtex = \
"""
@ARTICLE{2016ApJ...827..108D,
       author = {{Driver}, Simon P. and {Andrews}, Stephen K. and {Davies}, Luke J. and {Robotham}, Aaron S.~G. and {Wright}, Angus H. and {Windhorst}, Rogier A. and {Cohen}, Seth and {Emig}, Kim and {Jansen}, Rolf A. and {Dunne}, Loretta},
        title = "{Measurements of Extragalactic Background Light from the Far UV to the Far IR from Deep Ground- and Space-based Galaxy Counts}",
      journal = {\apj},
     keywords = {cosmic background radiation, cosmological parameters, diffuse radiation, galaxies: statistics, zodiacal dust, Astrophysics - Astrophysics of Galaxies, Astrophysics - Cosmology and Nongalactic Astrophysics},
         year = 2016,
        month = aug,
       volume = {827},
       number = {2},
          eid = {108},
        pages = {108},
          doi = {10.3847/0004-637X/827/2/108},
archivePrefix = {arXiv},
       eprint = {1605.01523},
 primaryClass = {astro-ph.GA},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2016ApJ...827..108D},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}
"""
notes = \
"""
- Table 3 in FITS format is available here: https://content.cld.iop.org/journals/0004-637X/827/2/108/revision1/apjaa28a0_table3.tar.gz
"""

_cols = 'Wavelength', 'Best Fit', 'Median',	'Lower Limit', \
    'Zero-point Error', 'Fitting Error', 'Poisson Error', 'CV Error'


_data = {}
_data['FUV'] = 0.153, 1.45, 1.45, 1.36, 0.07, 0.00, 0.04, 0.16
_data['NUV'] = 0.225, 3.15, 3.14, 2.86, 0.15, 0.02, 0.05, 0.45
_data['u']   = 0.356, 4.03, 4.01, 3.41, 0.19, 0.04, 0.09, 0.46
_data['g']   = 0.470, 5.36, 5.34, 5.05, 0.25, 0.04, 0.05, 0.59
_data['r']   = 0.618, 7.47, 7.45, 7.29, 0.34, 0.05, 0.04, 0.69
_data['i']   = 0.749, 9.55, 9.52, 9.35, 0.44, 0.00, 0.05, 0.92
_data['z']   = 0.895, 10.15, 10.13, 9.98, 0.47, 0.03, 0.05, 0.96
_data['Y']   = 1.021, 10.44, 10.41, 10.23, 0.48, 0.00, 0.07, 1.05
_data['J']   = 1.252, 10.38, 10.35, 10.22, 0.48, 0.00, 0.05, 0.99
_data['H']   = 1.643, 10.12, 10.10, 9.99, 0.47, 0.01, 0.06, 1.01
_data['K']   = 2.150, 8.72, 8.71, 8.57, 0.40, 0.02, 0.04, 0.76
_data['IRAC1'] = 3.544, 5.17, 5.15, 5.03, 0.24, 0.03, 0.06, 0.43
_data['IRAC2'] = 4.487, 3.60, 3.59, 3.47, 0.17, 0.02, 0.05, 0.28
_data['IRAC4'] = 7.841, 2.45, 2.45, 1.49, 0.11, 0.77, 0.15, 0.08

_bands = _data.keys()
_waves = [_data[key][0] for key in _data.keys()]

_mean = []
_err = []
_low = []
for i, band in enumerate(_bands):
    _mean.append(_data[band][1])
    _err_ = [_data[band][j]**2 for j in range(4, 8)]
    _err.append(sqrt(sum(_err_)))
    _low.append(_data[band][3])

data = \
{
 'waves': _waves,
 'mean': _mean,
 'err': _err,
 'low': _low,
}

def get_ebl_spectrum(use_lower_limit=False):
    if use_lower_limit:
        return data['waves'], data['low'], data['err']
    else:
        return data['waves'], data['mean'], data['err']


def get_available_bands():
    assert has_astropy, "Must have astropy to use Driver+ 2016 data."
    if not os.path.exists(f'{_input}/Table3MRT.fits'):
        raise IOError(f'Must download and unpack file {link_data} -> $HOME/.ebl_utils')

    hdulist = fits.open(f'{_input}/Table3MRT.fits')
    data = hdulist[1].data
    all_bands = []
    for element in data:

        if element[1] not in all_bands:
            all_bands.append(element[1])

    return all_bands

def get_number_counts(band):
    """
    Return number counts for a given band in [number / mag / deg^2].

    .. note :: Counts in D16 are reported in unnits of (0.5 mag)^-1. Here
        we have multiplied by 2 so that units are simply mag^-1

    Options include: ugriz, JHK, W1, W2, and Hubble filters
    """
    assert has_astropy, "Must have astropy to use Driver+ 2016 data."
    if not os.path.exists(f'{_input}/Table3MRT.fits'):
        raise IOError(f'Must download and unpack file {link_data} -> $HOME/.ebl_utils')

    hdulist = fits.open(f'{_input}/Table3MRT.fits')
    data = hdulist[1].data
    telescopes = []

    mags = []
    cts = []
    err = []
    for element in data:
        if element[1] != band:
            continue

        _err = np.sqrt(element[4]**2 + (1e-2 * element[6] * element[3] * 2)**2)

        mags.append(element[2])
        cts.append(element[3] * 2)
        err.append(_err)

    return np.array(mags), np.array(cts), np.array(err)
