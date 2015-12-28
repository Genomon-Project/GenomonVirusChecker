#! /usr/bin/env python


def fastq2fasta(input_file, output_file):

    hout = open(output_file, 'w')
    hin = open(input_file, 'r')

    line = hin.readline()
    while line:
        F = line.rstrip('\n').split(' ')
        print >> hout, ">" + F[0].lstrip('@')
        line = hin.readline()
        print >> hout, line.rstrip('\n')
        line = hin.readline()
        line = hin.readline()
        line = hin.readline()

    hin.close()
    hout.close()


def parse_virus_from_psl(input_file, output_file, seq_num, min_match):

    hout = open(output_file, 'w')
    hin = open(input_file, 'r')
    
    for i in range(6):
        line = hin.readline()
 
    while line:
        F = line.rstrip('\n').split('\t')
        if int(F[0]) > min_match:
            print >> hout, F[9] + '\t' + F[13] + '\t' + str(seq_num) + '\t' + F[0] + '\t' + F[8] + '\t' + F[15] + '\t' + F[16]
        line = hin.readline()

    hout.close()
    hin.close()


def count_virus_mapped_bases(input_file, output_file):

    hout = open(output_file, 'w')

    virus2mapped_bases = {}

    temp_read_id = ""
    temp_virus_1 = {}
    temp_virus_2 = {}
    with open(input_file, 'r') as hin:
        for line in hin:
            F = line.rstrip('\n').split('\t')
            if F[0] != temp_read_id:
                if temp_read_id != "":
                    for virus in temp_virus_1:
                        if virus in temp_virus_2:
                            virus_info_1 = temp_virus_1[virus]
                            virus_info_2 = temp_virus_2[virus] 
                            proper_flag = 0
                            if virus_info_1[1] == "+" and virus_info_2[1] == "-" and int(virus_info_1[2]) < int(virus_info_2[3]): proper_flag = 1
                            if virus_info_2[1] == "+" and virus_info_1[1] == "-" and int(virus_info_2[2]) < int(virus_info_1[3]): proper_flag = 1
                            if proper_flag == 1:
                                if virus in virus2mapped_bases:
                                    virus2mapped_bases[virus] = virus2mapped_bases[virus] + int(virus_info_1[0]) + int(virus_info_2[0])
                                else:
                                    virus2mapped_bases[virus] = int(virus_info_1[0]) + int(virus_info_2[0])

                temp_read_id = F[0]                    
                temp_virus_1 = {}
                temp_virus_2 = {}

            if F[2] == "1": temp_virus_1[F[1]] = [F[3], F[4], F[5], F[6]]
            if F[2] == "2": temp_virus_2[F[1]] = [F[3], F[4], F[5], F[6]]

    for virus in temp_virus_1:
        if virus in temp_virus_2:
            virus_info_1 = temp_virus_1[virus]
            virus_info_2 = temp_virus_2[virus]  
            proper_flag = 0
            if virus_info_1[1] == "+" and virus_info_2[1] == "-" and int(virus_info_1[2]) < int(virus_info_2[3]): proper_flag = 1
            if virus_info_2[1] == "+" and virus_info_1[1] == "-" and int(virus_info_2[2]) < int(virus_info_1[3]): proper_flag = 1
            if proper_flag == 1:
                if virus in virus2mapped_bases: 
                    virus2mapped_bases[virus] = virus2mapped_bases[virus] + int(virus_info_1[0]) + int(virus_info_2[0])
                else:
                    virus2mapped_bases[virus] = int(virus_info_1[0]) + int(virus_info_2[0])


    for virus in virus2mapped_bases:
        print >> hout, virus + '\t' + str(virus2mapped_bases[virus])

    hout.close()

if __name__ == "__main__":
    import sys

    fastq2fasta(sys.argv[1], sys.argv[2])

      
