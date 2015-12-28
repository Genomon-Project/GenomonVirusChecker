#! /usr/bin/env python

import os, subprocess 
import utils

def main(args):

    fastq_file_1 = args.fastq_file_1
    fastq_file_2 = args.fastq_file_2
    output_prefix = args.output_prefix
    virus_reference_file = args.virus_reference_file
    # virus_description_file = args.virus_description_file

    output_prefix_dir = os.path.dirname(output_prefix)
    if output_prefix_dir != "" and not os.path.exists(output_prefix_dir):
       os.makedirs(output_prefix_dir)

    utils.fastq2fasta(fastq_file_1, output_prefix + ".seq1.fasta")
    utils.fastq2fasta(fastq_file_2, output_prefix + ".seq2.fasta")


    # blat alignment
    FNULL = open(os.devnull, 'w')
    fRet = subprocess.call(["blat", virus_reference_file, 
                            output_prefix + ".seq1.fasta",
                            output_prefix + ".seq1.psl"], stdout = FNULL, stderr = subprocess.STDOUT)

    FNULL.close()
    if fRet != 0:
        print >> sys.stderr, "blat error, error code: " + str(fRet)
        sys.exit()


    FNULL = open(os.devnull, 'w')
    fRet = subprocess.call(["blat", virus_reference_file,
                            output_prefix + ".seq2.fasta",
                            output_prefix + ".seq2.psl"], stdout = FNULL, stderr = subprocess.STDOUT)
    
    FNULL.close()
    if fRet != 0:
        print >> sys.stderr, "blat error, error code: " + str(fRet)
        sys.exit()


    # psl parse
    utils.parse_virus_from_psl(output_prefix + ".seq1.psl", output_prefix + ".seq1.virus.txt", 1, 60)
    utils.parse_virus_from_psl(output_prefix + ".seq2.psl", output_prefix + ".seq2.virus.txt", 2, 60)


    hout = open(output_prefix + ".seq.virus.txt", 'w')
    fRet = subprocess.call(["cat", output_prefix + ".seq1.virus.txt", output_prefix + ".seq2.virus.txt"], stdout = hout)
    hout.close()

    hout = open(output_prefix + ".seq.virus.sort.txt", 'w')
    fRet = subprocess.call(["sort", "-k1,1", "-k2,2", "-k3,3", output_prefix + ".seq.virus.txt"], stdout = hout)
    hout.close()

    utils.count_virus_mapped_bases(output_prefix + ".seq.virus.sort.txt", output_prefix + ".virus.base.txt")

    fRet = subprocess.call(["rm", "-rf", output_prefix + ".seq1.fasta"])
    fRet = subprocess.call(["rm", "-rf", output_prefix + ".seq2.fasta"])
    fRet = subprocess.call(["rm", "-rf", output_prefix + ".seq1.psl"])
    fRet = subprocess.call(["rm", "-rf", output_prefix + ".seq2.psl"])
    fRet = subprocess.call(["rm", "-rf", output_prefix + ".seq1.virus.txt"])    
    fRet = subprocess.call(["rm", "-rf", output_prefix + ".seq2.virus.txt"])
    fRet = subprocess.call(["rm", "-rf", output_prefix + ".seq.virus.txt"])

