#!/bin/bash

# Command line to launch : cdc rund phylogeny:2.0 RFG_db_construction.sh


# CONCATENATION
cd /home/remi.gschwind/resfinder_FG/data/contigs

cat *.fasta > /home/remi.gschwind/resfinder_FG/output/DNA_insert_seq.fasta
mv DNA_insert_seq.fasta /home/remi.gschwind/resfinder_FG/output/DNA_insert_seq.fasta
echo "Concatenation done"

# CDHIT
cd /home/remi.gschwind/resfinder_FG/output
mkdir cdhit
cd-hit-est -i DNA_insert_seq.fasta -o /home/remi.gschwind/resfinder_FG/output/cdhit/DNA_insert_seq_cdhit.fasta -d 0 -c 1 -M 0
echo "cdhit done"

# PROKKA ANNOTATION
cd /home/remi.gschwind/resfinder_FG/output/cdhit
prokka --cpus 6 --locustag prokka --gcode 11 --outdir /home/remi.gschwind/resfinder_FG/output/output_prokka --prefix prokka DNA_insert_seq_cdhit.fasta
echo "Prokka done"

cd /home/remi.gschwind/resfinder_FG/script

# PROKKA ANNOTATION CURATION

mkdir /home/remi.gschwind/resfinder_FG/output/annotation_curation
python annotation_curation.py
echo "Annotation & curation done"

# GB INFORMATION RETRIEVE

mkdir /home/remi.gschwind/resfinder_FG/output/gb_info
python gb_info_retriever.py
echo "GB_information_retrieved"

# MERGING GB INFORMATION AND PROKKA ANNOTATION AND CURING ACCORDING TO ATB/GENE CORRESPONDANCE

mkdir /home/remi.gschwind/resfinder_FG/output/merged_data
python merge_gb_annot.py
echo "GB_and_Annot_merged"

# FILTERING ACCORDING TO GENE LENGTH 

mkdir /home/remi.gschwind/resfinder_FG/output/merged_data/lenght_checked
python length_check.py
echo "ARG_length_checked"

# FILTERING ACCORDING TO NUMBER OF ARG PER INSERTS

mkdir /home/remi.gschwind/resfinder_FG/output/merged_data/number_check
python gene_number_check.py
echo "ARG_number_check"

# COMPILATION OF THE DATABASE

mkdir /home/remi.gschwind/resfinder_FG/output/RFG_db
python3 compilation_db.py
echo "Compilation_done"

# CDHIT FOR NUCLEIC ACID VERSION OF DB

cd /home/remi.gschwind/resfinder_FG/output/RFG_db
cd-hit-est -i db.fasta -o ResFinder_FG.fasta -d 0 -c 1 -M 0
echo "Cdhit_fasta_Ãdone"

# TRANSLATION

cd /home/remi.gschwind/resfinder_FG/script
python3 translation.py
echo "Translation_done"

# CDHIT FOR PROTEIN VERSION OF DB

cd /home/remi.gschwind/resfinder_FG/output/RFG_db
cd-hit -i db.faa -o ResFinder_FG.faa -d 0 -c 1 -M 0
echo "Cdhit_faa_done"

# STATS ON OUTPUT

python /home/remi.gschwind/resfinder_FG/script/final_stats.py
echo "stats_done"
