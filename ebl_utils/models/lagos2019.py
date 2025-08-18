"""
Lagos et al. (2019)
"""
name = 'Lagos et al. (2019)'
year = 2019
link = 'https://ui.adsabs.harvard.edu/abs/2019MNRAS.489.4196L/abstract'
style = \
{
 'color': 'c',
 #'edgecolor': 'c',
 #'facecolor': 'none',
 #'marker': 'o',
 'ls': ':',
 'label': name,
}
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
- Used plotdigitizer to determine from Fig. 9 in Koushan+ 2021.
"""

model_type = 'semi-analytic'

waves = [0.1529610587988013,0.23094965464773778,0.356843908634806,
    0.472021519270448,0.6181734879715435,0.750638541208555,
    0.8925136527470028,1.016634122446549,1.252193595618071,
    1.646288190013089,2.150282135454358,3.3813311636874426,
    3.5189442843997223,4.449677048817908,4.637676004966552,5.64866022493932]


flux = [1.9156282910852342,2.5592289414585094,2.8986227049288753,
    4.266465238261362,6.094457788282436,7.206444370794972,
    8.032085739440767,8.506694056489081,8.690395141630303,
    8.224562024436976,7.114973359303452,3.8181927688697623,
    3.5873017598804684,2.353994122697241,2.2161104217183056,
    1.5428501572800486]


data = \
{
 'waves': waves,
 'mean': flux,
 'err': None,
}


def get_ebl_spectrum():
    return data['waves'], data['mean'], data['err']
