#!/usr/local/anaconda/bin/python
# analyze ABIDE data to examine PC-Q and PC-Age relationships

import numpy as np
import os 
import sys
import pandas as pd
import glob


datapath = '/home/despoB/kaihwang/Rest/Graph/'
Atlases =['_Gordon_plus_Morel_3mm', '_Gordon_plus_WTA_3mm']

def compile_dataframe():
	'''compile data'''
	demographic_df = pd.read_csv('Data/abide_subs.csv')
	df = pd.DataFrame(columns = ['Subject', 'Group', 'Atlas', 'ROI', 'Age', 'Sex', 'Site', 'PC'])
	for sub in demographic_df['FILE_ID']:
		for atlas in Atlases:
			try: 
				PC = np.loadtxt(datapath + sub + atlas + '_pcorr_meanPC')
				tmp_df = pd.DataFrame()
				tmp_df['PC'] = PC
				tmp_df['ROI'] = np.arange(1,len(PC)+1, dtype=int) 
				tmp_df['Atlas'] = atlas[1:]
				tmp_df['Subject'] = sub
				tmp_df['Group'] = np.squeeze([demographic_df[demographic_df['FILE_ID']==sub]['DX_GROUP'].values]*len(PC))
				tmp_df['Age'] = np.squeeze([demographic_df[demographic_df['FILE_ID']==sub]['AGE_AT_SCAN'].values]*len(PC))
				tmp_df['Site'] = np.squeeze([demographic_df[demographic_df['FILE_ID']==sub]['SITE_ID'].values]*len(PC))
				tmp_df['Sex'] = np.squeeze([demographic_df[demographic_df['FILE_ID']==sub]['SEX'].values]*len(PC))
				df = df.append(tmp_df,  ignore_index=True)
			except:
				continue
	return df


if __name__ == "__main__":

	df = compile_dataframe()
	df.to_csv('Data/pcdata.csv')

	PCcorr =[]
	for i in np.arange(1,np.max(df['ROI'])+1):
		PC = df[(df['Atlas']=='Gordon_plus_WTA_3mm') & (df['ROI']==i)]['PC'].values
		age = df[(df['Atlas']=='Gordon_plus_WTA_3mm') & (df['ROI']==i)]['Age'].values	
		PCcorr += [np.corrcoef(PC[~np.isnan(age)],age[~np.isnan(age)])[0,1]]