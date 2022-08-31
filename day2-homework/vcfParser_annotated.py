#!/usr/bin/env python3

import sys # let the user to input the file in the command line

def parse_vcf(fname):# define a function called parse_vcf, it takes an argument called "fname"
    vcf = [] # creat an empty list called "vcf" to store the VCF information
    info_description = {} # creat a dictionary
    info_type = {} # creat a dictrionary
    format_description = {} # creat a dictrionary
    type_map = {
        "Float": float,
        "Integer": int,
        "String": str
        } # allows us to use information from the header to tell python what data types to expect
    malformed = 0 #initianize a variable to count number of malformed VCF lines

    # try to open the vcf file; if it doesn't work, tell the err
    try: 
        fs = open(fname) # creating a variable called fs, which is storing the openned vcf file
    except:
        raise FileNotFoundError(f"{fname} does not appear to exist", file=sys.stderr)

    for h, line in enumerate(fs): # loop through every line in the VCF line, keeping track of the line number
        if line.startswith("#"):# for header lines only! we do not to annotate the header!
            try:
                if line.startswith("##FORMAT"):
                    fields = line.split("=<")[1].rstrip(">\r\n") + ","
                    i = 0
                    start = 0
                    in_string = False
                    while i < len(fields):
                        if fields[i] == "," and not in_string:
                            name, value = fields[start:i].split('=')
                            if name == "ID":
                                ID = value
                            elif name == "Description":
                                desc = value
                            start = i + 1
                        elif fields[i] == '"':
                            in_string = not in_string
                        i += 1
                    format_description[ID] = desc.strip('"')
                elif line.startswith("##INFO"):
                    fields = line.split("=<")[1].rstrip(">\r\n") + ","
                    i = 0
                    start = 0
                    in_string = False
                    while i < len(fields):
                        if fields[i] == "," and not in_string:
                            name = fields[start:i].split('=')[0]
                            value = fields[start:i].split('=')[1]
                            if name == "ID":
                                ID = value
                            elif name == "Description":
                                desc = value
                            elif name == "Type":
                                Type = value
                            start = i + 1
                        elif fields[i] == '"':
                            in_string = not in_string
                        i += 1
                    info_description[ID] = desc.strip('"')
                    info_type[ID] = Type
                elif line.startswith('#CHROM'):
                    fields = line.lstrip("#").rstrip().split("\t")
                    vcf.append(fields)
            except:
                raise RuntimeError("Malformed header")
        else: # if we are NOT on a header line, do this:
            try: # TRY doing all of this
                # fields is a list that stores the info in one line of the VCF  
                fields = line.rstrip().split("\t") # splits each line on a tab character, so that every column is an item in the list ("field")
                fields[1] = int(fields[1])# convert the SNP position into an integer (if this doesn't work, we'll automatically go to the "except" block)
                if fields[5] != ".": # if the QUAL column is not empty (i.e.,  it has a decimal in it that represents the SNP quality)
                    fields[5] = float(fields[5])# then forcibly convert it into a decimal
                info = {} # create a dictionary to store the information in the INFO column - lines 76-83 are going to be about parsing the INFO column
                    # we want the info dictionary to look like this:{"AC":91,
                                                                    #"AN":5096,
                                                                    #...,
                                                                    #"NS":2548}
                for entry in fields[7].split(";"): # the list looks like ["AC=91", "AN=5096", ..., "NS=2548"]
                    # the first entry we're working with is "AC=91"
                    temp = entry.split("=") # temp is a list. If we're working with "AC=91", temp=["AC","91"]
                    if len(temp) == 1: # if there's only one item in the temp list ("AC"), what we want to do is update the dictionary so that we know that AC has no value for this SNP
                        info[temp[0]] = None # temp[0] is "AC"
                        # dictionaries have keys and values. You add info to a dictionary by doing dic_name[new_key] = new_value. Ex: info["AC"]="91"
                    else: # otherwise, the INFO field is not empty and we're good
                        name, value = temp # temp = ["AC","91"], name="AC", value="91" My version: name = temp[0], value = temp[1]
                        # in these next two lines, we're converting the data in each entry to its correct data type. This data type was specified in the header section that we parsed above
                        Type = info_type[name] # here, we're getting the python function for data type conversion that corresponds to what the entry should be.
                        # Ex:  Type = info_type["AC"]. info_type is a dictonary we made in the header parsing section that tells us what data type that entry should be
                        info[name] = type_map[Type](value)# here, we're getting the python function for converting the entry to the correct data type
                        #Ex: for AC: info["AC"] = type_map["integer"]["91"]
                                   # info["AC"]
                fields[7] = info # replace the 8th item of the "fields" list (i.e., the list of columns in this line) with the "info" dictionary that we just made
                    # fields[7] used to be :["AC=91", "AN=5096", ..., "NS=2548"]
                    # now, fields[7] is {"AC":91,
                                       # "AN":5090
                                       # ...,
                                       # "NS":2548}
                if len(fields) > 8: # if we still have more columns after the INFO column, then we still have more stuff to do.
                    # example of fields[8] (the FORMAT column): "GT:DP:AF:BG:RU"
                    fields[8] = fields[8].split(":") # we are spliting the FORMAT column by ":"
                        # Ex: "GT:DP:AF:BG:RU" --> ["GT","DP","AF","BG","RU"]
                    if len(fields[8]) > 1: # if there are multiple things in the FORMAT column, we have to deal with all of them individually.
                        # FORMAT: GT:QV, HG00097: 0|0:0.3
                        for i in range(9, len(fields)): # this goes through all the genotype columns after the FORMAT column -> for us, this is range(9,2513)
                            fields[i] = fields[i].split(':')# slipt each genotype column along a ":"
                                # 0|0;0.3 -> ["0|0","0.3"]
                        # our "fields" list turns into: ["0|0;0.3","1|1;0.5",...] -> [["0|0","0.3"],["1|1","0.5"],...]
                    else:# if the genotypes donot have more than one value in them, then we're good 
                        fields[8] = fields[8][0] # fields[8] is ["GT"]
                                                 # this code gets you fields[8] = "GT"
                                                 # we set the value of fields[8] to be "GT", the first item in our fields[8] list 
                vcf.append(fields) # we've finished reformatting/cleaning all of the columns; now we add this line to our VCF list. The list is storing all the information from the VCF file
                    # "fields" is a list that contains the information for the current line that we're working on
            except: # if anything in the try block fails, then:
                malformed += 1
    # these next three lines ar modifying the first line of the vcf list to match information from the header
    vcf[0][7] = info_description
    if len(vcf[0]) > 8:
        vcf[0][8] = format_description
    # if there were any malformed lines, we're going to print out the number of lines so the user knows
    if malformed > 0:
        print(f"There were {malformed} malformed entries", file=sys.stderr)
    # at the very end of running the function, return the vcf list, Give me the data back.
    return vcf

#ignore all of these
if __name__ == "__main__":
    fname = sys.argv[1]
    vcf = parse_vcf(fname)
    for i in range(10):
        print(vcf[i])
