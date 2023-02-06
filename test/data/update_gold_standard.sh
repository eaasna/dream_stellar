#!/bin/bash

/home/evelin/DREAM-Stellar/dream_stellar/debug/bin/stellar -r -e 0.1 -l 50 -x 10 -k 7 -n 5000 -s 10000 -v -no-rt --out /home/evelin/DREAM-Stellar/dream_stellar/test/cli/gold_standard/dna5_reverse/e-1.txt /home/evelin/DREAM-Stellar/dream_stellar/test/cli/512_simSeq1_e-1.fa /home/evelin/DREAM-Stellar/dream_stellar/test/cli/512_simSeq2_e-1.fa

/home/evelin/DREAM-Stellar/dream_stellar/debug/bin/stellar --alphabet dna5 --reverse --epsilon 0.05 --minLength 50 --xDrop 10 --kmer 7 --numMatches 5000 --sortThresh 10000 --verbose --suppress-runtime-printing --out /home/evelin/DREAM-Stellar/dream_stellar/test/cli/gold_standard/dna5_reverse/5e-2.txt /home/evelin/DREAM-Stellar/dream_stellar/test/cli/512_simSeq1_5e-2.fa /home/evelin/DREAM-Stellar/dream_stellar/test/cli/512_simSeq2_5e-2.fa

/home/evelin/DREAM-Stellar/dream_stellar/debug/bin/stellar --alphabet dna5 --reverse --epsilon 0.025 --minLength 50 --xDrop 10 --kmer 7 --numMatches 5000 --sortThresh 10000 --verbose --suppress-runtime-printing --out /home/evelin/DREAM-Stellar/dream_stellar/test/cli/gold_standard/dna5_reverse/25e-3.txt /home/evelin/DREAM-Stellar/dream_stellar/test/cli/512_simSeq1_25e-3.fa /home/evelin/DREAM-Stellar/dream_stellar/test/cli/512_simSeq2_25e-3.fa

/home/evelin/DREAM-Stellar/dream_stellar/debug/bin/stellar --alphabet dna5 --reverse --epsilon 0.075 --minLength 50 --xDrop 10 --kmer 7 --numMatches 5000 --sortThresh 10000 --verbose --suppress-runtime-printing --out /home/evelin/DREAM-Stellar/dream_stellar/test/cli/gold_standard/dna5_reverse/75e-3.txt /home/evelin/DREAM-Stellar/dream_stellar/test/cli/512_simSeq1_75e-3.fa /home/evelin/DREAM-Stellar/dream_stellar/test/cli/512_simSeq2_75e-3.fa

/home/evelin/DREAM-Stellar/dream_stellar/debug/bin/stellar --alphabet dna5 --reverse --epsilon 0.0001 --minLength 50 --xDrop 10 --kmer 7 --numMatches 5000 --sortThresh 10000 --verbose --suppress-runtime-printing --out /home/evelin/DREAM-Stellar/dream_stellar/test/cli/gold_standard/dna5_reverse/e-4.txt /home/evelin/DREAM-Stellar/dream_stellar/test/cli/512_simSeq1_e-4.fa /home/evelin/DREAM-Stellar/dream_stellar/test/cli/512_simSeq2_e-4.fa

/home/evelin/DREAM-Stellar/dream_stellar/debug/bin/stellar --alphabet dna5 --reverse --epsilon 0.05 --minLength 20 --xDrop 10 --kmer 7 --numMatches 5000 --sortThresh 10000 --verbose --suppress-runtime-printing --out /home/evelin/DREAM-Stellar/dream_stellar/test/cli/gold_standard/dna5_reverse/minLen20.txt /home/evelin/DREAM-Stellar/dream_stellar/test/cli/512_simSeq1_5e-2.fa /home/evelin/DREAM-Stellar/dream_stellar/test/cli/512_simSeq2_5e-2.fa

/home/evelin/DREAM-Stellar/dream_stellar/debug/bin/stellar --alphabet dna5 --reverse --epsilon 0.05 --minLength 150 --xDrop 10 --kmer 7 --numMatches 5000 --sortThresh 10000 --verbose --suppress-runtime-printing --out /home/evelin/DREAM-Stellar/dream_stellar/test/cli/gold_standard/dna5_reverse/minLen150.txt /home/evelin/DREAM-Stellar/dream_stellar/test/cli/512_simSeq1_5e-2.fa /home/evelin/DREAM-Stellar/dream_stellar/test/cli/512_simSeq2_5e-2.fa

/home/evelin/DREAM-Stellar/dream_stellar/debug/bin/stellar --alphabet dna5 --reverse --epsilon 0.05 --minLength 20 --xDrop 10 --kmer 7 --numMatches 5000 --sortThresh 10000 --verbose --suppress-runtime-printing --out /home/evelin/DREAM-Stellar/dream_stellar/test/cli/gold_standard/dna5_reverse/5e-2_minLen20_100kbsplit.txt /home/evelin/DREAM-Stellar/dream_stellar/test/cli/512_simSeq1_5e-2_100kbsplit.fa /home/evelin/DREAM-Stellar/dream_stellar/test/cli/512_simSeq2_5e-2_100kbsplit.fa

