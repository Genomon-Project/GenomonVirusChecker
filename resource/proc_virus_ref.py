#! /usr/bin/env python

import  gzip, re

hout1 = open("viral.genomic.fasta", 'w') 
hout2 = open("viral_list.txt", 'w')

accession_number = ""
tempLength = 0
with gzip.open("viral.1.1.genomic.fna.gz", 'r') as hin:
    for line in hin:
        line = line.rstrip('\n')
        if line.startswith('>'):

            if accession_number != "":
                print >> hout2, accession_number + '\t' + str(tempLength) + '\t' + description

            line = line.lstrip('>')
            re_match = re.match(r'(\w{2}_\d{6}\.\d)', line)

            """
            # for debugging
            if re_match is None:
                print "error"
                sys.exit(1)
            """

            accession_number = re_match.group(1)
            description = re.sub(r'^\w{2}_\d{6}\.\d ', '', line)
            tempLength = 0
            print >> hout1, '>' + accession_number
        else:
            tempLength = tempLength + len(line)
            print >> hout1, line
            
print >> hout2, accession_number + '\t' + str(tempLength) + '\t' + description
hout1.close()
hout2.close()

