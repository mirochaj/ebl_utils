"""
Matsumoto et al. 2005
"""

name = 'Matsuomoto et al. (2005)'
year = 2005
experiment = 'IRTS'
link = 'https://ui.adsabs.harvard.edu/abs/2005ApJ...626...31M/abstract'
style = \
{
 'color': 'pink',
 'mfc': 'none',
 'marker': '<',
}

bibtex = \
"""
@ARTICLE{2005ApJ...626...31M,
       author = {{Matsumoto}, T. and {Matsuura}, S. and {Murakami}, H. and
       {Tanaka}, M. and {Freund}, M. and {Lim}, M. and {Cohen}, M. and
       {Kawada}, M. and {Noda}, M.},
        title = "{Infrared Telescope in Space Observations of the
        Near-Infrared Extragalactic Background Light}",
      journal = {\apj},
     keywords = {Cosmology: Diffuse Radiation, Infrared: General, Astrophysics},
         year = 2005,
        month = jun,
       volume = {626},
       number = {1},
        pages = {31-43},
          doi = {10.1086/429383},
archivePrefix = {arXiv},
       eprint = {astro-ph/0411593},
 primaryClass = {astro-ph},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2005ApJ...626...31M},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}
"""

notes = \
"""
Notes:
- Included errors are the total errors (see Table 1)
- Units are all nW m^-2 sr^-1
"""

zodi = 'kelsall'
dgl = None

data = \
{
 'waves':[3.98,3.88,3.78,3.68,3.58,3.48,3.38,3.28,3.17,3.07,2.98,
    2.88,2.54,2.44,2.34,2.24,2.14,2.03,1.93,1.83,1.73,1.63,1.53,1.43],
 'mean':
  [15.5,15.3,13.5,13.1,15.5,14.4,14.6,13.6,16.4,19.7,18.6,19.5,23.7,22.7,
    24.4,29.7,35.4,39.2,43.2,51.0,58.7,65.9,71.3,70.1],
 'err': [3.9,3.6,3.3,3.7,3.0,3.0,3.0,3.0,2.9,3.0,3.2,3.5,4.2,4.5,4.8,5.3,
    6.0,7.0,7.9,8.8,10.3,11.9,12.8,13.2],
}

def get_ebl_spectrum():
    return data['waves'], data['mean'], data['err']
