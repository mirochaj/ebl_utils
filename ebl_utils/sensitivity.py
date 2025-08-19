"""

sensitivity.py

Author: Jordan Mirocha
Affiliation: JPL / Caltech
Created on: Fri Dec 15 14:46:45 PST 2023

Description:

"""

import os
import zipfile
import numpy as np
from urllib.request import urlretrieve

_HOME = os.environ.get('HOME')

_msg_spherex = \
"""
* Did not find SPHEREx public products, which contains estimates for surface
* brightness and point source sensitivity. To download the latest files, do:
*
* >>> import ebl_utils
* >>> ebl_utils.sensitivity.download_spherex_sensitivity()
*
* Then, try again!
"""

_link_spherex = 'https://github.com/SPHEREx/Public-products/archive/refs/heads'
_file_spherex = 'master.zip'

def download_spherex_sensitivity():
    if not os.path.exists(f"{_HOME}/spherex"):
        os.mkdir(f"{_HOME}/spherex")

    urlretrieve(f"{_link_spherex}/{_file_spherex}",
                f"{_HOME}/spherex/{_file_spherex}")

    zip_ref = zipfile.ZipFile(f"{_HOME}/spherex/{_file_spherex}", 'r')
    zip_ref.extractall(f"{_HOME}/spherex/")
    zip_ref.close()

def get_spherex_noise():
    """
    This loads the surface brightness sensitivity of SPHEREx in each channel.
    The units are nW/m^2/sr per pixel (1 sigma).

    Returns
    -------
    Tuple containing: (wavelengths / micron, sensitivity [all sky],
        sensitivy [deep fields]).

    """
    path = os.path.join(_HOME, "spherex", "Public-products-master")

    fn = 'Surface_Brightness_v28_base_cbe.txt'
    full_path = os.path.join(path, fn)

    return np.loadtxt(full_path, unpack=True)

def get_ps_error(ell, Cell, fsky=0.0025, Omega=9e-10, Npix=3.37e7,
    sigma=1.):
    """
    Uncertainty on C_ell, e.g., Eq. 36 in Jason's NIRB paper.

    Parameters
    ----------
    ell : int, float, np.ndarray
        ell mode of interest.
    Cell : int, float, np.ndarray
        Cosmic variance
    sigma : int, float, np.ndarray
        1-sigma noise level (per pixel) in nW/m^2/sr.

    """

    Cell_noise = 4 * np.pi * fsky * sigma**2 * np.exp(ell**2 * Omega) \
        / float(Npix)

    return (Cell + Cell_noise) / np.sqrt(fsky * (ell + 0.5))

def get_ps_error_spherex(ell, Cell, wave=None, deep=True):
    """
    Special case of function `get_ps_error` in which SPHEREx-specific noise
    levels are automatically read from disk.

    Parameters
    ----------
    ell : int, float, np.ndarray
        Ell mode(s) of interest.

    wave : int, float
        If provided, this routine will return the PS error in the SPHEREx
        channel closest to `wave`.

    """

    fsky = 0.0025 if deep else np.nan
    Npix = 3.37e7 if deep else np.nan
    Omega = 9e-10

    waves, sens_all, sens_deep = get_spherex_noise()
    sens = sens_deep if deep else sens_all

    if wave is None:
        sigma = sens
    else:
        iw = np.argmin(np.abs(waves - wave))
        sigma = sens[iw]

    return get_ps_error(ell, Cell, sigma=sigma)

def get_ps_error_spherex_binned(ell_ebin_edges, spec_bin_factor=1):
    """
    Returns an "error staircase," i.e., the predicted RMS sensitivity to the
    EBL power spectrum [in nW m^-2 sr^-1] in a series of ell mode bins.

    .. note :: This is just a wrapper around `get_ps_error` but accounting
        for binning along the spatial and spectral axes.

    Parameters
    ----------
    ell_ebin_edges : np.ndarray
        Array of ell mode bin edges.
    spec_bin_factor : int, float
        Factor by which we bin spectrally, e.g., `spec_bin_factor=2` means we
        combine pairs of channels.

    Returns
    -------
    Tuple containing (ell mode left bin edges, expected error). The rationale
    here is that we want to be able to easily plot the result without looping
    over a series of bins. Choosing the left bin edge as a reference point
    just means that we can do the following:

    >>> err = get_error_staircase(ell_bin_edges)
    >>> plt.plot(ell_bin_edges[0:-1], err, drawstyle='steps-pre')

    """

    channels = get_spherex_noise()[0]

    err = get_ps_error_spherex(ell_ebin_edges, 0.0, wave=channels)

    err_out = np.zeros(ell_ebin_edges.size)
    for i, le in enumerate(ell_ebin_edges[0:-1]):
        dell = ell_ebin_edges[i+1] - le
        scale = np.mean([le, ell_ebin_edges[i+1]])

        err_out[i,:] = np.sqrt(scale * (scale + 1) * err / np.sqrt(dell) / 2. / np.pi) \
            / spec_bin_factor

    return err_out
