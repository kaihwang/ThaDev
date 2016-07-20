#WD='/home/despoB/connectome-thalamus'
SCRIPT='/home/despoB/kaihwang/bin/ThaDev'


for s in $(cat /home/despoB/kaihwang/bin/ThaDev/list_of_controls); do
	sed "s/KKI_0050815/${s}/g" < ${SCRIPT}/extract_TS.sh > ~/tmp/${s}.sh
	qsub -V -M kaihwang -m e -e ~/tmp -o ~/tmp ~/tmp/${s}.sh
done

for s in $(cat /home/despoB/kaihwang/bin/ThaDev/list_of_ASD); do
	sed "s/KKI_0050815/${s}/g" < ${SCRIPT}/extract_TS.sh > ~/tmp/${s}.sh
	qsub -V -M kaihwang -m e -e ~/tmp -o ~/tmp ~/tmp/${s}.sh
done