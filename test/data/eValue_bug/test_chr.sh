#!/bin/bash

MY_STELLAR=/home/evelin/DREAM-Stellar/dream_stellar/build/bin/stellar
STELLAR=/home/evelin/DREAM-Stellar/stellar/build/bin/stellar

errRate=0.05
minLen=10

query_file=query_e${errRate}.fasta

$MY_STELLAR -e $errRate -l $minLen --suppress-runtime-printing -o my_stellar_full.gff ref.fasta $query_file > my_stellar_full.stdout 

$STELLAR -e $errRate -l $minLen --suppress-runtime-printing -o stellar_full.gff ref.fasta $query_file > stellar_full.stdout 

$MY_STELLAR -e $errRate -l $minLen --suppress-runtime-printing -o my_stellar_chr3.gff ref_chr3.fasta $query_file > my_stellar_chr3.stdout 

$STELLAR -e $errRate -l $minLen --suppress-runtime-printing -o stellar_chr3.gff ref_chr3.fasta $query_file > stellar_chr3.stdout 
