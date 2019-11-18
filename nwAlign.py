#! /usr/bin/env python3

import sys

#print("K_mer value "+ str(sys.argv[1]))
#print("Name of the file readed "+ str(sys.argv[2]))
read1=sys.argv[1]
read2=sys.argv[2]
seq1=''
seq2=''
#my_file = open(read)
with open(read1) as my_file1:
    next(my_file1)
    for line in my_file1:
        seq1 = seq1 + line.replace('n','').strip()
        
#my_file_contents = my_file.read()
#my_dna = my_file_contents.rstrip("\n")
#print(seq)
with open(read2) as my_file2:
    next(my_file2)
    for line in my_file2:
        seq2 = seq2 + line.replace('n','').strip()
   
match    = 1
mismatch = -1
gap      = -1     
list1=[]
listM=[]
list2=[]

#making matrix
H = [[0 for x in range(len(seq2)+1)] for y in range(len(seq1)+1)]
for x in range(0,len(seq1)+1):
    for y in range(0,len(seq2)+1):
        
        i = int(x)
        j = int(y)
        #print(j)
        matched = H[i - 1][j - 1] + (match if (list(seq1))[i - 1] == (list(seq2))[j - 1] else - match)
        delete = H[i - 1][j] + gap
        insert = H[i][j - 1] + gap
        H[i][j] = max(matched, delete, insert)
        #H[i][j]=1
        if i==0:
           H[i][j]=mismatch*j 
        if j==0:
           H[i][j]=mismatch*i
            
# trace back
        
#for x in range(len(seq1)-1,1):   
#    for y in range(len(seq2)-1,1):
i=len(seq1)
j=len(seq2)

while i>0 and j>0:
    #print(i)
    #print((list(seq1))[i-1])
    if (list(seq1))[i - 1] == (list(seq2))[j - 1] and H[i - 1][j - 1]+ match == H[i][j]:
        list1.append((list(seq1))[i-1])
        listM.append("|")
        list2.append((list(seq2))[j-1])
        i=i-1
        j=j-1
    elif H[i - 1][j - 1]- match == H[i][j]:
        list1.append((list(seq1))[i-1])
        listM.append("*")
        list2.append((list(seq2))[j-1])
        i=i-1
        j=j-1
    elif H[i-1][j]+ gap == H[i][j]:
        list2.append("-")
        listM.append(" ")
        
        list1.append((list(seq1))[i-1])
        i=i-1
    #elif H[i - 1][j - 1]- insert == H[i][j-1]:
    else:
        
        list2.append((list(seq2))[j-1])
        listM.append(" ")
        list1.append("-")
        print((list(seq2))[j-1])
        j=j-1
    

#print(type(list1))
#print(listM)
#print(list2)
list1.reverse()

sys.stdout.write("".join(list1))
listM.reverse()
sys.stdout.write("\n")
sys.stdout.write("".join(listM))
list2.reverse()
sys.stdout.write("\n")
sys.stdout.write("".join(list2))
sys.stdout.write("\n")
sys.stdout.write("Alignment score: "+str(H[len(seq1)][len(seq2)]))
sys.stdout.write("\n")           
