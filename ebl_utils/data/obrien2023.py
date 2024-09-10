"""
O'Brien et al. 2023
"""

name = "O'Brien et al. 2023"

link = 'https://ui.adsabs.harvard.edu/abs/2023AJ....165..237O/abstract'
experiment = 'SKYSURF'
year = 2023

style = \
{
 'color': 'green',
 'mfc': None,
 'marker': 'p',
 'label': name,
 'fmt': 'o',
}


bibtex = \
"""
@ARTICLE{2023AJ....165..237O,
       author = {{O'Brien}, Rosalia and {Carleton}, Timothy and {Windhorst}, Rogier A. and {Jansen}, Rolf A. and {Carter}, Delondrae and {Tompkins}, Scott and {Caddy}, Sarah and {Cohen}, Seth H. and {Abate}, Haley and {Arendt}, Richard G. and {Berkheimer}, Jessica and {Calamida}, Annalisa and {Casertano}, Stefano and {Driver}, Simon P. and {Gelb}, Connor and {Goisman}, Zak and {Grogin}, Norman and {Henningsen}, Daniel and {Huckabee}, Isabela and {Kenyon}, Scott J. and {Koekemoer}, Anton M. and {Kramer}, Darby and {Mackenty}, John and {Robotham}, Aaron and {Sherman}, Steven},
        title = "{SKYSURF-4: Panchromatic Hubble Space Telescope All-Sky Surface-brightness Measurement Methods and Results}",
      journal = {\aj},
     keywords = {Zodiacal cloud, Hubble Space Telescope, Sky brightness, Cosmic background radiation, Optical astronomy, 1845, 761, 1462, 317, 1776, Astrophysics - Instrumentation and Methods for Astrophysics, Astrophysics - Cosmology and Nongalactic Astrophysics},
         year = 2023,
        month = jun,
       volume = {165},
       number = {6},
          eid = {237},
        pages = {237},
          doi = {10.3847/1538-3881/acccee},
archivePrefix = {arXiv},
       eprint = {2210.08010},
 primaryClass = {astro-ph.IM},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2023AJ....165..237O},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}
"""

data = \
{
 'waves': [1.25, 1.4, 1.6],
 'uplims': [22, 32, 25],
 'err': [0] * 3,
}

def get_ebl_spectrum():
    return data['waves'], data['uplims'], data['err']
