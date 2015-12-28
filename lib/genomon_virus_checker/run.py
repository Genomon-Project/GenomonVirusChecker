#! /usr/bin/env python

import os, subprocess 
import utils

def main(args):

    fastq_file_1 = args.fastq_file_1
    fastq_file_2 = args.fastq_file_2
    output_prefix = args.output_prefix
    virus_reference_file = args.virus_reference_file
    virus_description_file = args.virus_description_file

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


