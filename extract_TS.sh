# extract ROI and thalamus TS, for later pcorr calculation

WD='/home/despoB/kaihwang/Rest/ABIDE'

#cd ${WD}/func_preproc/

for s in KKI_0050815; do #$(cat /home/despoB/kaihwang/bin/ThaDev/list_of_controls)

	mkdir /tmp/KH_${s}/
	#cd ${WD}/func_preproc/

	if [ -e ${WD}/func_preproc/${s}_func_preproc.nii.gz ]; then
		for roi in Gordon_333_3mm Morel_Mask_IJK_3mm; do
			3dNetCorr \
			-inset ${WD}/func_preproc/${s}_func_preproc.nii.gz \
			-in_rois /home/despoB/kaihwang/Rest/ABIDE/ROIs/${roi}.nii.gz \
			-ts_out \
			-prefix /tmp/KH_${s}/${s}_${roi}_TS

			mv /tmp/KH_${s}/${s}_${roi}_TS_000.netts /home/despoB/connectome-thalamus/NotBackedUp/TS/		
		done
	fi

	rm -rf /tmp/KH_${s}/

	echo ${s} | python /home/despoB/kaihwang/bin/ThaDev/pcorr.py 
done