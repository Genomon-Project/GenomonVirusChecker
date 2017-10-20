#! /usr/bin/env python

import  sys, gzip, re


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

            line = line.lstrip('>')
            re_match = re.match(r'(\w{2}_\d{6}\.\d)', line)
            accession_number = re_match.group(1)

            # F = line.split('|')
            # compare ignoring the version number
            write_on = True if accession_number[:9] in cancer_virus else False
            if write_on == True: print >> hout1, '>' + accession_number
        else:
            if write_on == True: print >> hout1, line

            
hout1.close()

