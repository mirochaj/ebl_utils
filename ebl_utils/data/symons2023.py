"""
Symons et al. 2023
"""

name = 'Symons et al. (2023)'
year = 2023
link = 'https://ui.adsabs.harvard.edu/abs/2023ApJ...945...45S/abstract'

bibtex = \
"""
@ARTICLE{2023ApJ...945...45S,
       author = {{Symons}, Teresa and {Zemcov}, Michael and
       {Cooray}, Asantha and {Lisse}, Carey and {Poppe}, Andrew R.},
        title = "{A Measurement of the Cosmic Optical Background and
        Diffuse Galactic Light Scaling from the R < 50 au
        New Horizons-LORRI Data}",
      journal = {\apj},
     keywords = {Cosmic background radiation, Diffuse radiation,
     Astrophysical dust processes, 317, 383, 99,
     Astrophysics - Cosmology and Nongalactic Astrophysics,
     Astrophysics - Earth and Planetary Astrophysics,
     Astrophysics - Instrumentation and Methods for Astrophysics},
         year = 2023,
        month = mar,
       volume = {945},
       number = {1},
          eid = {45},
        pages = {45},
          doi = {10.3847/1538-4357/acaa37},
archivePrefix = {arXiv},
       eprint = {2212.07449},
 primaryClass = {astro-ph.CO},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2023ApJ...945...45S},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}
"""

data = \
{
 'waves': [0.6],
 'mean': [21.98],
 'err': [1.23],
 'sys': [1.36],
}

def get_ebl_spectrum():
    return data['waves'], data['mean'], data['err']
