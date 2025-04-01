import numpy as np
import pandas as pd
import pickle

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.gridspec import GridSpec
from matplotlib import rcParams
rcParams['font.family'] = 'arial'

# Fe
data_fe_all = pickle.load(open('DATA/data_fe_all_modified.pkl', 'rb'))
data_fe_all1 = pickle.load(open('DATA/data_fe_all1_modified.pkl', 'rb'))

# SiO2
data_sio2_all = pickle.load(open('DATA/data_sio2_all.pkl', 'rb'))
data_sio2_stix = pickle.load(open('DATA/data_sio2_stix.pkl', 'rb'))
t11_py_cot = pd.read_csv('DATA/t11_pr_cot.csv')
t11_cot_fe2p = pd.read_csv('DATA/t11_cot_fe2p.csv')
o05_py = pd.read_csv('DATA/oga05_pyrite.csv')

# MgO
data_mgo_all = pickle.load(open('DATA/data_mgo_all_modified.pkl', 'rb'))

# MgSiO3
data_mgsio3_all = pickle.load(open('DATA/data_mgsio3_all.pkl', 'rb'))
data_mgsio3_all1 = pickle.load(open('DATA/data_mgsio3_all1.pkl', 'rb'))
um17_1 = pd.read_csv('DATA/um17_mgsio3.csv',header=None)
um17_2 = pd.read_csv('DATA/um17_mgsi2o5.csv',header=None)
um17_3 = pd.read_csv('DATA/um17_mg2sio4.csv',header=None)

# Define scale conversion and marker/line settings
cm_scale = 1 / 2.54
ms, ms_old, ac_old, lw, lw_old = 4, 10, 0.6, 0, 0.8

# Create figure and axis using GridSpec
fig = plt.figure(figsize=(14 * cm_scale, 6 * cm_scale), dpi=300)
gs = GridSpec(1, 1, bottom=0.1, top=0.9, left=0.1, right=0.9, hspace=0.05, wspace=0.3)
ax = fig.add_subplot(gs[0])

# Plot contours for SiO2 data
ax.contour(data_sio2_all['pres'], data_sio2_all['temp'], data_sio2_all['phase'],
           colors='y', alpha=1, linewidths=1, zorder=0)
ax.contour(data_sio2_stix['pres'], data_sio2_stix['temp'], data_sio2_stix['phase'],
           colors='y', alpha=1, linewidths=1, zorder=0)

# Plot additional lines (all with similar style settings)
ax.plot(t11_py_cot['pres'][:31], t11_py_cot['temp'][:31], ls=':', lw=1, color='y')
ax.plot(t11_cot_fe2p['pres'], t11_cot_fe2p['temp'], ls=':', lw=1, color='y')
ax.plot([500, 1600], [9000, 13000], ls=':', lw=1, color='y')
ax.plot(o05_py['pres'] + 60, o05_py['temp'], ls=':', lw=1, color='y')
ax.plot([255, 240], [4000, 7000], ls=':', lw=1, color='y')

# Plot contours for Fe data
ax.contour(data_fe_all['pres'], data_fe_all['temp'], data_fe_all['phase'],
           colors='r', alpha=1, linewidths=1, zorder=0)
ax.contour(data_fe_all1['pres'], data_fe_all1['temp'], data_fe_all1['phase'],
           colors='r', alpha=1, linewidths=1, zorder=0)

# Plot contours for MgO and MgSiO3 data
ax.contour(data_mgo_all['pres'], data_mgo_all['temp'], data_mgo_all['phase'],
           colors='b', alpha=1, linewidths=1, zorder=0)
ax.contour(data_mgsio3_all['pres'], data_mgsio3_all['temp'], data_mgsio3_all['phase'],
           colors='g', alpha=1, linewidths=1, zorder=0)
ax.contour(data_mgsio3_all1['pres'], data_mgsio3_all1['temp'], data_mgsio3_all1['phase'],
           colors='g', alpha=1, linewidths=1, zorder=0)

# Plot dashed green lines
ax.plot(um17_1[0][2:51], um17_1[1][2:51], ls='--', color='g', alpha=1, linewidth=1, zorder=0)
ax.plot(um17_2[0][:48], um17_2[1][:48], ls='--', color='g', alpha=1, linewidth=1, zorder=0)
ax.plot(um17_3[0][:43], um17_3[1][:43], ls='--', color='g', alpha=1, linewidth=1, zorder=0)

# Set axis limits and scales
ax.set_xlim([5, 6000])
ax.set_ylim([500, 50000])
ax.set_xscale('log')
ax.set_yscale('log')

# Configure ticks and labels
ax.tick_params(labelsize=8, direction='in', which='both')
ax.minorticks_on()
ax.set_xticks([10, 100, 1000])
ax.set_xticklabels(['10', '100', '1000'])
ax.set_yticks([300, 1000, 3000, 10000, 30000])
ax.set_yticklabels(['300', '1000', '3000', '10000', '30000'])
ax.set_xlabel('Pressure (GPa)', fontsize=8, labelpad=5)
ax.set_ylabel('Temperature (K)', fontsize=8, labelpad=5)

# Create custom legend
custom_lines = [
    Line2D([0], [0], ls='-', color='b', lw=1),
    Line2D([0], [0], ls='-', color='y', lw=1),
    Line2D([0], [0], ls='-', color='green', lw=1),
    Line2D([0], [0], ls='-', color='red', lw=1)
]
ax.legend(custom_lines, ['MgO', 'SiO$_{\mathregular{2}}$', 'MgSiO$_{\mathregular{3}}$', 'Fe'],
          loc='upper left', fontsize=6)

# Define text labels as tuples.
# Tuples of length 4: (x, y, label, color)
# Tuples of length 7: (x, y, label, color, rotation, fontsize, bbox)
texts = [
    (6.5, 1700, 'coes', 'y'),
    (35, 500, 'st', 'y'),
    (85, 500, 'cacl2', 'y'),
    (160, 500, 'seif', 'y'),
    (420, 500, 'py', 'y'),
    (850, 7500, 'cot', 'y'),
    (1500, 500, 'fe2p', 'y'),
    (6, 1400, 'en', 'g'),
    (11, 1400, 'hpcen', 'g'),
    (19, 2340, 'mj', 'g'),
    (18, 1400, 'ak+', 'g'),
    (40, 2000, 'bg', 'g'),
    (180, 2000, 'ppv', 'g'),
    (850, 1500, 'Mg$_{\mathregular{2}}$SiO$_{\mathregular{4}}$ + MgSi$_{\mathregular{2}}$O$_{\mathregular{5}}$', 'g', 90, 4,
     dict(boxstyle="square,pad=0.1", fc='w', ec='w', lw=1, alpha=0)),
    (2000, 1500, 'Mg$_{\mathregular{2}}$SiO$_{\mathregular{4}}$ + SiO$_{\mathregular{2}}$', 'g', 90, 4,
     dict(boxstyle="square,pad=0.1", fc='w', ec='w', lw=1, alpha=0)),
    (4000, 4500, 'MgO + SiO$_{\mathregular{2}}$', 'g', 90, 4,
     dict(boxstyle="square,pad=0.1", fc='w', ec='w', lw=1, alpha=0)),
    (28, 1600, 'γ', 'r'),
    (8, 500, 'α', 'r'),
    (200, 900, 'ε', 'r'),
    (50, 1200, 'B1', 'b'),
    (2000, 3300, 'B2', 'b')
]

# Add text labels using a loop
for t in texts:
    if len(t) == 4:
        x, y, label, color = t
        ax.text(x, y, label, fontsize=6, ha="center", va="center", color=color, rotation=0)
    elif len(t) == 7:
        x, y, label, color, rot, fsize, bbox = t
        ax.text(x, y, label, fontsize=fsize, ha="center", va="center",
                color=color, rotation=rot, bbox=bbox)

# Save the figure
fig.savefig('fig8_phase_digrams.pdf', bbox_inches="tight")

# Plot the figure
plt.show()