import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['pdf.fonttype'] = 42
from scipy.stats import pearsonr
import json
import argparse
from pydscatter import pydscatter

parser = argparse.ArgumentParser()
parser.add_argument('bed', help='The BED file containing predictions merged with ground truth.')
parser.add_argument('o', help='Output file name, wihtout file type suffix.')
args = parser.parse_args()

fname = args.bed
oname = args.o

def plot_TPM(vec_true, vec_pred, oname):    

    order = np.argsort(vec_true)
    vec_true = np.array(vec_true)[order]
    vec_pred = np.array(vec_pred)[order]

    col, F, ctrs1, ctrs2 = pydscatter(np.log10(vec_true), np.log10(vec_pred), lamb=50)

    m, b = np.polyfit(vec_true, vec_pred, 1)

    fig, axs = plt.subplots(figsize=(4, 3))

    axs.scatter(vec_true, vec_pred, 5, col)
    axs.plot(vec_true, m*vec_true + b, '-r')
    axs.set_xscale('log')
    axs.set_yscale('log')
    # plt.axis('equal')
    axs.set_title("Pearson's correlation: %.3f"%(r))
    axs.set_xlabel('TPM for ground truth PAS')
    axs.set_ylabel('TPM for prediction PAS')

    plt.savefig(oname + '.png', dpi=300, bbox_inches='tight')
    plt.show()

out = pd.read_csv(fname, delimiter='\t')

# initialize vectors for ground truth sites and prediction
vec_true = []
vec_pred = []

# multiple predicted sites for one ground truth?
multiple_predicted_sites = out.duplicated(['chrom_g', 'chromStart_g', 'chromEnd_g', 'strand_g'], keep=False)

# iterate over matched sites
for (idx, row), is_mult in zip(out.iterrows(), multiple_predicted_sites):
    if is_mult:
        # sum up all prediction sites that were assigned to this ground truth site
        # needs to be implemented or can be skipped for now since these are usually only a few
        pass
    elif row['score_g'] == 0: # if there was no ground truth match, expression was set to 0 and the site is excluded
        pass
    else:
        vec_true.append(row['score_g'])
        # weighted expression in case there are multiple ground truth sites for one predicted site
        vec_pred.append(row['score_p']*row['weight'])

# correlation coefficient
r = pearsonr(vec_true, vec_pred)[0]

plot_TPM(vec_true, vec_pred, oname)
