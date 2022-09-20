'''
input:
#1 a FASTA-stype file containing two sequences to align
#2 a text file containing the scoring matrix you'd like to use for this alignment
#3 penalty for gaps
#4 The filepath to write your alignment to
'''

from fasta import readFASTA
import numpy as np
import sys

input_sequences = readFASTA(open(sys.argv[1]))#"/Users/cmdb/qbb2022-answers/week2-homework/needleman-wunsch/CTCF_38_M27_AA.faa"
#"/Users/cmdb/qbb2022-answers/week2-homework/needleman-wunsch/CTCF_38_M27_DNA.fna"


seq1_id, sequence1 = input_sequences[0]
seq2_id, sequence2 = input_sequences[1]


with open (sys.argv[2],"r") as f:#"/Users/cmdb/qbb2022-answers/week2-homework/needleman-wunsch/BLOSUM62.txt" / "/Users/cmdb/qbb2022-answers/week2-homework/needleman-wunsch/HOXD70.txt"
    content = f.readlines()
    a=content[0].replace(" ","")
    elements = list(a.strip()) #['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V', 'B', 'Z', 'X'], used for later index
score = np.loadtxt(sys.argv[2],skiprows=1,usecols=list(range(len(elements)+1))[1:])#sys.argv[2]

gap_penalty = float(sys.argv[3])

F_matrix = np.zeros((len(sequence1)+1,len(sequence2)+1))#we have an extra row and col filled with minus
T_matrix = np.zeros((len(sequence1)+1,len(sequence2)+1)) # trace back matrix


for i in range(len(sequence1)+1):
    F_matrix[i,0]= i * gap_penalty

# Now fill in the first row

for j in range(len(sequence2)+1):
    F_matrix[0,j] = j * gap_penalty

for i in range(1,len(sequence1)+1):
    for j in range(1, len(sequence2)+1):
#it is important to have i-1 here! because we add a row but sequence do not have that gap.
        d = F_matrix[i-1,j-1] + score[elements.index(sequence1[i-1]),elements.index(sequence2[j-1])]
        h = F_matrix[i,j-1] + gap_penalty
        v = F_matrix[i-1,j] + gap_penalty   
        #print(d,h,v)    
        F_matrix[i,j] = max(d,h,v)
        if F_matrix[i,j] == d:
            T_matrix[i,j] = 1
        else:
            if F_matrix[i,j] == h:
                T_matrix[i,j] = 2
            else:
                if F_matrix[i,j] == v:
                    T_matrix[i,j] = 3
        #break
    #break

#print(F_matrix)
#print(T_matrix)
seq1_align = ''
seq2_align = ''
m = len(sequence1) 
n = len(sequence2) 
gap1=0
gap2=0

while m*n > 0:
        if T_matrix[m,n] == 1:
            seq1_align += sequence1[m-1]
            seq2_align += sequence2[n-1]
            m += -1
            n += -1
        if T_matrix[m,n] == 2:
            seq1_align += '-'
            gap1 += 1
            seq2_align += sequence2[n-1]
            n += -1 
        if T_matrix[m,n] == 3:
            seq1_align += sequence1[m-1]
            seq2_align += '-'
            gap2 += 1        
            m += -1

while m > 0:
    seq2_align += '-'
    m += -1

while n > 0:
    seq1_align += '-'
    n += -1

          
align_score = F_matrix[-1][-1]        

print("Gaps in sequence 1: ",gap1)
print("Gaps in sequence 2: ",gap2)
print("alignment score: ",align_score)

f = open(sys.argv[4], "w") #/Users/cmdb/qbb2022-answers/week2-homework/align_protein       /Users/cmdb/qbb2022-answers/week2-homework/align_DNA 
f.write(seq1_align + "\n" + seq2_align)
f.close()