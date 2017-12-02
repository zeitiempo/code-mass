# coding:utf-8 #

import argparse
import codecs
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', help='set the input tensor file')
parser.add_argument('-d', '--delimiter', help='set the delimiter between the column of the tensor, eg: set -d \" \" which stands for the delimiter SPACE')
parser.add_argument('-c', '--column', help='set the number(s) of the column that you want to keep, eg: set -c 1,2,4 which stands for the 1st, 2nd, 4th column')
parser.add_argument('-o', '--output', help='set the output file')
args = parser.parse_args()

if args.input:
	input_src = args.input
if args.delimiter:
	delimiter = args.delimiter
if args.column:
	column_list = args.column.split(',')
if args.output:
	output_src = args.output

with codecs.open(input_src, 'r', 'utf-8') as fi,\
	codecs.open(output_src, 'w', 'utf-8') as fo:
	for line in fi:
		if line == '\n':
			fo.write('\n')
		else:
			o_flow = []
			i_flow = line.rstrip().split(delimiter)
			for column in column_list:
				o_flow.append(i_flow[int(column) - 1])
			fo.write(delimiter.join(o_flow)+'\n')
