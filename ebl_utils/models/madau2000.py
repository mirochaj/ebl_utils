"""
Madau & Pozzetti (2000)
"""
name = 'Madau & Pozzetti (2000)'
year = 2000
link = 'https://ui.adsabs.harvard.edu/abs/2000MNRAS.312L...9M/abstract'
bibtex = \
"""
@ARTICLE{2000MNRAS.312L...9M,
       author = {{Madau}, Piero and {Pozzetti}, Lucia},
        title = "{Deep galaxy counts, extragalactic background light and the stellar baryon budget}",
      journal = {\mnras},
     keywords = {GALAXY: HALO, GALAXIES: EVOLUTION, COSMOLOGY: MISCELLANEOUS, DARK MATTER, DIFFUSE RADIATION, Astrophysics},
         year = 2000,
        month = feb,
       volume = {312},
       number = {2},
        pages = {L9-L15},
          doi = {10.1046/j.1365-8711.2000.03268.x},
archivePrefix = {arXiv},
       eprint = {astro-ph/9907315},
 primaryClass = {astro-ph},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2000MNRAS.312L...9M},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}
"""
notes = \
"""
Notes:
- Different magnitude range for each wavelength!
- Included systematic errors are ordered as +/-
- Units are all nW m^-2 sr^-1
"""

model_type = 'empirical'

data = \
{
 'waves': [0.36,0.45,0.67,0.81,1.1,1.6,2.2],
 'mean': [2.87,4.57,6.74,8.04,9.71,9.02,7.92],
 'err': [(0.58,0.42),(0.73,0.47),(1.25,0.94),(1.62,0.92),(3.00,1.90),
    (2.62,1.68),(2.04,1.21)],
 'mags': [(18,28),(15,29),(15,30.5),(12,29),(10,29),(10,29),(12,25.5)]
}

def get_ebl_spectrum():
    return data['waves'], data['mean'], data['err']
