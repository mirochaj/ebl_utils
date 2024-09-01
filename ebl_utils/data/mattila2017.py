"""
Mattila et al. 2017.
"""

name = 'Mattila et al. (2017)'
year = 2024
experiment = 'ESO VLT/FORS'
link = 'https://ui.adsabs.harvard.edu/abs/2017MNRAS.470.2152M/abstract'
style = \
{
 'color': 'y',
 'mfc': None,
 'marker': '*',
}

bibtex = \
"""
@ARTICLE{2017MNRAS.470.2152M,
       author = {{Mattila}, K. and {V{\"a}is{\"a}nen}, P. and {Lehtinen}, K. and {von Appen-Schnur}, G. and {Leinert}, Ch.},
        title = "{Extragalactic background light: a measurement at 400 nm using dark cloud shadow - II. Spectroscopic separation of the dark cloud's light, and results$^{★}$}",
      journal = {\mnras},
     keywords = {ISM: clouds, dust, extinction, solar neighbourhood - diffuse radiation, cosmology: observations, Astrophysics - Astrophysics of Galaxies},
         year = 2017,
        month = sep,
       volume = {470},
       number = {2},
        pages = {2152-2169},
          doi = {10.1093/mnras/stx1296},
archivePrefix = {arXiv},
       eprint = {1705.10790},
 primaryClass = {astro-ph.GA},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2017MNRAS.470.2152M},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}
"""

notes = \
"""
Notes:
- Final numbers quoted in Table 1.
"""

zodi = None

data = \
{
 'waves': [0.4, 0.52],
 'mean': [11.6, 23.4],
 'err': [4.4, 0],
}

def get_ebl_spectrum():
    return data['waves'], data['mean'], data['err']
