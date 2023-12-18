"""
Matsuomoto et al. 2011, ApJ, 742, 124
"""
name = 'Matsuomoto et al. (2011)'
year = 2011
experiment = 'akari'

link = 'https://ui.adsabs.harvard.edu/abs/2011ApJ...742..124M/abstract'
bibtex = \
"""
@ARTICLE{2011ApJ...742..124M,
       author = {{Matsumoto}, T. and {Seo}, H.~J. and {Jeong}, W. -S. and {Lee}, H.~M. and {Matsuura}, S. and {Matsuhara}, H. and {Oyabu}, S. and {Pyo}, J. and {Wada}, T.},
        title = "{AKARI Observation of the Fluctuation of the Near-infrared Background}",
      journal = {\apj},
     keywords = {cosmology: observations, diffuse radiation, early universe, Astrophysics - Cosmology and Nongalactic Astrophysics},
         year = 2011,
        month = dec,
       volume = {742},
       number = {2},
          eid = {124},
        pages = {124},
          doi = {10.1088/0004-637X/742/2/124},
archivePrefix = {arXiv},
       eprint = {1010.0491},
 primaryClass = {astro-ph.CO},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2011ApJ...742..124M},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}
"""

"""
Notes:
- From Table 2.
- Only including "sky fluctuation" column.
- Units are all nW m^-2 sr^-1
- Angular scales are arcseconds.

"""

data = \
{
 'waves': [2.4, 3.2, 4.1],
 'scales': [111, 125, 143, 167, 200, 250, 333],
 'mean': [[0.35, 0.33, 0.26, 0.20, 0.093, 0.29, 0.29],
          [0.16, 0.16, 0.13, 0.079, 0.082, 0.13, 0.13],
          [0.078, 0.048, 0.040, 0.039, 0.031, 0.047, 0.029]],
 'err':  [[0.082, 0.043, 0.035, 0.050, 0.023, 0.045, 0.12],
          [0.035, 0.041, 0.017, 0.034, 0.016, 0.029, 0.046],
          [0.02, 0.011, 0.0075, 0.019, 0.007, 0.010, 0.012]],
 'maglim': [22.9, 23.2, 23.8],
}

scale_units = 'arcsec'

def get_ebl_anisotropies():
    return data['waves'], data['scales'], data['mean'], data['err']
