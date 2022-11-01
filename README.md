# SOSL (Screening of specific loci)
`SOSL` is a command line tool used for Screening of specific loci from single variety to multiple varieties. 

If you want to quickly find specific loci between a variety and multiple varieties in the chip data or Second generation sequencing data, you can use the following line of code to call our script to achieve your goal easily and quickly.

## Getting Started
0.Git clone SOSL

In order to download `SOSL`, you should clone this repository via the commands:
```
git clone https://github.com/Werewolfzy/SOSL.git
cd SOSL
```

1.Prepare the environment：

This script depends on the Python3 software and the Plink software and requires the following dependency packages:
```
pip install -r requirements.txt
```

2.Prepare the genotype file, the phenotype file and the significant snp file.

The genotype file is VCF format of PLink software. The phenotype file refer to the allname.txt.

3.The command line
```
python tezheng.py -g [genotype_file] -p [phenotype_file] -f [freq_cutoff  (The default is 0.5)] -o [out_file  (The default is result.txt)]
```









