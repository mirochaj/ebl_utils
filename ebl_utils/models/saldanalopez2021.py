"""
Saldana-Lopez et al. 2021.
"""

import os
import numpy as np

_HOME = os.environ.get('HOME')
_input = _HOME + '/.ebl_utils'

name = 'Saldana-Lopez et al. (2021)'
year = 2021
experiment = None
link = 'https://ui.adsabs.harvard.edu/abs/2021MNRAS.507.5144S/abstract'
style = \
{
 'color': 'y',
 'facecolor': 'none',
 'hatch': '|',
 'label': name,
}

bibtex = \
"""
@ARTICLE{2021MNRAS.507.5144S,
       author = {{Saldana-Lopez}, Alberto and {Dom{\'\i}nguez}, Alberto and {P{\'e}rez-Gonz{\'a}lez}, Pablo G. and {Finke}, Justin and {Ajello}, Marco and {Primack}, Joel R. and {Paliya}, Vaidehi S. and {Desai}, Abhishek},
        title = "{An observational determination of the evolving extragalactic background light from the multiwavelength HST/CANDELS survey in the Fermi and CTA era}",
      journal = {\mnras},
     keywords = {galaxies: evolution, galaxies: formation, diffuse radiation, gamma-rays: diffuse background, infrared: diffuse background, Astrophysics - Cosmology and Nongalactic Astrophysics, Astrophysics - Astrophysics of Galaxies, Astrophysics - High Energy Astrophysical Phenomena},
         year = 2021,
        month = nov,
       volume = {507},
       number = {4},
        pages = {5144-5160},
          doi = {10.1093/mnras/stab2393},
archivePrefix = {arXiv},
       eprint = {2012.03035},
 primaryClass = {astro-ph.CO},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2021MNRAS.507.5144S},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}
"""

notes = \
"""
Notes:
- Download files from https://www.ucm.es/blazars/ebl and move to $HOME/.ebl_utils
"""

link_data = 'https://www.ucm.es/blazars/file/ld_saldana21_comoving', \
    'https://www.ucm.es/blazars/file/ebl_saldana21_comoving', \
    'https://www.ucm.es/blazars/file/eblerr_saldana21_comoving'

def download_data():
    from urllib.request import urlretrieve

    if not os.path.exists(f"{_input}/"):
        os.mkdir(f"{_HOME}/.ebl_utils")

    for link in link_data:
        urlretrieve(link,
                f"{_HOME}/.ebl_utils/{link[link.rfind('/'):]}.txt")


_z = np.array([0., 0.01, 0.03, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.8, 1.0,
    1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8, 3.0, 3.2, 3.4, 3.6, 3.8, 4.0,
    4.2, 4.4, 4.6, 4.8, 5.0, 5.2, 5.4, 5.6, 5.8, 6.])

def get_ebl_spectrum(z=0, ztol=0.05):
    """
    Return EBL spectrum from provided redshift.
    """
    iz = np.argmin(np.abs(z - _z))

    if abs(_z[iz] - z) > ztol:
        raise ValueError('Closest redshift (z={_z[iz]}) to requested (z={z}) violates tolerance `ztol`!')

    data = np.loadtxt(f"{_input}/ebl_saldana21_comoving.txt", unpack=1)
    print(f"! Loaded {_input}/ebl_saldana21_comoving.txt.dat")
    err = np.loadtxt(f"{_input}/eblerr_saldana21_comoving.txt", unpack=1)


    return data[0], data[1+iz], err[1+iz]
