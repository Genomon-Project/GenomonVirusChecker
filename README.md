# GenomonVirusChecker

## Introduction

GenomonVirusChecker is a software for checking the viral sequences in fastq files.

## Dependency

### Python

Python (>= 2.7)

### Software

blat

## Install 
```
git clone https://github.com/friend1ws/GenomonVirusChecker.git
cd GenomonVirusChecker
python setup.py build
python setup.py install
```

## Preparation

First, you may need to prepare viral sequence reference files in fastq format.
We have provided an example script for preparing the reference files.

```
cd resource
bash prepareVirus.sh
```

Also, you need to set up the path for blat before running the program.


## Commands

```
genomon_virus_checker [-h] [--version] [-q minimum_match_thres] sequence1.fastq sequence2.fastq output_prefix virus_reference.fa
```


