#! /bin/bash

rm -rf viral.1.1.genomic.fna.gz

wget ftp://ftp.ncbi.nlm.nih.gov/refseq/release/viral//viral.1.1.genomic.fna.gz

echo "proc_virus_ref.py"
python proc_virus_ref.py


