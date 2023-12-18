"""
Matsuura et al. 2017.
"""

name = 'Matsuura et al. (2017)'
year = 2017

experiment = 'CIBER'

link = 'https://ui.adsabs.harvard.edu/abs/2017ApJ...839....7M/abstract'

bibtex = \
"""
@ARTICLE{2017ApJ...839....7M,
       author = {{Matsuura}, Shuji and {Arai}, Toshiaki and {Bock}, James J.
        and {Cooray}, Asantha and {Korngut}, Phillip M. and {Kim},
        Min Gyu and {Lee}, Hyung Mok and {Lee}, Dae Hee and {Levenson},
        Louis R. and {Matsumoto}, Toshio and {Onishi}, Yosuke and {Shirahata},
        Mai and {Tsumura}, Kohji and {Wada}, Takehiko and {Zemcov}, Michael},
        title = "{New Spectral Evidence of an Unaccounted Component of the
            Near-infrared Extragalactic Background Light from the CIBER}",
      journal = {\apj},
     keywords = {cosmology: observations, dark ages, reionization,
        first stars, diffuse radiation, infrared: diffuse background,
        infrared: general, zodiacal dust,
        Astrophysics - Astrophysics of Galaxies,
        Astrophysics - Cosmology and Nongalactic Astrophysics},
         year = 2017,
        month = apr,
       volume = {839},
       number = {1},
          eid = {7},
        pages = {7},
          doi = {10.3847/1538-4357/aa6843},
archivePrefix = {arXiv},
       eprint = {1704.07166},
 primaryClass = {astro-ph.GA},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2017ApJ...839....7M},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}
"""

fields = ['ELAIS-N1', 'NEP', 'Bootes-A', 'Bootes-B']

notes = \
"""
Notes:
- Assumes Kelsall model.
- Included systematic errors are ordered as +/-
- Units are all nW m^-2 sr^-1
"""

zodi = 'kelsall'

data_nominal = \
{
 'waves': [0.8, 0.83, 0.86, 0.9, 0.95, 1.00, 1.05, 1.11, 1.18, 1.25,
    1.33, 1.42, 1.51, 1.60, 1.70],
 'mean': [41.1, 30.6, 23.1, 29.6, 34.2, 31.2, 31.3, 36.7, 32.5,
    38.7, 41.7, 42.7, 37.8, 41.1, 35.7],
 'err': [4.8, 4.4, 4.2, 3.2, 3.3, 3.5, 3.2, 2.8, 2.2, 2.1, 2.0, 2.3, 2.9,
    3.3, 2.8],
 'sys': [(15.7, 15.3), (15.8, 14.7), (15.1, 14.4), (14.1, 14.0), (13.8, 13.7),
    (13.4, 13.5), (13.1, 12.9), (12.6, 12.6), (13.3, 12.2), (12.6, 11.6),
    (11.3, 10.9), (11.7, 10.3), (16.4, 10.1), (15.6, 9.3), (13.3, 8.4)]
}

data_minimum = \
{
 'waves': [1.05, 1.11, 1.18, 1.25, 1.33, 1.42, 1.51, 1.60, 1.70],
 'mean': [7.9, 15.4, 12.9, 20.1, 24.3, 28.7, 23.8, 27.1, 24.8],
 'err': [3.8, 3.4, 3.2, 3.1, 2.8, 3.0, 3.5, 3.8, 3.0],
 'sys': [(1.5, -0.6), (1.1, 0.8), (4.0, 0.9), (3.9, 1.1), (2.7, 1.3),
    (4.1, 1.5), (9.9, 1.4), (10, 1.5), (7.2, 1.4)]
}

final = (1.4, 42.7, (11.9, 10.6))

def get_ebl_spectrum(use_nominal=False, use_final=True):
    """
    Retrieve measured EBL spectrum.

    If use_final==True, returns only the single data point quoted in the text
    and abstract.


    """
    data = data_nominal if use_nominal else data_minimum

    return data['waves'], data['mean'], data['err']
