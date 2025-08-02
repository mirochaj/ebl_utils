"""
Windhorst et al. 2023.
"""

name = 'Windhorst et al. (2023)'
year = 2023
experiment = 'JWST'
link = 'https://ui.adsabs.harvard.edu/abs/2023AJ....165...13W/abstract'
style = \
{
 'color': 'g',
 'mfc': 'none',
 'marker': 'v',
 'label': name,
 #'fmt': 'o',
}

bibtex = \
"""
@ARTICLE{2023AJ....165...13W,
       author = {{Windhorst}, Rogier A. and {Cohen}, Seth H. and {Jansen}, Rolf A. and {Summers}, Jake and {Tompkins}, Scott and {Conselice}, Christopher J. and {Driver}, Simon P. and {Yan}, Haojing and {Coe}, Dan and {Frye}, Brenda and {Grogin}, Norman and {Koekemoer}, Anton and {Marshall}, Madeline A. and {O'Brien}, Rosalia and {Pirzkal}, Nor and {Robotham}, Aaron and {Ryan}, Russell E. and {Willmer}, Christopher N.~A. and {Carleton}, Timothy and {Diego}, Jose M. and {Keel}, William C. and {Porto}, Paolo and {Redshaw}, Caleb and {Scheller}, Sydney and {Wilkins}, Stephen M. and {Willner}, S.~P. and {Zitrin}, Adi and {Adams}, Nathan J. and {Austin}, Duncan and {Arendt}, Richard G. and {Beacom}, John F. and {Bhatawdekar}, Rachana A. and {Bradley}, Larry D. and {Broadhurst}, Tom and {Cheng}, Cheng and {Civano}, Francesca and {Dai}, Liang and {Dole}, Herv{\'e} and {D'Silva}, Jordan C.~J. and {Duncan}, Kenneth J. and {Fazio}, Giovanni G. and {Ferrami}, Giovanni and {Ferreira}, Leonardo and {Finkelstein}, Steven L. and {Furtak}, Lukas J. and {Gim}, Hansung B. and {Griffiths}, Alex and {Hammel}, Heidi B. and {Harrington}, Kevin C. and {Hathi}, Nimish P. and {Holwerda}, Benne W. and {Honor}, Rachel and {Huang}, Jia-Sheng and {Hyun}, Minhee and {Im}, Myungshin and {Joshi}, Bhavin A. and {Kamieneski}, Patrick S. and {Kelly}, Patrick and {Larson}, Rebecca L. and {Li}, Juno and {Lim}, Jeremy and {Ma}, Zhiyuan and {Maksym}, Peter and {Manzoni}, Giorgio and {Meena}, Ashish Kumar and {Milam}, Stefanie N. and {Nonino}, Mario and {Pascale}, Massimo and {Petric}, Andreea and {Pierel}, Justin D.~R. and {Polletta}, Maria del Carmen and {R{\"o}ttgering}, Huub J.~A. and {Rutkowski}, Michael J. and {Smail}, Ian and {Straughn}, Amber N. and {Strolger}, Louis-Gregory and {Swirbul}, Andi and {Trussler}, James A.~A. and {Wang}, Lifan and {Welch}, Brian and {B. Wyithe}, J. Stuart and {Yun}, Min and {Zackrisson}, Erik and {Zhang}, Jiashuo and {Zhao}, Xiurui},
        title = "{JWST PEARLS. Prime Extragalactic Areas for Reionization and Lensing Science: Project Overview and First Results}",
      journal = {\aj},
     keywords = {James Webb Space Telescope, Zodiacal cloud, Star counts, Galaxy counts, Cosmic background radiation, 2291, 1845, 1568, 588, 317, Astrophysics - Cosmology and Nongalactic Astrophysics, Astrophysics - Astrophysics of Galaxies},
         year = 2023,
        month = jan,
       volume = {165},
       number = {1},
          eid = {13},
        pages = {13},
          doi = {10.3847/1538-3881/aca163},
archivePrefix = {arXiv},
       eprint = {2209.04119},
 primaryClass = {astro-ph.CO},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2023AJ....165...13W},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}
"""

notes = \
"""
Notes:
- Final numbers quoted in Table 3.
"""

zodi = None#'kelsall'

data = \
{
 'waves': [0.883, 1.020, 1.250, 1.650, 2.150, 3.540, 4.490],
 'mean': [10.45, 11.33, 11.21, 10.98, 9.735, 4.583, 3.053],
 'err': [0.04, 0.06, 0.04, 0.04, 0.10, 0.09, 0.05],
}

def get_ebl_spectrum():
    return data['waves'], data['mean'], data['err']
