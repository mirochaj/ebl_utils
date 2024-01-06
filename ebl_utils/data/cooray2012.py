
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
- These measurements are actually presented in Zemcov et al. (2014), where the
only difference was the use of a shallower masking depth to compare with CIBER.
"""

data = \
{
 'waves': [3.6],
 'scales': [87.8503,122.466,170.722,237.993,331.771,462.500,644.741,898.792,
    1252.95,1746.65,2434.90,3394.33,4731.82,6596.32,9195.50,12818.9,17869.9,
    24911.3,34727.3,48411.0,67486.7,94078.8,131149.],
 'mean': [[0.134564,0.0217140,0.0198840,0.0265480,0.00305800,0.00274400,
    0.0120330,0.00434800,0.00453400,0.00673100,0.00781400,0.0132960,0.0139450,
    0.0193150,0.0273810,0.0452320,0.0753600,0.131023,0.231956,0.398387,0.655572,
    1.10979,2.41824]],
 'err': [[0.293058,0.0339500,0.0294390,0.0263380,0.00379100,0.00968800,0.00451800,
  0.00144900,0.00111600,0.00122900,0.00122000,0.00134000,0.00132700,0.00114600,
  0.00115100,0.00126300,0.00153600,0.00206600,0.00306400,0.00480900,0.00833400,
  0.0178670,0.0604150]]
}

scale_units = 'ell'
power_units = 'nW^2/m^4/sr' # I think these might be squared actually

# Masking depth quoted in Vega mags, these conversions are for J and H
# as tabulated here: https://www.gemini.edu/observing/resources/magnitudes-and-fluxes
# Note that these mag conversions can vary slightly.
# Also note that 3.6 micron has a correction of 2.93, but 2.779 in Timlin+2016
# Also seeing 2.669 for WISE W1 (https://wise2.ipac.caltech.edu/docs/release/allsky/expsup/sec4_4h.html)
masking_depth = [16 + 2.93]
masking_waves = [3.6]

def get_ebl_anisotropies():
    return data['waves'], data['scales'], data['mean'], data['err']
