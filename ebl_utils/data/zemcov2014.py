"""
Zemcov et al. 2014
"""

name = 'Zemcov et al. (2014)'
year = 2014
link = 'https://ui.adsabs.harvard.edu/abs/2014Sci...346..732Z/abstract'
bibtex = \
"""
@ARTICLE{2014Sci...346..732Z,
       author = {{Zemcov}, Michael and {Smidt}, Joseph and {Arai}, Toshiaki and {Bock}, James and {Cooray}, Asantha and {Gong}, Yan and {Kim}, Min Gyu and {Korngut}, Phillip and {Lam}, Anson and {Lee}, Dae Hee and {Matsumoto}, Toshio and {Matsuura}, Shuji and {Nam}, Uk Won and {Roudier}, Gael and {Tsumura}, Kohji and {Wada}, Takehiko},
        title = "{On the origin of near-infrared extragalactic background light anisotropy}",
      journal = {Science},
     keywords = {ASTRONOMY, Astrophysics - Cosmology and Nongalactic Astrophysics},
         year = 2014,
        month = nov,
       volume = {346},
       number = {6210},
        pages = {732-735},
          doi = {10.1126/science.1258168},
archivePrefix = {arXiv},
       eprint = {1411.1411},
 primaryClass = {astro-ph.CO},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2014Sci...346..732Z},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}
"""
experiment = 'ciber'

notes = \
"""
Notes:
- On masking: "The extended 2MASS catalog is 75% complete at J=17.5,
which translates to 17.5 and 17.0 in CIBER’s 1.1μm and 1.6μm bands,
respectively,and all fields are masked to this depth."
"""

data = \
{
 'waves': [1.1, 1.6],
 'scales': [163.109675, 226.175189, 313.624659, 434.886015, 603.032449,
   836.191834, 1159.501092, 1607.816207, 2229.470049, 3091.483141, 4286.789148,
   5944.254055, 8242.569218, 11429.516080, 15848.679505, 21976.489668,
   30473.586016, 42256.040829, 58594.121006, 81249.235592, 112663.833348],
 'mean': [[11.029968, 9.258115, 32.888573, 7.449895, 9.583225, 6.427002,
    2.202421, 2.671167, 4.198341, 4.876662, 5.523744, 8.509693, 15.289950,
    23.391431, 37.693763, 67.100562, 118.592945, 213.059887, 397.366138,
    949.054125, 1816.255206],
          [20.539763, 21.243314, 12.459137, 11.041647, 8.543302, 5.049253,
    4.529842, 3.466993, 2.194328, 3.200047, 4.421351, 5.271408, 10.716054,
    15.914549, 24.198570, 43.214995, 73.659107, 130.415398, 238.176960,
    514.693350, 1044.747370]],
 'err': [[(164.414836, 21.476076),(91.617503, 11.291547),
         (133.566424, 29.113963),(22.816076, 6.197335),
         (12.435307, 6.227228),(6.618910, 3.562695),(1.766532, 0.975299),
         (1.585845, 0.947782),(1.728775, 1.090538),(1.437632, 0.989301),
         (1.297581, 0.912240),(0.768115, 0.768115),(0.997986, 0.997986),
         (1.157041, 1.157041),(1.469666, 1.469666),(2.022272, 2.022272),
         (3.175099, 3.175099),(5.952660, 5.952660),(15.768413, 15.768413),
         (76.007495, 76.007495),(489.811705, 489.811705)],
         [(234.398133, 33.455746),(142.251729, 24.181435),
          (159.178397, 11.421187),(38.551629, 7.856096),(11.702387, 5.524188),
          (6.417825, 2.992838),(3.231330, 1.740923),(1.935983, 1.135344),
          (0.872827, 0.526373),(0.988621, 0.599358),(0.962971, 0.669790),
          (0.457333, 0.457333),(0.656497, 0.656497),(0.759805, 0.759805),
          (0.918096, 0.918096),(1.348869, 1.348869),(2.141193, 2.141193),
          (4.204249, 4.204249),(11.496256, 11.496256),(55.075427, 55.075427),
          (434.553817, 434.553817)]],

}

# Masking depth quoted in Vega mags, these conversions are for J and H
# as tabulated here: https://www.gemini.edu/observing/resources/magnitudes-and-fluxes
# Note that these mag conversions can vary slightly.
# Also note that 3.6 micron has a correction of 2.93, but 2.779 in Timlin+2016
# Also seeing 2.669 for WISE W1 (https://wise2.ipac.caltech.edu/docs/release/allsky/expsup/sec4_4h.html)
masking_depth = [17.5 + 0.94, 17. + 1.38]
masking_waves = [1.1, 1.6]
# Masking depth for Spitzer 3.6 micron is 16.
# All use 2MASS catalogs

# Dataset 'err' is actually upper and lower bounds.
# Convert to error bar to be consistent with other datasets
#data['err'] = []
#for i, wave in enumerate(data['waves']):
#    data['err'].append([])
#    for j, scale in enumerate(data['scales']):
#        err = data['bounds'][i][j][0] - data['mean'][i][j], \
#              abs(data['mean'][i][j] - data['bounds'][i][j][1])
#        data['err'][i].append(err)

scale_units = 'ell'
power_units = 'nW^2/m^4/sr' # I think these might be squared actually

def get_ebl_anisotropies():
    return data['waves'], data['scales'], data['mean'], data['err']
