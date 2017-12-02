# coding:utf-8 #

import codecs
import argparse

def cut(str):

	return [x for x in str.split(' ') if x != '']

punct = punct = [u' ', u'，', u'。', u'！', u'.', u'？',\
		u'~', u'、', u'…', u'"', u'-', u'：',u',',\
		u'·', u'；', u'“', u'”', u'?', u'!', u'～']

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', help='set input file')
parser.add_argument('-o', '--output', help='set output file')
args = parser.parse_args()

if args.input and args.output:
	with codecs.open(args.input, 'r', 'utf-8') as fi,\
		codecs.open(args.output, 'w', 'utf-8') as fo:
		for line in fi:
			if '< EOS >' in line:
				fo.write('<EOS>\n')
			else:
				seg, seg_prob, pos, pos_prob, dep = \
				line.rstrip().split('\t')
				seg_list = cut(seg)
				pos_list = cut(pos)
				dep_seq = cut(dep)
				dep_list = [y.split('_')[2] for y in dep_seq]
				spd_tuple = zip(seg_list, pos_list, dep_list)
				for spd in spd_tuple:
					word, word_pos, word_dep = spd
					i = 0
					for char in word:
						fo.write(' '.join([char, str(i), word_pos, word_dep])+'\n')
						i += 1
						if char in punct:
							fo.write('<PUNCT>\n')