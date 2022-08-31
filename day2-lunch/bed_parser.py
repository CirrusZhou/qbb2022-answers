#!/usr/bin/env python3

# in order to make the result clear in future analysis, I ask the script to feedback the exact error, and also the error number. This could be a little different from the equirement.

import sys

def parse_bed(fname):
    # initiate the error_num to count errors
    error_num=0
    try:
        fs = open(fname, 'r')
    except:
        raise FileNotFoundError("That file doesn’t appear to exist")
    bed = []
    #1.chrom/ 2.chromstart/ 3.chromend/ 4.name/ 5.score/ 6.strand/ 7.thickend/ 8.thickend/ 9.itemRgb
    field_types = [str, int, int, str, float, str, int, int,str,int,str,str]
    for i, line in enumerate(fs):
        # go through and find the data lines, which is not started by #
        if line.startswith("#"):
            continue
        #take away \n and \r, and split the line into list
        fields = line.rstrip().split('\t')
        #see how many elements in the list, also tell the bed format
        fieldN = len(fields)

        # check whether our file has the least cols to make a good bed file
        if fieldN < 3:
            #if not, feedback the error to the user
            print(f"Line {i} appears even not BED3", file=sys.stderr)
            error_num+=1
            # continue if we do not get the good bed file
            continue
        #check whether the input file is in BED10 or BED11
        if fieldN == 10 or fieldN == 11:
            #if so, feedback error
            print(f"Line {i} appears BED10 or BED11", file=sys.stderr)
            error_num+=1
            # continue if we do not get the good bed file
            continue
        

        # try to convert each element into the data type it should be
        try:
            
            for j in range(min(len(field_types), len(fields))):
                # sometimes the score is not an int, but a "."
                if fields[j] == ".":
                    #just skip it and do not interupt our program
                    continue
                # turn each element into the right type
                fields[j] = field_types[j](fields[j])
                
                # for col 9, make sure there are 3 integers for the itemRGB entries
                if j == 8:
                    try:
                        # split the str into list
                        fields[j] = fields[j].split(",")
                        # convert the str in the list into int
                        fields[j] = list (map (int,fields[j]))
                        # verify there are 3 integers, not more or less.
                        assert len(fields[j]) == 3
                    # if error raised, tell the user itemRGB may be wrong in this line
                    except:
                        print(f"Line {i} appears malformed, with bad itemRGB", file=sys.stderr)
                        error_num+=1
                # for BED 12, make sure that the lengths of blockSizes and blockStarts match blockCount
                if j == 10 :
                    try:
                        # try to get rid of the last comma, and split the str by "," to get a list
                        fields[j] = fields[j].strip(",").split(',')
                        # let's see whether the lengths of blockSizes match blockCount
                        fields[j] = list (map (int,fields[j]))
                        assert len(fields[j]) == fields[9]
                    # if error raised, tell the user sth is wrong with blockSizes.
                    except:
                        print(f"Line {i} appears malformed, with bad blockSizes ", file=sys.stderr)
                        error_num+=1
                if j == 11:
                    try:
                        fields[j] = fields[j].strip(",").split(',')
                        # let's see whether the lengths of blockStarts match blockCount
                        fields[j] = list (map (int,fields[j]))
                        assert len(fields[j]) == fields[9]
                    # if error raised, tell the user sth is wrong with blockStarts.
                    except:
                        print(f"Line {i} appears malformed, with bad blockStarts", file=sys.stderr)
                        error_num+=1
                        #print (fields)
                        #print(line)
            # append the fields into bed
            bed.append(fields)
        #if any element is not in the supposed type, feedback to the user.    
        except:
            print(f"Line {i} appears malformed, totally!", file=sys.stderr)
            error_num+=1
    fs.close()
    
    # if the error_num not equals 0, tell the user how many errors are here.
    try:
        assert error_num==0
    except:
        print(f"There are {error_num} errors! ", file=sys.stderr)
    return bed
    

if __name__ == "__main__":
    fname = sys.argv[1]
    bed = parse_bed(fname)
 
