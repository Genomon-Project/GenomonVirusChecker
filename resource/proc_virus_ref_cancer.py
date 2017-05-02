#! /usr/bin/env python

import  sys, gzip


cancer_virus = {}
with open("cancer_virus_list.txt", 'r') as hin:
    for line in hin:
        # remove version numbers
        cancer_virus[line[:9]] = 1


hout1 = open("viral.genomic.cancer.fasta", 'w') 
write_on = False
with gzip.open("viral.1.1.genomic.fna.gz", 'r') as hin:
    for line in hin:
        line = line.rstrip('\n')
        if line.startswith('>'):
            F = line.split('|')
            # compare ignoring the version number
            write_on = True if F[1][:9] in cancer_virus else False
            if write_on == True: print >> hout1, '>' + F[1]
        else:
            if write_on == True: print >> hout1, line

            
hout1.close()

