#! /bin/bash

rm -rf viral.1.1.genomic.fna.gz

wget ftp://ftp.ncbi.nlm.nih.gov/refseq/release/viral//viral.1.1.genomic.fna.gz

echo "python proc_virus_ref.py"
python proc_virus_ref.py

echo "python proc_virus_ref_cancer.py"
python proc_virus_ref_cancer.py

