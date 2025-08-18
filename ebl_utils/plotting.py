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
from .read import read as read_data, list_models, list_experiments

label_flux = r'$\nu I_{\nu} \ [\rm{nW} \ \rm{m}^{-2} \ \rm{sr}^{-1}]$'
label_wave = r'$\lambda \ [\mu\rm{m}]$'
label_power = r'$\sqrt{\ell(\ell+1) C_{\ell}} \ [\rm{nW} \ \rm{m}^{-2} \ \rm{sr}^{-1}]$'

def plot_ebl_spectrum(ax=None, fig=1, fig_kwargs={},
    include_datasets='all', include_models='all',
    color_by=None, use_newest=True, show_as_band=True,
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
    fig_kwargs : dict, optional
        Can provide a dictionary of optional keyword arguments that will be
        passed along to `subplots`, e.g., 'figsize'.
    include_datasets : str, list, bool, None
        List of datasets to include in plot, e.g., ['pioneer', 'ciber'].
        Can also set to False or None to skip data.
    include_models : str, list, bool, None
        List of models to include in plot, e.g., ['helgason2012', 'driver2016'].
        Can also set to False or None to skip data.
    show_as_band : bool
        For models, if True, will use `fill_between` to shade between the +/-
        boundaries of the model.

    Returns
    -------
    A tuple containing instances of the following:
        (matplotlib.figure.Figure, matplotlib.axes._subplots.AxesSubplot)

    """

    if ax is None:
        fig, ax = plt.subplots(1, 1, **fig_kwargs)

    if include_datasets == 'all':
        include_datasets = list_experiments()
    elif include_datasets in [False, None]:
        include_datasets = []

    if include_models == 'all':
        include_models = list_models()
    elif include_models in [False, None]:
        include_models = []

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

        if err is None:
            ax.plot(x, y, label=data.name, **kwargs)
            continue

        # Plot it
        y = np.array(y)
        err = np.array(err)

        if err.ndim == 1:
            if show_as_band:
                ax.fill_between(x, y-err, y+err, label=data.name, **kwargs)
            else:
                ax.errorbar(x, y, yerr=err, fmt='o',
                    label=data.name, **kwargs)
        else:
            if show_as_band:
                ax.fill_between(x, y-err.T[1], y+err.T[0], label=data.name, **kwargs)
            else:
                ax.errorbar(x, y, yerr=err[:,-1::-1].T, fmt='o',
                    label=data.name, **kwargs)

    ##
    # Make nice
    ax.set_xlabel(label_wave, fontsize=24)
    ax.set_ylabel(label_flux, fontsize=24)
    ax.set_yscale('log')
    ax.set_xscale('log')

    ax.set_xticks([1,2,3,4,5], minor=False)
    ax.set_xticks(np.arange(0.1, 1, 0.1), minor=True)
    ax.set_xticklabels(['1', '2', '3', '4', '5'])

    ax.set_xlim(0.1, 6)
    ax.set_ylim(1, 100)

    fig.subplots_adjust(left=0.2, bottom=0.2)

    ##
    # Done
    return fig, ax

def plot_anisotropy_color(fig=None, ax=None, fig_kwargs={}, ell_bin=(500, 1e3),
    include_datasets=['ciber', 'akari', 'hubble', 'spitzer'],
    binning_method='closest',
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

            if dset.power_units.startswith('nw^2'):
                ps = np.sqrt(ps)
                # Need to fix errors too
            else:
                pass

            err = np.array(err)

            for i, wave in enumerate(waves):

                print('hi', i, dset.name, ok.sum(), np.array(ps)[i,ok==1])

                if binning_method in ['avg', 'mean']:
                    ax.errorbar(wave, np.array(ps)[i,ok==1].mean(),
                        yerr=err[i,ok==1].mean(), fmt='o',
                        label=data.name, **kwargs)

                    continue
                elif binning_method.startswith('close'):
                    y = np.array(ps)[i,ok==1]
                    ax.errorbar(wave, y[np.argmin(np.abs(x[ok==1] - np.mean(ell_bin)))],
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
    ax.set_xlabel(label_wave, fontsize=24)
    ax.set_ylabel(label_power, fontsize=24)

    ax.set_yscale('log')
    ax.set_xscale('log')
    ax.set_xticks([1,2,3,4,5], minor=False)
    ax.set_xticks(np.arange(0.1, 1, 0.1), minor=True)
    ax.set_xticklabels(['1', '2', '3', '4', '5'])

    ax.set_xlim(0.1, 6)
    ax.set_ylim(1e-2, 10)

    fig.subplots_adjust(left=0.2, bottom=0.2)

    return fig, ax
