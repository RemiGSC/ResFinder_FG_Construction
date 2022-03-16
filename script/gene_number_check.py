#!/usr/bin/python

# HERE WE WANT TO CHECK IF THERE ARE SEVERAL ANNOTATION FOR EACH ACCESSION NUMBER AND KEEP ONLY CERTAIN PHENOTYPE CAUSING GENE

# First, we define all the input and output file :  

i_inserts = "/home/remi.gschwind/resfinder_FG/output/merged_data/lenght_checked/inserts_rf_cured_atb_size_valid.csv"
o_duplicate = "/home/remi.gschwind/resfinder_FG/output/merged_data/number_check/duplicate.csv"
o_no_duplicate = "/home/remi.gschwind/resfinder_FG/output/merged_data/number_check/inserts_rf_cured_atb_size_valid_nodup.csv"
o_stats = "/home/remi.gschwind/resfinder_FG/output/merged_data/number_check/stats_gene_number_check.csv"

# We create lists for the input lines, the accession numbers in those lines and a list for the future duplicates identified
list_an = []
list_line = []
duplicate_an = []

# We retrieve all the lines and the accession numbers
u = 0
with open(i_inserts , 'r') as f :
    for line in f :
        list_an.append(line.strip().split(';')[0])
        list_line.append(line.strip())
        u += 1
        
print("input :")
print("lines :" , len(list_line))
print("an :" , len(list_an))

# We then add to the duplicate list all the accession numbers which have a count > 1 in the list_an. We also retrieve data for the future stats.
x=0 ; y=0 ; z = 0 ; w=0
for an in list_an :
    if list_an.count(an) > 1 :
        duplicate_an.append(an)
        if list_an.count(an) == 2 :
            x += 1
        if list_an.count(an) == 3 :
            y += 1
        if list_an.count(an) == 4 :
            z += 1
    else :
        w += 1
print("single :" , w , "double :" , x , "triple :" , y , "quadruple :" , z)

for an in duplicate_an :
    for acc in list_an :
        if an == acc :
            list_an.remove(an)
        
duplicate_an = list(set(duplicate_an))

with open(o_no_duplicate , 'w') as f:
    with open(o_duplicate , 'w') as g :
        for line in list_line :
            for an in list_an :
                if an in line :
                    f.write(line + '\n')
            for an in duplicate_an :
                if an in line :
                    g.write(line + '\n')



# Statistics.        
with open(o_stats , 'w') as f :
    f.write("input lines" + ';' + str(u) + '\n' + "single" + ';' + str(w) + '\n' + "double" + ';' + str(x) + '\n' + "triple" + ';' + str(y) + '\n' + "quadruple" + ';' + str(z) + '\n' + "output" + ';' + str(len(list_line)) + '\n')
    
# Controls
list_anf = []
with open(o_no_duplicate , 'r') as f :
    for line in f :
        list_anf.append(line.strip().split(';')[0])
list_dupf = []
with open(o_duplicate, 'r') as f :
    for line in f :
        list_dupf.append(line.strip().split(';')[0])

if (len(list_dupf)+len(list_anf)) > len(list_line) :
    print("LINES COUNTED TWO TIMES")
if (len(list_dupf)+len(list_anf)) < len(list_line) :
    print("MISSING LINES")
if (len(list_dupf)+len(list_anf)) == len(list_line) :
    print("LINES NUMBER OK")

x = 0        
for an in list_an :
    if list_anf.count(an) > 1 : 
        print(an)
        x += 1
if x != 0 :
    print("STILL DUPLICATES !!")
else :
    print("NO DUPLICATES LEFT")

x = 0
for an in duplicate_an :
    for acc in list_anf :
        if an == acc :
            x += 1
if x > 0 :
    print("ERROR -> not each member of duplicates have been erased")
if x == 0 :
    print("OK -> each member of duplicates have been erased")

