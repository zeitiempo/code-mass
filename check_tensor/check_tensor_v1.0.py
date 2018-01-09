# coding:utf-8 #

# check NER-Collection
# flow format: [single char][sep][bio tag which is 'B or I or O']-[ner type]\n

import codecs
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input')
args = parser.parse_args()

if args.input:
    error_line_list = []
    with codecs.open(args.input, 'r', 'utf-8') as fi:
        i = 1
        for line in fi:
            if line == '\n':
                pass
            else:
                line = line.rstrip()
                if len(line) <= 2:
                    error_line_list.append(i)
                else:
                    c = line[0]
                    sep = line[1]
                    bio = line[2]
                    if sep != '\t' or bio not in ['B', 'I', 'O']:
                        error_line_list.append(i)
            i += 1
    if error_line_list:
        with codecs.open('error_line', 'w', 'utf-8') as f_err:
            for error_line in error_line_list:
                print(str(error_line))
                f_err.write(str(error_line)+'\n')
    else:
        print('no error')
