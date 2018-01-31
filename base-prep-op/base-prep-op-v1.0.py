# coding:utf-8 #

import codecs
import argparse
import os
import pickle

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--tensor')
parser.add_argument('-r', '--raw')
parser.add_argument('-p', '--pkl')
parser.add_argument('-d', '--delimiter')
args = parser.parse_args()

# tensor should be specified

if args.tensor and args.delimiter and args.raw and args.pkl:
    with codecs.open(args.tensor, 'r', 'utf-8') as ft,\
        codecs.open(args.raw, 'w', 'utf-8') as fr,\
        codecs.open(args.pkl, 'wb') as fpkl:
        args.delimiter = '\t'
        # the delimiter TAB cannot be specified, i dont know why
        pkl_load, sent_list = [], []
        for tline in ft:
            if tline == '\n':
                pkl_load.append(sent_list)
                sent_list = []
                fr.write('\n')
            else:
                sent_list.append(tuple(tline.rstrip().split(args.delimiter)))
                fr.write((tline.rstrip().split(args.delimiter))[0])
        pickle.dump(pkl_load, fpkl)
else:
    print('neccessary args unspecified')