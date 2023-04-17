#! /usr/bin/env python3
# -*- coding:utf-8 -*-
import sys

File=sys.argv[1]  #input tree file
Netnum=sys.argv[2] #input net number
spe_number=14 #species number
mode='InferNetwork_ML' #PhyloNet command

space=200

def get_tree(File):
    with open(File,'r') as f:
        trees = 0
        for line in f:
            line = line.strip()
            t1 = line.split(',')
            d = []
            for sp in t1:
                sp = sp.split(':')[0].split('(')[-1]
                d.append(sp)
            if len(d) >= spe_number:
                D = d
                trees += 1
                if trees <= space:
                    print('Tree'+' '+'gt'+str(trees)+'='+line)
    return D


#====================
print('#NEXUS\n')
print('BEGIN Trees;\n')
species = get_tree(File)
print('\nEND;\n')
print('BEGIN PHYLONET;\n')
print(mode+' (all) '+Netnum+' -a <'+';'.join(i+':'+i for i in species)+'>'+' -pl 8;\n')
print('END;')
