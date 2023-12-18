"""
Tsumura et al. 2013.
"""

name = 'Tsumura et al. (2013)'
link = 'https://ui.adsabs.harvard.edu/abs/2013PASJ...65..121T/abstract'
bibtex = \
"""
@ARTICLE{2013PASJ...65..121T,
       author = {{Tsumura}, Kohji and {Matsumoto}, Toshio and {Matsuura}, Shuji
       and {Sakon}, Itsuki and {Wada}, Takehiko},
        title = "{Low-Resolution Spectrum of the Extragalactic Background
        Light with the AKARI InfraRed Camera}",
      journal = {\pasj},
     keywords = {cosmology: diffuse radiation, cosmology: early universe, cosmology: observations, galaxies: intergalactic medium, interplanetary medium, Astrophysics - Cosmology and Nongalactic Astrophysics},
         year = 2013,
        month = dec,
       volume = {65},
          eid = {121},
        pages = {121},
          doi = {10.1093/pasj/65.6.121},
archivePrefix = {arXiv},
       eprint = {1307.6740},
 primaryClass = {astro-ph.CO},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2013PASJ...65..121T},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}
"""

notes = \
"""
Notes:
- Data not in Table from paper, not sure how we got electronic data. Just by request?
"""

zodi = 'kelsall'

data = \
{
 'waves': [1.8078,2.2547,2.4434,2.5882,2.7103,2.8178,2.9151,3.0045,3.0877,
    3.1659,3.2399,3.3102,3.3774,3.4418,3.5038,3.5637,3.6216,3.6777,3.7321,
    3.7851,3.8367,3.887, 3.9361,3.9842,4.0312,4.0772,4.1223,4.1666,4.21,
    4.2527,4.2947,4.3359,4.3765,4.4165,4.4558,4.4946,4.5329],
 'mean': [31.474,22.633,17.851,16.245,16.158,15.762,15.509,13.882,14.285,
    8.7716,9.5626,8.6702,12.376,11.277,10.998,14.859,13.156,7.1844,12.164,
    13,10.619,11.011,8.3831,10.37, 8.2433,5.012, 5.463, 7.57,7.8737,9.5695,
    10.164,6.0543,8.6696,5.4738,3.0293,7.0392,5.6856],
 'err': [6.5998,6.8059,2.9384,3.0729,2.9557,3.2313,2.9947,2.9112,2.3028,
   2.6992,2.8372,3.4739,3.3936,3.3499,3.3198,3.539,3.2647,3.3219,2.991,
   3.4501,2.9842,3.1995,3.1047,3.3646,3.3647,3.0309,2.9069,3.3932,3.087,
   3.358,2.8042,4.4106,3.2949,3.5149,3.0768,4.0574,4.0146]
}

def get_ebl_spectrum():
    return data['waves'], data['mean'], data['err']
