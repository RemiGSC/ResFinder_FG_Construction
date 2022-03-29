#!/usr/bin/python

# SCRIPT FOR DATABASE COMPILATION

# Since we use biopython in the following script, we use SeqIO from Bio.

from Bio import SeqIO

# We specify the directions of input and output files

i_lines = "/home/remi.gschwind/resfinder_FG/output/merged_data/ARGs_number_valid.csv"
i_seq = "/home/remi.gschwind/resfinder_FG/output/DNA_insert_seq.fasta"
o_db = "/home/remi.gschwind/resfinder_FG/output/RFG_db/db.fasta"

# We create the list to group accession numbers, start, end, strand, antibiotic used for selection, gene annotation and isolation source.
list_an=[]
list_start=[]
list_end=[]
list_sens=[]
list_ATB=[]
list_gene=[]
list_source=[]

# We retrieve all the information in the corresponding list.
with open(i_lines ,'r') as f :
    for line in f :
        list_an.append(line.strip().split(';')[0])
        list_start.append(int(line.strip().split(';')[4]))
        list_end.append(int(line.strip().split(';')[5]))
        list_sens.append(line.strip().split(';')[6])
        list_ATB.append(line.strip().split(';')[1])
        list_gene.append(line.strip().split(';')[7])
        list_source.append(line.strip().split(';')[2])
        
# We retrieve the sequences in the insert seq fasta file (the right proportion of the sequence). 
list_seq_dico = []
list_seq_id = []
dico = {}

x = 0
for seq_record in SeqIO.parse(i_seq , "fasta"):
    list_seq_id.append(seq_record.id)
    list_seq_dico.append(seq_record.seq)

while x <= len(list_seq_id)-1 :
    dico[list_seq_id[x]] = list_seq_dico[x]
    x += 1

x = 0
list_seq = []
for an in list_an :
    if list_sens[x] == '+' :
        list_seq.append(dico[an][list_start[x]-1:list_end[x]])
    else :
        list_seq.append(dico[an][list_start[x]-1:list_end[x]].reverse_complement())
    x += 1

x =0
with open(o_db , 'w') as f :
    for an in list_an :
        f.write('>' + str(list_gene[x]) + '|' + str(list_an[x]) + '|' + str(list_source[x]) + '|' + str(list_ATB[x]) + '\n' + str(list_seq[x]) + '\n' )
        x += 1
print("entries" , x)
