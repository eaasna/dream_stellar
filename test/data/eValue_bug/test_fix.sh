#!/bin/bash

FIXED_STELLAR=/home/evelin/DREAM-Stellar/dream_stellar/build/bin/stellar
STELLAR=/home/evelin/DREAM-Stellar/dream_stellar/master_build/bin/stellar

errRate=0.05
minLen=50

data_dir=/home/evelin/DREAM-Stellar/test-dream-stellar/reproduce-stellar/10Mb

ref_file=$data_dir/ref_rep0.fasta
query_file=$data_dir/query/with_insertions_rep0_e${errRate}.fasta

$STELLAR --verbose -e $errRate -l $minLen -o stellar_10Mb.gff $ref_file $query_file > stellar_10Mb.stdout 

#$FIXED_STELLAR --verbose -e $errRate -l $minLen -o fixed_stellar_10Mb.gff $ref_file $query_file > fixed_stellar_10Mb.stdout 
