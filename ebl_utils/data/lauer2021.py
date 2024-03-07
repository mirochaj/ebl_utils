"""
Lauer et al. 2021
"""

name = 'Lauer et al. (2021)'
year = 2021
link = 'https://ui.adsabs.harvard.edu/abs/2021ApJ...906...77L/abstract'
experiment = 'New Horizons'

bibtex = \
"""
@ARTICLE{2021ApJ...906...77L,
       author = {{Lauer}, Tod R. and {Postman}, Marc and {Weaver}, Harold A. and {Spencer}, John R. and {Stern}, S. Alan and {Buie}, Marc W. and {Durda}, Daniel D. and {Lisse}, Carey M. and {Poppe}, A.~R. and {Binzel}, Richard P. and {Britt}, Daniel T. and {Buratti}, Bonnie J. and {Cheng}, Andrew F. and {Grundy}, W.~M. and {Hor{\'a}nyi}, Mihaly and {Kavelaars}, J.~J. and {Linscott}, Ivan R. and {McKinnon}, William B. and {Moore}, Jeffrey M. and {N{\'u}{\~n}ez}, J.~I. and {Olkin}, Catherine B. and {Parker}, Joel W. and {Porter}, Simon B. and {Reuter}, Dennis C. and {Robbins}, Stuart J. and {Schenk}, Paul and {Showalter}, Mark R. and {Singer}, Kelsi N. and {Verbiscer}, Anne J. and {Young}, Leslie A.},
        title = "{New Horizons Observations of the Cosmic Optical Background}",
      journal = {\apj},
     keywords = {Cosmic background radiation, Diffuse radiation, Population III stars, Galaxy formation, 317, 383, 1285, 595, Astrophysics - Astrophysics of Galaxies, Astrophysics - Cosmology and Nongalactic Astrophysics},
         year = 2021,
        month = jan,
       volume = {906},
       number = {2},
          eid = {77},
        pages = {77},
          doi = {10.3847/1538-4357/abc881},
archivePrefix = {arXiv},
       eprint = {2011.03052},
 primaryClass = {astro-ph.GA},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2021ApJ...906...77L},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}
"""

notes = \
"""
- Results from Table 6.
- Only recording total error here (including random and systematic).
"""

data_cob_z17 = \
{
 'waves': [0.6],
 'mean': [15.9],
 'err': [4.2],
}

data_cob_bd12 = \
{
 'waves': [0.6],
 'mean': [18.7],
 'err': [3.8],
}

data_dcob_z17 = \
{
 'waves': [0.6],
 'mean': [8.8],
 'err': [4.9],
}

data_dcob_bd12 = \
{
 'waves': [0.6],
 'mean': [11.9],
 'err': [4.6],
}

def get_ebl_spectrum(use_dCOB=False, dgl_model='zemcov'):
    """
    Parameters
    ----------
    use_dCOB : bool
        This controls whether the values returned correspond to the diffuse COB,
        i.e., whether or not an attempt has been made to subtract IGL etc.
    dgl_model : str
        Need to specify which DGL model to use. The top row of Table 6
        corresponds to Zemcov+ 2017 (dgl_model='zemcov'), while the bottom row
        corresponds to Brandt & Draine 2012 (dgl_model='bd2012').
    """

    if use_dCOB:
        if dgl_model == 'zemcov':
            return data_dcob_z17['waves'], data_dcob_z17['mean'], data_dcob_z17['err']
        else:
            return data_dcob_bd12['waves'], data_dcob_bd12['mean'], data_dcob_bd12['err']
    else:
        if dgl_model == 'zemcov':
            return data_cob_z17['waves'], data_cob_z17['mean'], data_cob_z17['err']
        else:
            return data_cob_bd12['waves'], data_cob_bd12['mean'], data_cob_bd12['err']
