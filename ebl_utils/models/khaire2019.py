import os
import numpy as np

# Speed of light - [c] = cm/s
c = 29979245800.0
# 10^7 erg / J, so 1 W = 1 J / s = 10^7 erg/s
erg_per_s_per_W = 1e7
erg_per_s_per_nW = 1e7 / 1e9

_input = os.environ.get('HOME') + '/.ebl_utils'

name = 'Khaire & Srianand (2019)'
name_short = 'KS19'
link = 'https://ui.adsabs.harvard.edu/abs/2019MNRAS.484.4174K/abstract'
link_data = None
"""
@ARTICLE{2019MNRAS.484.4174K,
       author = {{Khaire}, Vikram and {Srianand}, Raghunathan},
        title = "{New synthesis models of consistent extragalactic background light over cosmic time}",
      journal = {\mnras},
     keywords = {galaxies: evolution, intergalactic medium, quasars: general, diffuse radiation, Astrophysics - Astrophysics of Galaxies, Astrophysics - Cosmology and Nongalactic Astrophysics},
         year = 2019,
        month = apr,
       volume = {484},
       number = {3},
        pages = {4174-4199},
          doi = {10.1093/mnras/stz174},
archivePrefix = {arXiv},
       eprint = {1801.09693},
 primaryClass = {astro-ph.GA},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2019MNRAS.484.4174K},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}
"""
notes = \
"""
- Data available at https://academic.oup.com/mnras/article/484/3/4174/5304986#sec10.
- Scroll to bottom to Supplementary Information to download file. Move it (`KS_2018_EBL`)
into $HOME/.ebl_utils
"""

def get_ebl_spectrum():
    """
    Return EBL spectrum from provided redshift.
    """

    x, y = np.loadtxt(f"{_input}/KS_2018_EBL/Fiducial_Q18/EBL_KS18_Q18_z_ 0.0.txt",
        unpack=1)
    print(f"! Loaded {_input}/KS_2018_EBL/Fiducial_Q18/EBL_KS18_Q18_z_ 0.0.txt")

    nu = c / (x * 1e-8)
    flux_si = nu * (y / erg_per_s_per_nW) * 1e4

    return x * 1e-4, flux_si, None
