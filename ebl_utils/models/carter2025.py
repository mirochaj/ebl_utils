"""
Carter et al. 2025.
"""

name = 'Carter et al. (2025)'
year = 2025
experiment = 'HST'
link = 'https://ui.adsabs.harvard.edu/abs/2025arXiv250705323C/abstract'
style = \
{
 'color': 'g',
 #'edgecolor': 'g',
 #'mfc': None,
 'marker': 'H',
 'label': name,
 #'fmt': 'o',
}

bibtex = \
"""
@ARTICLE{2025arXiv250705323C,
       author = {{Carter}, Delondrae D. and {Carleton}, Timothy and {Henningsen}, Daniel and {Windhorst}, Rogier A. and {Cohen}, Seth H. and {Tompkins}, Scott and {O'Brien}, Rosalia and {Koekemoer}, Anton M. and {Li}, Juno and {Goisman}, Zak and {Driver}, Simon P. and {Robotham}, Aaron and {Jansen}, Rolf and {Grogin}, Norman and {Huang}, Haina and {Acharya}, Tejovrash and {Berkheimer}, Jessica and {Abate}, Haley and {Gelb}, Connor and {Huckabee}, Isabela and {MacKenty}, John},
        title = "{SKYSURF-10: A Novel Method for Measuring Integrated Galaxy Light}",
      journal = {arXiv e-prints},
     keywords = {Instrumentation and Methods for Astrophysics, Cosmology and Nongalactic Astrophysics},
         year = 2025,
        month = jul,
          eid = {arXiv:2507.05323},
        pages = {arXiv:2507.05323},
          doi = {10.48550/arXiv.2507.05323},
archivePrefix = {arXiv},
       eprint = {2507.05323},
 primaryClass = {astro-ph.IM},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2025arXiv250705323C},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}
"""

notes = \
"""
Notes:
- Data from Table 6 ("extrapolated" IGL).
"""

zodi = None

# Copy-pasted from PDF
_tab6 = \
[['SV', 'ACSWFC',  'F435W',  0.4342, 5.52,  0.247, 4.47,  3.22, 0.089, 5.85,  0.211, 3.61, 1.82],
['SV', 'ACSWFC',   'F475W',  0.4709, 5.64,  0.181, 3.20,  3.28, 0.037, 5.77,  0.164, 2.84, 1.76],
['SV', 'ACSWFC',   'F555W',  0.5332, 8.03,  0.925, 11.52, 2.78, 0.230, 6.30,  0.507, 8.04, 2.27],
['SV', 'ACSWFC',   'F606W',  0.5809, 8.79,  0.408, 4.64,  4.93, 0.148, 9.07,  0.331, 3.65, 1.84],
['SV', 'ACSWFC',   'F625W',  0.6266, 8.65,  0.332, 3.83,  5.04, 0.061, 9.14,  0.313, 3.43, 1.81],
['SV', 'ACSWFC',   'F775W',  0.7652, 10.78, 0.566, 5.25,  6.02, 0.084, 11.48, 0.581, 5.06, 1.91],
['SV', 'ACSWFC',   'F814W',  0.7973, 10.59, 0.522, 4.92,  6.18, 0.068, 11.28, 0.545, 4.83, 1.83],
['SV', 'ACSWFC',   'F850LP', 0.9005, 9.85,  0.333, 3.38,  7.16, 0.087, 11.28, 0.355, 3.14, 1.57],
['SV', 'WFC3IR',   'F105W',  1.0431, 11.10, 0.471, 4.24,  7.43, 0.201, 11.41, 0.363, 3.19, 1.54],
['SV', 'WFC3IR',   'F110W',  1.1201, 10.48, 0.676, 6.45,  7.28, 0.316, 11.17, 0.531, 4.76, 1.53],
['SV', 'WFC3IR',   'F125W',  1.2364, 10.04, 0.263, 2.62,  7.15, 0.115, 10.95, 0.216, 1.97, 1.53],
['SV', 'WFC3IR',   'F140W',  1.3735, 9.20,  0.556, 6.04,  7.03, 0.065, 10.19, 0.602, 5.91, 1.45],
['SV', 'WFC3IR',   'F160W',  1.5278, 11.27, 0.229, 2.03,  7.45, 0.096, 11.27, 0.171, 1.52, 1.51],
['SV', 'WFC3UVIS', 'F336W',  0.3359, 3.11,  0.268, 8.62,  2.22, 0.153, 4.05,  0.186, 4.59, 1.83],
['SV', 'WFC3UVIS', 'F390W',  0.4022, 5.45,  0.650, 11.94, 2.22, 0.048, 4.94,  0.567, 11.49, 2.22],
['SV', 'WFC3UVIS', 'F438W',  0.4323, 5.80,  0.366, 6.32,  3.22, 0.089, 5.85,  0.211, 3.61, 1.82],
['SV', 'WFC3UVIS', 'F475W',  0.4732, 6.06,  0.212, 3.50,  3.28, 0.037, 5.77,  0.164, 2.84, 1.76],
['SV', 'WFC3UVIS', 'F555W',  0.5236, 12.12, 1.476, 12.18, 2.78, 0.230, 6.30,  0.507, 8.04, 2.27],
['SV', 'WFC3UVIS', 'F606W',  0.5782, 9.42,  0.448, 4.75,  4.93, 0.148, 9.07,  0.331, 3.65, 1.84],
['SV', 'WFC3UVIS', 'F625W',  0.6188, 8.43,  0.392, 4.65,  5.04, 0.061, 9.14,  0.313, 3.43, 1.81],
['SV', 'WFC3UVIS', 'F775W',  0.7613, 10.33, 0.766, 7.42,  6.02, 0.084, 11.48, 0.581, 5.06, 1.91],
['SV', 'WFC3UVIS', 'F814W',  0.7964, 11.05, 0.554, 5.01,  6.18, 0.068, 11.28, 0.545, 4.83, 1.83],
['SV', 'WFC3UVIS', 'F850LP', 0.9154, 8.65,  0.522, 6.03,  7.16, 0.087, 11.28, 0.355, 3.14, 1.57],
['MV', 'ACSWFC',   'F435W',  0.4342, 5.79,  0.281, 4.85,  3.22, 0.089, 5.85,  0.211, 3.61, 1.82],
['MV', 'ACSWFC',   'F475W',  0.4709, 5.68,  0.205, 3.62,  3.28, 0.037, 5.77,  0.164, 2.84, 1.76],
['MV', 'ACSWFC',   'F555W',  0.5332, 8.62,  1.033, 11.99, 2.78, 0.230, 6.30,  0.507, 8.04, 2.27],
['MV', 'ACSWFC',   'F606W',  0.5809, 9.34,  0.444, 4.76,  4.93, 0.148, 9.07,  0.331, 3.65, 1.84],
['MV', 'ACSWFC',   'F625W',  0.6266, 8.67,  0.342, 3.94,  5.04, 0.061, 9.14,  0.313, 3.43, 1.81],
['MV', 'ACSWFC',   'F775W',  0.7652, 10.71, 0.564, 5.27,  6.02, 0.084, 11.48, 0.581, 5.06, 1.91],
['MV', 'ACSWFC',   'F814W',  0.7973, 9.99,  0.500, 5.00,  6.18, 0.068, 11.28, 0.545, 4.83, 1.83],
['MV', 'ACSWFC',   'F850LP', 0.9005, 9.50,  0.339, 3.57,  7.16, 0.087, 11.28, 0.355, 3.14, 1.57],
['MV', 'WFC3IR',   'F105W',  1.0431, 10.54, 0.456, 4.33,  7.43, 0.201, 11.41, 0.363, 3.19, 1.54],
['MV', 'WFC3IR',   'F110W',  1.1201, 10.63, 0.690, 6.49,  7.28, 0.316, 11.17, 0.531, 4.76, 1.53],
['MV', 'WFC3IR',   'F125W',  1.2364, 10.05, 0.276, 2.75,  7.15, 0.115, 10.95, 0.216, 1.97, 1.53],
['MV', 'WFC3IR',   'F140W',  1.3735, 9.07,  0.548, 6.04,  7.03, 0.065, 10.19, 0.602, 5.91, 1.45],
['MV', 'WFC3IR',   'F160W',  1.5278, 11.16, 0.232, 2.08,  7.45, 0.096, 11.27, 0.171, 1.52, 1.51],
['MV', 'WFC3UVIS', 'F336W',  0.3359, 2.63,  0.255, 9.70,  2.22, 0.153, 4.05,  0.186, 4.59, 1.83],
['MV', 'WFC3UVIS', 'F390W',  0.4022, 5.27,  0.639, 12.12, 2.22, 0.048, 4.94,  0.567, 11.49, 2.22],
['MV', 'WFC3UVIS', 'F438W',  0.4323, 4.81,  0.343, 7.14,  3.22, 0.089, 5.85,  0.211, 3.61, 1.82],
['MV', 'WFC3UVIS', 'F475W',  0.4732, 5.87,  0.266, 4.53,  3.28, 0.037, 5.77,  0.164, 2.84, 1.76],
['MV', 'WFC3UVIS', 'F555W',  0.5236, 10.82, 1.392, 12.86, 2.78, 0.230, 6.30,  0.507, 8.04, 2.27],
['MV', 'WFC3UVIS', 'F606W',  0.5782, 9.28,  0.450, 4.85,  4.93, 0.148, 9.07,  0.331, 3.65, 1.84],
['MV', 'WFC3UVIS', 'F625W',  0.6188, 8.10,  0.425, 5.24,  5.04, 0.061, 9.14,  0.313, 3.43, 1.81],
['MV', 'WFC3UVIS', 'F775W',  0.7613, 10.40, 0.977, 9.40,  6.02, 0.084, 11.48, 0.581, 5.06, 1.91],
['MV', 'WFC3UVIS', 'F814W',  0.7964, 10.40, 0.532, 5.12,  6.18, 0.068, 11.28, 0.545, 4.83, 1.83],
['MV', 'WFC3UVIS', 'F850LP', 0.9154, 9.70,  0.849, 8.76,  7.16, 0.087, 11.28, 0.355, 3.14, 1.57]]


data = \
{
 'visit_type': [element[0] for element in _tab6],
 'instrument': [element[1] for element in _tab6],
 'filter': [element[2] for element in _tab6],
 'waves': [element[3] for element in _tab6],
 'mean': [element[4] for element in _tab6],
 'err': [element[5] for element in _tab6],
}

def get_ebl_spectrum(visit_type='both', instrument='any', exclude_filters=None):
    if visit_type == 'both' and instrument == 'any':
        return data['waves'], data['mean'], data['err']
    
    waves = []
    igl = []
    err = []
    for i in range(len(data['waves'])):
        if exclude_filters is not None:
            if data['filter'][i] in exclude_filters:
                continue 
            
        if visit_type.lower() in ['single', 'sv']:
            if data['visit_type'][i] == 'MV':
                continue 
        if visit_type.lower() in ['multi', 'MV']:
            if data['visit_type'][i] == 'SV':
                continue 
        
        # Done in this case
        if instrument == 'any':
            waves.append(data['waves'][i])
            igl.append(data['mean'][i])
            err.append(data['err'][i])
            continue 

        if instrument.lower()[0:3] != data['instrument'][i].lower()[0:3]:
            continue

        waves.append(data['waves'][i])
        igl.append(data['mean'][i])
        err.append(data['err'][i])
        
    return waves, igl, err
        
