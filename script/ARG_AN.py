#!/usr/bin/python

# HERE WE WANT TO RETRIEVE ALL THE ACCESSION NUMBER RESULTING FROM THE PREVIOUS CURATION AND GROUP IT REGARDING THEIR ORIGINAL PUBLICATION

# We put every AN in the corresponding list
allen188 = [] ; marathe19 = [] ; bohm= [] ; cheng13 = []
berman = [] ; martiny = [] ; zhang = [] ; torres = []
campbell = [] ; mcgarvey = [] ; willms19 = []
cheng11 = [] ; mcgivern = [] ; parks = [] ; allen192 = []
clemente = [] ; moore13 = [] ; wang17 = []
donato = [] ; moore15 = [] ; pawlowski = []
florez = [] ; munck = [] ; versluis = [] ; zhou = []
forsberg12 = [] ; pehrsonn = []
forsberg14= [] ; uyaguari = [] ; perron = []
gibson = [] ; vercammen = [] ; udikovic = []
gonzalez = [] ; willms21 = [] ; sommer = []
gudeta = [] ; obermeier = [] ; riesenfeld = []
hatosy = [] ; reynolds = [] ; wichmann = []
lau = [] ; rahman = [] ; su = [] ; tian = []
marathe18 = [] ; wang21 = [] ; lopez = [] ; parsley = []
i_an = "/home/remi.gschwind/resfinder_FG/output/ARGs_inserts.csv"
o_an = "/home/remi.gschwind/resfinder_FG/output/an_for_gb_retrieve.csv"
x = 0
y = 0
with open(i_an , 'r') as f :
    for line in f :
        x += 1
        if "MN3400" in line :
            mcgivern.append(line.strip().split(';')[0])
            y += 1
        if "MW6019" in line :
            willms21.append(line.strip().split(';')[0])
            y += 1
        if "EU4083" in line :
            allen188.append(line.strip().split(';')[0])
            y += 1
        if "KF7910" in line :
            berman.append(line.strip().split(';')[0])
            y += 1
        if "MK93" in line :
            campbell.append(line.strip().split(';')[0])
            y += 1
        if "JN0861" in line :
            cheng11.append(line.strip().split(';')[0])
            y += 1
        if "KJ91" in line :
            clemente.append(line.strip().split(';')[0])
            y += 1
        if "GQ244" in line :
            donato.append(line.strip().split(';')[0])
            y += 1
        if "KY686" in line :
            florez.append(line.strip().split(';')[0])
            y += 1
        if "JX009" in line :
            forsberg12.append(line.strip().split(';')[0])
            y += 1
        if "KJ69" in line :
            forsberg14.append(line.strip().split(';')[0])
            y += 1
        if "KU60" in line :
            gibson.append(line.strip().split(';')[0])
            y += 1
        if "MG58" in line :
            gonzalez.append(line.strip().split(';')[0])
            y += 1
        if "KU1670" in line :
            gudeta.append(line.strip().split(';')[0])
            y += 1
        if "KS307" in line :
            hatosy.append(line.strip().split(';')[0])
            y += 1
        if "KY7053" in line :
            lau.append(line.strip().split(';')[0])
            y += 1
        if "MG7395" in line :
            marathe18.append(line.strip().split(';')[0])
            y += 1
        if "MN0172" in line :
            marathe19.append(line.strip().split(';')[0])
            y += 1
        if "JM42" in line :
            martiny.append(line.strip().split(';')[0])
            y += 1
        if "JF924" in line :
            mcgarvey.append(line.strip().split(';')[0])
            y += 1
        if "KF6" in line :
            moore13.append(line.strip().split(';')[0])
            y += 1
        if "KX12" in line :
            moore15.append(line.strip().split(';')[0])
            y += 1
        if "KT387" in line :
            munck.append(line.strip().split(';')[0])
            y += 1
        if "HQ605913.1" in line :
            uyaguari.append(line.strip().split(';')[0])
            y += 1
        if "KF033132.1" in line :
            vercammen.append(line.strip().split(';')[0])   
            y += 1
        if "MK831000" in line :
            obermeier.append(line.strip().split(';')[0])
            y += 1
        if "MF344584" in line :
            reynolds.append(line.strip().split(';')[0])
            y += 1
        if "KU8862" in line :
            rahman.append(line.strip().split(';')[0])
            y += 1
        if "MW23445" in line :
            wang21.append(line.strip().split(';')[0])
            y += 1
        if "MN215968" in line :
            bohm.append(line.strip().split(';')[0])
            y += 1
        if "KF4853" in line :
            zhang.append(line.strip().split(';')[0])
            y += 1
        if "MK1590" in line :
            willms19.append(line.strip().split(';')[0])
            y += 1
        if "MF445022" in line :
            parks.append(line.strip().split(';')[0])
            y += 1
        if "KX1617" in line :
            wang17.append(line.strip().split(';')[0])
            y += 1
        if "KY6972" in line :
            wang17.append(line.strip().split(';')[0])
            y += 1
        if "KY85366" in line :
            wang17.append(line.strip().split(';')[0])
            y += 1
        if "KX5310" in line :
            pawlowski.append(line.strip().split(';')[0])
            y += 1
        if "KU5779" in line :
            versluis.append(line.strip().split(';')[0])
            y += 1
        if "KU54" in line :
            pehrsonn.append(line.strip().split(';')[0])
            y += 1
        if "KC5204" in line :
            perron.append(line.strip().split(';')[0])
            y += 1
        if "KM1137" in line :
            udikovic.append(line.strip().split(';')[0])
            y += 1
        if "GQ34" in line :
            sommer.append(line.strip().split(';')[0])
            y += 1
        if "AY5668" in line :
            riesenfeld.append(line.strip().split(';')[0])
            y += 1
        if "KJ5129" in line :
            wichmann.append(line.strip().split(';')[0])
            y += 1
        if "JX8755" in line :
            su.append(line.strip().split(';')[0])
            y += 1
        if "KF169941" in line :
            lopez.append(line.strip().split(';')[0])
            y += 1
        if "JQ9669" in line :
            tian.append(line.strip().split(';')[0])            
            y += 1
        if "JS807" in line :
            tian.append(line.strip().split(';')[0])  
            y += 1
        if "JN6257" in line :
            zhou.append(line.strip().split(';')[0])
            y += 1
        if "JN629036" in line :
            cheng13.append(line.strip().split(';')[0]) 
            y += 1
        if "FN6404" in line :
            torres.append(line.strip().split(';')[0]) 
            y += 1
        if "GU72" in line :
            parsley.append(line.strip().split(';')[0])
            y += 1
        if "EU8859" in line :
            allen192.append(line.strip().split(';')[0])
            y += 1
print("input line (after Rf curation) :" , x , "; an put into new files :" , y)
# We make a file for each publication
with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/an_files/berman.txt" , 'w') as f :
    x = 0
    for an in berman :
        f.write(berman[x] + '\n')
        x += 1

with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/an_files/allen188.txt" , 'w') as f :
    x = 0
    for an in allen188 :
        f.write(allen188[x] + '\n')
        x += 1
       
with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/an_files/campbell.txt" , 'w') as f :
    x = 0
    for an in campbell :
        f.write(campbell[x] + '\n')
        x += 1

with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/an_files/cheng11.txt" , 'w') as f :
    x = 0
    for an in cheng11 :
        f.write(cheng11[x] + '\n')
        x += 1
        
with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/an_files/clemente.txt" , 'w') as f :
    x = 0
    for an in clemente :
        f.write(clemente[x] + '\n')
        x += 1
        
with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/an_files/donato.txt" , 'w') as f :
    x = 0
    for an in donato :
        f.write(donato[x] + '\n')
        x += 1
        
with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/an_files/florez.txt" , 'w') as f :
    x = 0
    for an in florez :
        f.write(florez[x] + '\n')
        x += 1
        
with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/an_files/forsberg12.txt" , 'w') as f :
    x = 0
    for an in forsberg12 :
        f.write(forsberg12[x] + '\n')
        x += 1
        
with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/an_files/forsberg14.txt" , 'w') as f :
    x = 0
    for an in forsberg14 :
        f.write(forsberg14[x] + '\n')
        x += 1
        
with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/an_files/gibson.txt" , 'w') as f :
    x = 0
    for an in gibson :
        f.write(gibson[x] + '\n')
        x += 1
        
with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/an_files/gonzalez.txt" , 'w') as f :
    x = 0
    for an in gonzalez :
        f.write(gonzalez[x] + '\n')
        x += 1
        
with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/an_files/gudeta.txt" , 'w') as f :
    x = 0
    for an in gudeta :
        f.write(gudeta[x] + '\n')
        x += 1
        
with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/an_files/hatosy.txt" , 'w') as f :
    x = 0
    for an in hatosy :
        f.write(hatosy[x] + '\n')
        x += 1
        
with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/an_files/lau.txt" , 'w') as f :
    x = 0
    for an in lau :
        f.write(lau[x] + '\n')
        x += 1
        
with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/an_files/marathe18.txt" , 'w') as f :
    x = 0
    for an in marathe18 :
        f.write(marathe18[x] + '\n')
        x += 1
        
with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/an_files/marathe19.txt" , 'w') as f :
    x = 0
    for an in marathe19 :
        f.write(marathe19[x] + '\n')
        x += 1
        
with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/an_files/allen192.txt" , 'w') as f :
    x = 0
    for an in allen192 :
        f.write(allen192[x] + '\n')
        x += 1
        
with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/an_files/martiny.txt" , 'w') as f :
    x = 0
    for an in martiny :
        f.write(martiny[x] + '\n')
        x += 1
        
with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/an_files/mcgarvey.txt" , 'w') as f :
    x = 0
    for an in mcgarvey :
        f.write(mcgarvey[x] + '\n')
        x += 1

with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/an_files/mcgivern.txt" , 'w') as f :
    x = 0
    for an in mcgivern :
        f.write(mcgivern[x] + '\n')
        x += 1

with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/an_files/moore13.txt" , 'w') as f :
    x = 0
    for an in moore13 :
        f.write(moore13[x] + '\n')
        x += 1
        
with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/an_files/moore15.txt" , 'w') as f :
    x = 0
    for an in moore15 :
        f.write(moore15[x] + '\n')
        x += 1
        
with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/an_files/munck.txt" , 'w') as f :
    x = 0
    for an in munck :
        f.write(munck[x] + '\n')
        x += 1
        
with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/an_files/uyaguari.txt" , 'w') as f :
    x = 0
    for an in uyaguari :
        f.write(uyaguari[x] + '\n')
        x += 1
        
with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/an_files/vercammen.txt" , 'w') as f :
    x = 0
    for an in vercammen :
        f.write(vercammen[x] + '\n')
        x += 1
        
with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/an_files/obermeier.txt" , 'w') as f :
    x = 0
    for an in obermeier :
        f.write(obermeier[x] + '\n')
        x += 1
        
with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/an_files/reynolds.txt" , 'w') as f :
    x = 0
    for an in reynolds :
        f.write(reynolds[x] + '\n')
        x += 1
        
with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/an_files/rahman.txt" , 'w') as f :
    x = 0
    for an in rahman :
        f.write(rahman[x] + '\n')
        x += 1
        
with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/an_files/wang21.txt" , 'w') as f :
    x = 0
    for an in wang21 :
        f.write(wang21[x] + '\n')
        x += 1
        
with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/an_files/willms21.txt" , 'w') as f :
    x = 0
    for an in willms21 :
        f.write(willms21[x] + '\n')
        x += 1
        
with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/an_files/bohm.txt" , 'w') as f :
    x = 0
    for an in bohm :
        f.write(bohm[x] + '\n')
        x += 1
        
with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/an_files/zhang.txt" , 'w') as f :
    x = 0
    for an in zhang :
        f.write(zhang[x] + '\n')
        x += 1
        
with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/an_files/willms19.txt" , 'w') as f :
    x = 0
    for an in willms19 :
        f.write(willms19[x] + '\n')
        x += 1
        
with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/an_files/parks.txt" , 'w') as f :
    x = 0
    for an in parks :
        f.write(parks[x] + '\n')
        x += 1
        
with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/an_files/wang17.txt" , 'w') as f :
    x = 0
    for an in wang17 :
        f.write(wang17[x] + '\n')
        x += 1
        
with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/an_files/pawlowski.txt" , 'w') as f :
    x = 0
    for an in pawlowski :
        f.write(pawlowski[x] + '\n')
        x += 1
        
with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/an_files/versluis.txt" , 'w') as f :
    x = 0
    for an in versluis :
        f.write(versluis[x] + '\n')
        x += 1
        
with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/an_files/pehrsonn.txt" , 'w') as f :
    x = 0
    for an in pehrsonn :
        f.write(pehrsonn[x] + '\n')
        x += 1
        
with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/an_files/perron.txt" , 'w') as f :
    x = 0
    for an in perron :
        f.write(perron[x] + '\n')
        x += 1

with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/an_files/udikovic.txt" , 'w') as f :
    x = 0
    for an in udikovic :
        f.write(udikovic[x] + '\n')
        x += 1
        
with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/an_files/sommer.txt" , 'w') as f :
    x = 0
    for an in sommer :
        f.write(sommer[x] + '\n')
        x += 1
        
with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/an_files/riesenfeld.txt" , 'w') as f :
    x = 0
    for an in riesenfeld :
        f.write(riesenfeld[x] + '\n')
        x += 1
        
with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/an_files/wichmann.txt" , 'w') as f :
    x = 0
    for an in wichmann :
        f.write(wichmann[x] + '\n')
        x += 1

with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/an_files/su.txt" , 'w') as f :
    x = 0
    for an in su :
        f.write(su[x] + '\n')
        x += 1
        
with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/an_files/lopez.txt" , 'w') as f :
    x = 0
    for an in lopez :
        f.write(lopez[x] + '\n')
        x += 1
        
with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/an_files/tian.txt" , 'w') as f :
    x = 0
    for an in tian :
        f.write(tian[x] + '\n')
        x += 1
        
with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/an_files/zhou.txt" , 'w') as f :
    x = 0
    for an in zhou :
        f.write(zhou[x] + '\n')
        x += 1

with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/an_files/cheng13.txt" , 'w') as f :
    x = 0
    for an in cheng13 :
        f.write(cheng13[x] + '\n')
        x += 1

with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/an_files/torres.txt" , 'w') as f :
    x = 0
    for an in torres :
        f.write(torres[x] + '\n')
        x += 1

with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/an_files/parsley.txt" , 'w') as f :
    x = 0
    for an in parsley :
        f.write(parsley[x] + '\n')
        x += 1

# We want to enumerate how much unique an we have.
x = 0
all_an = allen188 + marathe19 + bohm + cheng13 + berman + martiny + zhang + torres + campbell + mcgarvey + willms19 + cheng11 + mcgivern + parks + allen192 + clemente + moore13 + wang17 + donato + moore15 + pawlowski + florez + munck + versluis + zhou + forsberg12 + pehrsonn + forsberg14 + uyaguari + perron + gibson + vercammen + udikovic + gonzalez + willms21 + sommer + gudeta + obermeier + riesenfeld + hatosy + reynolds + wichmann + lau + rahman + su + tian + marathe18 + wang21 + lopez + parsley
all_an_unique = []
all_an_dup = []
for an in all_an :
    if all_an.count(an) == 1 :
        all_an_unique.append(an)
    else :
        if all_an_unique.count(an) == 0 :
            all_an_unique.append(an)
            
print(len(all_an) , len(all_an_unique))       
with open(o_an , 'w') as f :
    for an in all_an_unique :
        f.write(an + '\n')
        x += 1
print("list all an (no dup) :" , x)


# Then, we use batch entrez with each text file to retrieve the corresponding gb file
# We check the number of an we retrieved with batch entrez :
y = 0
with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/allen188.gb" , 'r') as f :
    x = 0
    for line in f :
        if "LOCUS" in line :
            x += 1
print("allen188 :" , x)
y += x  

with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/allen192.gb" , 'r') as f :
    x = 0
    for line in f :
        if "LOCUS" in line :
            x += 1
print("allen192 :" , x)
y += x

with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/berman.gb" , 'r') as f :
    x = 0
    for line in f :
        if "LOCUS" in line :
            x += 1
print("berman :" , x)
y += x

with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/bohm.gb" , 'r') as f :
    x = 0
    for line in f :
        if "LOCUS" in line :
            x += 1
print("bohm :" , x)
y += x
     
with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/campbell.gb" , 'r') as f :
    x = 0
    for line in f :
        if "LOCUS" in line :
            x += 1
print("campbell :" , x)
y += x

with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/cheng11.gb" , 'r') as f :
    x = 0
    for line in f :
        if "LOCUS" in line :
            x += 1
print("cheng11 :" , x)
y += x

with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/cheng13.gb" , 'r') as f :
    x = 0
    for line in f :
        if "LOCUS" in line :
            x += 1
print("cheng13 :" , x)
y += x
       
with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/clemente.gb" , 'r') as f :
    x = 0
    for line in f :
        if "LOCUS" in line :
            x += 1
print("clemente :" , x)
y += x
      
with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/donato.gb" , 'r') as f :
    x = 0
    for line in f :
        if "LOCUS" in line :
            x += 1
print("donato :" , x)
y += x
        
with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/florez.gb" , 'r') as f :
    x = 0
    for line in f :
        if "LOCUS" in line :
            x += 1
print("florez :" , x)
y += x
        
with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/forsberg12.gb" , 'r') as f :
    x = 0
    for line in f :
        if "LOCUS" in line :
            x += 1
print("forsberg12 :" , x)
y += x
       
with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/forsberg14.gb" , 'r') as f :
    x = 0
    for line in f :
        if "LOCUS" in line :
            x += 1
print("forsberg14 :" , x)
y += x
        
with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/gibson.gb" , 'r') as f :
    x = 0
    for line in f :
        if "LOCUS" in line :
            x += 1
print("gibson :" , x)
y += x

with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/gonzalez.gb" , 'r') as f :
    x = 0
    for line in f :
        if "LOCUS" in line :
            x += 1
print("gonzalez :" , x)
y += x

with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/gudeta.gb" , 'r') as f :
    x = 0
    for line in f :
        if "LOCUS" in line :
            x += 1
print("gudeta :" , x)
y += x
       
with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/hatosy.gb" , 'r') as f :
    x = 0
    for line in f :
        if "LOCUS" in line :
            x += 1
print("hatosy :" , x)
y += x

with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/lau.gb" , 'r') as f :
    x = 0
    for line in f :
        if "LOCUS" in line :
            x += 1
print("lau :" , x)
y += x
        
with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/lopez.gb" , 'r') as f :
    x = 0
    for line in f :
        if "LOCUS" in line :
            x += 1
print("lopez :" , x)
y += x

with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/macgarvey.gb" , 'r') as f :
    x = 0
    for line in f :
        if "LOCUS" in line :
            x += 1
print("macgarvey :" , x)
y += x

with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/marathe18.gb" , 'r') as f :
    x = 0
    for line in f :
        if "LOCUS" in line :
            x += 1
print("marathe18 :" , x)
y += x

with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/marathe19.gb" , 'r') as f :
    x = 0
    for line in f :
        if "LOCUS" in line :
            x += 1
print("marathe19 :" , x)
y += x

with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/martiny.gb" , 'r') as f :
    x = 0
    for line in f :
        if "LOCUS" in line :
            x += 1
print("martiny :" , x)
y += x

with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/mcgivern.gb" , 'r') as f :
    x = 0
    for line in f :
        if "LOCUS" in line :
            x += 1
print("mcgivern :" , x)
y += x

with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/moore13.gb" , 'r') as f :
    x = 0
    for line in f :
        if "LOCUS" in line :
            x += 1
print("moore13 :" , x)
y += x
        
with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/moore15.gb" , 'r') as f :
    x = 0
    for line in f :
        if "LOCUS" in line :
            x += 1
print("moore15 :" , x)
y += x
        
with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/munck.gb" , 'r') as f :
    x = 0
    for line in f :
        if "LOCUS" in line :
            x += 1
print("munck :" , x)
y += x
        
with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/obermeier.gb" , 'r') as f :
    x = 0
    for line in f :
        if "LOCUS" in line :
            x += 1
print("obermeier :" , x)
y += x
        
with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/parks.gb" , 'r') as f :
    x = 0
    for line in f :
        if "LOCUS" in line :
            x += 1
print("parks :" , x)
y += x
        
with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/parsley.gb" , 'r') as f :
    x = 0
    for line in f :
        if "LOCUS" in line :
            x += 1
print("parsley :" , x)
y += x
        
with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/pawlowski.gb" , 'r') as f :
    x = 0
    for line in f :
        if "LOCUS" in line :
            x += 1
print("pawlowski :" , x)
y += x

with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/pehrsson.gb" , 'r') as f :
    x = 0
    for line in f :
        if "LOCUS" in line :
            x += 1
print("pehrsson :" , x)
y += x

with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/perron.gb" , 'r') as f :
    x = 0
    for line in f :
        if "LOCUS" in line :
            x += 1
print("perron :" , x)
y += x

with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/rahman.gb" , 'r') as f :
    x = 0
    for line in f :
        if "LOCUS" in line :
            x += 1
print("rahman :" , x)
y += x

with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/reynolds.gb" , 'r') as f :
    x = 0
    for line in f :
        if "LOCUS" in line :
            x += 1
print("reynolds :" , x)
y += x

with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/riesenfeld.gb" , 'r') as f :
    x = 0
    for line in f :
        if "LOCUS" in line :
            x += 1
print("riesenfeld :" , x)
y += x
        
with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/sommer.gb" , 'r') as f :
    x = 0
    for line in f :
        if "LOCUS" in line :
            x += 1
print("sommer :" , x)
y += x

with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/su.gb" , 'r') as f :
    x = 0
    for line in f :
        if "LOCUS" in line :
            x += 1
print("su :" , x)
y += x

with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/tian.gb" , 'r') as f :
    x = 0
    for line in f :
        if "LOCUS" in line :
            x += 1
print("tian :" , x)
y += x

with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/torres.gb" , 'r') as f :
    x = 0
    for line in f :
        if "LOCUS" in line :
            x += 1
print("torres :" , x)
y += x

with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/udikovic.gb" , 'r') as f :
    x = 0
    for line in f :
        if "LOCUS" in line :
            x += 1
print("udikovic :" , x)
y += x

with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/uyaguari.gb" , 'r') as f :
    x = 0
    for line in f :
        if "LOCUS" in line :
            x += 1
print("uyaguari :" , x)
y += x

with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/vercammen.gb" , 'r') as f :
    x = 0
    for line in f :
        if "LOCUS" in line :
            x += 1
print("vercammen :" , x)
y += x

with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/versluis.gb" , 'r') as f :
    x = 0
    for line in f :
        if "LOCUS" in line :
            x += 1
print("versluis :" , x)
y += x

with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/wang17.gb" , 'r') as f :
    x = 0
    for line in f :
        if "LOCUS" in line :
            x += 1
print("wang17 :" , x)
y += x

with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/wang20.gb" , 'r') as f :
    x = 0
    for line in f :
        if "LOCUS" in line :
            x += 1
print("wang20 :" , x)
y += x

with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/wichmann.gb" , 'r') as f :
    x = 0
    for line in f :
        if "LOCUS" in line :
            x += 1
print("wichmann :" , x)
y += x
        
with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/willms18.gb" , 'r') as f :
    x = 0
    for line in f :
        if "LOCUS" in line :
            x += 1
print("willms18 :" , x)
y += x

with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/willms21.gb" , 'r') as f :
    x = 0
    for line in f :
        if "LOCUS" in line :
            x += 1
print("willms21 :" , x)
y += x
                
with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/zhang.gb" , 'r') as f :
    x = 0
    for line in f :
        if "LOCUS" in line :
            x += 1
print("zhang :" , x)
y += x
        
with open("C:/Users/Stagiaire R.Ruppé AD/Desktop/Resfinder FG/210811/ResFinder_FG_db/gb_retrieval/zhou.gb" , 'r') as f :
    x = 0
    for line in f :
        if "LOCUS" in line :
            x += 1
print("zhou :" , x)
y += x
        
print("tot : ", y)
