
name = 'Cooray et al. (2012)'
link = 'https://ui.adsabs.harvard.edu/abs/2012Natur.490..514C/abstract'
bibtex = \
"""
@ARTICLE{2012Natur.490..514C,
       author = {{Cooray}, Asantha and {Smidt}, Joseph and {de Bernardis}, Francesco and {Gong}, Yan and {Stern}, Daniel and {Ashby}, Matthew L.~N. and {Eisenhardt}, Peter R. and {Frazer}, Christopher C. and {Gonzalez}, Anthony H. and {Kochanek}, Christopher S. and {Koz{\l}owski}, Szymon and {Wright}, Edward L.},
        title = "{Near-infrared background anisotropies from diffuse intrahalo light of galaxies}",
      journal = {\nat},
         year = 2012,
        month = oct,
       volume = {490},
       number = {7421},
        pages = {514-516},
          doi = {10.1038/nature11474},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2012Natur.490..514C},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}
"""

notes = \
"""
Notes:
- Power spectrum measurements in Table SI 1.
- Reported in nW m^-2 sr^-1, here we square for consistency with other datasets.
- Masking is done with the Spitzer Wide Deep Survey (Ashby et al. 2009; https://ui.adsabs.harvard.edu/abs/2009ApJ...701..428A/abstract),
so the `masking_depth` attribute contains the limiting magnitudes at 3.5 and 4.6
microns from that paper. This work says sources from the NOAO Wide-field
Survey are also masked (Januzzi & Dey 1999; https://ui.adsabs.harvard.edu/abs/1999ASPC..191..111J/abstract).
That survey is quite a bit deeper, BRI >= 26 AB mag, JH = 21 AB mag, and K = 21.4 AB mag.
"""

# Converting from Vega to AB
masking_depth = [19.77 + 2.779, 18.83 + 3.264]

# This is the raw data, as reported in SI Table 1. Square everything below.
_data = \
{
 'scales': [243, 313,402,517,665,854,1099,1412,1815,2332,2997,3851,4949,6360,
8173,1.05e4,1.35e4,1.735e4,2.229e4,2.865e4,3.682e4,4.731e4,6.081e4,7.814e4,
1.004e5,1.291e5,1.658e5,2.131e5,2.739e5,3.520e5,4.523e5],
 'waves': [3.6, 4.5],
 'mean': [[0.27e-2,0.52e-2,0.18e-2,0.51e-2,0.32e-2,0.43e-2,0.25e-2,0.18e-2,0.26e-2,
  0.19e-2,0.34e-2,0.29e-2,0.43e-2,0.32e-2,0.36e-2,0.34e-2,0.42e-2,0.53e-2,
  0.72e-2,1.02e-2,1.49e-2,2.14e-2,3.05e-2,4.28e-2,5.87e-2,7.67e-2,8.99e-2,
  9.28e-2,7.67e-2,5.21e-2,3.25e-2],
          [2.04e-2,2.81e-2,0.54e-2,0.89e-2,0.23e-2,0.28e-2,0.23e-2,0.24e-2,0.27e-2,
  0.21e-2,0.20e-2,0.22e-2,0.24e-2,0.28e-2,0.22e-2,0.22e-2,0.25e-2,0.35e-2,
  0.54e-2,0.71e-2,1.03e-2,1.48e-2,2.10e-2,2.97e-2,4.11e-2,5.27e-2,6.15e-2,
  5.92e-2,4.84e-2,3.06e-2,1.70e-2]],
 'err': [[0.36e-2,0.58e-2,0.24e-2,0.50e-2,0.26e-2,0.42e-2,0.12e-2,0.11e-2,0.16e-2,
  0.09e-2,0.08e-2,0.05e-2,0.09e-2,0.13e-2,0.13e-2,0.10e-2,0.08e-2,0.05e-2,
  0.03e-2,0.04e-2,0.04e-2,0.03e-2,0.03e-2,0.05e-2,0.06e-2,0.09e-2,0.08e-2,
  0.04e-2,0.02e-2,0.14e-2,0.16e-2],
         [2.82e-2,3.33e-2,0.49e-2,0.87e-2,0.23e-2,0.18e-2,0.12e-2,0.12e-2,
  0.08e-2,0.04e-2,0.03e-2,0.04e-2,0.05e-2,0.09e-2,0.08e-2,0.09e-2,0.10e-2,
  0.11e-2,0.12e-2,0.16e-2,0.17e-2,0.19e-2,0.15e-2,0.13e-2,0.14e-2,0.12e-2,
  0.06e-2,0.12e-2,0.08e-2,0.07e-2,0.15e-2]]
}

data = {}
data['scales'] = _data['scales']
data['waves'] = _data['waves']
data['mean'] = []
data['err'] = []

for i, wave in enumerate(data['waves']):
    new_m = []
    new_e = []
    for j, ell in enumerate(data['scales']):
        new_m.append(_data['mean'][i][j]**2)
        new_e.append(_data['err'][i][j]**2)

    data['mean'].append(new_m)
    data['err'].append(new_e)

scale_units = 'ell'
power_units = 'nW^2/m^4/sr' # I think these might be squared actually

def get_ebl_anisotropies():
    return data['waves'], data['scales'], data['mean'], data['err']
