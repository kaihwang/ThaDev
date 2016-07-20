import pandas as pd


subjlist = pd.read_csv('Data/abide_subs.csv')

#control subjects that passed QC, younger than 30, mean FD frames <10%
control_list = subjlist[(subjlist.DX_GROUP==2) & (subjlist.qc_rater_1=="OK") & (subjlist.qc_anat_rater_3=="OK") & (subjlist.qc_anat_rater_2=="OK") & (subjlist.func_perc_fd<10) & (subjlist.AGE_AT_SCAN<30)]
control_list.FILE_ID.to_csv('list_of_controls', index=False)

#ASD subjects that passed QC, younger than 30, mean FD frames <10%
ASD_list = subjlist[(subjlist.DX_GROUP==1) & (subjlist.qc_rater_1=="OK") & (subjlist.qc_anat_rater_3=="OK") & (subjlist.qc_anat_rater_2=="OK") & (subjlist.func_perc_fd<10) & (subjlist.AGE_AT_SCAN<30)]
ASD_list.FILE_ID.to_csv('list_of_ASD', index=False)