import os, re, sys, tarfile, zipfile
try:
    from urllib.request import urlretrieve # this option only true with Python3
except:
    from urllib import urlretrieve

dataset = sys.argv[1]

##
# Download CIBER data.
if dataset in ['ciber', 'all']:
    path = 'http://ciber.caltech.edu/zemcovetal/data'
    all_fn = 'zemcovetal_1.1x1.1.txt', \
             'zemcovetal_1.6x1.6.txt', \
             'zemcovetal_1.1x1.6.txt', \
             'zemcovetal_1.1x3.6.txt', \
             'zemcovetal_1.6x3.6.txt', \
             'zemcovetal_3.6x3.6.txt'

    if not os.path.exists('data/ciber'):
        os.mkdir('data/ciber')

    for fn in all_fn:
        print(f"Downloading {fn}...")
        urlretrieve(f'{path}/{fn}', f'data/ciber/{fn}')
