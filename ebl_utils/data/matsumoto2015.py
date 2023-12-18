
name = 'Matsuomoto et al. (2015)'
year = 2015
experiment = 'IRTS'

link = 'https://ui.adsabs.harvard.edu/abs/2015ApJ...807...57M/abstract'
bibtex = \
"""
@ARTICLE{2015ApJ...807...57M,
       author = {{Matsumoto}, T. and {Kim}, M.~G. and {Pyo}, J. and {Tsumura}, K.},
        title = "{Reanalysis of the Near-infrared Extragalactic Background Light Based on the IRTS Observations}",
      journal = {\apj},
     keywords = {methods: data analysis, cosmology: observations, infrared: diffuse background, Astrophysics - Astrophysics of Galaxies, Astrophysics - Cosmology and Nongalactic Astrophysics},
         year = 2015,
        month = jul,
       volume = {807},
       number = {1},
          eid = {57},
        pages = {57},
          doi = {10.1088/0004-637X/807/1/57},
archivePrefix = {arXiv},
       eprint = {1501.01359},
 primaryClass = {astro-ph.GA},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2015ApJ...807...57M},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}
"""

notes = \
"""
Notes:
- Also have results for Wright ZL model, just haven't transcribed.
"""

zodi = 'kelsall'
dgl = True

data = \
{
 'waves':[3.98,3.88,3.78,3.68,3.58,3.48,3.38,3.28,3.17,3.07,2.98,
    2.88,2.54,2.44,2.34,2.24,2.14,2.03,1.93,1.83,1.73,1.63,1.53,1.43],
 'mean':
  [16.0,15.8,12.9,10.6,14.0,12.7,12.9,11.6,15.1,18.5,17.1,19.0,22.3,20.5,
    23.6,29.2,35.4,38.,40.1,42.4,53.1,58.3,59.9,58.1],
 'err': [4,3.6,3.3,3.7,3.0,3.1,3.0,3.1,3.0,3.0,3.2,3.5,4.2,4.6,4.9,5.3,5.9,
    6.8,7.8,8.7,10.1,11.8,12.7,13.1],
}

def get_ebl_spectrum():
    return data['waves'], data['mean'], data['err']
