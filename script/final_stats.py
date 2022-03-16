#!/usr/bin/python

db_fasta = "/home/remi.gschwind/resfinder_FG/output/RFG_db/db.fasta"
rfg_fasta = "/home/remi.gschwind/resfinder_FG/output/RFG_db/ResFinder_FG.fasta"
db_faa = "/home/remi.gschwind/resfinder_FG/output/RFG_db/db.faa"
rfg_faa = "/home/remi.gschwind/resfinder_FG/output/RFG_db/ResFinder_FG.faa"
o_stats = "/home/remi.gschwind/resfinder_FG/output/RFG_db/stats.csv"

x = 0
with open(db_fasta , 'r') as f :
	for line in f :
		if ">" in line :
			x += 1
y = 0
with open(rfg_fasta , 'r') as f :
        for line in f :
                if ">" in line :
                        y += 1

z = 0
with open(db_faa , 'r') as f :
        for line in f :
                if ">" in line :
                        z += 1

a = 0
with open(rfg_faa , 'r') as f :
        for line in f :
                if ">" in line :
                        a += 1

with open(o_stats , 'w') as f :
	f.write("db_fasta" + ";" + str(x) + "\n")
	f.write("rfg_fasta" + ";" + str(y) + "\n")
	f.write("db_faa" + ";" + str(z) + "\n")
	f.write("rfg_faa" + ";" + str(a) + "\n")
