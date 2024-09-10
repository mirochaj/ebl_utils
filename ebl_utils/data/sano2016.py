"""
Sano et al. 2016.
"""

name = 'Sano et al. (2016)'
year = 2016
experiment = 'DIRBE+WISE'
link = 'https://ui.adsabs.harvard.edu/abs/2016ApJ...818...72S/abstract'
style = \
{
 'color': 'm',
 'mfc': None,
 'marker': 'o',
 'label': name,
 'fmt': 'o',
}

bibtex = \
"""
@ARTICLE{2016ApJ...818...72S,
       author = {{Sano}, K. and {Kawara}, K. and {Matsuura}, S.
       and {Kataza}, H. and {Arai}, T. and {Matsuoka}, Y.},
        title = "{Measurements of Diffuse Sky Emission Components
        in High Galactic Latitudes at 3.5 and 4.9 um Using Dirbe
        and WISE Data}",
      journal = {\apj},
     keywords = {cosmic background radiation, cosmology: observations,
     infrared: ISM, infrared: stars, ISM: general, zodiacal dust,
     Astrophysics - Astrophysics of Galaxies,
     Astrophysics - Cosmology and Nongalactic Astrophysics},
         year = 2016,
        month = feb,
       volume = {818},
       number = {1},
          eid = {72},
        pages = {72},
          doi = {10.3847/0004-637X/818/1/72},
archivePrefix = {arXiv},
       eprint = {1512.08072},
 primaryClass = {astro-ph.GA},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2016ApJ...818...72S},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}
"""

notes = \
"""
Notes:
- Final numbers quoted in Table 1, final columns for nu_i d_i, which is the
residual after subtraction of ZL and DGL.
- Errors quoted here are the total errors, which include systematics.
"""

zodi = 'kelsall'

data = \
{
 'waves': [3.5,4.9],
 'mean': [8.92,2.67],
 'err': [3.35,15.30],
}

def get_ebl_spectrum():
    return data['waves'], data['mean'], data['err']
