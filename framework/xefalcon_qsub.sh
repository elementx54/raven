#!/bin/bash

date

source ~/loadraven.source

#Change to directory with the input file
# This should be the directory that the script was run from
echo $PBS_O_WORKDIR
cd $PBS_O_WORKDIR
#Count number of processors
myprocs=`cat $PBS_NODEFILE | wc -l`
echo $myprocs

#Link log with job log
JOB_NUM=${PBS_JOBID%\.*}
if [ $PBS_O_WORKDIR != $HOME ]
then
ln -s $HOME/$PBS_JOBNAME.o$JOB_NUM $PBS_JOBNAME.o$JOB_NUM
fi

# Section to run!
which python
which mpiexec
echo $COMMAND
$COMMAND

#End of script
echo "Finishing..."
date

#Remove the link and move the job file
if [ $PBS_O_WORKDIR != $HOME ]
then
rm $PBS_JOBNAME.o$JOB_NUM
mv $HOME/$PBS_JOBNAME.o$JOB_NUM $PBS_JOBNAME.o$JOB_NUM
fi
