#! /usr/bin/env python


def fastq2fasta(input_file, output_file):

    hout = open(output_file, 'w')
    hin = open(input_file, 'r')

    line = hin.readline()
    while line:
        F = line.rstrip('\n').split(' ')
        print >> hout, ">" + F[0]
        line = hin.readline()
        print >> hout, line.rstrip('\n')
        line = hin.readline()
        line = hin.readline()
        line = hin.readline()

    hin.close()
    hout.close()


if __name__ == "__main__":
    import sys

    fastq2fasta(sys.argv[1], sys.argv[2])

      
