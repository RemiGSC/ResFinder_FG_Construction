# ResFinder_FG_Construction

## DATA: directory with data recovered from publications using functional metagenomics.

### an : directory with all the accession number retrieved from publications using functional metagenomics.
### contigs : directory with all the inserts sequence retrieve from the accession numbers using batch entrez.
### gb : directory with all the genebank files retrieved from the accession numbers using batch entrez. 
### rf_4 : directory with a table containing all the ARG annotation obtained after ResFinder 4.0 annotation using Prokka.

## SCRIPT: Directory containing all the scripts needed for ResFinder FG construction.

### Process :
#### All the accession numbers were retrieved from the publications and can be found in data/an/ directory.

#### All the fasta files retrieved using accesion numbers found in publications and Batch Entrez are concatenated into one fasta in data/contigs directory.
#### Fasta files are then concatenated using command: cat *fasta > DNA_insert_seq.fasta

#### CD-HIT is used to remove redundant sequences in the concatenated fasta file. 
##### Command: cd-hit-est -i DNA_insert_seq.fasta -o /home/remi.gschwind/resfinder_FG/output/cdhit/DNA_insert_seq_cdhit.fasta -d 0 -c 1 -M 0

#### PROKKA is used to annotate each insert sequence.
#### Command: prokka --cpus 6 --locustag prokka --gcode 11 --outdir /home/remi.gschwind/resfinder_FG/output/output_prokka --prefix prokka DNA_insert_seq_cdhit.fasta
#### OUTPUT: output/output_prokka/ -> Directory with all the output from PROKKA annotation. Next step are done using the prokka.gff file.
#### annotation_curation.py is used to discard insert sequences without ARGs annotation.

#### All the Genebank files retrieved using accesion numbers found in publications and Batch Entrez are found in data/gb directory.
#### gb_info_retriever.py is used to get information (antibiotic used for selection, environment) associated to insert.

#### merge_gb_annot.py is used to merge information coming from genebank and PROKKA annotations. Additional step si added to discard non relevant ARG-antibiotic pair.
#### length_check.py is used to discard genes if length is not relevant.
#### gene_number_check.py is used to discard insert that hold more than one ARG annotation (If several ARG are present on 1 insert we do not know which one is responsible of the phenotype).
#### compilation_db.py is used to compile the database in a fasta file. A header composed of the accession number, the antibiotic used for selection, the environment and the annotation ; followed by the gene annotation sequence. 

#### CD-HIT is again used to discard redundant genes and we obtain the final nucleic acid database in a fasta format.
#### CD-HIT command: cd-hit-est -i DNA_insert_seq.fasta -o /home/remi.gschwind/resfinder_FG/output/cdhit/DNA_insert_seq_cdhit.fasta -d 0 -c 1 -M 0
#### To obtain a protein version of the database, translation.py is used to translate the database and then an extra CD-HIT is used to remove redundant protein.
#### CD-HIT command: cd-hit -i DNA_insert_seq.fasta -o /home/remi.gschwind/resfinder_FG/output/cdhit/DNA_insert_seq_cdhit.fasta -d 0 -c 1 -M 0

#### final_stats.py used to check the number of genes obtained in the database. 

#### RFG_db_construction.sh : script which allows to launch successively the different scripts.
