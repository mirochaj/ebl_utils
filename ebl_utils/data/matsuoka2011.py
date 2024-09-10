"""
Matsuoka et al. 2011
"""

name = 'Matsuoka et al. (2011)'
year = 2011
experiment = 'Pioneer'
link = 'https://ui.adsabs.harvard.edu/abs/2011ApJ...736..119M/abstract'
style = \
{
 'color': 'b',
 'mfc': None,
 'marker': 'o',
 'label': name,
 'fmt': 'o',
}

bibtex = \
"""
@ARTICLE{2011ApJ...736..119M,
       author = {{Matsuoka}, Y. and {Ienaka}, N. and {Kawara}, K. and {Oyabu}, S.},
        title = "{Cosmic Optical Background: The View from Pioneer 10/11}",
      journal = {\apj},
     keywords = {cosmic background radiation, cosmology: observations, dark ages, reionization, first stars, dust, extinction, galaxies: evolution, infrared: ISM, Astrophysics - Cosmology and Nongalactic Astrophysics, Astrophysics - Astrophysics of Galaxies},
         year = 2011,
        month = aug,
       volume = {736},
       number = {2},
          eid = {119},
        pages = {119},
          doi = {10.1088/0004-637X/736/2/119},
archivePrefix = {arXiv},
       eprint = {1106.4413},
 primaryClass = {astro-ph.CO},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2011ApJ...736..119M},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}
"""

notes = \
"""
Notes:
- Units are all nW m^-2 sr^-1
- Data from Table 4
"""


data = \
{
 'waves': [0.44,0.64],
 'mean': [7.9,7.7],
 'err': [4,5.8],
}

def get_ebl_spectrum():
    return data['waves'], data['mean'], data['err']
