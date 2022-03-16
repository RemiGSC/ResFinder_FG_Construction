#!/usr/bin/python

# HERE WE CHECK FOR THE SIZE OF OUR ANNOTATED GENES TO BE SURE THAT THEY ARE ACTUAL GENE

# Size selection details : - 780bp for beta-lactamases - 534bp for Cat - 1134bp for Tet_efflux - 1919bp for Tet_protection
# - 741 bp for 16S rRNA methlytransferases - 474bp for Dfr - 300bp for d-ala-d-ligase - 300 bp for any other genes

i_inserts = "/home/remi.gschwind/resfinder_FG/output/merged_data/inserts_rf_cured_atb_valid.csv"
o_size_ok = "/home/remi.gschwind/resfinder_FG/output/merged_data/lenght_checked/inserts_rf_cured_atb_size_valid.csv"
o_size_no = "/home/remi.gschwind/resfinder_FG/output/merged_data/lenght_checked/inserts_rf_cured_atb_wrong_size.csv"
o_size_stats = "/home/remi.gschwind/resfinder_FG/output/merged_data/lenght_checked/size_selection_stats.csv"

# We put all the lines of the input table in a list and then remove the line if end-start is below our standard
w_size = []
all_lines = []
i=0
with open(i_inserts , 'r') as f :
    for line in f :
        all_lines.append(line.strip())
        cutline = line.strip().split(';')
        i += 1
        if int(cutline[5])-int(cutline[4]) < 300 :
            w_size.append(cutline[0])
            all_lines.remove(line.strip())
        else :
            if "eta-lactamase" in line :
                if int(cutline[5])-int(cutline[4]) < 780 :
                    w_size.append(cutline[0])
                    all_lines.remove(line.strip())
            if "tetracycline efflux" in line :
                if int(cutline[5])-int(cutline[4]) < 1134 :
                    w_size.append(cutline[0])
                    all_lines.remove(line.strip())
            if "Chloramphenicol acetyltransferase" in line :
                if int(cutline[5])-int(cutline[4]) < 535 :
                    w_size.append(cutline[0])
                    all_lines.remove(line.strip())
            if "tetracycline resistance ribosomal protection" in line :
                if int(cutline[5])-int(cutline[4]) < 1919 :
                    w_size.append(cutline[0])
                    all_lines.remove(line.strip())
            if "methyltransferase" in line :
                if int(cutline[5])-int(cutline[4]) < 740 :
                    w_size.append(cutline[0])
                    all_lines.remove(line.strip())
            if "Dihydrofolate reductase" in line :
                if int(cutline[5])-int(cutline[4]) < 475 :
                    w_size.append(cutline[0])
                    all_lines.remove(line.strip())
        
print("wrong size :" , len(w_size))
print("input insert :" , i)
print("correct size :" , len(all_lines))

with open(o_size_no , 'w') as f :
    for acc_number in w_size :
        f.write(acc_number + '\n')

with open(o_size_ok , 'w') as f :
    for lines in all_lines :
        f.write(lines + '\n')

# STATS        
with open(o_size_stats , 'w') as f :
    f.write("input inserts" + ';' + str(i) + '\n' + "size ok" + ';' + str(len(all_lines)) + '\n' + "size not ok" + ';' + str(len(w_size)))
        
# CONTROLS
size_no = []
with open(o_size_no , 'r') as f :
    for line in f :
        size_no.append(line.strip())
size_ok = []
with open(o_size_ok , 'r') as f :
    for lines in f :
        size_ok.append(line.strip())

        
if (len(size_no) + len(size_ok)) != i :
    print("ERROR : INPUT != OUTPUT")
if (len(size_no) + len(size_ok)) == i :
    print("OK : INPUT = OUTPUT")
