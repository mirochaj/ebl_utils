"""
Watts et al. 2024.
"""

name = 'Watts et al. (2024)'
year = 2024
experiment = 'DIRBE+COBE'
link = 'https://ui.adsabs.harvard.edu/abs/2024arXiv240601491W/abstract'
style = \
{
 'color': 'm',
 'mfc': None,
 'marker': 's',
}

bibtex = \
"""
@ARTICLE{Watts2024,
       author = {{Watts}, D.~J. and {Galloway}, M. and {Gjerl{\o}w}, E. and {San},
       M. and {Aurlien}, R. and {Basyrov}, A. and {Brilenkov}, M. and {Eriksen},
       H.~K. and {Fuskeland}, U. and {Herman}, D. and {Ihle}, H.~T. and {Lunde},
       J.~G.~S. and {N{\ae}ss}, S.~K. and {Stutzer}, N. -O. and {Thommesen}, H.
       and {Wehus}, I.~K.},
        title = "{Cosmoglobe DR2. II. CIB monopole measurements from COBE-DIRBE through global Bayesian analysis}",
      journal = {arXiv e-prints},
     keywords = {Astrophysics - Cosmology and Nongalactic Astrophysics},
         year = 2024,
        month = jun,
          eid = {arXiv:2406.01491},
        pages = {arXiv:2406.01491},
          doi = {10.48550/arXiv.2406.01491},
archivePrefix = {arXiv},
       eprint = {2406.01491},
 primaryClass = {astro-ph.CO},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2024arXiv240601491W},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}

"""

notes = \
"""
Notes:
- Final numbers quoted in Table 1.
"""

zodi = None#'kelsall'

data = \
{
 'waves': [1.25, 2.2, 3.5, 4.9],
 'mean': [35, 10.2, 9.2, 8],
 'err': [6, 1.2, 1.3, 0],
}

def get_ebl_spectrum():
    return data['waves'], data['mean'], data['err']
