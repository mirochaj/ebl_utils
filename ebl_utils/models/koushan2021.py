"""
Kousha et al. (2021)
"""
name = 'Koushan et al. (2021)'
year = 2021
link = 'https://ui.adsabs.harvard.edu/abs/2021MNRAS.503.2033K/abstract'
bibtex = \
"""
@ARTICLE{2021MNRAS.503.2033K,
       author = {{Koushan}, Soheil and {Driver}, Simon P. and {Bellstedt}, Sabine and {Davies}, Luke J. and {Robotham}, Aaron S.~G. and {Lagos}, Claudia del P. and {Hashemizadeh}, Abdolhosein and {Obreschkow}, Danail and {Thorne}, Jessica E. and {Bremer}, Malcolm and {Holwerda}, B.~W. and {Hopkins}, Andrew M. and {Jarvis}, Matt J. and {Siudek}, Malgorzata and {Windhorst}, Rogier A.},
        title = "{GAMA/DEVILS: constraining the cosmic star formation history from improved measurements of the 0.3-2.2 {\ensuremath{\mu}}m extragalactic background light}",
      journal = {\mnras},
     keywords = {methods: data analysis, galaxies: evolution, galaxies: statistics, cosmology: cosmic background radiation, cosmological parameters, diffuse radiation, Astrophysics - Cosmology and Nongalactic Astrophysics, Astrophysics - Astrophysics of Galaxies},
         year = 2021,
        month = may,
       volume = {503},
       number = {2},
        pages = {2033-2052},
          doi = {10.1093/mnras/stab540},
archivePrefix = {arXiv},
       eprint = {2102.12323},
 primaryClass = {astro-ph.CO},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2021MNRAS.503.2033K},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}
"""
notes = \
"""
Notes:
- IGL drawn from Table 3.
- Transcribed errors are reported as percent, hence the conversion as a
separate step below.
- EBL reported in nW m^-2 sr^-1
- This is essentially an update from Driver+ 2016.
"""

model_type = 'empirical'

data = \
{
 'bands': list('ugrizYJHK'),
 'waves': [0.3577, 0.4744, 0.6312, 0.7584, 0.8833, 1.0224, 1.2546, 1.6477, 2.1549],
 'mean': [4.13, 5.76, 8.11, 9.94, 10.71, 11.58, 11.22, 11.17, 9.42],
 'err_rel': [6.87, 4.02, 4.08, 4.44, 5.20, 4.52, 4.92, 4.73, 5.21],
}

data['err'] = []
for i, wave in enumerate(data['waves']):
    data['err'].append(data['err_rel'][i] * 1e-2 * data['mean'][i])


def get_ebl_spectrum():
    return data['waves'], data['mean'], data['err']
