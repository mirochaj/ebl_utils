"""

read.py

Author: Jordan Mirocha
Affiliation: JPL / Caltech
Created on: Sat Dec 16 13:35:11 PST 2023

Description:

"""

import os
import importlib

def list_experiments():
    all_exp = []
    data = importlib.import_module(f'ebl_utils.data')

    for fn in os.listdir(data.__path__[0]):
        # Hacky way to figure out if this is for a single paper
        if ('19' in fn) or ('20' in fn):
            continue
        if fn.startswith('__'):
            continue

        all_exp.append(fn.split('.py')[0])

    return all_exp

def list_datasets():
    all_dat = []
    data = importlib.import_module(f'ebl_utils.data')

    for fn in os.listdir(data.__path__[0]):
        # Hacky way to figure out if this is for a single paper
        if ('19' not in fn) and ('20' not in fn):
            continue
        if fn.startswith('__'):
            continue

        all_dat.append(fn.split('.py')[0])

    return all_dat

def list_models():
    all_dat = []
    data = importlib.import_module(f'ebl_utils.models')

    for fn in os.listdir(data.__path__[0]):
        if fn.startswith('__'):
            continue

        all_dat.append(fn.split('.py')[0])

    return all_dat

def read(prefix, path=None, verbose=True):
    """
    Read data from the literature.

    Parameters
    ----------
    prefix : str
        Everything preceeding the '.py' in the name of the module.
    path : str
        If you want to look somewhere besides ebl_utils/data, provide
        that path here.
    """

    is_data = False
    is_model = False
    # First: try to import from ares.data (i.e., right here)
    try:
        mod = importlib.import_module(f'ebl_utils.data.{prefix}')
        is_data = True
        return mod
    except ModuleNotFoundError:
        try:
            mod = importlib.import_module(f'ebl_utils.models.{prefix}')
            is_model = True
            return mod
        except ModuleNotFoundError:
            pass

    if path is not None:
        loc = path
    else:
        fn = f"{prefix}.py"
        has_local = os.path.exists(os.path.join(os.getcwd(), fn))

        # Load custom defaults
        if has_local:
            loc = os.getcwd()
        elif is_data:
            loc = 'data'
        elif is_model:
            loc = 'models'
        else:
            raise NotImplemented('help')

    mod = importlib.__import__(f"{loc}/{prefix}")

    # Save this for sanity checks later
    mod.path = loc

    return mod
