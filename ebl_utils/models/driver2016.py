from math import sqrt

name = 'Driver et al. (2016)'
link = None
bibtex = None

_cols = 'Wavelength', 'Best Fit', 'Median',	'Lower Limit', \
    'Zero-point Error', 'Fitting Error', 'Poisson Error', 'CV Error'


_data = {}
_data['FUV'] = 0.153, 1.45, 1.45, 1.36, 0.07, 0.00, 0.04, 0.16
_data['NUV'] = 0.225, 3.15, 3.14, 2.86, 0.15, 0.02, 0.05, 0.45
_data['u']   = 0.356, 4.03, 4.01, 3.41, 0.19, 0.04, 0.09, 0.46
_data['g']   = 0.470, 5.36, 5.34, 5.05, 0.25, 0.04, 0.05, 0.59
_data['r']   = 0.618, 7.47, 7.45, 7.29, 0.34, 0.05, 0.04, 0.69
_data['i']   = 0.749, 9.55, 9.52, 9.35, 0.44, 0.00, 0.05, 0.92
_data['z']   = 0.895, 10.15, 10.13, 9.98, 0.47, 0.03, 0.05, 0.96
_data['Y']   = 1.021, 10.44, 10.41, 10.23, 0.48, 0.00, 0.07, 1.05
_data['J']   = 1.252, 10.38, 10.35, 10.22, 0.48, 0.00, 0.05, 0.99
_data['H']   = 1.643, 10.12, 10.10, 9.99, 0.47, 0.01, 0.06, 1.01
_data['K']   = 2.150, 8.72, 8.71, 8.57, 0.40, 0.02, 0.04, 0.76
_data['IRAC1'] = 3.544, 5.17, 5.15, 5.03, 0.24, 0.03, 0.06, 0.43
_data['IRAC2'] = 4.487, 3.60, 3.59, 3.47, 0.17, 0.02, 0.05, 0.28
_data['IRAC4'] = 7.841, 2.45, 2.45, 1.49, 0.11, 0.77, 0.15, 0.08

_bands = _data.keys()
_waves = [_data[key][0] for key in _data.keys()]

_mean = []
_err = []
for i, band in enumerate(_bands):
    _mean.append(_data[band][1])
    _err_ = [_data[band][j]**2 for j in range(4, 8)]
    _err.append(sqrt(sum(_err_)))

data = \
{
 'waves': _waves,
 'mean': _mean,
 'err': _err
}

def get_ebl_spectrum():
    return data['waves'], data['mean'], data['err']
