
name = 'Kashlinsky et al. (2012)'
year = 2012
link = 'https://ui.adsabs.harvard.edu/abs/2012ApJ...753...63K/abstract'
bibtex = \
"""
@ARTICLE{2012ApJ...753...63K,
       author = {{Kashlinsky}, A. and {Arendt}, R.~G. and {Ashby}, M.~L.~N. and {Fazio}, G.~G. and {Mather}, J. and {Moseley}, S.~H.},
        title = "{New Measurements of the Cosmic Infrared Background Fluctuations in Deep Spitzer/IRAC Survey Data and Their Cosmological Implications}",
      journal = {\apj},
     keywords = {cosmology: observations, diffuse radiation, early Universe, Astrophysics - Cosmology and Nongalactic Astrophysics},
         year = 2012,
        month = jul,
       volume = {753},
       number = {1},
          eid = {63},
        pages = {63},
          doi = {10.1088/0004-637X/753/1/63},
archivePrefix = {arXiv},
       eprint = {1201.5617},
 primaryClass = {astro-ph.CO},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2012ApJ...753...63K},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}
"""
experiment = 'spitzer'

notes = \
"""
Notes:
- All data points extracted using plotdigitizer.com/app and so may not be
identical to the actual measurements in the paper. They should be pretty close,
however. This also explains the insane number of "significant" figures (I've
just copy-pasted what plotdigitizer gives you).
- On small scales the error bars are imperceptibly small on the plots, so have
been assigned an error of zero. This will obviously cause problems if you
try to use this data in a fit! Beware.
"""

_data = \
{
 'waves': [3.6, 4.5],
 'scales': [3.3587208342562045, 3.7678013477934096, 4.21642076665649,
    4.746127838788807, 5.324683900700283, 5.975291311308151, 6.691095076047526,
    7.486738810638138, 8.390611088985542, 9.477650990197212, 10.65842659132052,
    11.915870862740622, 13.247066338625126, 14.95529719650429, 16.753458878063313,
    18.826708091916768, 21.160450731279568, 23.639327763711815, 26.466876888997454,
    29.820947797960677, 33.41114382489407, 37.5266280574673,
    42.102125301232505, 47.24426713054064,  52.93454359726454,
    59.2620288103113, 66.50925415050594, 74.54236065996683, 84.11177014539754,
    94.51625877817263, 105.87803711188744, 118.53132687738442, 133.4688128276755,
    156.31035003412498, 190.43538937055305, 228.10290519612604, 271.70358190888885,
    376.45678407673677, 616.4005190515678,  1042.7008778966929, 2177.007029667999],
 'mean': [[0.05234185307763492,0.05502854491804953,0.05970094032356915,
    0.06295259878475597,0.06396855334636145,0.06385750625890652,
    0.06207848851591852,0.058636215804688724,0.0529735712362114,
    0.049367948714095916,0.045515543841676914,0.042989913428157035,
    0.040428438571053806,0.03782036154641948,0.03464046604950954,
    0.031653206493953735,0.029528047213744083,0.027085668258342015,
    0.02343367333323637,0.01945007264808319,0.017444980344341054,
    0.01592543301232412,0.013653924547601495,0.012703537860810316,
    0.010715053423156842,0.010448045200917565,0.009107636368881166,
    0.007989932237630738,0.00818734465258897,0.006941869593685512,
    0.00556869294889829,0.005519840146659663,0.007681064975515539,
    0.004739184275964023,0.00509605415939079,0.005091628955505264,
    0.002028792487887482,0.00393550116157109,0.004684024956518253,
    0.004092906954562224,0.01007578301661428],
    [0.019479253232669944,0.0216735602963903,0.024914918012655995,
     0.02675159008308366,0.02739246714695792,0.026866731662551838,
     0.026008291789029553,0.024513648696699697,0.022879705896660777,
     0.02183650096099006,0.021030560861829504,0.019443577071522587,
     0.019779457039921334,0.01764703961084997,0.016553812502476287,
     0.01562048773702762,0.014129750407145222,0.012660022427167466,
     0.011103343355976975,0.009686187966315799,0.007936825941339421,
     0.007236382610227865,0.00676254119756381,0.005787706088088108,
     0.004854256860177904,0.004612829273224026,0.003805160094796084,
     0.0031696359846526525,0.0031717949038126457,0.0027344088144620774,
     0.0023600555375634003,0.002302185134645178,0.0038295526240380343,
     0.0016222711997133424,0.0017007522781369044,0.002037806649563031,
     0.0010327629473942668,0.0017688913275329516,0.001468911217284971,
     0.0005869597142196108,0.0015842333921889124]
  ],
 'shot': [4.8e-11, 2.2e-11],
}

# Lower and upper edges of errorbars.
lo_36 = [0] * 20 + [0.01681646033922299,0.015287651723875173,
    0.012972256091332204,0.012010544759618665,0.01000558629196886,
    0.00979467476851445,0.008519036762210889,0.0074101482547616485,
    0.0075869557725709354,0.006418193365043493,0.00502862167401554,
    0.0049764714315639474,0.006660279009302534,0.004380766565058311,
    0.004498485838684407,0.004448335703641371,0.0016034840078678436,
    0.003317967079244363,0.003305773493957943,0.002562983905706542,
    0.004037077988104764]
hi_36 = [0] * 20 + [0.017675987761983005,
    0.01620321010915066,0.013867391349275802,0.0130066466407356,
    0.01102166470563834,0.010916390646441768,0.00946290085946025,
    0.008416401326917232,0.008703199653766753,0.00743809650267512,
    0.006124057825338282,0.006141817494537654,0.008677315533406706,
    0.0052139788751128825,0.00587393981237928,0.005925191146447514,
    0.002465027953346225,0.004503140622834648,0.006549350025179397,
    0.006247652861059601,0.02412916967950248]

lo_45 = [0] * 21 + [0.006880082045343966, 0.006486736057694129,
    0.005489780232647974,0.004481138913744279,0.004273461707230448,
    0.0035840441791993105,0.0029605358428619988,0.002926158115325439,
    0.002547741028451846,0.002174661868900773,0.002122004216449595,
    0.003378253460193281,0.0014753881043699235,0.0014666817580510625,
    0.001808613594857272,0.0008312620559227746,0.0014771665127860938,
    0.001014800036468567,0.0003793469178097528,0.0006224216602367518]

hi_45 = [0] * 21 + [0.00763069364542622, 0.006971128065234671,
    0.005918604871770445, 0.004914631898433929, 0.004786343540595095,
    0.003995725886161544, 0.003385515828274934, 0.003348657804930673,
    0.0029673664499178893,0.0025971877889504427,0.002588496355493997,
    0.004336822668471388, 0.0017960584587342523,0.0019571549076403644,
    0.0023841583675178416,0.0013183278574049326,0.002078989271735489,
    0.002041331884520336,0.0008968990149170687,0.0036532208883852573]



_data['bounds'] = []
_data['bounds'].append([(hi_36[i], lo_36[i]) for i in range(len(_data['scales']))])
_data['bounds'].append([(hi_45[i], lo_45[i]) for i in range(len(_data['scales']))])

masking_depth = [25, 25]
masking_waves = _data['waves']

#
data = _data.copy()

# Native dataset is q^2 P(q) / 2pi vs. 2pi/q [arcsec]
from math import pi
#q = 2 * pi / _data['scales']

# Placeholder
data['err'] = []
for i, wave in enumerate(data['waves']):
    data['err'].append([])
    for j, scale in enumerate(data['scales']):
        if data['bounds'][i][j][0] == 0:
            data['err'][i].append((0, 0))
            continue

        err = data['bounds'][i][j][0] - data['mean'][i][j], \
              data['mean'][i][j] - data['bounds'][i][j][1]
        data['err'][i].append(err)

scale_units = 'arcsec'
power_units = 'nW^2/m^4/sr^-2'

def get_ebl_anisotropies():
    return data['waves'], data['scales'], data['mean'], data['err']
