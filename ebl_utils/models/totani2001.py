"""
Totani et al. 2001.
"""
name = 'Totani et al. (2001)'
year = 2001
link = 'https://ui.adsabs.harvard.edu/abs/2001ApJ...550L.137T/abstract'
bibtex = \
"""
@ARTICLE{2001ApJ...550L.137T,
       author = {{Totani}, Tomonori and {Yoshii}, Yuzuru and {Iwamuro}, Fumihide and {Maihara}, Toshinori and {Motohara}, Kentaro},
        title = "{Diffuse Extragalactic Background Light versus Deep Galaxy Counts in the Subaru Deep Field: Missing Light in the Universe?}",
      journal = {\apjl},
     keywords = {Cosmology: Observations, Cosmology: Diffuse Radiation, Galaxies: Evolution, Galaxies: Formation, Astrophysics},
         year = 2001,
        month = apr,
       volume = {550},
       number = {2},
        pages = {L137-L141},
          doi = {10.1086/319646},
archivePrefix = {arXiv},
       eprint = {astro-ph/0102328},
 primaryClass = {astro-ph},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2001ApJ...550L.137T},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}
"""
notes = \
"""
Notes:
- All data from Table 1.
- Includes 'best guess EBL', or what some call extrapolated IGL (eIGL) these days.
"""

model_type = 'empirical'
data_igl = \
{
 'waves': [0.3, 0.45, 0.61, 0.81, 1.25, 2.2],
 'mean': [2.7, 4.4, 6.0, 8.1, 10.9, 8.3],
 'err': [0.3, 0.4, 0.6, 0.8, 1.1, 0.8],
}

data_eigl = \
{
 'waves': [0.3, 0.45, 0.61, 0.81, 1.25, 2.2],
 'bound_lo': [2.9, 4.3, 5.8, 7.6, 10.1, 7.8],
 'bound_hi': [4.4, 7.9, 8.9, 10.9, 12.8, 10.2],
}

def get_ebl_spectrum(use_eigl=False):
    """
    If use_eigl==True, returns lower and upper bound on extrapolated IGL, rather
    than mean IGL with uncertainties.
    """
    if use_eigl:
        return data_eigl['waves'], data_eigl['bound_lo'], data_eigl['bound_hi']
    else:
        return data_igl['waves'], data_igl['mean'], data_igl['err']
