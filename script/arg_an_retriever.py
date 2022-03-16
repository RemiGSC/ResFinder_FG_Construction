#!/usr/bin/python

# HERE THE OBJECTIVE IS TO RETRIEVE EACH ACCESSION NUMBER OF REMAINING ANNOTATED ARG IN ORDER TO EASILY RETRIEVE GB FILE AND ASSOCIATED INFORMATION WITH BATCH ENTREZ

i_an = "/home/remi.gschwind/resfinder_FG/output/ARGs_inserts.csv"
o_an = "/home/remi.gschwind/resfinder_FG/output/an_for_gb_retrieve.csv"
list_an = []

with open(i_an , 'r') as f :
	for line in f :
		if list_an.count(line.strip().split(";")[0]) == 0 : 
			list_an.append(line.strip().split(";")[0])
with open(o_an , 'w') as f :
	for an in list_an :
		f.write(an + '\n')	
