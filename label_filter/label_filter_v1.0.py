# coding:utf-8 #

import argparse
import codecs

parser = argparse.ArgumentParser()
parser.add_argument('-i',\
	                '--input',\
	                default=None,\
	                help='set the input tensor file')
parser.add_argument('-d',\
	                '--delimiter',\
	                default=" ",\
	                help='set the delimiter between the column of the tensor,\
	                 default is " ", namely SPACE,\
	                 eg: set -d \" \" which stands for the delimiter SPACE')
parser.add_argument('-ul',\
		            '--unique_label',\
		            default=None,\
		            help='output the unique label(s)\
		             in the input tensor file,\
		              namely the last column of the tensor,\
		              eg: set -ul True to get it')
parser.add_argument('-f',\
	                '--filter',\
	                default=None,\
	                help='set the label filter,\
	                 eg: set -f [label1],[label2] stands for\
	                  the label1 and label2 that you want to filter')
parser.add_argument('-o',\
	                '--output',\
	                default=None,\
	                help='set the output file')
args = parser.parse_args()

if args.input and args.delimiter and args.unique_label:
	input_src = args.input
	delimiter = args.delimiter
	label_list = []
	with codecs.open(input_src, 'r', 'utf-8') as fi:
		for line in fi:
			label_list.append(line.rstrip().split(delimiter)[-1])
		u_label_list = list(set(label_list))
		for u_label in u_label_list:
			print(u_label)
elif args.input and args.delimiter and args.filter and args.output:
	input_src = args.input
	output_src = args.output
	delimiter = args.delimiter
	if 't' in delimiter:
		delimiter = '\t'
	fltr = args.filter
	fltr_list = fltr.split(',')
	with codecs.open(input_src, 'r', 'utf-8') as fi,\
		codecs.open(output_src, 'w', 'utf-8') as fo:
		for line in fi:
			if line == '\n':
				fo.write(line)
			else:
				_, label = line.rstrip().split(delimiter)[:-1],\
				           line.rstrip().split(delimiter)[-1]
				f = 0
				for fltr_e in fltr_list:
					if fltr_e in label:
						f = 1
						break
				if f:
					fo.write(delimiter.join(_)+' O\n')
				else:
					fo.write(line)