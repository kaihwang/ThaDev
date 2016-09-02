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
fn = ts_path + subject + '_Gordon_333_3mm_TS_000.netts' 
cortical_roi_ts = np.loadtxt(fn)

path_to_ROIs = '/home/despoB/connectome-thalamus/ROIs'
Cortical_CI = np.loadtxt(path_to_ROIs + '/Gordon_consensus_CI')
Cortical_ROIs = np.loadtxt(path_to_ROIs+'/Gordon_333', dtype = int)
Output_path = '/home/despoB/kaihwang/Rest/Graph/'
Thalamus_Parcels = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
CI = np.append(Cortical_CI, Thalamus_Parcels)
#np.append(Cortical_CI, Thalamus_Parcels)
Thalamus_parcel_positions = np.arange(len(Cortical_CI),len(np.append(Cortical_CI, Thalamus_Parcels)),1)


for mask in ['WTA_3mm']:
	fn = ts_path + subject + '_' + mask + '_TS_000.netts'
	thalamus_ts = np.loadtxt(fn)
	pcorr_mat = pcorr_subcortico_cortical_connectivity(thalamus_ts, cortical_roi_ts)
	pcorr_mat[np.isnan(pcorr_mat)]=0

	fn = pcorr_path + subject + '_Gordon_plus_' + mask + '_pcorr_mat'
	save_object(pcorr_mat, fn)

	_, _, cost_thresholds = map_subcortical_cortical_targets(pcorr_mat, Cortical_ROIs, Thalamus_parcel_positions)

	PCs = []
	for c in cost_thresholds:
		Par_adj = pcorr_mat.copy()
		Par_adj[Par_adj<c]=0
		PCs += [bct.participation_coef(Par_adj, CI)]

	mean_PC = np.sum(PCs,axis=0)/13.5

	fn = Output_path + subject + '_Gordon_plus_' + mask + '_pcorr_meanPC'
	np.savetxt(fn, mean_PC)
	fn = Output_path + subject + '_Gordon_plus_' + mask + '_pcorr_PCs'
	np.savetxt(fn, PCs)


	#full correlation
	adj = np.loadtxt(pcorr_path + subject + '_Gordon_plus_WTA_3mm_corrmat')
	adj[np.isnan(adj)]=0

	PCs = []
	for c in np.arange(0.01,0.16, 0.01):
		M = bct.threshold_proportional(adj, c, copy=True)
		PCs += [bct.participation_coef(M, CI)]

	mean_PC = np.sum(PCs,axis=0)/13.5
	fn = Output_path + subject + '_Gordon_plus_WTA_3mm_corr_meanPC'
	np.savetxt(fn, mean_PC)
	fn = Output_path + subject + '_Gordon_plus_WTA_3mm_corr_PCs'
	np.savetxt(fn, PCs)	