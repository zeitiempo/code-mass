# coding:utf-8 #

import codecs

def sort_by_len(foo_unsort, foo_sort):
    unsort_list = []
    sort_list = []
    with codecs.open(foo_unsort, 'r', 'utf-8') as fus:
        for lus in fus:
            unsort_list.append(lus.rstrip())
    sort_list = sorted(unsort_list, key=len, reverse=True)
    with codecs.open(foo_sort, 'w', 'utf-8') as fs:
        for i in range(len(sort_list)):
            fs.write(sort_list[i]+'\n')
