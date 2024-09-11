"""
Postman et al. 2024.
"""

name = 'Postman et al. (2024)'
year = 2024
experiment = 'New Horizons'
link = 'https://ui.adsabs.harvard.edu/abs/2024ApJ...972...95P/abstract'
style = \
{
 'color': 'orange',
 'mfc': None,
 'marker': 's',
 'label': name,
 'fmt': 'o',
}

bibtex = \
"""
@ARTICLE{2024ApJ...972...95P,
       author = {{Postman}, Marc and {Lauer}, Tod R. and {Parker}, Joel W. and {Spencer}, John R. and {Weaver}, Harold A. and {Shull}, J. Michael and {Stern}, S. Alan and {Brandt}, Pontus and {Conard}, Steven J. and {Gladstone}, G. Randall and {Lisse}, Carey M. and {Porter}, Simon B. and {Singer}, Kelsi N. and {Verbiscer}, Anne. J.},
        title = "{New Synoptic Observations of the Cosmic Optical Background with New Horizons}",
      journal = {\apj},
     keywords = {Galactic and extragalactic astronomy, 563, Astrophysics - Astrophysics of Galaxies, Astrophysics - Cosmology and Nongalactic Astrophysics},
         year = 2024,
        month = sep,
       volume = {972},
       number = {1},
          eid = {95},
        pages = {95},
          doi = {10.3847/1538-4357/ad5ffc},
archivePrefix = {arXiv},
       eprint = {2407.06273},
 primaryClass = {astro-ph.GA},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2024ApJ...972...95P},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}
"""

notes = \
"""
Notes:
- Final numbers quoted in abstract.
"""

zodi = None#'kelsall'

data = \
{
 'waves': [0.608],
 'mean': [11.16],
 'err': [1.65],
}

def get_ebl_spectrum():
    return data['waves'], data['mean'], data['err']
