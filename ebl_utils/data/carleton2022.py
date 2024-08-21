"""
Carleton et al. (2022)
"""

link = 'https://ui.adsabs.harvard.edu/abs/2022AJ....164..170C/abstract'
name = 'Carleton et al. (2022)'
year = 2022
experiment = 'SKYSURF'

style = \
{
 'color': 'green',
 'mfc': 'none',
 'marker': 'p',
}

bibtex = \
"""
@ARTICLE{2022AJ....164..170C,
       author = {{Carleton}, Timothy and {Windhorst}, Rogier A.
       and {O'Brien}, Rosalia and {Cohen}, Seth H.
       and {Carter}, Delondrae and {Jansen}, Rolf
       and {Tompkins}, Scott and {Arendt}, Richard G. and {Caddy}, Sarah
       and {Grogin}, Norman and {Kenyon}, Scott J. and {Koekemoer}, Anton
       and {MacKenty}, John and {Casertano}, Stefano and {Davies}, Luke J.~M.
       and {Driver}, Simon P. and {Dwek}, Eli
       and {Kashlinsky}, Alexander and {Miles}, Nathan and {Pirzkal}, Nor
       and {Robotham}, Aaron and {Ryan}, Russell and {Abate}, Haley
       and {Andras-Letanovszky}, Hanga and {Berkheimer}, Jessica
       and {Goisman}, Zak and {Henningsen}, Daniel and {Kramer}, Darby
       and {Rogers}, Ci'mone and {Swirbul}, Andi},
        title = "{SKYSURF: Constraints on Zodiacal Light and
        Extragalactic Background Light through Panchromatic
        HST All-sky Surface-brightness Measurements: II.
        First Limits on Diffuse Light at 1.25, 1.4, and 1.6 {\ensuremath{\mu}}m}",
      journal = {\aj},
     keywords = {Star counts, Galaxy counts, Zodiacal cloud,
     Cosmic background radiation, 1568, 588, 1845, 317,
     Astrophysics - Cosmology and Nongalactic Astrophysics},
         year = 2022,
        month = nov,
       volume = {164},
       number = {5},
          eid = {170},
        pages = {170},
          doi = {10.3847/1538-3881/ac8d02},
archivePrefix = {arXiv},
       eprint = {2205.06347},
 primaryClass = {astro-ph.CO},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2022AJ....164..170C},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}
"""

data = \
{
 'waves': [1.25, 1.4, 1.6],
 'uplims': [29, 40, 29],
 'err': [0] * 3,
}

def get_ebl_spectrum():
    return data['waves'], data['uplims'], data['err']
