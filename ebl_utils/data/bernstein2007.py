"""
Bernstein 2007, ApJ, 666, 2
"""
name = 'Bernstein (2007)'
year = 2007
link = 'https://ui.adsabs.harvard.edu/abs/2007ApJ...666..663B/abstract'
experiment = 'hubble'
bibtex = \
"""
@ARTICLE{2007ApJ...666..663B,
       author = {{Bernstein}, Rebecca A.},
        title = "{The Optical Extragalactic Background Light:
        Revisions and Further Comments}",
      journal = {\apj},
     keywords = {Cosmology: Diffuse Radiation},
         year = 2007,
        month = sep,
       volume = {666},
       number = {2},
        pages = {663-673},
          doi = {10.1086/519824},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2007ApJ...666..663B},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}
"""

notes = \
"""
Notes:
- All from Table 3.
- Results quoted in specific intensities in cgs units, hence conversion.
"""

# 1 W = 10^7 erg/s, 10^4 cm^2 / m^2
# Note that of course there should be a 10^9 nW / W conversion factor,
# but Table 3 in the paper reports cgs fluxes in units of 10^-9 erg/s/cm^2/A/sr
cgs_to_si = 1e-7 * 1e4

data = \
{
 'waves': [0.3, 0.555, 0.814],
 'mean': [33.5 * cgs_to_si * 0.3e4,
         105.7 * cgs_to_si * 0.555e4,
          72.4 * cgs_to_si * 0.814e4],
 'err': [3.3 * cgs_to_si * 0.3e4,
         2.3 * cgs_to_si * 0.555e4,
         2.0 * cgs_to_si * 0.814e4],
}

def get_ebl_spectrum():
    return data['waves'], data['mean'], data['err']
