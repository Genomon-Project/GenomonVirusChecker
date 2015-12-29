#! /usr/bin/env python

import  gzip

hout1 = open("viral.genomic.fasta", 'w') 
hout2 = open("viral_list.txt", 'w')

tempVirus = ""
tempLength = 0
tempDescription = ""
with gzip.open("viral.1.1.genomic.fna.gz", 'r') as hin:
    for line in hin:
        line = line.rstrip('\n')
        if line.startswith('>'):
            F = line.split('|')
            print >> hout1, '>' + F[3]
            if tempVirus != "":
                print >> hout2, tempVirus + '\t' + str(tempLength) + '\t' + tempDescription
            tempVirus = F[3]
            tempDescription = F[4].strip(' ')
            tempLength = 0
        else:
            tempLength = tempLength + len(line)
            print >> hout1, line
            
print >> hout2, tempVirus + '\t' + str(tempLength) + '\t' + tempDescription
hout1.close()
hout2.close()

