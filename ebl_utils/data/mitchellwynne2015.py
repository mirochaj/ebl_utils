"""
Mitchell-Wynne et al. 2015

Supplementary Table 1

Values are in ell^2 C_ell / 2pi
"""

name = 'Mitchell-Wynne et al. (2015)'
link = 'https://ui.adsabs.harvard.edu/abs/2015NatCo...6.7945M/abstract'
bibtex = \
"""
@ARTICLE{2015NatCo...6.7945M,
       author = {{Mitchell-Wynne}, Ketron and {Cooray}, Asantha and {Gong}, Yan and {Ashby}, Matthew and {Dolch}, Timothy and {Ferguson}, Henry and {Finkelstein}, Steven and {Grogin}, Norman and {Kocevski}, Dale and {Koekemoer}, Anton and {Primack}, Joel and {Smidt}, Joseph},
        title = "{Ultraviolet luminosity density of the universe during the epoch of reionization}",
      journal = {Nature Communications},
     keywords = {Astrophysics - Cosmology and Nongalactic Astrophysics},
         year = 2015,
        month = sep,
       volume = {6},
          eid = {7945},
        pages = {7945},
          doi = {10.1038/ncomms8945},
archivePrefix = {arXiv},
       eprint = {1509.02935},
 primaryClass = {astro-ph.CO},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2015NatCo...6.7945M},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}
"""

notes = \
"""
Notes:
- Shot noise constraints quoted in Table 1, using "best fit" (i.e., first
column) only for now.
- Power spectra from SI Table 1.
"""

power_units = r'nW^2/m^4/sr^2'
scale_units = 'ell'
experiment = 'hubble'

# In CANDELS wide, deep and HUDF in F160W
masking_depth = [27.4, 28.2, 29.7]
masking_waves = [1.6, 1.6, 1.6]

data = \
{
 'waves': [0.606, 0.775, 0.85, 1.25, 1.6],
 'scales': [1.81e3, 2.64e3, 4.04e3, 6.40e3, 1.04e4, 1.71e4, 2.85e4,
     4.76e4, 7.99e4, 1.34e5, 2.26e5, 3.82e5, 6.44e5, 1.09e6],
 'mean': [[1.70e-1, 9.01e-2, 4.74e-2, 3.29e-2, 2.71e-2, 1.86e-2, 1.24e-2,
           9.62e-3, 1.13e-2, 1.67e-2, 3.27e-2, 8.96e-2, 2.26e-1, 7.08e-1],
          [2.30e-1, 9.02e-2, 7.21e-2, 9.40e-2, 3.98e-2, 3.70e-2, 3.02e-2,
           2.30e-2, 1.92e-2, 2.75e-2, 5.16e-2, 1.20e-1, 3.24e-1, 1.09],
          [1.86e-1, 9.55e-2, 8.30e-2, 9.61e-2, 6.70e-2, 3.13e-2, 2.66e-2,
           2.90e-2, 2.54e-2, 3.76e-2, 7.76e-2, 2.33e-1, 5.73e-1, 2.31],
          [1.10, 1.08, 7.94e-1, 9.61e-1, 6.60e-1, 5.29e-1, 3.71e-1, 3.39e-1,
           2.85e-1, 4.03e-1, 8.50e-1, 1.80, 4.96, 1.55e1],
          [1.10, 8.30e-1, 7.78e-1, 6.33e-1, 4.18e-1, 4.01e-1, 2.89e-1,
           2.76e-1, 2.50e-1, 3.19e-1, 7.29e-1, 1.62, 4.59, 1.49e1]
         ],
 'err': [[1.30e-1, 5.38e-2, 2.47e-2, 1.17e-2, 0.57e-2, 0.27e-2, 0.17e-2,
          1.74e-3, 0.24e-2, 0.34e-2, 0.47e-2, 0.75e-2, 0.13e-1, 0.70e-1],
         [1.69e-1, 6.19e-2, 3.29e-2, 3.34e-2, 0.91e-2, 0.57e-2, 0.39e-2,
          0.34e-2, 0.40e-2, 0.55e-2, 0.74e-2, 0.10e-1, 0.22e-1, 0.47],
         [1.33e-1, 5.10e-2, 3.25e-2, 3.23e-2, 1.47e-2, 0.41e-2, 0.28e-2,
          0.27e-2, 0.30e-2, 0.45e-2, 0.69e-2, 0.13e-1, 0.48e-1, 0.80],
         [0.98, 0.72, 4.04e-1, 3.53e-1, 1.43e-1, 0.77e-1, 0.46e-1, 0.41e-1,
          0.46e-1, 0.63e-1, 0.89e-1, 0.11, 0.16, 0.05e1],
         [1.17, 6.60e-1, 4.09e-1, 2.30e-1, 0.94e-1, 0.63e-1, 0.39e-1, 0.37e-1,
          0.43e-1, 0.56e-1, 0.80e-1, 0.09, 0.13, 0.02e1]
         ],
 'shot': [3.27e-12, 4.60e-12, 7.73e-12, 7.77e-11, 7.54e-11],
 'shot_err': [(0.24e-12,0.21e-12), (0.5e-12,0.3e-12), (0.75e-12,0.45e-12),
    (0.21e-11, 0.28e-11), (0.13e-11, 0.13e-11)],
}


def get_ebl_anisotropies():
    return data['waves'], data['scales'], data['mean'], data['err']
