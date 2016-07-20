# for calculating pcorr

import sys
from FuncParcel import *
from functools import partial
from multiprocessing import Pool
from itertools import product
import time

#pool = Pool(4)

# script to do partial corr

subject = sys.stdin.read().strip('\n')

ts_path = '/home/despoB/connectome-thalamus/NotBackedUp/TS/'

pcorr_path = '/home/despoB/kaihwang/Rest/NotBackedUp/ParMatrices/'

fn = ts_path + subject + '_Morel_Mask_IJK_3mm_TS_000.netts'
thalamus_ts = np.loadtxt(fn)

fn = ts_path + subject + '_Gordon_333_3mm_TS_000.netts' 
cortical_roi_ts = np.loadtxt(fn)

pcorr_mat = pcorr_subcortico_cortical_connectivity(thalamus_ts, cortical_roi_ts)

fn = pcorr_path + subject + '_Gordon_plus_Morel_Thalamus_pcorr_mat'
#np.savetxt(fn, pcorr_mat, fmt='%.4f')
save_object(pcorr_mat, fn)