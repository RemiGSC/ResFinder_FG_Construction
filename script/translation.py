#!/usr/bin/python

# SCRIPT TO GET THE TRANSLATION OF THE DATABASE

# We use SeqIO from biopython.
from Bio import SeqIO

# We specify the direction of the several input and output files.
i_db = "/home/remi.gschwind/resfinder_FG/output/RFG_db/ResFinder_FG.fasta"
o_db = "/home/remi.gschwind/resfinder_FG/output/RFG_db/db.faa"

# We take every sequence, translate it into protein and then put it in a list.
list_prot = []
for seq_record in SeqIO.parse(i_db, "fasta") :
    sequences = seq_record.seq
    an = seq_record.description
    prot = sequences.translate().split("*")
    list_prot.append(an + '\n' + prot[0])
    if len(sequences)%3 != 0 :
        print("not ok")
        print(an)
    
# We write the new database with the an and the protein sequence.
x = 0
with open(o_db, 'w') as f :
    for an in list_prot :
        f.write(">" + str(an) + '\n')
        x += 1

print("genes :" , x)
