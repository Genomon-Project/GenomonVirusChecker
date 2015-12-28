#! /usr/bin/env python

import  sys, gzip


cancer_virus = {}
with open("cancer_virus_list.txt", 'r') as hin:
    for line in hin:
        cancer_virus[line.rstrip('\n')] = 1


hout1 = open("viral.genomic.cancer.fasta", 'w') 
write_on = False
with gzip.open("viral.1.1.genomic.fna.gz", 'r') as hin:
    for line in hin:
        line = line.rstrip('\n')
        if line.startswith('>'):
            F = line.split('|')
            write_on = True if F[3] in cancer_virus else False
            if write_on == True: print >> hout1, '>' + F[3]
        else:
            if write_on == True: print >> hout1, line

            
hout1.close()

