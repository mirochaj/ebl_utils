"""
Sano et al. 2015.
"""

name = 'Sano et al. (2015)'
year = 2015
experiment = 'DIRBE'
link = 'https://ui.adsabs.harvard.edu/abs/2015ApJ...811...77S/abstract'

style = \
{
 'color': 'm',
 'mfc': 'none',
 'marker': 'o',
 'label': name,
 'fmt': 'o',
}

bibtex = \
"""
@ARTICLE{2015ApJ...811...77S,
       author = {{Sano}, K. and {Kawara}, K. and {Matsuura}, S.
        and {Kataza}, H. and {Arai}, T. and {Matsuoka}, Y.},
        title = "{Derivation of a Large Isotopic Diffuse Sky Emission
            Component at 1.25 and 2.2um from the COBE/DIRBE Data}",
      journal = {\apj},
     keywords = {cosmic background radiation, dust, extinction,
        infrared: ISM, infrared: stars, scattering, zodiacal dust,
        Astrophysics - Astrophysics of Galaxies,
        Astrophysics - Cosmology and Nongalactic Astrophysics},
         year = 2015,
        month = oct,
       volume = {811},
       number = {2},
          eid = {77},
        pages = {77},
          doi = {10.1088/0004-637X/811/2/77},
archivePrefix = {arXiv},
       eprint = {1508.02806},
 primaryClass = {astro-ph.GA},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2015ApJ...811...77S},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}
"""

notes = \
"""
Notes:
- Final numbers quoted in first paragraph of Section 5.4.
"""

zodi = 'wright'

data = \
{
 'waves': [1.25, 2.20],
 'mean': [60.15, 27.68],
 'err': [16.14, 6.21],
}

def get_ebl_spectrum():
    return data['waves'], data['mean'], data['err']
