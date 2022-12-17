
big_list=[]
for i in range(6):
    small_list=[]
    with open(f"bin.{i+1}.fa") as f:
        for j in f:
            if j.startswith(">"):
                small_list.append(j.strip()[1:])
    big_list.append(small_list)
    
    
taxo_list=[]
taxo={}
with open("/Users/cmdb/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/KRAKEN/assembly.kraken") as f:
    for i in f:
        taxo[i.strip().split('\t')[0]] = i.strip().split('\t')[1]
        #print(taxo)


all_counter=[]
for i in range(6):
    counter={}
    for j in big_list[i]:
        for k in taxo[j].split(";"):
            if k in counter.keys(
            ):
                counter[k]+=1
            if k not in counter.keys():
                counter[k]=1
    all_counter.append(counter)
for i in all_counter:
    for j in i:
        print(j," ",i[j])


    
# taxo.append(i.strip().split('\t')[1].split(";"))