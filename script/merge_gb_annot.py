#!/usr/bin/python

# WE WANT TO MERGE THE GENEBANK INFORMATION TABLE AND THE RESFINDER CURATED INSERTS TABLE

i_gb = "/home/remi.gschwind/resfinder_FG/output/gb_info/gb_output.csv"
i_inserts = "/home/remi.gschwind/resfinder_FG/output/annotation_curation/ARGs_inserts.csv"
o_merge = "/home/remi.gschwind/resfinder_FG/output/merged_data/o_merge.csv"
o_db_file = "/home/remi.gschwind/resfinder_FG/output/merged_data/ARGs_ATB_valid.csv"
o_elim = "/home/remi.gschwind/resfinder_FG/output/merged_data/inserts_atb_non_valid.csv"
o_stats = "/home/remi.gschwind/resfinder_FG/output/merged_data/atb_correspondance_stats.csv"

# We put the lines from the inserts input in a list
i_insert = []
i_an = []
with open(i_inserts ,'r') as f :
    i = 0
    for line in f :
        i_insert.append(line.strip())
        i_an.append(line.strip().split(';')[0])
        i += 1
print("input inserts :" , i)

# We check if each AN in the gb file is present in the list we just created and we make a new list with both lines coming from the two tables
line_kept = []
i_genebank = []
with open(i_gb,'r') as f :
    i = 0
    for line in f :
        i_genebank.append(line.strip())
        i += 1
print("input gb :" , i)

for line in i_genebank :
    for inserts in i_insert :
        if line.strip().split(';')[0] == inserts.strip().split(';')[0] :
            merged_line = ''.join(line.strip() + ';' + inserts)
            line_kept.append(merged_line.strip())

print("merged" , len(line_kept))

# We write a new table with merged information from the two tables
with open(o_merge , 'w') as f :
    j = 0
    for element in line_kept :
        f.write(line_kept[j] + '\n')
        j += 1
print("MERGE OK")
        
# We cure the o_merge table to keep only lines with antibiotics corresponding to the annotation.
list_corresponding = []
list_non_corresponding = []
with open(o_merge , 'r') as f :
    for line in f :
        #BETA-LACTAMS
        if "AMC" in line :
            if "eta-lactamase" in line :
                list_corresponding.append(line)
            elif "carboxypeptidase" in line :
                list_corresponding.append(line)
            elif "transpeptidase" in line :
                list_corresponding.append(line)
            elif "Methicillin resistance mecR1 protein" in line :
                list_corresponding.append(line)
            else :
                list_non_corresponding.append(line)
        elif ";AMP;" in line :
            if "eta-lactamase" in line :
                list_corresponding.append(line)
            elif "carboxypeptidase" in line :
                list_corresponding.append(line)
            elif "transpeptidase" in line :
                list_corresponding.append(line)
            elif "Methicillin resistance mecR1 protein" in line :
                list_corresponding.append(line)
            else :
                list_non_corresponding.append(line)
        elif "AMX" in line :
            if "eta-lactamase" in line :
                list_corresponding.append(line)
            elif "carboxypeptidase" in line :
                list_corresponding.append(line)
            elif "transpeptidase" in line :
                list_corresponding.append(line)
            elif "Methicillin resistance mecR1 protein" in line :
                list_corresponding.append(line)
            else :
                list_non_corresponding.append(line)
        elif "ATM" in line :
            if "eta-lactamase" in line :
                list_corresponding.append(line)
            elif "carboxypeptidase" in line :
                list_corresponding.append(line)
            elif "transpeptidase" in line :
                list_corresponding.append(line)
            elif "Methicillin resistance mecR1 protein" in line :
                list_corresponding.append(line)
            else :
                list_non_corresponding.append(line)
        elif "CAR" in line :
            if "eta-lactamase" in line :
                list_corresponding.append(line)
            elif "carboxypeptidase" in line :
                list_corresponding.append(line)
            elif "transpeptidase" in line :
                list_corresponding.append(line)
            elif "Methicillin resistance mecR1 protein" in line :
                list_corresponding.append(line)
            else :
                list_non_corresponding.append(line)
        elif "CAZ" in line :
            if "eta-lactamase" in line :
                list_corresponding.append(line)
            elif "carboxypeptidase" in line :
                list_corresponding.append(line)
            elif "transpeptidase" in line :
                list_corresponding.append(line)
            elif "Methicillin resistance mecR1 protein" in line :
                list_corresponding.append(line)
            else :
                list_non_corresponding.append(line)
        elif "CDR" in line :
            if "eta-lactamase" in line :
                list_corresponding.append(line)
            elif "carboxypeptidase" in line :
                list_corresponding.append(line)
            elif "transpeptidase" in line :
                list_corresponding.append(line)
            elif "Methicillin resistance mecR1 protein" in line :
                list_corresponding.append(line)
            else :
                list_non_corresponding.append(line)
        elif "CTX" in line :
            if "eta-lactamase" in line :
                list_corresponding.append(line)
            elif "carboxypeptidase" in line :
                list_corresponding.append(line)
            elif "transpeptidase" in line :
                list_corresponding.append(line)
            elif "Methicillin resistance mecR1 protein" in line :
                list_corresponding.append(line)
            else :
                list_non_corresponding.append(line)
        elif "CEF" in line :
            if "eta-lactamase" in line :
                list_corresponding.append(line)
            elif "carboxypeptidase" in line :
                list_corresponding.append(line)
            elif "transpeptidase" in line :
                list_corresponding.append(line)
            elif "Methicillin resistance mecR1 protein" in line :
                list_corresponding.append(line)
            else :
                list_non_corresponding.append(line)
        elif "CST" in line :
            if "eta-lactamase" in line :
                list_corresponding.append(line)
            elif "carboxypeptidase" in line :
                list_corresponding.append(line)
            elif "transpeptidase" in line :
                list_corresponding.append(line)
            elif "Methicillin resistance mecR1 protein" in line :
                list_corresponding.append(line)
            else :
                list_non_corresponding.append(line)
        elif "FEP" in line :
            if "eta-lactamase" in line :
                list_corresponding.append(line)
            elif "carboxypeptidase" in line :
                list_corresponding.append(line)
            elif "transpeptidase" in line :
                list_corresponding.append(line)
            elif "Methicillin resistance mecR1 protein" in line :
                list_corresponding.append(line)
            else :
                list_non_corresponding.append(line)
        elif "FOX" in line :
            if "eta-lactamase" in line :
                list_corresponding.append(line)
            elif "carboxypeptidase" in line :
                list_corresponding.append(line)
            elif "transpeptidase" in line :
                list_corresponding.append(line)
            elif "Methicillin resistance mecR1 protein" in line :
                list_corresponding.append(line)
            else :
                list_non_corresponding.append(line)
        elif "MEM" in line :
            if "eta-lactamase" in line :
                list_corresponding.append(line)
            elif "carboxypeptidase" in line :
                list_corresponding.append(line)
            elif "transpeptidase" in line :
                list_corresponding.append(line)
            elif "Methicillin resistance mecR1 protein" in line :
                list_corresponding.append(line)
            else :
                list_non_corresponding.append(line)
        elif "PEN" in line :
            if "eta-lactamase" in line :
                list_corresponding.append(line)
            elif "carboxypeptidase" in line :
                list_corresponding.append(line)
            elif "transpeptidase" in line :
                list_corresponding.append(line)
            elif "Methicillin resistance mecR1 protein" in line :
                list_corresponding.append(line)
            else :
                list_non_corresponding.append(line)
        elif "PIP" in line :
            if "eta-lactamase" in line :
                list_corresponding.append(line)
            elif "carboxypeptidase" in line :
                list_corresponding.append(line)
            elif "transpeptidase" in line :
                list_corresponding.append(line)
            elif "Methicillin resistance mecR1 protein" in line :
                list_corresponding.append(line)
            else :
                list_non_corresponding.append(line)
        elif "TZB" in line :
            if "eta-lactamase" in line :
                list_corresponding.append(line)
            elif "carboxypeptidase" in line :
                list_corresponding.append(line)
            elif "transpeptidase" in line :
                list_corresponding.append(line)
            elif "Methicillin resistance mecR1 protein" in line :
                list_corresponding.append(line)
            else :
                list_non_corresponding.append(line)
        elif "TZP" in line :
            if "eta-lactamase" in line :
                list_corresponding.append(line)
            elif "carboxypeptidase" in line :
                list_corresponding.append(line)
            elif "transpeptidase" in line :
                list_corresponding.append(line)
            elif "Methicillin resistance mecR1 protein" in line :
                list_corresponding.append(line)
            else :
                list_non_corresponding.append(line)
        # #PHENICOL
        elif "CHL" in line :
            if "phenicol" in line :
                list_corresponding.append(line)
            else :
                list_non_corresponding.append(line)
        elif "FCL" in line :
            if "phenicol" in line :
                list_corresponding.append(line)
            else :
                list_non_corresponding.append(line)
        # #AMINOSIDE
        elif "GEN" in line :
            if "))-methyltransferase" in line :
                list_corresponding.append(line)
            elif "minoglycoside" in line :
                list_corresponding.append(line)
            elif "Bifunctional AAC/APH" in line :
                list_corresponding.append(line)
            elif "Gentamicin 3-N-acetyltransferase" in line :
                list_corresponding.append(line)
            elif "Streptomycin 3''-adenylyltransferase" in line :
                list_corresponding.append(line)
            else :
                list_non_corresponding.append(line)
        elif "KAN" in line :
            if "))-methyltransferase" in line :
                list_corresponding.append(line)
            elif "minoglycoside" in line :
                list_corresponding.append(line)
            elif "Bifunctional AAC/APH" in line :
                list_corresponding.append(line)
            elif "Gentamicin 3-N-acetyltransferase" in line :
                list_corresponding.append(line)
            elif "Streptomycin 3''-adenylyltransferase" in line :
                list_corresponding.append(line)
            else :
                list_non_corresponding.append(line)
        elif "AMK" in line :
            if "))-methyltransferase" in line :
                list_corresponding.append(line)
            elif "minoglycoside" in line :
                list_corresponding.append(line)
            elif "Bifunctional AAC/APH" in line :
                list_corresponding.append(line)
            elif "Gentamicin 3-N-acetyltransferase" in line :
                list_corresponding.append(line)
            elif "Streptomycin 3''-adenylyltransferase" in line :
                list_corresponding.append(line)
            else :
                list_non_corresponding.append(line)
        elif "TOB" in line :
            if "))-methyltransferase" in line :
                list_corresponding.append(line)
            elif "minoglycoside" in line :
                list_corresponding.append(line)
            elif "Bifunctional AAC/APH" in line :
                list_corresponding.append(line)
            elif "Gentamicin 3-N-acetyltransferase" in line :
                list_corresponding.append(line)
            elif "Streptomycin 3''-adenylyltransferase" in line :
                list_corresponding.append(line)
            else :
                list_non_corresponding.append(line)
        elif "SIS" in line :
            if "))-methyltransferase" in line :
                list_corresponding.append(line)
            elif "minoglycoside" in line :
                list_corresponding.append(line)
            elif "Bifunctional AAC/APH" in line :
                list_corresponding.append(line)
            elif "Gentamicin 3-N-acetyltransferase" in line :
                list_corresponding.append(line)
            elif "Streptomycin 3''-adenylyltransferase" in line :
                list_corresponding.append(line)
            else :
                list_non_corresponding.append(line)
        elif "SPT" in line :
            if "))-methyltransferase" in line :
                list_corresponding.append(line)
            elif "minoglycoside" in line :
                list_corresponding.append(line)
            elif "Bifunctional AAC/APH" in line :
                list_corresponding.append(line)
            elif "Gentamicin 3-N-acetyltransferase" in line :
                list_corresponding.append(line)
            elif "Streptomycin 3''-adenylyltransferase" in line :
                list_corresponding.append(line)
            else :
                list_non_corresponding.append(line)
        elif "STR" in line :
            if "))-methyltransferase" in line :
                list_corresponding.append(line)
            elif "minoglycoside" in line :
                list_corresponding.append(line)
            elif "Bifunctional AAC/APH" in line :
                list_corresponding.append(line)
            elif "Gentamicin 3-N-acetyltransferase" in line :
                list_corresponding.append(line)
            elif "Streptomycin 3''-adenylyltransferase" in line :
                list_corresponding.append(line)
            else :
                list_non_corresponding.append(line)
        # #CYCLINES
        elif "MIN" in line :
            if "etracycline" in line :
                list_corresponding.append(line)
            else :
                list_non_corresponding.append(line)
        elif "OXY" in line :
            if "etracycline" in line :
                list_corresponding.append(line)
            else :
                list_non_corresponding.append(line)
        elif ";TET;" in line :
            if "etracycline" in line :
                list_corresponding.append(line)
            else :
                list_non_corresponding.append(line)
        elif "TGC" in line :
            if "etracycline" in line :
                list_corresponding.append(line)
            else :
                list_non_corresponding.append(line)
        elif "DOX" in line :
            if "etracycline" in line :
                list_corresponding.append(line)
            else :
                list_non_corresponding.append(line)
        # #SULFAMIDES
        elif "SDX" in line :
            if "Dihydropteroate" in line :
                list_corresponding.append(line)
            else :
                list_non_corresponding.append(line)
        elif "SMZ" in line :
            if "Dihydropteroate" in line :
                list_corresponding.append(line)
            else :
                list_non_corresponding.append(line)
        elif "STX" in line :
            if "Dihydropteroate" in line :
                list_corresponding.append(line)
            else :
                list_non_corresponding.append(line)
        elif "SXT" in line :
            if "Dihydrofolate" in line :
                list_corresponding.append(line)
            elif "Dihydropteroate" in line :
                list_corresponding.append(line)
            else :
                list_non_corresponding.append(line)
        elif "TMP" in line :
            if "Dihydrofolate" in line :
                list_corresponding.append(line)
            else :
                list_non_corresponding.append(line)
        #CYCLOSERINE
        elif "CYC" in line :
            if "UDP-N-acetylmuramoyl-tripeptide--D-alanyl-D-alanine ligase" in line :
                list_corresponding.append(line)
            elif "Vancomycin" in line :
                list_corresponding.append(line)
            elif "D-alanine--D-alanine ligase" in line :
                list_corresponding.append(line)
            else :
                list_non_corresponding.append(line)
        # #MACROLIDES
        elif "AZM" in line :
            if "ABC-F type ribosomal protection protein Msr(E)" in line :
                list_corresponding.append(line)
            elif "Ribosomal RNA small subunit methyltransferase A" in line :
                list_corresponding.append(line)
            else :
                list_non_corresponding.append(line)
        elif "ERY" in line :
            if "ABC-F type ribosomal protection protein Msr(E)" in line :
                list_corresponding.append(line)
            elif "Ribosomal RNA small subunit methyltransferase A" in line :
                list_corresponding.append(line)
            else :
                list_non_corresponding.append(line)
        elif "TYL" in line :
            if "ABC-F type ribosomal protection protein Msr(E)" in line :
                list_corresponding.append(line)
            elif "Ribosomal RNA small subunit methyltransferase A" in line :
                list_corresponding.append(line)
            else :
                list_non_corresponding.append(line)
        # #QUINOLONES
        elif "CIP" in line :
            if "Pentapeptide repeat protein" in line :
                list_corresponding.append(line)
            else :
                list_non_corresponding.append(line)
        elif "NAL" in line :
            if "Pentapeptide repeat protein" in line :
                list_corresponding.append(line)
            else :
                list_non_corresponding.append(line)
        # # FOSFOMYCINE
        elif "FOF" in line :
            if "Glutathione transferase FosA" in line :
                list_corresponding.append(line)
            else :
                list_non_corresponding.append(line)
        else :
              list_non_corresponding.append(line)

print(len(list_corresponding))
print(len(list_non_corresponding))


# We write in new files the lines with good ATB-gene match and the others
with open(o_db_file, 'w') as f :
    for element in list_corresponding :
        f.write(element)
with open(o_elim , 'w') as f :
    for element in list_non_corresponding :
        f.write(element)        

# Stats
with open(o_stats , 'w') as f :
    f.write("input inserts" + ';' + str(len(i_insert)) + '\n' + "input gb" + ';' + str(i) + '\n' + "acc number tested" + ';' + str(len(line_kept)) + '\n' + 'atb valid' + ';' + str(len(list_corresponding)) + '\n' + 'atb non valid' + ';' + str(len(list_non_corresponding)))

# CONTROLS
list_merge = []
with open(o_merge, 'r') as f :
    for line in f :
        list_merge.append(line.strip().split(';')[0])
print("merge", len(list_merge))
list_ok = []
with open(o_db_file, 'r') as f :
    for line in f :
        list_ok.append(line.strip())
list_no = []
with open(o_elim, 'r') as f :
    for line in f :
        list_ok.append(line.strip())
        
if (len(list_ok) + len(list_no)) != len(i_insert) :
    print("ERROR : INPUT != OUTPUT")
if (len(list_ok) + len(list_no)) == len(i_insert) :
    print("OK : INPUT = OUTPUT")

## This part of the script is to check for non merged lines in case of INPUT != OUTPUT
# an_no = []
# for an in i_an :
#     if list_merge.count(an) == 0 :
#         an_no.append(an)
    
# print(an_no[0:10])
# print(len(an_no))
# with open("no line.csv" ,'w') as f :
#     for an in an_no :
#         for line in i_insert :
#             if an in line :
#                 f.write(line + '\n')
