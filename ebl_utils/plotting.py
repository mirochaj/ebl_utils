"""

plotting.py

Author: Jordan Mirocha
Affiliation: Jet Propulsion Laboratory
Created on: Fri Nov  4 17:38:53 PDT 2022

Description: Stolen from Chi and Mike.

"""

import os
import numpy as np
import matplotlib.pyplot as plt
from .read import read as read_data

#from .data import PATH
PATH = os.environ.get('EBLUTILS')

str_nuInu = r'$\lambda I_{\lambda} \ [\rm{nW} \ \rm{m}^{-2} \ \rm{sr}^{-1}]$'
str_waves = r'$\lambda / \mu\rm{m}$'
str_power = r'$\sqrt{\ell(\ell+1)C_{\ell}} \ [\rm{nW} \ \rm{m}^{-1} \ \rm{sr}^{-1}]$'

def plot_spectrum(ax=None, fig=1, fig_kwargs={}, include_models=[],
    include_datasets=['ciber', 'dirbe', 'irts', 'newhorizons', 'akari', 'hubble'],
    color_by=None, use_newest=True,
    dataset_kw={}, label_experiments=True, label_papers=False, **kwargs):
    """
    Make a nice-ish plot of the EBL spectrum.

    Parameters
    ----------
    ax : matplotlib.axes._subplots.AxesSubplot
        If None, will initialize a new plot.
    fig : int, matplotlib.figure.Figure
        Pre-existing figure object or an integer that will be used as the
        ID number for a new plot window.


    Returns
    -------
    A tuple containing instances of the following:
        (matplotlib.figure.Figure, matplotlib.axes._subplots.AxesSubplot)

    """

    if ax is None:
        fig, ax = plt.subplots(1, 1, **fig_kwargs)

    ##
    # First, plot data
    for dataset in include_datasets:
        # Read from ebl_utils.data
        data = read_data(dataset)

        is_exp = hasattr(data, 'all_datasets')

        if is_exp:
            if hasattr(data, 'newest_dataset') and use_newest:
                contents = data.newest_dataset,
            else:
                contents = data.all_datasets
        else:
            contents = [data]

        for i, dset in enumerate(contents):

            # Some datasets
            if not hasattr(dset, 'get_ebl_spectrum'):
                continue

            name = dset.__name__[dset.__name__.rfind('.')+1:]

            if label_experiments and is_exp and i == 0:
                label = data.name
            elif label_papers:
                label = dset.name
            else:
                label = None

            # Check for keyword arguments
            if name in dataset_kw.keys():
                kw = dataset_kw[dataset]
            else:
                kw = {}

            # Load it
            x, y, err = dset.get_ebl_spectrum(**kw)

            # Plot it
            err = np.array(err)
            if err.ndim == 1:
                ax.errorbar(x, y, yerr=err, fmt='o',
                    label=label, **kwargs)
            else:
                ax.errorbar(x, y, yerr=err[:,-1::-1].T, fmt='o',
                    label=label, **kwargs)

    ##
    # Models too?
    for dataset in include_models:
        # Read from ebl_utils.models
        data = read_data(dataset)

        # Load it
        x, y, err = data.get_ebl_spectrum()

        # Plot it
        err = np.array(err)
        if err.ndim == 1:
            ax.errorbar(x, y, yerr=err, fmt='o',
                label=data.name, **kwargs)
        else:
            ax.errorbar(x, y, yerr=err[:,-1::-1].T, fmt='o',
                label=data.name, **kwargs)

    ##
    # Make nice
    ax.set_xlabel(str_waves, fontsize=24)
    ax.set_ylabel(str_nuInu, fontsize=24)
    ax.set_yscale('log')
    ax.set_xscale('log')

    ax.set_xticks([1,2,3,4,5], minor=False)
    ax.set_xticks(np.arange(0.5, 1, 0.1), minor=True)
    ax.set_xticklabels(['1', '2', '3', '4', '5'])

    ax.set_xlim(0.3, 6)
    ax.set_ylim(1, 150)

    fig.subplots_adjust(left=0.15, bottom=0.15)

    ##
    # Done
    return fig, ax

def plot_anisotropy_color(fig=None, ax=None, fig_kwargs={}, ell_bin=(500, 1e3),
    include_datasets=['ciber', 'akari'], ell_avg=True,
    label_experiments=True, label_papers=False, **kwargs):
    """
    Make a nice-ish plot of the "anistropy color," i.e., the amplitude of
    fluctuations at a given scale vs. wavelength.

    Returns
    -------
    A tuple containing instances of the following:
        (matplotlib.figure.Figure, matplotlib.axes._subplots.AxesSubplot)

    """
    if ax is None:
        fig, ax = plt.subplots(1, 1, **fig_kwargs)

    ##
    # Loop over datasets
    for dataset in include_datasets:
        # Read from ebl_utils.data
        data = read_data(dataset)

        is_exp = hasattr(data, 'all_datasets')

        if is_exp:
            if hasattr(data, 'newest_dataset') and use_newest:
                contents = data.newest_dataset,
            else:
                contents = data.all_datasets
        else:
            contents = [data]

        for i, dset in enumerate(contents):

            # Some datasets only have mean EBL
            if not hasattr(dset, 'get_ebl_anisotropies'):
                continue

            name = dset.__name__[dset.__name__.rfind('.')+1:]

            if label_experiments and is_exp and i == 0:
                label = data.name
            elif label_papers and (not is_exp):
                label = dset.name
            else:
                label = None

            # Load it
            waves, scales, ps, err = dset.get_ebl_anisotropies()

            # Figure out which scales fall in our specified window
            if dset.scale_units == 'ell':
                x = np.array(scales)
            elif dset.scale_units.startswith('arcsec'):
                # This is an approximation!
                x = 180 * 3600 / np.array(scales)
            else:
                raise NotImplemented('help')

            ok = np.logical_and(x >= ell_bin[0], x < ell_bin[1])

            err = np.array(err)

            for i, wave in enumerate(waves):

                if ell_avg:
                    ax.errorbar(wave, np.array(ps)[i,ok==1].mean(),
                        yerr=err[i,ok==1].mean(), fmt='o',
                        label=data.name, **kwargs)

                    continue


                if err.ndim == 2:
                    ax.errorbar([wave]*ok.sum(), np.array(ps)[i,ok==1],
                        yerr=err[i,ok==1], fmt='o',
                        label=data.name, **kwargs)
                else:
                    ax.errorbar([wave]*ok.sum(), np.array(ps)[i,ok==1],
                        yerr=err[i,ok==1,:][:,-1::-1].T, fmt='o',
                        label=data.name, **kwargs)


    ##
    # Make nice
    ax.set_xlabel(str_waves, fontsize=24)
    ax.set_ylabel(str_power, fontsize=24)

    ax.set_yscale('log')
    ax.set_xscale('log')
    ax.set_xticks([1,2,3,4,5], minor=False)
    ax.set_xticks(np.arange(0.5, 1, 0.1), minor=True)
    ax.set_xticklabels(['1', '2', '3', '4', '5'])

    ax.set_xlim(0.3, 6)
    ax.set_ylim(1e-2, 10)

    fig.subplots_adjust(left=0.15, bottom=0.15)

    return fig, ax

def plot_anisotropies():
    pass

def get_ciber_data(wave1=1.1, wave2=1.1):
    if wave1 == wave2 == 3.6:
        ell, pell, err = \
            np.loadtxt(f'{PATH}/data/ciber/zemcovetal_{wave1}x{wave2}.txt',
                unpack=True, comments=[';;', ';'])

        # `pell` is ell^2 Cl/2pi
        # `err` is ell^2 dCl/2pi
        Cl = pell * 2 * np.pi / ell**2
        Clerr = err * 2 * np.pi / ell**2
        norm = ell * (ell + 1) / 2. / np.pi

        return ell, np.sqrt(norm * Cl), np.sqrt(norm * Clerr)

    else:
        ell, cen, dn, up = \
            np.loadtxt(f'{PATH}/data/ciber/zemcovetal_{wave1}x{wave2}.txt',
                unpack=True, comments=[';;', ';'])
        Cl = cen * 2 * np.pi / ell**2
        pdn = dn * 2 * np.pi / ell**2
        pup = up * 2 * np.pi / ell**2
        norm = ell * (ell + 1) / 2. / np.pi

        return ell, np.sqrt(norm * Cl), np.sqrt([norm*pdn, norm*pup])

def get_dgl_spectrum():
    ohmb = 2.
    x, y = np.loadtxt(f'{PATH}/data/zda04_bc03.dat', unpack=True)
    x = x / 1e4
    y = y * ohmb * 1.73

    return x, y

def get_zodi_spectrum():
    zodi = np.loadtxt(f'{PATH}/data/zodi_extrap.csv',
        delimiter=' ', unpack=True)
    dist = np.arange(1, 8, 1)

    return dist, zodi

def plot_ciber(wave1=1.1, wave2=1.1, ax=None, fig=1, **kwargs):
    """

    """

    if ax is None:
        fig, ax = plt.subplots(1, 1, num=fig)

    if wave1 == wave2 == 3.6:
        ell, pell, err = \
            np.loadtxt(f'{PATH}/data/ciber/zemcovetal_{wave1}x{wave2}.txt',
                unpack=True, comments=[';;', ';'])

        Cl = pell * 2 * np.pi / ell**2
        norm = ell * (ell + 1) / 2. / np.pi
        s = err * 2 * np.pi / ell**2
        ax.errorbar(ell, np.sqrt(norm * Cl),
            yerr=np.sqrt(norm*s), fmt='o', **kwargs)
        #ax.scatter(ell, np.sqrt(norm * Cl), marker='o', **kwargs)
        #ax.plot([ell]*2, np.sqrt([norm*(Cl-s), norm*(Cl+s)]), **kwargs)

    else:
        ell, cen, dn, up = \
            np.loadtxt(f'{PATH}/data/ciber/zemcovetal_{wave1}x{wave2}.txt',
                unpack=True, comments=[';;', ';'])

        Cl = cen * 2 * np.pi / ell**2
        pdn = dn * 2 * np.pi / ell**2
        pup = up * 2 * np.pi / ell**2
        norm = ell * (ell + 1) / 2. / np.pi
        #ax.errorbar(ell, np.sqrt(norm * Cl),
        #    yerr=np.sqrt(norm * np.array([dn, up])),
        #    fmt='o', **kwargs)
        ax.scatter(ell, np.sqrt(norm * Cl), marker='o', **kwargs)

        lo = np.sqrt(norm*(Cl-pdn))
        hi = np.sqrt(norm*(Cl+pup))
        lo[np.isnan(lo)] = 1e-10
        ax.plot([ell]*2, [lo, hi], **kwargs)

    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.set_xticks(np.logspace(2, 6, 5))
    ax.set_xlim(1e2, 1e5)
    ax.set_ylim(1e-3, 5e2)


    return fig, ax

def plot_zemcov_fig1(axes=None, fig=1):
    """
    Replicate Zemcov et al. (2014) Fig. 1.
    """

    if axes is None:
        fig, axes = plt.subplots(2, 2, figsize=(10, 10))
        ((ax_ps_cib, ax_cibxcib), (ax_cibxspi, ax_ps_spi)) = axes


    plot_ciber(wave1=1.1, wave2=1.1, ax=ax_ps_cib, color='k')
    plot_ciber(wave1=1.6, wave2=1.6, ax=ax_ps_cib, color='b')
    plot_ciber(wave1=1.1, wave2=1.6, ax=ax_cibxcib, color='c')
    plot_ciber(wave1=1.1, wave2=3.6, ax=ax_cibxspi, color='orange')
    plot_ciber(wave1=1.6, wave2=3.6, ax=ax_cibxspi, color='m')
    plot_ciber(wave1=3.6, wave2=3.6, ax=ax_ps_spi, color='r')

    ax_ps_cib.annotate(r'$1.1\mu\rm{m}$,', (0.05, 0.95), color='k',
        xycoords='axes fraction', ha='left', va='top')
    ax_ps_cib.annotate(r'$1.6\mu\rm{m}$', (0.3, 0.95), color='b',
        xycoords='axes fraction', ha='left', va='top')
    ax_cibxcib.annotate(r'$1.1\mu\rm{m} \ x \ 1.6\mu\rm{m}$', (0.05, 0.95),
        color='c', xycoords='axes fraction', ha='left', va='top')
    ax_cibxspi.annotate(r'$1.1\mu\rm{m} \ x \ 3.6\mu\rm{m}$', (0.05, 0.95),
        color='orange', xycoords='axes fraction', ha='left', va='top')
    ax_cibxspi.annotate(r'$1.6\mu\rm{m} \ x \ 3.6\mu\rm{m}$', (0.05, 0.87),
        color='magenta', xycoords='axes fraction', ha='left', va='top')


    ax_ps_spi.annotate(r'$3.6\mu\rm{m}$', (0.05, 0.95), color='r',
        xycoords='axes fraction', ha='left', va='top')

    fig.text(0.05, 0.5,
        r'$\sqrt{\ell (\ell+1) C_{\ell} / 2\pi} \ [\rm{nW} \ \rm{m}^{-2} \ \rm{sr}^{-1}]$',
        rotation=90, fontsize=24, ha='right', va='center')
    ax_cibxspi.set_xlabel(r'$\ell$', fontsize=24)
    ax_ps_spi.set_xlabel(r'$\ell$', fontsize=24)

    ax_ps_cib.set_xticklabels([])
    ax_cibxcib.set_xticklabels([])

    ax_cibxcib.set_yticklabels([])
    ax_ps_spi.set_yticklabels([])

    fig.subplots_adjust(hspace=0.1, wspace=0.1)

    return fig, axes


def plot_ebl_spectrum(ax=None, fig=1, show_akari=True, show_zodi=[1,6],
    show_new_horizons=True, show_irts=True, show_ciber=True,
    show_dgl=True, show_dirbe=True, show_pioneer=True, show_dark_cloud=False,
    show_igl=True, show_gamma_ray=True, annotate=True, fig_kwargs={}):
    """
    Make a nice-ish plot of the EBL spectrum.

    Parameters
    ----------
    ax : matplotlib.axes._subplots.AxesSubplot
        If None, will initialize a new plot.
    fig : int, matplotlib.figure.Figure
        Pre-existing figure object or an integer that will be used as the
        ID number for a new plot window.
    show_* : bool
        Whether or not to show constraints from given observation, hopefully
        self-explanatory.

    Returns
    -------
    A tuple containing instances of the following:
        (matplotlib.figure.Figure, matplotlib.axes._subplots.AxesSubplot)

    """

    if ax is None:
        fig, ax = plt.subplots(1, 1, num=fig, **fig_kwargs)

    ##
    # Zodiacal light models
    if show_zodi:
        zodi = np.loadtxt(f'{PATH}/data/zodi_extrap.csv',
            delimiter=' ', unpack=True)
        dist = np.arange(1, 8, 1)

        if type(show_zodi) not in [list, tuple, np.ndarray]:
            show_zodi = [show_zodi]

        for _d_ in show_zodi:
            i = np.argmin(np.abs(_d_ - dist))
            ax.plot(zodi[0], zodi[1+i], ls='-', color='gray')

            if annotate:
                j = np.argmin(np.abs(zodi[0] - 1.))
                ax.annotate(f'Zodi at {dist[i]} AU',
                    (zodi[0,j], 0.9 * zodi[1+i,j]),
                    rotation=-15, color='gray', fontsize=10,
                    ha='center', va='bottom')

    ##
    # DGL models
    if show_dgl:
        ohmb = 2.
        x, y = np.loadtxt(f'{PATH}/data/zda04_bc03.dat', unpack=True)
        x = x / 1e4
        y = y * ohmb * 1.73
        plt.plot(x, y, color='forestgreen', ls='--')

        if annotate:
            i = np.argmax(y)
            ax.annotate(r'DGL (ZDA04)', (x[i], 1.3 * y[i]),
                rotation=0, color='forestgreen', fontsize=16,
                ha='center', va='bottom')
    ##
    # AKARI measurements
    if show_akari:

        akari_l, akari_y, akari_e = np.loadtxt(f'{PATH}/data/akari_ebl.txt',
            delimiter=',', unpack=True)

        ax.errorbar(akari_l, akari_y, yerr=akari_e, fmt='+',
            color='rosybrown',
            zorder=1000)

        if annotate:
            i = np.argmax(akari_l + akari_e)
            ax.annotate(r'Akari', (akari_l[i], 1.2 * (akari_y[i]+akari_e[i])),
                rotation=0, color='rosybrown', fontsize=10,
                ha='center', va='bottom')

    ##
    # IRTS
    if show_irts:
        x, y, err = np.loadtxt(f'{PATH}/data/matsumoto2005.txt',
            unpack=True)
        ax.errorbar(x, y, yerr=err, fmt='+', color='orange')

        if annotate:
            i = np.argmax(y + err)
            ax.annotate(r'IRTS', (x[i], 1.2 * y[i]), color='orange', fontsize=10)

    ##
    # DIRBE
    if show_dirbe:
        # Cambresy 2001
        ax.errorbar(0.97 * np.array([1.25,1.25]), np.array([54.0,54.0]),
            yerr=np.array([16.8,16.8]), color='rosybrown', marker='D',
            zorder=1000)

        # Levenson 2007
        ax.errorbar(0.99*np.array([1.25,1.25]),2.99*np.array([8.9,8.9])/1.25,
            yerr=2.99*np.array([6.3,6.3])/1.25,color='coral',marker='D',
            zorder=1000)

        # Wright 2001 - http://iopscience.iop.org/article/10.1086/320942/pdf
        ax.errorbar(1.01*np.array([1.25,1.25]),np.array([28.9,28.9]),
            yerr=np.array([16.3,16.3]),color='lightcoral',marker='D',
            zorder=1000)

        # Wright 2004 - http://adsabs.harvard.edu/abs/2004NewAR..48..465W
        ax.errorbar(1.03*np.array([1.25,1.25]),np.array([28.0,28.0]),
            yerr=np.array([15,15]),color='lightsalmon',marker='D',
            zorder=1000)

        # Sano 2015
        ax.errorbar(np.array([1.25,2.2]),np.array([60.2,27.7]),
            yerr=np.array([16.1,6.2]),linestyle='',color='tomato',marker='D',
            zorder=1000)

        # Sano 2016
        ax.errorbar(np.array([3.5,4.9]),np.array([8.9,2.7]),
            yerr=np.array([3.4,15]),linestyle='',color='chocolate',marker='D',
            zorder=1000)

        if annotate:
            ax.annotate(r'DIRBE', (1.1, 1e2), color='coral', fontsize=10)


    ##
    # New Horizons
    if show_new_horizons:
        ax.plot(np.array([0.440, 0.870]), np.array([19.3, 19.3]),
            color='red', linestyle='-', linewidth=1, zorder=1000)
        ax.errorbar([np.sqrt(0.44*0.870)], [19.3], yerr=9,
            uplims=True, color='red', linewidth=1, zorder=1000)

        if annotate:
            ax.annotate(r'New Horizons',
                (10**np.mean(np.log10([0.440, 0.870])), 1.05 * 19.3),
                color='r', ha='center', va='bottom', fontsize=10, zorder=1000)

    ##
    # Pioneer
    if show_pioneer:
        # matsuoka et al 2011
        ax.errorbar(np.asarray([0.44,0.44]),np.asarray([7.9,7.9]),yerr=np.asarray([4.0,4.0]),marker='o',color='darkred')
        ax.errorbar(np.asarray([0.64,0.64]),np.asarray([7.7,7.7]),yerr=np.asarray([5.8,5.8]),marker='o',color='darkred')
        ax.plot([0.3950,0.4850],[7.9,7.9],color='darkred',linestyle='-',
            zorder=1000)
        ax.plot([0.59,0.69],[7.7,7.7],color='darkred',linestyle='-',
            zorder=1000)

        # Toller 1983
        ax.plot([0.44],[19.8],marker='o',color='darkred')
        ax.errorbar([0.44],[19.8],yerr=6, uplims=True,color='darkred')
        ax.plot([0.44],[19.8],marker='o',color='darkred')

        if annotate:
            ax.annotate(r'Pioneer', (0.45, 25), color='darkred', fontsize=10,
                ha='right', va='bottom')

    ##
    # CIBER
    if show_ciber:

        # Zemcov+ 2014
        ax.errorbar([1.1], [16.7], yerr=[[4],[5]], color='indianred', fmt='p')
        ax.errorbar([1.6], [20.4], yerr=[[5.1],[6]], color='indianred', fmt='p')

        # Matsuura+ 2017
        mat_wl, mat_il, mat_er = np.loadtxt(f'{PATH}/data/matsuura2017.txt',
            delimiter=',', unpack=False)

        #mat_wl=np.array([1.05,1.11,1.18,1.25,1.33,1.42,1.51,1.60,1.70])
        #mat_il=np.array([7.91,15.39,12.86,20.13,24.27,28.68,23.79,27.05,24.82])
        #mat_er=np.array([3.83,3.44,3.18,3.05,2.84,2.99,3.52,3.79,3.016])

        ax.errorbar(mat_wl, mat_il, yerr=mat_er, color='orangered',
            fmt='p')

        if annotate:
            i = np.argmax(mat_il + mat_er)
            ax.annotate(r'CIBER', (mat_wl[i], 0.7 * (mat_il[i] - mat_er[i])),
                color='r', ha='center', va='bottom', fontsize=10)

    ##
    # dark cloud Mattila 2017
    if show_dark_cloud:

        ax.errorbar([0.400], [11.6], yerr=[[4.4],[4.4]], color='dimgrey',
            fmt='s')
        ax.errorbar([0.430], [20.0], yerr=[10], uplims=True, color='dimgrey',
            fmt='s')
        ax.errorbar([0.520], [23.4], yerr=[10], uplims=True, color='dimgrey',
            fmt='s')

    ##
    # IGL
    if show_igl:
        lmadau=[0.36,0.45,0.67,0.81,1.1,1.6,2.2]
        fmadau=[2.87,4.57,6.74,8.04,9.71,9.02,7.92]
        errmadauup=[0.58,0.73,1.25,1.62,3.00,2.62,2.04]
        errmadaudn=[0.42,0.47,0.94,0.92,1.90,1.68,1.21]

        errmadau = np.vstack((errmadaudn,errmadauup))

        ax.errorbar(lmadau,fmadau,yerr=errmadau,fmt='o',color='blue')

        ####
        ## Totani (2001) - Subaru
        ## http://adsabs.harvard.edu/abs/2001ApJ...550L.137T
        ltot=[0.3,0.45,0.61,0.81,1.25,2.2]
        ftot=[2.7,4.4,6.0,8.1,10.9,8.3]
        errtot=[0.3,0.4,0.6,0.8,1.1,0.8]

        plt.errorbar(ltot,ftot,yerr=errtot,linestyle='',marker='o',color='blue')

        ####
        ## Fazio (2004) - Spitzer 3.5 um, best expressed as an upper limt
        ## http://adsabs.harvard.edu/abs/2004ApJS..154...39F
        lfaz=[3.6]
        fazkjy=[5.4]
        ferr = 2.0
        fup = np.array([1,0]*5)

        ax.errorbar(lfaz,fazkjy,yerr=ferr,uplims=True,linestyle='',marker='o',\
                     color='blue')

        # Gardner 2000 - http://adsabs.harvard.edu/abs/2000ApJ...542L..79G
        ax.errorbar([0.2365],[3.6],yerr=[[0.5],[0.7]],marker='s',color='dodgerblue',markerfacecolor='none',linestyle='')
        #ax.annotate(r'STIS',xy=(0.0,0.0),xytext=(0.165,0.4),xycoords='figure fraction',textcoords='figure fraction',rotation=360+0,color='black',fontsize=10)

        # Keenan 2010
        ax.errorbar([0.99*1.25],[11.7],yerr=[[2.6],[5.6]],marker='>',color='blue',linestyle='')
        ax.errorbar([0.99*1.6],[11.5],yerr=[[1.5],[4.5]],marker='>',color='blue',linestyle='')

        if annotate:
            ax.annotate(r'IGL', (0.32, 5), color='b',
                ha='left', va='bottom', fontsize=16)

    ##
    # Show gamma-ray constraints
    if show_gamma_ray:
        xup, yup = np.loadtxt(f'{PATH}/data/aharonian2014_up.txt',
            delimiter=',', unpack=True)
        xdn, ydn = np.loadtxt(f'{PATH}/data/aharonian2014_dn.txt',
            delimiter=',', unpack=True)

        x = np.hstack((xup,xdn[::-1]))
        y = np.hstack((yup,ydn[::-1]))

        ax.fill_between(x, y, color='#fed976', alpha=0.7)

        if annotate:
            ax.annotate(r'$\gamma$-ray EBL', (0.3, 6), color='#fed976',
                ha='left', va='center', fontsize=16)


    # Nice labels
    ax.set_xlabel(r'$\lambda \ [\mu\rm{m}]$', fontsize=24)
    ax.set_ylabel(r'$\lambda I_{\lambda} \ [\rm{nW} \ \rm{m}^{-2} \ \rm{sr}^{-1}]$', fontsize=24)
    ax.set_yscale('log')
    ax.set_xscale('log')
    ax.set_xlim(0.3, 6)
    ax.set_ylim(1e-3, 1e3)

    return fig, ax
