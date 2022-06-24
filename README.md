# Construction of the ResFinder FG v.2.0 database 

**DATA** contains all the data recovered from publications using functional metagenomics, namely:
- an: all the accession number retrieved from publications using functional metagenomics
- contigs: all the inserts sequence retrieve from the accession numbers using Batch Entrez
- gb: all the GenBank files retrieved from the accession numbers using Batch Entrez 
- rf_4: a table containing all the ARG annotation obtained after ResFinder v.4.0 annotation using PROKKA.

In **SCRIPT** you can found all the scripts needed for ResFinder FG v.2.0 construction.

## ResFinder FG construction workflow

![Ceci est un exemple d’image](https://github.com/RemiGSC/ResFinder_FG_Construction/blob/main/Construction_scheme.png)

1. All the accession numbers were retrieved from the publications and can be found in data/an/ directory. All the fasta files retrieved using accesion numbers found in publications and Batch Entrez are concatenated into one fasta in data/contigs directory.
Fasta files are then concatenated using command: 
```
cat *fasta > DNA_insert_seq.fasta 
```

2. CD-HIT is used to remove redundant sequences in the concatenated fasta file. 
```
cd-hit-est -i DNA_insert_seq.fasta -o /home/remi.gschwind/resfinder_FG/output/cdhit/DNA_insert_seq_cdhit.fasta -d 0 -c 1 -M 0
```

3. PROKKA is used to annotate each insert sequence.
```
prokka --cpus 6 --locustag prokka --gcode 11 --outdir /home/remi.gschwind/resfinder_FG/output/output_prokka --prefix prokka DNA_insert_seq_cdhit.fasta
```

output/output_prokka/ contains all the output from PROKKA annotation. Next step is done using the prokka.gff file.

4. annotation_curation.py is used to discard insert sequences without ARGs annotation.

5. All the GenBank files retrieved using accesion numbers found in publications and Batch Entrez are found in data/gb directory.
gb_info_retriever.py is used to get information (antibiotic used for selection, environment) associated to insert.

6. merge_gb_annot.py is used to merge information coming from GenBank and PROKKA annotations. Additional step si added to discard non relevant ARG-antibiotic pair.
length_check.py is used to discard genes if length is not relevant.

7. gene_number_check.py is used to discard insert that hold more than one ARG annotation (NOTE: If several ARG are present on 1 insert we do not know which one is responsible of the phenotype).

8. compilation_db.py is used to compile the database in a fasta file. A header composed of the accession number, the antibiotic used for selection, the environment and the annotation; followed by the gene annotation sequence. 

9. CD-HIT is again used to discard redundant genes and we obtain the final nucleic acid database in a fasta format.
```
CD-HIT command: cd-hit-est -i DNA_insert_seq.fasta -o /home/remi.gschwind/resfinder_FG/output/cdhit/DNA_insert_seq_cdhit.fasta -d 0 -c 1 -M 0
```
10. To obtain a protein version of the database, translation.py is used to translate the database and then an extra CD-HIT is used to remove redundant protein.

```
CD-HIT command: cd-hit -i DNA_insert_seq.fasta -o /home/remi.gschwind/resfinder_FG/output/cdhit/DNA_insert_seq_cdhit.fasta -d 0 -c 1 -M 0
```
11. final_stats.py used to check the number of genes obtained in the database. NOTE: RFG_db_construction.sh : script which allows to launch successively the different scripts.

**The final database can be downloaded from /output/RFG_db/ResFinder_FG.fasta (nucleic acid version) or /output/RFG_db/ResFinder_FG.faa (amino acid version).**
