#USAGE: python Zhou_tail.py input_filename [number_lines_to_display_from_tail]


import sys #import module
filename = sys.argv[1]#SET the input filename
if len(sys.argv) > 2:#IF user-specified number of lines provided
    n_lines = sys.argv[2]#SET the desired number of lines
else:#OTHERWISE
    n_lines = 10#SET the desired number of lines to a default

stor_list = []#SET a storage list for lines in the file 

for line in open(filename):#FOR every line in the open file
    stor_list.append(line)#ADD the line to the storage list

desire_list = stor_list[-int(n_lines):]#GET a subset of the storage list to be the last disired number items in the storage list
for ele in desire_list:#FOR every line in the subset
    print(ele)#PRINT the line

