
# import the function we need from "vcfParser_annotated.py"
from vcfParser_annotated import parse_vcf

# load file "random_snipped.vcf", get the returned result stored into "random"
random = parse_vcf("random_snippet.vcf")
# load file "dbSNP_snippet.vcf" get the returned result stored into "dbSNP"
dbSNP = parse_vcf("dbSNP_snippet.vcf")

# creat a directory to store the position and id
pos_id = {}

# go through every line in dbSNP (except the head line), and store the position as key and id as value into pos_id
for i in range(len(dbSNP)):
    if i == 0:
        continue
    else:
        pos_id[dbSNP[i][1]] = dbSNP[i][2]

# initiate a variable which represents the number of records without id.
unlabel = 0
# go through every line in random (except the head line)       
for i in range(len(random)):
    if i == 0:
        print(random[0][0:5])
        continue
    # try to find id in pos_id according to the position.
    '''
    if random[i][1] in pos_id.keys():
        random[i][2] = pos_id[random[i][1]]
    else:
        unlabel +=1
    ''' 
    try:
        # Replaces the ID in each record from random_snippet.vcf with the correct label
        random[i][2] = pos_id[random[i][1]]
        # print(pos_id[random[i][1]])
    # if id is not found, add one to unlabel, showing one more record does not have id.
    except:
        unlabel +=1
    
# tell the user how many records are not labeled.
print (f"There are {unlabel} enlabeled records.")      

#print(dbSNP[1][2])
'''
for i in range(10):
    print(random[i+1][2])
'''
#CHROM  POS     ID      REF     ALT     QUAL    FILTER  INFO
