# ResFinder_FG_Construction

## DATA: recovered from publications using functional metagenomics.

### an : directory with all the accession number retrieved from publications using functional metagenomics.
### contigs : directory with all the inserts sequence retrieve from the accession numbers using batch entrez.
### gb : directory with all the genebank files retrieved from the accession numbers using batch entrez. 
### rf_4 : directory with a table containing all the ARG annotation obtained after ResFinder 4.0 annotation using Prokka.

## SCRIPT: Directory containing all the scripts needed for ResFinder FG construction.

### RFG_db_construction.sh : script which allows to launch successively the different scripts.
### All the fasta files retrieved using accesion numbers found in publications and Batch Entrez are concatenated into one fasta.
#### OUTPUT: output/DNA_insert_seq.fasta
### CD-HIT is used to remove redundant sequences in the concatenated fasta file. Command: 
#### OUTPUT: output/cdhit/DNA_insert_seq_cdhit.fasta
### PROKKA ANNOTATION: used to annotate each insert sequence. 
#### OUTPUT: output/output_prokka/prokka.gff
### PROKKA ANNOTATION CURATION: annotation_curation.py is used to discard insert sequences without ARGs.
#### OUTPUT: output/annotation_curation/ARGs_inserts.csv
### GB INFORMATION RETRIEVE: gb_info_retriever.py is used to get all the information associated to each insert (antibiotic used for selection, environment)
#### OUTPUT: output/gb_info/gb_output.csv
### MERGE GB INFORMATION - PROKKA ANNOTATION AND CHECKING ATB/ANNOTATION LINK: merge_gb_annot.py is used to merge information coming from genebank and the PROKKA annotation. Additional step si added to discard unrelevant ARG-antibiotic pair.
#### OUTPUT: output/merged_data/ARGs_ATB_valid.csv
### GENE LENGTH CHECK: length_check.py is used to discard genes if length is not relevant. 
#### OUTPUT: output/merged_data/ARGs_size_valid.csv 
### NUMBER OF ARG PER INSERTS CHECK: gene_number_check.py is used to discard insert that hold more than one ARG annotation.
#### OUTPUT: output/merged_data/ARGs_number_valid.csv 
### DATABASE COMPILATION: compilation_db.py is used to compile the database in a fasta file.
#### OUTPUT: output/RFG_db/db.fasta
### CD-HIT: used to discard redundant genes.
#### OUTPUT: output/RFG_db/ResFinder_FG.fasta
### TRANSLATION: used to translate the nucleic acid version of the database in protein version.
#### OUTPUT: output/RFG_db/db.faa
### CD-HIT: used to discard redundant proteins.
#### OUTPUT: output/RFG_db/ResFinder_FG.faa
### STATS: final_stats.py used to check the number of genes of the db
