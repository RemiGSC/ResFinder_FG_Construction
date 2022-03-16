#!/usr/bin/python

# HERE WE HAVE TO RETRIEVE THE REMAINING ACCESSION NUMBER FOR GETTING ONLY THE GENEBANK WE NEED

i_an = "/home/remi.gschwind/resfinder_FG/output/inserts_rf_cured_atb_size_valid_nodup.csv"
o_an = "/home/remi.gschwind/resfinder_FG/output/remaining_an.csv"
list_an=[]
x = 0
with open( i_an , 'r') as f :
    for line in f :
        list_an.append(line.strip().split(';')[0])
        x += 1
print(x)
y = 0 
# We write all the accession number in a new table used for batch entrez
with open(o_an , 'w') as f :
    for an in list_an :
        f.write(an + '\n')
        y += 1
print(y)
# To make the batch entrez, the file will be split in two text files manually. (batch entrez does not work if there are too many entries)
