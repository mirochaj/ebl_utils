# **ebl_utils**

This repository is meant to facilitate easy plotting of pre-existing EBL measurements and models. The primary use case is in making custom plots for talks and papers.


Quick example
-------------
To get started, import:

```python
import ebl_utils
```  

To obtain a quick plot of the available mean EBL datasets and models, you can
do
```python
fig, ax = ebl_utils.plot_ebl_spectrum()
```
This will be kind of a mess, given that the default behavior is to plot everything we have. To see a full listing of what that includes, you can do

```python
print(ebl_utils.list_experiments())
```
or to see all the individual papers that report results from these experiments,
```python
print(ebl_utils.list_datasets())
```
Similarly, for models, you can do
```python
print(ebl_utils.list_models())
```
For a more controlled approach, you can provide specific datasets to be included via the `include_datasets` and `include_models` keyword arguments. See the links below for examples of how to access the data directly and make custom versions of plots.  

Accessing original datasets
---------------------------
All included datasets include links to the original paper, notes about where in the paper the data comes from, and a bibtex entry. These bits of information live in the `link`, `notes`, and `bibtex` attributes of each object, respectively. For example,


```python
h12 = ebl_utils.read('helgason2012')

print(h12.link)
```
We follow this `<lastnameoffirstauthor><year>` naming convention throughout.

If interested in the mean EBL spectrum, you're looking for the method `get_ebl_spectrum` in a dataset object, e.g.,

```python
waves, spec, err = h12.get_ebl_spectrum()

import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 1, num=1)
ax.plot(waves, spec)
ax.set_xlabel(ebl_utils.label_wave)
ax.set_ylabel(ebl_utils.label_flux)

# You can also make some plots automatically, e.g.,
ebl_utils.plot_ebl_spectrum(ax=ax, fig=fig, alpha=0.5,
  include_datasets=False, include_models=['helgason2012'])
# Or if you want to see the model predictions as points with error-bars:
ebl_utils.plot_ebl_spectrum(ax=ax, fig=fig, show_as_band=0,
  include_datasets=False, include_models=['helgason2012'])
```

For more examples, check out the Jupyter notebooks in `ebl_utils/docs/source`.

Disclaimers
-----------
Many datasets included in this repository have been transcribed by hand from tables in the relevant papers, and so should be an exact representation of the original work. In other cases, where results were not reported in tables, we have done our best to convert the data to electronic format via the [plot digitizer tool online](https://plotdigitizer.com/app), and indicated this in the `notes` attribute. If you are an original author of one of these works and would like to contribute the real measurements, please consider opening a pull request!

Next, a note about units. Constraints on the EBL are generally reported in $\nu I_{\nu}$ units of $\rm{nW} \ \rm{m}^{-2} \ \rm{sr}^{-1}$. For fluctuations, values are often reported in these same units, but might also be reported as $\rm{nW}^2 \ \rm{m}^{-4} \ \rm{sr}^{-2}$. Internally, we have made an effort to record the data in its native units, kept in the hidden attribute `_data`, but then add a conversion step for fluctuations to $\rm{nW}^2 \ \rm{m}^{-4} \ \rm{sr}^{-2}$ for consistency. Similarly, for studies that report power spectra in the Fourier basis, we convert angular scales to multipoles using the approximation $\ell \sim 180 / \theta$.

Note that several datasets report multiple results for the mean EBL fluctuations that correspond to different analysis choices, e.g., which Zodi or DGL model has been used. There is not currently a great way to alert users to this possibility, other than to accept keyword arguments in `get_ebl_spectrum` or `get_ebl_anisotropies`. We have attempted to be conservative in our choice of defaults, i.e., all default value choices are not indicative of a bias in favor one Zodi or DGL model over another.

Finally, some studies quote masking depths in Vega magnitudes. Again, for consistency, all Vega mags are converted to AB magnitudes in the `masking_depth` attribute of relevant datasets. At the moment, if you want to track this conversion, you'll have to navigate to the source code for now. We've taken conversion factors from [Timlin et al. (2016)](https://ui.adsabs.harvard.edu/abs/2016ApJS..225....1T/abstract), but note that slightly different values are listed by
[Gemini](https://www.gemini.edu/observing/resources/magnitudes-and-fluxes) and [IPAC](https://wise2.ipac.caltech.edu/docs/release/allsky/expsup/sec4_4h.html).

## External datasets

Much of the contents in this repository *are* data. However, in a few cases there are some files that have way more stuff than we'd like to transcribe here and/or track with git.

Our convention at the moment is to stick these files in `$HOME/.ebl_utils`. So, e.g, if you want to use the Driver et al. 2016 compilation of galaxy number counts, you need to download [this file](https://content.cld.iop.org/journals/0004-637X/827/2/108/revision1/apjaa28a0_table3.tar.gz), and unpack it in `$HOME/.ebl_utils`. 
