#!/usr/bin/python

# HERE WE WANT TO SELECT FOR SPECIFIC ANNOTATIONS THAT ARE ARGs.

i_r = "/home/remi.gschwind/resfinder_FG/data/rf_4/resfinder4_cured.csv"
i_contigs = "/home/remi.gschwind/resfinder_FG/output/output_prokka/prokka.gff"
o_rf_cured_temp = "/home/remi.gschwind/resfinder_FG/output/annotation_curation/inserts_rf_cured_temp.csv"
o_stats = "/home/remi.gschwind/resfinder_FG/output/annotation_curation/rf_curation_stats.csv"
o_rf_cured = "/home/remi.gschwind/resfinder_FG/output/annotation_curation/ARGs_inserts.csv"

# retrieve all the line from the cured resfinder annotation table
list_gene_rf = []
with open(i_r , 'r') as f :
    for line in f :
        list_gene_rf.append(line.strip())
print("rf annotation :" , len(list_gene_rf))        

# Retrieve all the line from the prokka annotation table  
line_i = [] 
with open(i_contigs , 'r') as f :
    for line in f :
	if "Prodigal:002006" in line :
	        cutline = line.strip().split("\"")
        	line_i.append(cutline[0])
print("input_line_for_inserts_curation :" , len(line_i))

# Keep the line which have a valid annotation (present in the cured resfinder table)
line_kept = []
for entry in line_i :
    gene = entry.strip().split("product=")[1]
    if list_gene_rf.count(gene) != 0 :
	line_kept.append(entry.strip())
print("kept_line :" , len(line_kept))
print(gene)

with open(o_rf_cured , 'w') as f :
    for line in line_kept  :
        f.write(str(line.strip().split("\t")[0]) + ';' + str(line.strip().split("\t")[3]) + ';' + str(line.strip().split("\t")[4]) + ';' + str(line.strip().split("\t")[6]) + ';' + str(line.strip().split("product=")[1]) +'\n')

# Note : an extra step on excel to get rid of one "\"" in each annotation can be done easily with excel replace function
            
with open(o_stats , 'w') as f :
    f.write("inserts annotations" + ';' + str(len(line_i)) + '\n' + "rf annotations" + ';' + str(len(list_gene_rf)) + '\n' + "selected inserts" + ';' + str(len(line_kept)))
