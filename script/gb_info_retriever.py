#!/usr/bin/python

# GENEBANK INFORMATION RETRIEVAL IN EACH PUBLICATION GENEBANK

o_gb = "/home/remi.gschwind/resfinder_FG/output/gb_info/gb_output.csv"

list_AN = []
list_source = []
list_ATB = []

allen188 = []
with open("/home/remi.gschwind/resfinder_FG/data/gb/allen08.gb", 'r') as f :
    for line in f :
        if "VERSION" in line : 
            list_AN.append(line.strip().split("     ")[1])
            allen188.append("1")
        if "/clone=" in line :
            if "CRB" in line :
                list_ATB.append(str("CAR"))
            if "ERY" in line :
                list_ATB.append(str("ERY"))
            if "BLR" in line :
                list_ATB.append(str("bLac"))
        if "/isolation_source=" in line :
            cutline1 = line.strip().split("\"")
            list_source.append(cutline1[1])
            
allen192 = []
with open("/home/remi.gschwind/resfinder_FG/data/gb/allen09.gb", 'r') as f :
    for line in f :
        if "VERSION" in line : 
            list_AN.append(line.strip().split("     ")[1])
            allen192.append("1")
        if "/clone=" in line :
            if "CRB" in line :
                list_ATB.append(str("CAR"))
            if "ERY" in line :
                list_ATB.append(str("ERY"))
            if "BLR" in line :
                list_ATB.append(str("bLac"))
        if "/isolation_source=" in line :
            cutline1 = line.strip().split("\"")
            list_source.append(cutline1[1])

berman = []
with open("/home/remi.gschwind/resfinder_FG/data/gb/berman.gb", 'r') as f :
    for line in f :
        if "VERSION" in line : 
            cutline1 = line.strip().split("     ")
            list_AN.append(cutline1[1])
            berman.append("1")
        if "/clone=" in line :
            if "pAMP" in line :
                list_ATB.append(str("AMP"))
            if "pAZT" in line :
                list_ATB.append(str("ATM"))
            if "pCIP" in line :
                list_ATB.append(str("CIP"))
            if "pTRM" in line :
                list_ATB.append(str("TMP"))
            if "pSXT" in line :
                list_ATB.append(str("SXT"))
        if "/isolation_source=" in line :
            list_source.append(str("retail host"))
            
bohm = []
with open("/home/remi.gschwind/resfinder_FG/data/gb/bohm.gb", 'r') as f :
    for line in f :
        if "VERSION" in line :
            cutline1 = line.strip().split("     ")
            list_AN.append(cutline1[1])
            bohm.append("1")
        if "/isolation_source" in line :
            list_source.append("river_sediment")
        if "/isolate=" in line :
            list_ATB.append("GEN")
            
campbell = []
with open("/home/remi.gschwind/resfinder_FG/data/gb/campbell.gb", 'r') as f :
    for line in f :
        if "VERSION" in line : 
            cutline1 = line.strip().split("     ")
            list_AN.append(cutline1[1])
            campbell.append("1")
        if "/clone=" in line :
            if "PE" in line :
                list_ATB.append(str("PEN"))
            if "AZ" in line :
                list_ATB.append(str("ATM"))
            if "CH" in line :
                list_ATB.append(str("CHL"))
            if "CI" in line :
                list_ATB.append(str("CIP"))
            if "CL" in line :
                list_ATB.append(str("CST"))
            if "CP" in line :
                list_ATB.append(str("FEP"))
            if "CT" in line :
                list_ATB.append(str("CTX"))
            if "CX" in line :
                list_ATB.append(str("FOX"))
            if "CY" in line :
                list_ATB.append(str("CYC"))
            if "CZ" in line :
                list_ATB.append(str("CAZ"))
            if "GE" in line :
                list_ATB.append(str("GEN"))
            if "ME" in line :
                list_ATB.append(str("MEM"))
            if "PI" in line :
                list_ATB.append(str("PIP"))
            if "PI-TZ" in line :
                list_ATB.append(str("TZP"))
            if "TE" in line :
                list_ATB.append(str("TET"))
            if "TG" in line :
                list_ATB.append(str("TGC"))
            if "TR" in line :
                list_ATB.append(str("TMP"))
            if "TR-SX" in line :
                list_ATB.append(str("SXT"))
            if "AMO" in line :
                list_ATB.append(str("AMX"))
            if "AMP" in line :
                list_ATB.append(str("AMP"))
        if "/host=" in line :
            if "gorilla" in line :
                list_source.append(str("Gorilla_feces"))
            if "Homo" in line :
                list_source.append(str("Human_feces"))
            if "troglodyte" in line :
                list_source.append(str("Pan_troglodytes_feces"))

cheng11 = []
with open("/home/remi.gschwind/resfinder_FG/data/gb/cheng.gb", 'r') as f :
    for line in f :
        if "VERSION" in line : 
            cutline1 = line.strip().split("     ")
            list_AN.append(cutline1[1])
            cheng11.append("1")
        if "/isolation_source=" in line :
            cutline1 = line.strip().split("\"")
            list_source.append(cutline1[1])
        if "/clone=" in line :
            if "AC" in line :
                list_ATB.append("AMX")
            if "CY" in line :
                list_ATB.append("CYC")
            if "TE" in line :
                list_ATB.append("TET")
            if "KM" in line :
                list_ATB.append("KAN")

clemente = []
with open("/home/remi.gschwind/resfinder_FG/data/gb/clemente.gb" , 'r') as f :
    for line in f :
        if "VERSION" in line :
            cutline1 = line.strip().split("     ")
            list_AN.append(cutline1[1])
            clemente.append("1")
        if "/host=" in line :
            list_source.append("feces")
        if "/clone=" in line :
            if "PE" in line :
                list_ATB.append("PEN")
            if "PI_" in line :
                list_ATB.append("PIP")
            if "PITZ" in line :
                list_ATB.append("TZP")
            if "CT" in line :
                list_ATB.append("CTX")
            if "CZ" in line :
                list_ATB.append("CAZ")
            if "CP" in line :
                list_ATB.append("FEP")
            if "ME" in line :
                list_ATB.append("MEM")
            if "AZ" in line :
                list_ATB.append("ATM")
            if "CH" in line :
                list_ATB.append("CHL")
            if "TE" in line :
                list_ATB.append("TET")
            if "TG" in line :
                list_ATB.append("TGC")
            if "GE" in line :
                list_ATB.append("GEN")
            if "CI" in line :
                list_ATB.append("CIP")
            if "CL" in line :
                list_ATB.append("CST")
            if "NI" in line :
                list_ATB.append("NIT")

donato = []
with open("/home/remi.gschwind/resfinder_FG/data/gb/donato.gb", 'r') as f :
    for line in f :
        if "VERSION" in line : 
            cutline1 = line.strip().split("     ")
            list_AN.append(cutline1[1])
            donato.append("1")
        if "/isolation_source=" in line :
            cutline1 = line.strip().split("\"")
            list_source.append(cutline1[1])
        if "/clone=" in line :
            if "Amox" in line :
                list_ATB.append("AMX")
            if "Carb" in line :
                list_ATB.append("CAR")
            if "Cefta" in line :
                list_ATB.append("CAZ")
            if "Pip" in line :
                list_ATB.append("PIP")
            if "Tet" in line :
                list_ATB.append("TET")
            if "Kan" in line :
                list_ATB.append("TET")

florez = []
with open("/home/remi.gschwind/resfinder_FG/data/gb/florez.gb", 'r') as f :
    for line in f :
        if "VERSION" in line : 
            cutline1 = line.strip().split("     ")
            list_AN.append(cutline1[1])
            florez.append("1")
        if "/isolation_source=" in line :
            cutline1 = line.strip().split("\"")
            list_source.append(cutline1[1])
        if "/clone=" in line :
            list_ATB.append("TET")

forsberg12 = []
with open("/home/remi.gschwind/resfinder_FG/data/gb/forsberg12.gb", 'r') as f :
    for line in f :
        if "VERSION" in line : 
            cutline1 = line.strip().split("     ")
            list_AN.append(cutline1[1])
            forsberg12.append("1")
        if "/isolation_source=" in line :
            cutline1 = line.strip().split("\"")
            list_source.append(cutline1[1])
        if "/clone=" in line :
            if "AX" in line :
                list_ATB.append("AMX")
            if "CA" in line :
                list_ATB.append("CAR")
            if "CF" in line :
                list_ATB.append("CDR")
            if "CH" in line :
                list_ATB.append("CHL")
            if "MN" in line :
                list_ATB.append("MIN")
            if "PE" in line :
                list_ATB.append("PEN")
            if "PI" in line :
                list_ATB.append("PIP")
            if "SI" in line :
                list_ATB.append("SIS")
            if "CY" in line :
                list_ATB.append("CYC")
            if "GE" in line :
                list_ATB.append("GEN")
            if "OX" in line :
                list_ATB.append("OXY")
            if "TE" in line :
                list_ATB.append("TET")

forsberg14 = []              
with open("/home/remi.gschwind/resfinder_FG/data/gb/forsberg14.gb", 'r') as f :
    for line in f :
        if "VERSION" in line : 
            cutline1 = line.strip().split("     ")
            list_AN.append(cutline1[1])
            forsberg14.append("1")
        if "/isolation_source=" in line :
            cutline1 = line.strip().split("\"")
            list_source.append(cutline1[1])
        if "/clone=" in line :
            if "AZ" in line :
                list_ATB.append("ATM")
            if "CH" in line :
                list_ATB.append("CHL")
            if "CI" in line :
                list_ATB.append("CIP")
            if "CL" in line :
                list_ATB.append("CST")
            if "CP" in line :
                list_ATB.append("FEP")
            if "CT" in line :
                list_ATB.append("CTX")
            if "CX" in line :
                list_ATB.append("FOX")
            if "CY" in line :
                list_ATB.append("CYC")
            if "CZ" in line :
                list_ATB.append("CAZ")
            if "GE" in line :
                list_ATB.append("GEN")
            if "ME" in line :
                list_ATB.append("MEM")
            if "PE" in line :
                list_ATB.append("PEN")
            if "PI" in line :
                list_ATB.append("PIP")
            if "PI-TZ" in line :
                list_ATB.append("TZP")
            if "TE" in line :
                list_ATB.append("TET")
            if "TG" in line :
                list_ATB.append("TGC")
            if "TRSX" in line :
                list_ATB.append("SXT")
            if "TR_" in line :
                list_ATB.append("TMP")                      

gibson= []
with open("/home/remi.gschwind/resfinder_FG/data/gb/gibson.gb", 'r') as f :
    for line in f :
        if "VERSION" in line : 
            cutline1 = line.strip().split("     ")
            list_AN.append(cutline1[1])
            gibson.append("1")
        if "/isolation_source=" in line :
            cutline1 = line.strip().split("\"")
            list_source.append("Preterm_infant_stool")
        if "/clone=" in line :
            if "AXCL" in line :
                list_ATB.append("AMC")
            if "AX_" in line :
                list_ATB.append("AMX")
            if "AP" in line :
                list_ATB.append("AMP")
            if "AZ" in line :
                list_ATB.append("ATM")
            if "CP" in line :
                list_ATB.append("FEP")
            if "CX" in line :
                list_ATB.append("FOX")
            if "CZ" in line :
                list_ATB.append("CAZ")
            if "CH" in line :
                list_ATB.append("CHL")
            if "CI" in line :
                list_ATB.append("CIP")
            if "COL" in line :
                list_ATB.append("CST")
            if "GE" in line :
                list_ATB.append("GEN")
            if "ME" in line :
                list_ATB.append("MEM")
            if "PE" in line :
                list_ATB.append("PEN")
            if "PI" in line :
                list_ATB.append("PIP")
            if "TE" in line :
                list_ATB.append("TET")
            if "TG" in line :
                list_ATB.append("TGC")

gonzalez = []
with open("/home/remi.gschwind/resfinder_FG/data/gb/gonzalezplaza.gb", 'r') as f :
    for line in f :
        if "VERSION" in line : 
            cutline1 = line.strip().split("     ")
            list_AN.append(cutline1[1])
            gonzalez.append("1")
        if "/isolation_source=" in line :
            if "river sediment\"" in line :
                list_source.append("river_sediment")
            if "macrolide" in line :
                list_source.append("macrolide_ polluted_river_sediment")
            if "stream sediment" in line :
                if "polluted" in line :
                    list_source.append("antibiotics_polluted_stream_sediment")
                else :
                    list_source.append("stream_sediment")
            if "pharmaceutical effluent" in line :
                list_source.append("pharmaceutical_effluent")
            if "stream effluent" in line :
                list_source.append("stream_effluent")
        if "/clone=" in line :
            if "AZI" in line :
                list_ATB.append("AZM")
            if "ERI" in line :
                list_ATB.append("ERY")
            if "TRM" in line :
                list_ATB.append("TMP")
            if "TET" in line :
                list_ATB.append("TET")
            if "OTC" in line :
                list_ATB.append("OXY")
            if "AMP" in line :
                list_ATB.append("AMP")
            if "CTX" in line :
                list_ATB.append("CTX")
            if "CIP" in line :
                list_ATB.append("CIP")
            if "SMZ" in line :
                list_ATB.append("SMZ")                

gudeta = []
with open("/home/remi.gschwind/resfinder_FG/data/gb/gudeta.gb", 'r') as f :
    for line in f :
        if "VERSION" in line : 
            cutline1 = line.strip().split("     ")
            list_AN.append(cutline1[1])
            gudeta.append("1")
        if "/isolation_source=" in line :
            cutline1 = line.strip().split("\"")
            list_source.append(cutline1[1])
        if "/country=" in line :
            list_ATB.append("AMX")

hatosy = []
with open("/home/remi.gschwind/resfinder_FG/data/gb/hatosy.gb", 'r') as f :
    for line in f :
        if "VERSION" in line :
            cutline1 = line.strip().split("     ")
            list_AN.append(cutline1[1])
            hatosy.append("1")
        if "/organism" in line :
            list_source.append("ocean")
        if "/clone=" in line :
            if "TET" in line :
                list_ATB.append("TET")
            if "AMP" in line :
                list_ATB.append("AMP")
            if "NIT" in line :
                list_ATB.append("NIT")
            if "SUL" in line :
                list_ATB.append("SDX")     
            if "KAN" in line :
                list_ATB.append("KAN")

lau = []
with open("/home/remi.gschwind/resfinder_FG/data/gb/lau.gb", 'r') as f :
    for line in f :
        if "VERSION" in line : 
            cutline1 = line.strip().split("     ")
            list_AN.append(cutline1[1])
            lau.append("1")
        if "/isolation_source=" in line :
            cutline1 = line.strip().split("\"")
            list_source.append(cutline1[1])
        if "/clone=" in line :
            if "AZI" in line :
                if "AZI" in line :
                    list_ATB.append("AZM")
            else :
                cutline1 = line.strip().split("-")
                list_ATB.append(cutline1[1])

marathe18 = []
with open("/home/remi.gschwind/resfinder_FG/data/gb/marathe18.gb", 'r') as f :
    for line in f :
        if "VERSION" in line : 
            cutline1 = line.strip().split("     ")
            list_AN.append(cutline1[1])
            marathe18.append("1")
        if "/isolation_source=" in line :
            cutline1 = line.strip().split("\"")
            list_source.append(cutline1[1])
        if "/clone=" in line :
            list_ATB.append("AMP")

marathe19 = []
with open("/home/remi.gschwind/resfinder_FG/data/gb/marathe19.gb", 'r') as f :
    for line in f :
        if "VERSION" in line : 
            cutline1 = line.strip().split("     ")
            list_AN.append(cutline1[1])
            marathe19.append("1")
        if "/isolation_source=" in line :
            cutline1 = line.strip().split("\"")
            list_source.append(cutline1[1])
        if "/clone=" in line :
            list_ATB.append("AMP")

martiny = []
with open("/home/remi.gschwind/resfinder_FG/data/gb/martiny.gb", 'r') as f :
    for line in f :
        if "VERSION" in line : 
            cutline1 = line.strip().split("     ")
            list_AN.append(cutline1[1])
            martiny.append("1")
        if "/organism=" in line :
            if "wastewater" in line :
                list_source.append("wastewater")
            if "gut metagenome" in line :
                list_source.append("gull_gut")
            if "soil" in line :
                list_source.append("soil")
        if "/clone=" in line :
            if "_Amp_" in line :
                list_ATB.append("AMP")
            if "_TET_" in line :
                list_ATB.append("TET")
            if "_Pen_" in line :
                list_ATB.append("PEN")
            if "_AX_" in line :
                list_ATB.append("AMX")

mcgarvey = []
with open("/home/remi.gschwind/resfinder_FG/data/gb/mcgarvey.gb", 'r') as f :
    for line in f :
        if "VERSION" in line : 
            cutline1 = line.strip().split("     ")
            list_AN.append(cutline1[1])
            mcgarvey.append("1")
        if "/isolation_source=" in line :
            cutline1 = line.strip().split("\"")
            list_source.append(cutline1[1])
        if "/clone=" in line :
            if "\"kan" in line :
                list_ATB.append("KAN")
            if "\"gen" in line :
                list_ATB.append("GEN")
            if "\"tri" in line :
                list_ATB.append("TMP")
            if "\"tet" in line :
                list_ATB.append("TET")
            if "\"chl" in line :
                list_ATB.append("CHL")
            if "\"rif" in line :
                list_ATB.append("RIF")

mcgivern = []
with open("/home/remi.gschwind/resfinder_FG/data/gb/mcgivern.gb", 'r') as f :
    for line in f :
        if "VERSION" in line : 
            cutline1 = line.strip().split("     ")
            list_AN.append(cutline1[1])
            mcgivern.append("1")
        if "/isolation_source=" in line :
            list_source.append("wastewater+triclosan")
        if "/clone=" in line :
            if "\"Carb" in line :
                list_ATB.append("CAR")
            if "\"Kan" in line :
                list_ATB.append("KAN")
            if "\"Spec" in line :
                list_ATB.append("SPT")
            if "\"Tet" in line :
                list_ATB.append("TET")
	    if "\"Tri" in line :
		list_ATB.append("triclosan")

moore15 = []
with open("/home/remi.gschwind/resfinder_FG/data/gb/moore15.gb", 'r') as f :
    for line in f :
        if "VERSION" in line : 
            cutline1 = line.strip().split("     ")
            list_AN.append(cutline1[1])
            moore15.append("1")
        if "DEFINITION" in line :
            if "_Mom_" in line :
                list_source.append("human_gut")
            if "_Twin" in line :
                list_source.append("newborn_gut")
        if "/clone=" in line :
            if "_PE_" in line :
                list_ATB.append("PEN")
            if "_PI_" in line :
                list_ATB.append("PIP")
            if "_PI-TZ_" in line :
                list_ATB.append("TZP")
            if "_pi-tz_" in line :
                list_ATB.append("TZP")
            if "_PITZ_" in line :
                list_ATB.append("TZP")
            if "_CX_" in line :
                list_ATB.append("FOX")
            if "_CT_" in line :
                list_ATB.append("CTX")
            if "_CZ_" in line :
                list_ATB.append("CAZ")
            if "_CP" in line :
                list_ATB.append("FEP")
            if "_ME_" in line :
                list_ATB.append("MEM")
            if "_AZ_" in line :
                list_ATB.append("ATM")
            if "_GE_" in line :
                list_ATB.append("GEN")
            if "_TE_" in line :
                list_ATB.append("TET")
            if "_TG_" in line :
                list_ATB.append("TGC")
            if "_CL_" in line :
                list_ATB.append("CST")
            if "_CL-" in line :
                list_ATB.append("CST")
            if "_CI_" in line :
                list_ATB.append("CIP")
            if "_TR_" in line :
                list_ATB.append("TMP")
            if "_TR-SX_" in line :
                list_ATB.append("SXT")
            if "_TRSX_" in line :
                list_ATB.append("SXT")
            if "_CY_" in line :
                list_ATB.append("CYC")
            if "_CH_" in line :
                list_ATB.append("CHL")
            if "_TZ_" in line :
                list_ATB.append("TZB")

moore13 = []
with open("/home/remi.gschwind/resfinder_FG/data/gb/moore13.gb", 'r') as f :
    for line in f :
	if "VERSION" in line : 
            cutline1 = line.strip().split("     ")
            list_AN.append(cutline1[1])
            moore13.append("1")
        if "/isolation_source=" in line :
            list_source.append("pediatric_fecal_sample")
        if "/clone=" in line :
            if "_GE_" in line :
                list_ATB.append("GEN")
            if "_PE_" in line :
                list_ATB.append("PEN")
	    if "_PEra_" in line :
		list_ATB.append("PEN")
            if "_PI_" in line :
                list_ATB.append("PIP")
            if "_PI-TZ_" in line :
                list_ATB.append("TZP")
            if "_pi-tz_" in line :
                list_ATB.append("TZP")
            if "_PITZ_" in line :
                list_ATB.append("TZP")
            if "_CX_" in line :
                list_ATB.append("FOX")
            if "_CT_" in line :
                list_ATB.append("CTX")
            if "_CZ_" in line :
                list_ATB.append("CAZ")
            if "_CP_" in line :
                list_ATB.append("FEP")
            if "_AZ_" in line :
                list_ATB.append("ATM")
            if "_ME_" in line :
                list_ATB.append("MEM")
            if "_TE" in line :
                list_ATB.append("TET")
            if "_TG_" in line :
                list_ATB.append("TGC")
            if "_CH_" in line :
                list_ATB.append("CHL")
            if "_CY" in line :
                list_ATB.append("CYC")
            if "_CL_" in line :
                list_ATB.append("CST")
            if "_TR" in line :
                if not "SX" in line :
                    list_ATB.append("TMP")
            if "_TR-SX_" in line :
                list_ATB.append("SXT")
            if "_TRSX" in line :
                list_ATB.append("SXT")
            if "_CI_" in line :
                list_ATB.append("CIP")
            if "_TGp15" in line :
                list_ATB.append("TGC")
            if "_TGp14_" in line :
		list_ATB.append("TGC")
print("MOORE13")
if len(list_AN) != (len(list_ATB)) :
        print("atb missing" , len(list_AN) , len(list_ATB))
else :
        print("atb ok" , len(list_AN) , len(list_ATB))
if len(list_AN) != (len(list_source)) :
        print("source missing" ,  len(list_AN) , len(list_source))
else :
        print("source ok" , len(list_AN) , len(list_source))

munck= []
with open("/home/remi.gschwind/resfinder_FG/data/gb/munck.gb", 'r') as f :
    for line in f :
        if "VERSION" in line : 
            cutline1 = line.strip().split("     ")
            list_AN.append(cutline1[1])
            munck.append("1")
        if "/isolation_source=" in line :
            cutline1 = line.strip().split("\"")
            list_source.append(cutline1[1])
        if "/clone=" in line :
            if "AMP" in line :
                list_ATB.append("AMP")
            if "AMX" in line :
                list_ATB.append("AMX")
            if "CAR" in line :
                list_ATB.append("CAR")
            if "PIP" in line :
                list_ATB.append("PIP")
            if "CTZ" in line :
                list_ATB.append("CAZ")
            if "AMK" in line :
                list_ATB.append("AMK")
            if "GEN" in line :
                list_ATB.append("GEN")
            if "SPC" in line :
                list_ATB.append("SPT")
            if "AZI" in line :
                list_ATB.append("AZM")
            if "ERY" in line :
                list_ATB.append("ERY")
            if "TET" in line :
                list_ATB.append("TET")
            if "CAM" in line :
                list_ATB.append("CHL")
            if "RIF" in line :
                list_ATB.append("RIF")
            if "TMP" in line :
                list_ATB.append("TMP")
            if "SXT" in line :
                list_ATB.append("SXT")
            if "ERM" in line :
                list_ATB.append("ERY")
            if "STX" in line :
                list_ATB.append("SXT")

print("MUNCK")
if len(list_AN) != (len(list_ATB)) :
        print("atb missing" , len(list_AN) , len(list_ATB))
else :
        print("atb ok" , len(list_AN) , len(list_ATB))
if len(list_AN) != (len(list_source)) :
        print("source missing" ,  len(list_AN) , len(list_source))
else :
        print("source ok" , len(list_AN) , len(list_source))

obermeier = []
with open("/home/remi.gschwind/resfinder_FG/data/gb/obermeier.gb", 'r') as f :
    for line in f :
        if "VERSION" in line : 
            cutline1 = line.strip().split("     ")
            list_AN.append(cutline1[1])
            obermeier.append("1")
        if "/isolation_source=" in line :
            cutline1 = line.strip().split("\"")
            list_source.append(cutline1[1])
        if "/clone=" in line :
            list_ATB.append("AMP")

print("OBERMEIER")
if len(list_AN) != (len(list_ATB)) :
        print("atb missing" , len(list_AN) , len(list_ATB))
else :
        print("atb ok" , len(list_AN) , len(list_ATB))
if len(list_AN) != (len(list_source)) :
        print("source missing" ,  len(list_AN) , len(list_source))
else :
        print("source ok" , len(list_AN) , len(list_source))

pawlowski = []
with open("/home/remi.gschwind/resfinder_FG/data/gb/pawlowski.gb", 'r') as f :
    for line in f :
        if "VERSION" in line : 
            cutline1 = line.strip().split("     ")
            list_AN.append(cutline1[1])
            pawlowski.append("1")
        if "/isolation_source=" in line :
            list_source.append(str("Paenibacillus_from_Lechuguilla_cave"))
        if "DEFINITION" in line :
            if "mupirocin" in line :
                list_ATB.append("MUP")
            if "tetracycline" in line :
                list_ATB.append("TET")
            if "lincosamide" in line :
                list_ATB.append("CLI")
            if "chloramphenicol" in line :
                list_ATB.append("CHL")
            if "bacitracin" in line :
                list_ATB.append("CHL")
            if "tiamulin" in line :
                list_ATB.append("TIA")
            if "streptogramin" in line :
                list_ATB.append("STG")
            if "kasugamycin" in line :
                list_ATB.append("KSG")
            if "rifampin" in line :
                list_ATB.append("RIF")
            if "aminoglycoside" in line :
                list_ATB.append("KAN")
            if "capreomycin" in line :
                list_ATB.append("CAP")
            if "macrolide" in line :
                list_ATB.append("CAP")

print("PAWLOWSKI")
if len(list_AN) != (len(list_ATB)) :
        print("atb missing" , len(list_AN) , len(list_ATB))
else :
        print("atb ok" , len(list_AN) , len(list_ATB))
if len(list_AN) != (len(list_source)) :
        print("source missing" ,  len(list_AN) , len(list_source))
else :
        print("source ok" , len(list_AN) , len(list_source))

pehrsson = []
with open("/home/remi.gschwind/resfinder_FG/data/gb/pehrsonn.gb", 'r') as f :
    for line in f :
        if "VERSION" in line :
            cutline1 = line.strip().split("     ")
            list_AN.append(cutline1[1])
            pehrsson.append("1")
        if "/isolation_source" in line :
            cutline1 = line.strip().split("\"")
            list_source.append(cutline1[1])
        if "/clone=" in line :
            if "\"PE" in line :
                list_ATB.append("PEN")
            if "\"AX" in line :
                list_ATB.append("AMX")
            if "\"PI" in line :
                if "TZ" not in line :
                    list_ATB.append("PIP")
                else :
                    list_ATB.append("TZP")
            if "\"CX" in line :
                list_ATB.append("FOX")
            if "\"CT" in line :
                list_ATB.append("CTX")
            if "\"CZ" in line :
                list_ATB.append("CAZ")
            if "\"CP" in line :
                list_ATB.append("FEP")
            if "\"AZ" in line :
                list_ATB.append("ATM")
            if "\"CH" in line :
                list_ATB.append("CHL")
            if "\"TE" in line :
                list_ATB.append("TET")
            if "\"TG" in line :
                list_ATB.append("TGC")
            if "\"GE" in line :
                list_ATB.append("GEN")
            if "\"CI" in line :
                list_ATB.append("CIP")
            if "\"CL" in line :
                list_ATB.append("CST")
            if "\"NI" in line :
                list_ATB.append("NIT")

print("PEHRSONN")
if len(list_AN) != (len(list_ATB)) :
        print("atb missing" , len(list_AN) , len(list_ATB))
else :
        print("atb ok" , len(list_AN) , len(list_ATB))
if len(list_AN) != (len(list_source)) :
        print("source missing" ,  len(list_AN) , len(list_source))
else :
        print("source ok" , len(list_AN) , len(list_source))

perron = []
with open("/home/remi.gschwind/resfinder_FG/data/gb/perron.gb", 'r') as f :
    for line in f :
        if "VERSION" in line :
            cutline1 = line.strip().split("     ")
            list_AN.append(cutline1[1])
            perron.append("1")
        if "/isolation_source" in line :
            cutline1 = line.strip().split("\"")
            list_source.append(cutline1[1])
        if "/clone=" in line :
            list_ATB.append(line[29:32])

print("PERRON")
if len(list_AN) != (len(list_ATB)) :
        print("atb missing" , len(list_AN) , len(list_ATB))
else :
        print("atb ok" , len(list_AN) , len(list_ATB))
if len(list_AN) != (len(list_source)) :
        print("source missing" ,  len(list_AN) , len(list_source))
else :
        print("source ok" , len(list_AN) , len(list_source))

rahman = []
with open("/home/remi.gschwind/resfinder_FG/data/gb/rahman.gb" , 'r') as f :
    for line in f :
        if "VERSION" in line :
            cutline1 = line.strip().split("     ")
            list_AN.append(cutline1[1])
            rahman.append("1")
        if "/isolation_source" in line :
            list_source.append("human_saliva")
        if "/clone" in line :
            list_ATB.append("CYC")

reynolds = []
with open("/home/remi.gschwind/resfinder_FG/data/gb/reynolds.gb", 'r') as f :
    for line in f :
        if "VERSION" in line :
            cutline1 = line.strip().split("     ")
            list_AN.append(cutline1[1])
            reynolds.append("1")
        if "/isolation_source" in line :
            list_source.append(str("human_saliva"))
        if "/clone=" in line :
            list_ATB.append(str("TET"))

print("REYNOLDS")
if len(list_AN) != (len(list_ATB)) :
        print("atb missing" , len(list_AN) , len(list_ATB))
else :
        print("atb ok" , len(list_AN) , len(list_ATB))
if len(list_AN) != (len(list_source)) :
        print("source missing" ,  len(list_AN) , len(list_source))
else :
        print("source ok" , len(list_AN) , len(list_source))
            
riesenfeld = []
with open("/home/remi.gschwind/resfinder_FG/data/gb/riesenfeld.gb", 'r') as f :
    for line in f :
        if "VERSION" in line :
            cutline1 = line.strip().split("     ")
            list_AN.append(cutline1[1])
            riesenfeld.append("1")
        if "/isolation_source" in line :
            list_source.append(str("human_saliva"))
        if "/clone=" in line :
            if "CR4" in line :
                list_ATB.append("TET")
            if "CR6" in line :
                list_ATB.append("KAN")
            if "CR5" in line :
                list_ATB.append("KAN")
            if "171D10" in line :
                list_ATB.append("KAN")
            if "85C1" in line :
                list_ATB.append("KAN")
            if "CR7" in line :
                list_ATB.append("KAN")
            if "CR8" in line :
                list_ATB.append("APR")
            if "CR9" in line :
                list_ATB.append("BUT")
            if "CR10" in line :
                list_ATB.append("TOB")
            if "CR11" in line :
                list_ATB.append("SIS")

print("RIESENFELD")
if len(list_AN) != (len(list_ATB)) :
        print("atb missing" , len(list_AN) , len(list_ATB))
else :
        print("atb ok" , len(list_AN) , len(list_ATB))
if len(list_AN) != (len(list_source)) :
        print("source missing" ,  len(list_AN) , len(list_source))
else :
        print("source ok" , len(list_AN) , len(list_source))

sommer = []                
with open("/home/remi.gschwind/resfinder_FG/data/gb/sommer.gb", 'r') as f :
    for line in f :
        if "VERSION" in line :
            cutline1 = line.strip().split("     ")
            list_AN.append(cutline1[1])
            sommer.append("1")
        if "/isolation_source" in line :
            cutline1 = line.strip().split("\"")
            list_source.append(cutline1[1])
        if "DEFINITION" in line :
            if "CY_" in line :
                list_ATB.append("CYC")
            if "AM_" in line :
                list_ATB.append("AMK")
            if "GE_" in line :
                list_ATB.append("GEN")
            if "SI_" in line :
                list_ATB.append("SIS")
            if "chloramphenicol" in line :
                list_ATB.append("CHL")
            if "AX_" in line :
                list_ATB.append("AMX")
            if "CA_" in line :
                list_ATB.append("CAR")
            if "PE_" in line :
                list_ATB.append("PEN")
            if "PI_" in line :
                list_ATB.append("PIP")
            if "CF_" in line :
                list_ATB.append("CDR")
            if "MN_" in line :
                list_ATB.append("MIN")
            if "OX_" in line :
                list_ATB.append("OXY")
            if "TE_" in line :
                list_ATB.append("TET")

print("SOMMER")
if len(list_AN) != (len(list_ATB)) :
        print("atb missing" , len(list_AN) , len(list_ATB))
else :
        print("atb ok" , len(list_AN) , len(list_ATB))
if len(list_AN) != (len(list_source)) :
        print("source missing" ,  len(list_AN) , len(list_source))
else :
        print("source ok" , len(list_AN) , len(list_source))

su = []
with open("/home/remi.gschwind/resfinder_FG/data/gb/su.gb", 'r') as f :
    for line in f :
        if "VERSION" in line :
            cutline1 = line.strip().split("     ")
            list_AN.append(cutline1[1])
            su.append("1")
        if "/isolation_source" in line :
            cutline1 = line.strip().split("\"")
            list_source.append(cutline1[1])
        if "/clone=" in line :
            if "Kan" in line :
                list_ATB.append("KAN")
            if "Str" in line :
                list_ATB.append("STR")
            if "Rif" in line :
                list_ATB.append("RIF")
            if "Chl" in line :
                list_ATB.append("CHL")
            if "Ami" in line :
                list_ATB.append("AMK")
            if "Gen" in line :
                list_ATB.append("GEN")
            if "Tet" in line :
                list_ATB.append("TET")
            if "Min" in line :
                list_ATB.append("MIN")

print("SU")
if len(list_AN) != (len(list_ATB)) :
        print("atb missing" , len(list_AN) , len(list_ATB))
else :
        print("atb ok" , len(list_AN) , len(list_ATB))
if len(list_AN) != (len(list_source)) :
        print("source missing" ,  len(list_AN) , len(list_source))
else :
        print("source ok" , len(list_AN) , len(list_source))

tian = []
with open("/home/remi.gschwind/resfinder_FG/data/gb/tian.gb", 'r') as f :
    for line in f :
        if "VERSION" in line :
            cutline1 = line.strip().split("     ")
            list_AN.append(cutline1[1])
            tian.append("1")
        if "DEFINITION" in line :
            list_source.append("honeybee_gut")
        if "/clone=" in line :
            if "T4" in line :
                list_ATB.append("TET")
	    if "T8" in line :
                list_ATB.append("TET")
            if "T9" in line :
                list_ATB.append("TET")
            if "T13" in line :
                list_ATB.append("TET")
            if "T2-5" in line :
                list_ATB.append("TET")
            if "\"TA12\"" in line :
                list_ATB.append("TET")
	    if "TA3" in line :
		list_ATB.append("TET")
            if "TA4" in line :
                list_ATB.append("TET")
	    if "TA7" in line :
		list_ATB.append("TET")
	    if "TA8" in line :
		list_ATB.append("TET")
	    if "\"TA1\"" in line :
		list_ATB.append("TET")
	    if "\"TA1_" in line :
		list_ATB.append("TET")
            if "T3" in line :
                list_ATB.append("TET")
            if "Tc" in line :
                list_ATB.append("TET")
            if "\"A1\"" in line :
                list_ATB.append("TET")
            if "A2" in line :
                list_ATB.append("TET")
            if "\"A3" in line :
                list_ATB.append("TET/AMP")
	    if "RES" in line :
		list_ATB.append("?")
	    if "R_14" in line : 
		list_ATB.append("?")
            if "R_10" in line :
                list_ATB.append("?")
	    if "RE27" in line :
		list_ATB.append("?")
	    if "Res" in line :
		list_ATB.append("?")
	    if len(list_AN) != len(list_ATB) :
	        print(list_AN[len(list_AN)-1])
		print(line)
                break

print("TIAN")
if len(list_AN) != (len(list_ATB)) :
        print("atb missing" , len(list_AN) , len(list_ATB))
else :
        print("atb ok" , len(list_AN) , len(list_ATB))
if len(list_AN) != (len(list_source)) :
        print("source missing" ,  len(list_AN) , len(list_source))
else :
        print("source ok" , len(list_AN) , len(list_source))

torres = []
with open("/home/remi.gschwind/resfinder_FG/data/gb/torrescortes.gb", 'r') as f :
    for line in f :
        if "VERSION" in line :
            cutline1 = line.strip().split("     ")
            list_AN.append(cutline1[1])
            torres.append("1")
        if "/isolation_source" in line :
            cutline1 = line.strip().split("\"")
            list_source.append(cutline1[1])
        if "/clone=" in line :
            if "\"Ap" in line :
                list_ATB.append("AMP")
            if "\"Gm" in line :
                list_ATB.append("GEN")
            if "\"Cm" in line :
                list_ATB.append("CHL")
            if "\"Tm" in line :
                list_ATB.append("TMP")
                
print("TORRES")
if len(list_AN) != (len(list_ATB)) :
        print("atb missing" , len(list_AN) , len(list_ATB))
else :
        print("atb ok" , len(list_AN) , len(list_ATB))
if len(list_AN) != (len(list_source)) :
        print("source missing" ,  len(list_AN) , len(list_source))
else :
        print("source ok" , len(list_AN) , len(list_source))

udikovic = []
with open("/home/remi.gschwind/resfinder_FG/data/gb/udikovic.gb", 'r') as f :
    for line in f :
        if "VERSION" in line :
            cutline1 = line.strip().split("     ")
            list_AN.append(cutline1[1])
            udikovic.append("1")
        if "/isolation_source" in line :
            cutline1 = line.strip().split("\"")
            list_source.append(cutline1[1])
        if "/clone=" in line :
            list_ATB.append("CEF")

print("UDIKOVIC")
if len(list_AN) != (len(list_ATB)) :
        print("atb missing" , len(list_AN) , len(list_ATB))
else :
        print("atb ok" , len(list_AN) , len(list_ATB))
if len(list_AN) != (len(list_source)) :
        print("source missing" ,  len(list_AN) , len(list_source))
else :
        print("source ok" , len(list_AN) , len(list_source))

uyaguari = []
with open("/home/remi.gschwind/resfinder_FG/data/gb/uyaguari.gb", 'r') as f :
    for line in f :
        if "VERSION" in line :
            cutline1 = line.strip().split("     ")
            list_AN.append(cutline1[1])
            uyaguari.append("1")
        if "/isolation_source" in line :
            cutline1 = line.strip().split("\"")
            list_source.append(cutline1[1])
        if "/clone=" in line :
            list_ATB.append("AMP")            

print("UYAGUARI")
if len(list_AN) != (len(list_ATB)) :
        print("atb missing" , len(list_AN) , len(list_ATB))
else :
        print("atb ok" , len(list_AN) , len(list_ATB))
if len(list_AN) != (len(list_source)) :
        print("source missing" ,  len(list_AN) , len(list_source))
else :
        print("source ok" , len(list_AN) , len(list_source))

vercammen = []            
with open("/home/remi.gschwind/resfinder_FG/data/gb/vercamen.gb", 'r') as f :
    for line in f :
        if "VERSION" in line :
            cutline1 = line.strip().split("     ")
            list_AN.append(cutline1[1])
            vercammen.append("1")
        if "/isolation_source" in line :
            cutline1 = line.strip().split("\"")
            list_source.append(cutline1[1])
        if "/clone=" in line :
            list_ATB.append("AMP")

print("VERCAMMEN")
if len(list_AN) != (len(list_ATB)) :
        print("atb missing" , len(list_AN) , len(list_ATB))
else :
        print("atb ok" , len(list_AN) , len(list_ATB))
if len(list_AN) != (len(list_source)) :
        print("source missing" ,  len(list_AN) , len(list_source))
else :
        print("source ok" , len(list_AN) , len(list_source))

versluis = []
with open("/home/remi.gschwind/resfinder_FG/data/gb/versluis.gb", 'r') as f :
    for line in f :
        if "VERSION" in line :
            cutline1 = line.strip().split("     ")
            list_AN.append(cutline1[1])
            versluis.append("1")
        if "/host" in line :
            list_source.append(str("acuatic_sponge"))
        if "/note=" in line :
            if "ampicillin" in line :
                list_ATB.append("AMP")
            if "chloramphenicol" in line :
                list_ATB.append("CHL")
            if "gentamycin" in line :
                list_ATB.append("GEN")
            if "cycloserine" in line :
                list_ATB.append("CYC")
            if "amikacyn" in line :
                list_ATB.append("AMK")
            if "trimethoprim" in line :
                list_ATB.append("TMP")
            if "rifampicin" in line :
                list_ATB.append("RIF")

print("VERSLUIS")
if len(list_AN) != (len(list_ATB)) :
        print("atb missing" , len(list_AN) , len(list_ATB))
else :
        print("atb ok" , len(list_AN) , len(list_ATB))
if len(list_AN) != (len(list_source)) :
        print("source missing" ,  len(list_AN) , len(list_source))
else :
        print("source ok" , len(list_AN) , len(list_source))
            
wang17 = []
with open("/home/remi.gschwind/resfinder_FG/data/gb/wang17.gb", 'r') as f :
    for line in f :
        if "VERSION" in line :
            cutline1 = line.strip().split("     ")
            list_AN.append(cutline1[1])
            wang17.append("1")
        if "/isolation_source" in line :
            cutline1 = line.strip().split("\"")
            list_source.append(cutline1[1])
        if "/clone=" in line :
            list_ATB.append("TET")

print("WANG17")
if len(list_AN) != (len(list_ATB)) :
        print("atb missing" , len(list_AN) , len(list_ATB))
else :
        print("atb ok" , len(list_AN) , len(list_ATB))
if len(list_AN) != (len(list_source)) :
        print("source missing" ,  len(list_AN) , len(list_source))
else :
        print("source ok" , len(list_AN) , len(list_source))

wang21 = []            
with open("/home/remi.gschwind/resfinder_FG/data/gb/wang21.gb", 'r') as f :
    for line in f :
        if "VERSION" in line :
            cutline1 = line.strip().split("     ")
            list_AN.append(cutline1[1])
            wang21.append("1")
        if "/isolation_source" in line :
            cutline1 = line.strip().split("\"")
            list_source.append(cutline1[1])
        if "/note=" in line :
            if "blaDWA1" in line :
                list_ATB.append("AMX/AMP")
            if "blaDWA2" in line :
                list_ATB.append("CAZ/CTX")
            if "blaDWA3" in line :
                list_ATB.append("FOX")
            if "blaDWA4" in line :
                list_ATB.append("AMX")
            if "blaDWB1" in line :
                list_ATB.append("AMX/AMP")
            if "fosU1" in line :
                list_ATB.append("FOF")
            if "fosU2" in line :
                list_ATB.append("FOF")
                
print("WANG21")
if len(list_AN) != (len(list_ATB)) :
        print("atb missing" , len(list_AN) , len(list_ATB))
else :
        print("atb ok" , len(list_AN) , len(list_ATB))
if len(list_AN) != (len(list_source)) :
        print("source missing" ,  len(list_AN) , len(list_source))
else :
        print("source ok" , len(list_AN) , len(list_source))

wichmann = []
with open("/home/remi.gschwind/resfinder_FG/data/gb/wichmann.gb", 'r') as f :
    for line in f :
        if "VERSION" in line :
            cutline1 = line.strip().split("     ")
            list_AN.append(cutline1[1])
            wichmann.append("1")
        if "/isolation_source" in line :
            cutline1 = line.strip().split("\"")
            list_source.append(cutline1[1])
        if "/clone=" in line :
            if "Carb" in line :
                list_ATB.append("CAR")
            if "Ceft" in line :
                list_ATB.append("CAZ")
            if "Cm" in line :
                list_ATB.append("CHL")
            if "Kan" in line :
                list_ATB.append("KAN")
            if "Tet" in line :
                list_ATB.append("TET")

print("WICHMANN")
if len(list_AN) != (len(list_ATB)) :
        print("atb missing" , len(list_AN) , len(list_ATB))
else :
        print("atb ok" , len(list_AN) , len(list_ATB))
if len(list_AN) != (len(list_source)) :
        print("source missing" ,  len(list_AN) , len(list_source))
else :
        print("source ok" , len(list_AN) , len(list_source))

willms19 = []
with open("/home/remi.gschwind/resfinder_FG/data/gb/willms19.gb", 'r') as f :
    for line in f :
        if "VERSION" in line :
            cutline1 = line.strip().split("     ")
            list_AN.append(cutline1[1])
            willms19.append("1")
        if "/isolation_source" in line :
            cutline1 = line.strip().split("\"")
            list_source.append(cutline1[1])
        if "/clone=" in line :
            if "_tet" in line :
                list_ATB.append("TET")
            if "_dhps" in line :
                list_ATB.append("STX")

print("WILLMS19")
if len(list_AN) != (len(list_ATB)) :
        print("atb missing" , len(list_AN) , len(list_ATB))
else :
        print("atb ok" , len(list_AN) , len(list_ATB))
if len(list_AN) != (len(list_source)) :
        print("source missing" ,  len(list_AN) , len(list_source))
else :
        print("source ok" , len(list_AN) , len(list_source))

willms21 = []
with open("/home/remi.gschwind/resfinder_FG/data/gb/willms21.gb", 'r') as f :
    for line in f :
        if "VERSION" in line :
            cutline1 = line.strip().split("     ")
            list_AN.append(cutline1[1])
            willms21.append("1")
        if "/isolation_source" in line :
            cutline1 = line.strip().split("\"")
            list_source.append(cutline1[1])
        if "/clone=" in line :
            if "_amp" in line :
                list_ATB.append("AMP")
            if "_chl" in line :
                list_ATB.append("CHL")
            if "_cef" in line :
                list_ATB.append("CAZ")
            if "_fos" in line :
                list_ATB.append("FOF")
            if "_tri" in line :
                list_ATB.append("TMP")

print("WILLMS21")
if len(list_AN) != (len(list_ATB)) :
        print("atb missing" , len(list_AN) , len(list_ATB))
else :
        print("atb ok" , len(list_AN) , len(list_ATB))
if len(list_AN) != (len(list_source)) :
        print("source missing" ,  len(list_AN) , len(list_source))
else :
        print("source ok" , len(list_AN) , len(list_source))

zhang = []
with open("/home/remi.gschwind/resfinder_FG/data/gb/zhang.gb", 'r') as f :
    for line in f :
        if "VERSION" in line :
            cutline1 = line.strip().split("     ")
            list_AN.append(cutline1[1])
            zhang.append("1")
        if "/isolation_source" in line :
            cutline1 = line.strip().split("\"")
            list_source.append(cutline1[1])
        if "/clone=" in line :
            if "AM1" in line :
                list_ATB.append("CAZ")
            if "RM3" in line :
                list_ATB.append("CAZ")
            if "CX1" in line :
                list_ATB.append("CAZ")
            if "H5" in line :
                list_ATB.append("CAZ")
            if "H33" in line :
                list_ATB.append("CAZ")
            if "CM1" in line :
                list_ATB.append("CTX")

print("ZHANG")
if len(list_AN) != (len(list_ATB)) :
        print("atb missing" , len(list_AN) , len(list_ATB))
else :
        print("atb ok" , len(list_AN) , len(list_ATB))
if len(list_AN) != (len(list_source)) :
        print("source missing" ,  len(list_AN) , len(list_source))
else :
        print("source ok" , len(list_AN) , len(list_source))

zhou = []                
with open("/home/remi.gschwind/resfinder_FG/data/gb/zhou.gb", 'r') as f :
    for line in f :
        if "VERSION" in line :
            cutline1 = line.strip().split("     ")
            list_AN.append(cutline1[1])
            zhou.append("1")
        if "/isolation_source" in line :
            list_source.append("chicken_microbiota")
        if "/clone=" in line :
            if "AMP" in line :
                list_ATB.append("AMP")
            if "TET" in line :
                list_ATB.append("TET")
            if "SPE" in line :
                list_ATB.append("SPT")
            if "CHL" in line :
                list_ATB.append("CHL")

print("ZHOU")
if len(list_AN) != (len(list_ATB)) :
        print("atb missing" , len(list_AN) , len(list_ATB))
else :
        print("atb ok" , len(list_AN) , len(list_ATB))
if len(list_AN) != (len(list_source)) :
        print("source missing" ,  len(list_AN) , len(list_source))
else :
        print("source ok" , len(list_AN) , len(list_source))
          
print(len(list_AN))
print(len(list_source))
print(len(list_ATB))

# We check how many accession numbers we retrieved from each publications :
print("allen188", len(allen188), "allen192", len(allen192), "berman", len(berman), "bohm", len(bohm), "campbell", len(campbell), "cheng11", len(cheng11))
print("clemente", len(clemente), "donato", len(donato), "florez", len(florez), "forsberg12", len(forsberg12), "forsberg14", len(forsberg14), "gibson", len(gibson))
print("gonzalez", len(gonzalez), "gudeta", len(gudeta), "hatosy", len(hatosy), "lau", len(lau), "marathe18", len(marathe18), "marathe19", len(marathe19))
print("martiny", len(martiny), "mcgarvey", len(mcgarvey), "mcgivern", len(mcgivern), "moore13", len(moore13), "moore15", len(moore15), "munck", len(munck))
print("obermeier", len(obermeier), "pawlowski", len(pawlowski), "pehrsson", len(pehrsson), "perron", len(perron), "rahman", len(rahman), "reynolds", len(reynolds))
print("riesenfeld", len(riesenfeld), "sommer", len(sommer), "su", len(su), "tian", len(tian), "torres", len(torres), "udikovic", len(udikovic), "uyaguari", len(uyaguari))
print("vercammen", len(vercammen), "versluis", len(versluis), "wang17", len(wang17), "wang21", len(wang21), "wichmann", len(wichmann), "willms19", len(willms19))
print("willms21", len(willms21), "zhang", len(zhang), "zhou", len(zhou))

# WE WRITE THE INFORMATION IN A NEW TABLE
x = 0
with open(o_gb , 'w') as f :
    for AN in list_AN :
        f.write(list_AN[x] + ';' + list_ATB[x] + ';' + list_source[x] + '\n')
        x = x + 1

print(x)
