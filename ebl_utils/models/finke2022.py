import os
import numpy as np

_input = os.environ.get('HOME') + '/.ebl_utils'

name = 'Finke et al. (2022)'
name_short = 'F22'
link = 'https://ui.adsabs.harvard.edu/abs/2022ApJ...941...33F/abstract'
link_data = 'https://zenodo.org/records/7023073/files/EBL_intensity.tar.gz?download=1'
bibtex = \
"""
@ARTICLE{2022ApJ...941...33F,
       author = {{Finke}, Justin D. and {Ajello}, Marco and {Dom{\'\i}nguez}, Alberto and {Desai}, Abhishek and {Hartmann}, Dieter H. and {Paliya}, Vaidehi S. and {Saldana-Lopez}, Alberto},
        title = "{Modeling the Extragalactic Background Light and the Cosmic Star Formation History}",
      journal = {\apj},
     keywords = {Diffuse radiation, Gamma-rays, Gamma-ray astronomy, Gamma-ray sources, Blazars, 383, 637, 628, 633, 164, Astrophysics - Astrophysics of Galaxies},
         year = 2022,
        month = dec,
       volume = {941},
       number = {1},
          eid = {33},
        pages = {33},
          doi = {10.3847/1538-4357/ac9843},
archivePrefix = {arXiv},
       eprint = {2210.01157},
 primaryClass = {astro-ph.GA},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2022ApJ...941...33F},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}
"""
notes = \
"""
- Data available on Zenodo: https://zenodo.org/records/7023073
"""

def download_finke2022_models():
    if not os.path.exists(f"{_HOME}/.ebl_utils"):
        os.mkdir(f"{_HOME}/.ebl_utils")

    urlretrieve(link_data,
                f"{_HOME}/.ebl_utils/EBL_intensity.tar.gz")

    zip_ref = zipfile.ZipFile(f"{_HOME}/.ebl_utils/{_file_spherex}", 'r')
    zip_ref.extractall(f"{_HOME}/spherex/")
    zip_ref.close()

_z = np.arange(0, 7.02, 0.02)

def get_ebl_spectrum(z=0):
    """
    Return EBL spectrum from provided redshift.
    """
    iz = np.argmin(np.abs(z - _z))
    x, y = np.loadtxt(f"{_input}/EBL_intensity_total_z{_z[iz]:.2f}.dat", unpack=1)
    print(f"! Loaded {_input}/EBL_intensity_total_z{_z[iz]:.2f}.dat")

    return x * 1e-4, y, None
