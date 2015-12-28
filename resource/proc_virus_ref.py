#! /usr/bin/env python

import  gzip

hout1 = open("viral.genomic.fasta", 'w') 
hout2 = open("viral_list.txt", 'w')

with gzip.open("viral.1.1.genomic.fna.gz", 'r') as hin:
    for line in hin:
        line = line.rstrip('\n')
        if line.startswith('>'):
            F = line.split('|')
            print >> hout1, '>' + F[3]
            print >> hout2, F[3] + '\t' + F[4].strip(' ')
        else:
            print >> hout1, line

            
hout1.close()
hout2.close()

