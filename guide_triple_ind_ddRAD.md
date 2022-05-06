# *Adapter Trimming for triple-indexed ddRAD*
Om Kulkarni - 03/05/22 

## 1) Raw data processing

Find the fastq files for your sample, should look like this:

5'->3' forward read

`Sample-0X_SZZZ_L001_R1_001.fastq.gz` 

3'->5' reverse read

`Sample-0X_SZZZ_L001_R2_001.fastq.gz` 

#### *Unzip using command:*
`gzip Sample-01_S306_L001_R2_001.fastq.gz `

Have a look at FastQC, points to note:
> \>Sequence quality - drop off in the end

> \>Tile quality - evenly distributed blue, not one single row or column with red

> \>Sequence content - adapters in 5' &  3'

> \>N content - small peaks but roughly following theoretical distribution

> \>Adapter content

## 2) Sanity check

Each sample has a barcode, and dual indices 50X+70X

e.g. Kalanchoe strepthanta	TATCCAGT barcode, 502+701 index code corresponding to TGCTAAGT + ACCACTGT

Barcode should be somewhere near the 5' of the fwd reads.

The indices are 50X at 5' 70X at 3', 
The 50X should not appear in the fwd reads, sometimes in the reverse reads
The 70X will be sometimes in the fwd reads, should not be in reverse reads

Check the frequency:
`grep -o ‘GATC' a.fastq | wc -l`

## 3) Cutadapt

We need to apply cutadapt multiple times

TO ADD : option to run all barcodes, and not just the Samples' designated barcode. Would help to quantify barcode hopping.

> ### 3a) 5' trimming - for forward reads trim barcode & discard non barcoded reads

`cutadapt -j 6 -q 20 --discard-untrimmed -g TATCCAGT -o s2g.fastq -p s2g_rev.fastq Sample-02_S307_L001_R1_001.fastq Sample-02_S307_L001_R2_001.fastq > cutadapt_s2g.log`

> ### 3b) 3' trimming FWD Illumina Truseq, REV barcode, allow error of 1bp (corresponding to 0.125%)

`cutadapt -j 6 -e 0.125 -a AGATCGGAAGAGCACACGTCTGAACTCCAGTCA -A ACTGGATAAGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT -o s2gaA.fastq -p s2gaA_rev.fastq s2g.fastq s2g_rev.fastq > cutadapt_s2gaA.log`