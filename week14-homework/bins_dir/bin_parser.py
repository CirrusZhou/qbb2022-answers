
for j in range(6):
    with open(f"bin.{j+1}.fa") as f:
        count=0
        length=0
        for i in f:
            if i.startswith(">"):
                length += int(i.split("_")[3])             
                count +=1
        print(j,"has ", count)
        print("total length is ", length)
    

with open("/Users/cmdb/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/assembly.fasta") as f:
    count=0
    length=0
    for i in f:
        if i.startswith(">"):
            count +=1
            length += int(i.split("_")[3]) 
    print("Total assembly has ", count)  
    print("total length is ", length)
    