# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Werewolfzy

import sys
import getopt
import pandas as pd
import numpy as np
import os
import multiprocessing
import time
from pandas.core.frame import DataFrame



def single_run(filename, freq_cutoff):
    i = filename
    f = freq_cutoff

    list1 = []
    data6 = data5.loc[data5['IID2'] == '%s' % i.upper()]
    data7 = data5.loc[data5['IID2'] != '%s' % i.upper()]
    data6.drop('IID', axis=1, inplace=True)
    data7.drop('IID', axis=1, inplace=True)
    data6.drop('IID2', axis=1, inplace=True)
    data7.drop('IID2', axis=1, inplace=True)
    value1 = len(data6)
    value2 = len(data7)
    print(i.upper())
    # print(data6)
    # print(data7)
    for x in range(0, len(data6.columns)):
        value3 = data6.iloc[:, [x]].values[0][0]
        value4 = len(data6.loc[data6[data6.columns[x]] == value3])

        if value4 == value1:
            # print(data6.columns[x])
            value5 = len(data7.loc[data7[data6.columns[x]] == value3])

            if value5 <= value2 * f:
                list1.append(data6.columns[x])

    data8 = DataFrame(list1)
    data8.to_csv('%stezhengweidianid.txt' % i, header=0, index=False)
    #print(data8)


def conbine(out_file):
    os.system('rm test2.*')

    data11 = pd.DataFrame(data=None, columns=[0])
    data_results = data11[0]

    for i in file:
        path = "%stezhengweidianid.txt" % i

        if os.path.getsize(path) > 0:
            #print(path)
            data12 = pd.read_csv(path, encoding="gbk", sep="\t", header=None)
            # data2 = data1[1]
            df_list = [data_results, data12]
            data_results = pd.concat(df_list)

    data_results.to_csv(out_file, header=0, index=False)



def prepare(vcf_file):
    file = vcf_file
    global data5
    os.system('cp %s test1.txt' %(file))
    os.system('sed "/^##/d" test1.txt > test2.txt')
    os.system('rm test1.*')
    path = "test2.txt"
    data = pd.read_csv(path, encoding="gbk", sep="\t")
    data.rename(columns={'#CHROM': 'CHROM'}, inplace=1)
    data1 = data.copy()
    data2 = data1.drop(labels=['CHROM', 'POS', 'REF', 'ALT', 'QUAL', 'FILTER', 'INFO', 'FORMAT'], axis=1)
    data3 = data2.set_index('ID')
    data4 = data3.T
    data4['IID'] = data4.index
    data5 = data4.replace({"0/0": 1, "0/1": 2, "1/1": 3, "./.": 0})
    data5['IID2'] = data5['IID'].replace('[0-9]', '', regex=True)






def parallel(allfilename, freq_cutoff):

    files = allfilename
    freq_cutoff = freq_cutoff

    procs = []

    for i in files:
        filename = i
        #print(filename)
        procs.append(multiprocessing.Process(target=single_run, args=(filename,freq_cutoff)))
        pass

    for proc in procs:
        proc.start()
    for proc in procs:
        proc.join()

























if __name__ == '__main__':


    def usage():
        print(
            """
            usage: python [{0}] ... [-g genotype_file | -p all_kinds_species_file |  -f freq_cutoff | -o out_file]  ...
            参数说明:
            -g     : 基因型文件VCF文件前缀
            -p     : 所有群体名字文件
            -f     : 设定的位点差异值，数字越小差异越大，默认是0.5
            -o     : 数据保存名字
            -h     : 帮助信息
            """.format(sys.argv[0]))


    def main():
        opts, args = getopt.getopt(sys.argv[1:], "hg:p:f:o:")
        genotype_file = ""
        phenotype_file = ""
        freq_cutoff = 0.5
        out_file = "result.txt"

        for op, value in opts:
            if op == '-g':
                genotype_file = value
            elif op == "-p":
                phenotype_file = value
            elif op == "-f":
                freq_cutoff = value
            elif op == "-o":
                out_file = value
            else:
                usage()
                sys.exit()
                return

        begin_time = time.time()
        data5 = 1
        path10 = genotype_file
        data10 = pd.read_csv(path10, encoding="gbk", sep="\t", header=None)
        train_data = np.array(data10)
        file2 = train_data.tolist()
        file = []
        for i in range(0, len(file2)):
            file.append(file2[i][0])

        prepare(genotype_file)
        parallel(file, freq_cutoff)
        conbine(out_file)



        end_time = time.time()
        print("parallel time: ", end_time - begin_time)
