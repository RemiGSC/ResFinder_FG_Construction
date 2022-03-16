mv: cannot stat 'DNA_insert_seq.fasta': No such file or directory
[10:52:43] This is prokka 1.14.6
[10:52:43] Written by Torsten Seemann <torsten.seemann@gmail.com>
[10:52:43] Homepage is https://github.com/tseemann/prokka
[10:52:43] Local time is Wed Mar 16 10:52:43 2022
[10:52:43] You are remi.gschwind
[10:52:43] Operating system is linux
[10:52:43] You have BioPerl 1.007002
[10:52:43] System has 48 cores.
[10:52:43] Will use maximum of 6 cores.
[10:52:43] Annotating as >>> Bacteria <<<
[10:52:43] Creating new output folder: /home/remi.gschwind/resfinder_FG/output/output_prokka
[10:52:43] Running: mkdir -p \/home\/remi\.gschwind\/resfinder_FG\/output\/output_prokka
[10:52:43] Using filename prefix: prokka.XXX
[10:52:43] Setting HMMER_NCPU=1
[10:52:43] Writing log to: /home/remi.gschwind/resfinder_FG/output/output_prokka/prokka.log
[10:52:43] Command: /usr/bin/prokka --cpus 6 --locustag prokka --gcode 11 --outdir /home/remi.gschwind/resfinder_FG/output/output_prokka --prefix prokka DNA_insert_seq_cdhit.fasta
[10:52:43] Appending to PATH: /opt/progs/prokka/bin/../binaries/linux
[10:52:43] Appending to PATH: /opt/progs/prokka/bin/../binaries/linux/../common
[10:52:43] Appending to PATH: /opt/progs/prokka/bin
[10:52:43] Looking for 'aragorn' - found /opt/progs/prokka/bin/../binaries/linux/aragorn
[10:52:43] Determined aragorn version is 001002 from 'ARAGORN v1.2.38 Dean Laslett'
[10:52:43] Looking for 'blastp' - found /usr/bin/blastp
[10:52:43] Determined blastp version is 002010 from 'blastp: 2.10.0+'
[10:52:43] Looking for 'cmpress' - found /opt/progs/prokka/bin/../binaries/linux/cmpress
[10:52:43] Determined cmpress version is 001001 from '# INFERNAL 1.1.2 (July 2016)'
[10:52:43] Looking for 'cmscan' - found /opt/progs/prokka/bin/../binaries/linux/cmscan
[10:52:43] Determined cmscan version is 001001 from '# INFERNAL 1.1.2 (July 2016)'
[10:52:43] Looking for 'egrep' - found /usr/bin/egrep
[10:52:43] Looking for 'find' - found /usr/bin/find
[10:52:43] Looking for 'grep' - found /usr/bin/grep
[10:52:43] Looking for 'hmmpress' - found /opt/progs/prokka/bin/../binaries/linux/hmmpress
[10:52:43] Determined hmmpress version is 003001 from '# HMMER 3.1b2 (February 2015); http://hmmer.org/'
[10:52:43] Looking for 'hmmscan' - found /opt/progs/prokka/bin/../binaries/linux/hmmscan
[10:52:43] Determined hmmscan version is 003001 from '# HMMER 3.1b2 (February 2015); http://hmmer.org/'
[10:52:43] Looking for 'java' - found /usr/bin/java
[10:52:43] Looking for 'makeblastdb' - found /usr/bin/makeblastdb
[10:52:44] Determined makeblastdb version is 002010 from 'makeblastdb: 2.10.0+'
[10:52:44] Looking for 'minced' - found /opt/progs/prokka/bin/../binaries/linux/../common/minced
[10:52:44] Determined minced version is 002000 from 'minced 0.2.0'
[10:52:44] Looking for 'parallel' - found /usr/bin/parallel
[10:52:44] Determined parallel version is 20160222 from 'GNU parallel 20160222'
[10:52:44] Looking for 'prodigal' - found /usr/local/bin/prodigal
[10:52:44] Determined prodigal version is 002006 from 'Prodigal V2.6.3: February, 2016'
[10:52:44] Looking for 'prokka-genbank_to_fasta_db' - found /opt/progs/prokka/bin/prokka-genbank_to_fasta_db
[10:52:44] Looking for 'sed' - found /usr/bin/sed
[10:52:44] Looking for 'tbl2asn' - found /opt/progs/prokka/bin/../binaries/linux/tbl2asn
[tbl2asn] This copy of tbl2asn is more than a year old.  Please download the current version.
[10:52:44] Determined tbl2asn version is 025008 from 'tbl2asn 25.8   arguments:'
[10:52:44] Using genetic code table 11.
[10:52:44] Loading and checking input file: DNA_insert_seq_cdhit.fasta
[10:52:47] Wrote 21135 contigs totalling 36266595 bp.
[10:52:47] Predicting tRNAs and tmRNAs
[10:52:47] Running: aragorn -l -gc11  -w \/home\/remi\.gschwind\/resfinder_FG\/output\/output_prokka\/prokka\.fna
[10:52:48] 1 tRNA-Arg [38734,38810] 35 (cct)
[10:52:48] 1 tRNA-Pro c[18813,18889] 35 (cgg)
[10:52:48] 1 tRNA-Ile c[1998,2074] 35 (gat)
[10:52:48] 1 tRNA-Ala [2682,2756] 35 (tgc)
[10:52:48] 1 tRNA-Gln [1615,1686] 33 (ttg)
[10:52:48] 1 tRNA-Phe [2654,2727] 34 (gaa)
[10:52:48] 1 tRNA-Lys c[2059,2131] 34 (ttt)
[10:52:48] 1 tRNA-Pro [589,662] 35 (cgg)
[10:52:48] 1 tRNA-Leu c[1502,1584] 35 (tag)
[10:52:48] 1 tRNA-Arg c[1766,1842] 35 (acg)
[10:52:49] 1 tRNA-Leu [598,680] 35 (tag)
[10:52:49] 1 tRNA-Val [1016,1091] 34 (tac)
[10:52:49] 2 tRNA-Asp [1345,1421] 35 (gtc)
[10:52:49] 1 tRNA-Leu [576,657] 34 (tag)
[10:52:49] 1 tmRNA* c[1446,1787] 213,251 ANDNYAEARLAA*
[10:52:49] 1 tRNA-Leu c[68,150] 35 (tag)
[10:52:49] 1 tRNA-Val [2128,2203] 34 (tac)
[10:52:49] 2 tRNA-Asp [2459,2535] 35 (gtc)
[10:52:49] 1 tRNA-Val [2878,2953] 34 (tac)
[10:52:49] 2 tRNA-Asp [3209,3285] 35 (gtc)
[10:52:49] 1 tmRNA* [538,880] 214,252 ANDNYAEARLAA*
[10:52:49] 1 tRNA-Arg c[1362,1439] 36 (acg)
[10:52:49] 1 tRNA-Ser c[345,436] 32 (cga)
[10:52:49] 1 tRNA-Gln c[1153,1227] 33 (ttg)
[10:52:49] 1 tmRNA* [826,1170] 216,254 ANDNYAEARLAA*
[10:52:49] 1 tRNA-Ser c[186,277] 32 (cga)
[10:52:49] 1 tRNA-Asn [1022,1095] 34 (gtt)
[10:52:49] 1 tRNA-Phe c[136,209] 34 (gaa)
[10:52:49] 1 tRNA-Lys [939,1012] 34 (ctt)
[10:52:49] 1 tRNA-Ser c[359,450] 32 (cga)
[10:52:49] 1 tRNA-Phe [3807,3880] 34 (gaa)
[10:52:49] 1 tRNA-Thr [2068,2141] 34 (ggt)
[10:52:49] 2 tRNA-Met [2197,2272] 35 (cat)
[10:52:49] 1 tRNA-Ile [2226,2302] 35 (gat)
[10:52:49] 1 tRNA-Val c[507,582] 34 (tac)
[10:52:50] 1 tRNA-Met c[987,1062] 35 (cat)
[10:52:50] 2 tRNA-Thr c[1117,1190] 34 (ggt)
[10:52:50] 1 tRNA-Trp c[11,86] 34 (cca)
[10:52:50] 1 tmRNA* [1973,2320] 216,257 ANDNNAKEYAPAA*
[10:52:50] 1 tRNA-Asp c[35,111] 35 (gtc)
[10:52:50] 2 tRNA-Val c[365,440] 34 (tac)
[10:52:50] 1 tRNA-Trp [3214,3289] 34 (cca)
[10:52:50] 1 tRNA-Arg [1433,1506] 35 (tcg)
[10:52:50] 1 tRNA-Trp [3214,3289] 34 (cca)
[10:52:50] 1 tRNA-Val c[1352,1428] 35 (cac)
[10:52:50] 1 tRNA-Trp c[22,97] 34 (cca)
[10:52:50] 1 tRNA-Met [434,508] 33 (cat)
[10:52:50] 1 tmRNA* c[221,568] 216,257 ANDNNAKEYALAA*
[10:52:50] 1 tRNA-Arg [49,136] 32 (tcg)
[10:52:50] 1 tRNA-Val c[758,834] 35 (cac)
[10:52:50] 1 tmRNA* c[2231,2572] 213,251 ANDNYAEARLAA*
[10:52:50] 1 tmRNA* [176,517] 213,251 ANDNYAEARLAA*
[10:52:50] 1 tRNA-Val c[2230,2306] 35 (tac)
[10:52:50] 2 tRNA-Val c[2497,2573] 35 (cac)
[10:52:50] 1 tRNA-Lys c[217,292] 34 (ctt)
[10:52:50] 1 tRNA-Glu [2881,2957] 35 (ctc)
[10:52:50] 1 tRNA-Phe [2686,2758] 34 (gaa)
[10:52:50] 1 tRNA-Met [518,592] 35 (cat)
[10:52:50] 2 tRNA-Asp [1063,1137] 35 (gtc)
[10:52:51] 1 tRNA-Phe [158,230] 34 (gaa)
[10:52:51] 1 tRNA-Thr [2138,2213] 34 (tgt)
[10:52:51] 2 tRNA-Tyr [2223,2308] 35 (gta)
[10:52:51] 3 tRNA-Gly [2343,2419] 35 (tcc)
[10:52:51] 4 tRNA-Thr [2460,2534] 33 (ggt)
[10:52:51] 1 tRNA-Met [1404,1476] 33 (cat)
[10:52:51] 1 tRNA-Glu [1426,1502] 35 (ctc)
[10:52:51] 1 tRNA-SeC [149,241] 34 (tca)
[10:52:51] 1 tRNA-Phe [3246,3319] 34 (gaa)
[10:52:51] 1 tRNA-Phe c[1075,1147] 34 (gaa)
[10:52:51] 1 tRNA-Arg c[1450,1523] 35 (tcg)
[10:52:51] 1 tmRNA* [1501,1864] 235,273 ANDNYAEAALAA*
[10:52:51] 1 tRNA-Phe c[2540,2612] 34 (gaa)
[10:52:51] 1 tRNA-Arg [2593,2669] 35 (tcg)
[10:52:51] 1 tRNA-Pro [937,1013] 35 (tgg)
[10:52:51] 1 tRNA-Val [1118,1193] 34 (tac)
[10:52:51] 1 tRNA-Cys c[79,152] 33 (gca)
[10:52:51] 1 tRNA-Met c[2492,2565] 33 (cat)
[10:52:52] 1 tRNA-Leu [431,505] 35 (caa)
[10:52:52] 1 tRNA-Lys [340,413] 34 (ctt)
[10:52:52] 2 tRNA-Lys [3702,3775] 34 (ctt)
[10:52:52] 1 tRNA-Ile [3362,3438] 35 (gat)
[10:52:52] 2 tRNA-Ala [3475,3550] 34 (tgc)
[10:52:52] 1 tRNA-Ile [3175,3251] 35 (gat)
[10:52:52] 2 tRNA-Ala [3288,3363] 34 (tgc)
[10:52:52] 1 tRNA-Lys c[2548,2621] 34 (ctt)
[10:52:53] 1 tRNA-Lys [780,854] 34 (ctt)
[10:52:53] 2 tRNA-Lys [4143,4217] 34 (ctt)
[10:52:53] 1 tRNA-SeC c[1533,1627] 35 (tca)
[10:52:53] 1 tRNA-Met [331,407] 35 (cat)
[10:52:53] 1 tRNA-Leu c[243,327] 35 (caa)
[10:52:53] 1 tRNA-Ser [232,321] 35 (gga)
[10:52:53] 1 tRNA-Lys [206,281] 35 (ttt)
[10:52:53] 1 tRNA-Met [54,130] 35 (cat)
[10:52:53] 1 tRNA-Gly c[670,745] 34 (gcc)
[10:52:53] 1 tRNA-Lys [22641,22714] 34 (ctt)
[10:52:53] 1 tRNA-Leu [2459,2545] 35 (caa)
[10:52:53] 2 tRNA-Ser c[10755,10844] 35 (gga)
[10:52:53] 1 tRNA-Leu [22653,22739] 35 (cag)
[10:52:53] 2 tRNA-Val c[24504,24580] 35 (tac)
[10:52:53] 3 tRNA-Leu c[24595,24679] 35 (gag)
[10:52:53] 4 tRNA-Phe [25305,25380] 34 (gaa)
[10:52:53] 5 tRNA-Gly [25385,25460] 34 (gcc)
[10:52:53] 6 tRNA-Cys [29637,29710] 33 (gca)
[10:52:53] 7 tRNA-Leu [29711,29795] 35 (taa)
[10:52:53] 1 tRNA-Arg [334,410] 35 (acg)
[10:52:53] 2 tRNA-Arg [507,583] 35 (acg)
[10:52:53] 3 tRNA-Arg [639,715] 35 (acg)
[10:52:53] 1 tRNA-Pro [23519,23592] 35 (tgg)
[10:52:53] 2 tRNA-Arg [23637,23712] 36 (tct)
[10:52:53] 3 tRNA-His [23742,23815] 34 (gtg)
[10:52:53] 4 tRNA-Lys [23920,23994] 35 (ctt)
[10:52:53] 1 tRNA-Ser c[8,93] 34 (tga)
[10:52:53] 1 tRNA-Lys c[3556,3630] 35 (ctt)
[10:52:53] 2 tRNA-His c[3652,3727] 34 (gtg)
[10:52:53] 3 tRNA-Arg c[3758,3832] 35 (tct)
[10:52:53] 4 tRNA-Pro c[3873,3946] 35 (tgg)
[10:52:53] 1 tRNA-Ala [8062,8138] 35 (tgc)
[10:52:53] 2 tRNA-Ile [8139,8212] 35 (gat)
[10:52:53] 1 tRNA-Gln [17579,17653] 33 (ttg)
[10:52:53] 1 tRNA-Gln c[28636,28710] 33 (ctg)
[10:52:53] 1 tRNA-Gln [7298,7371] 33 (ctg)
[10:52:53] 1 tRNA-Ala c[8651,8727] 35 (ggc)
[10:52:53] 2 tRNA-Arg c[8773,8850] 36 (gcg)
[10:52:53] 1 tRNA-Asn [9899,9971] 33 (gtt)
[10:52:54] 1 tRNA-Phe [61,138] 37 (gaa)
[10:52:54] 2 tRNA-Tyr [139,221] 36 (gta)
[10:52:54] 3 tRNA-Trp [226,298] 34 (cca)
[10:52:54] 4 tRNA-His [318,392] 35 (gtg)
[10:52:54] 5 tRNA-Gln [404,477] 34 (ttg)
[10:52:54] 6 tRNA-Cys [483,553] 33 (gca)
[10:52:54] 7 tRNA-Leu [575,658] 35 (caa)
[10:52:54] 1 tRNA-Leu c[6566,6648] 35 (caa)
[10:52:54] 1 tmRNA [8312,8666] 94,126 ANDETYALAA*
[10:52:54] 1 tRNA-Leu c[13637,13719] 35 (caa)
[10:52:54] 1 tRNA-Lys c[34513,34588] 34 (ctt)
[10:52:54] 2 tRNA-Arg [35434,35510] 35 (tcg)
[10:52:54] 3 tRNA-Arg [35816,35892] 35 (ccg)
[10:52:54] 1 tRNA-Arg c[13387,13457] 30 (acg)
[10:52:54] 1 tRNA-Val c[1,74] 34 (cac)
[10:52:54] 2 tRNA-Val c[122,194] 33 (gac)
[10:52:54] 3 tRNA-Cys c[235,306] 33 (gca)
[10:52:54] 4 tRNA-Gly c[333,406] 34 (gcc)
[10:52:54] 1 tRNA-Trp c[462,537] 34 (cca)
[10:52:54] 1 tRNA-Asp [37,111] 35 (gtc)
[10:52:54] 1 tRNA-Asp c[2920,2994] 35 (gtc)
[10:52:54] 1 tRNA-Asp c[3292,3366] 35 (gtc)
[10:52:54] 1 tRNA-Asp c[390,464] 35 (gtc)
[10:52:54] 1 tRNA-Asp [170,244] 35 (gtc)
[10:52:54] 1 tRNA-Asp c[3334,3408] 35 (gtc)
[10:52:54] 1 tRNA-Asp [34,108] 35 (gtc)
[10:52:54] 1 tRNA-Asp [34,108] 35 (gtc)
[10:52:55] 1 tRNA-Asp [60,134] 35 (gtc)
[10:52:55] 1 tRNA-Ala c[747,822] 34 (tgc)
[10:52:55] 1 tRNA-Asp [136,210] 35 (gtc)
[10:52:55] 1 tRNA-Ser c[1928,2017] 35 (gga)
[10:52:55] 1 tRNA-Ser c[434,523] 35 (gga)
[10:52:55] 1 tRNA-Asp [507,581] 35 (gtc)
[10:52:56] 1 tRNA-Arg [220,292] 34 (cct)
[10:52:56] 1 tRNA-Asp c[1608,1684] 35 (gtc)
[10:52:56] 1 tRNA-Asp [1412,1486] 35 (gtc)
[10:52:56] 1 tRNA-Asp c[941,1015] 35 (gtc)
[10:52:56] 1 tRNA-Asp [190,264] 35 (gtc)
[10:52:56] 1 tRNA-Asp c[3531,3605] 35 (gtc)
[10:52:56] 1 tRNA-Asp c[3002,3076] 35 (gtc)
[10:52:56] 1 tRNA-Thr [136,211] 34 (cgt)
[10:52:56] 1 tRNA-Thr c[4908,4983] 34 (cgt)
[10:52:56] 1 tRNA-Thr c[679,754] 34 (cgt)
[10:52:56] 1 tRNA-Asp [1675,1751] 35 (gtc)
[10:52:56] 1 tRNA-Ser c[558,647] 35 (gga)
[10:52:56] 1 tRNA-Ser c[483,572] 35 (gga)
[10:52:56] 1 tRNA-Ser c[2017,2106] 35 (gga)
[10:52:56] 1 tRNA-Ser c[536,625] 35 (gga)
[10:52:56] 1 tRNA-Thr c[3918,3993] 34 (cgt)
[10:52:56] 1 tRNA-Thr c[5194,5269] 34 (cgt)
[10:52:56] 1 tRNA-Thr c[4261,4336] 34 (cgt)
[10:52:56] 1 tRNA-Ser [267,356] 35 (gga)
[10:52:56] 1 tRNA-Ser [145,234] 35 (gga)
[10:52:56] 1 tRNA-Ser c[2064,2153] 35 (gga)
[10:52:56] 1 tRNA-Trp [279,351] 34 (cca)
[10:52:56] 1 tRNA-Leu [204,288] 35 (tag)
[10:52:56] 1 tRNA-Ile [522,598] 35 (gat)
[10:52:56] 2 tRNA-Ala [641,716] 34 (tgc)
[10:52:56] 1 tRNA-Asp c[2,78] 35 (gtc)
[10:52:57] 1 tRNA-Asp [544,618] 35 (gtc)
[10:52:57] 2 tRNA-Phe [657,732] 34 (gaa)
[10:52:57] 1 tRNA-Val c[3695,3769] 35 (tac)
[10:52:57] 1 tRNA-Ile [590,666] 35 (gat)
[10:52:57] 2 tRNA-Ala [677,752] 34 (tgc)
[10:52:57] 1 tRNA-Ile [602,678] 35 (gat)
[10:52:57] 2 tRNA-Ala [689,764] 34 (tgc)
[10:52:57] 1 tRNA-Ile [583,659] 35 (gat)
[10:52:57] 2 tRNA-Ala [670,745] 34 (tgc)
[10:52:57] 1 tRNA-Gly c[511,584] 33 (tcc)
[10:52:57] 1 tRNA-Ser [288,375] 35 (gct)
[10:52:57] 1 tRNA-Leu c[386,467] 35 (taa)
[10:52:57] 1 tRNA-Arg [671,744] 34 (cct)
[10:52:57] 1 tRNA-Met [1727,1803] 35 (cat)
[10:52:57] 1 tRNA-Ala c[1543,1616] 34 (cgc)
[10:52:57] 1 tRNA-Arg c[5,78] 35 (ccg)
[10:52:57] 1 tRNA-Ala [777,851] 35 (tgc)
[10:52:57] 2 tRNA-Ile [912,988] 36 (gat)
[10:52:57] 1 tRNA-Asn [2163,2235] 34 (gtt)
[10:52:57] 2 tRNA-Glu [2271,2342] 34 (ttc)
[10:52:57] 3 tRNA-Thr [2357,2429] 34 (tgt)
[10:52:57] 4 tRNA-Met [2481,2555] 35 (cat)
[10:52:57] 1 tRNA-Gly [773,846] 34 (gcc)
[10:52:57] 2 tRNA-Val [892,964] 33 (gac)
[10:52:57] 1 tRNA-Asp [779,856] 36 (gtc)
[10:52:57] 1 tRNA-Arg [1090,1165] 34 (ccg)
[10:52:57] 1 tRNA-Lys c[214,288] 35 (ctt)
[10:52:57] 1 tRNA-Asp [740,814] 35 (gtc)
[10:52:57] 1 tRNA-Glu [127,199] 34 (ttc)
[10:52:57] 1 tRNA-Met [1702,1774] 35 (cat)
[10:52:57] 1 tRNA-Ser [272,361] 35 (gga)
[10:52:57] 1 tRNA-Thr c[1235,1308] 33 (cgt)
[10:52:57] 1 tRNA-Asn c[1356,1429] 34 (gtt)
[10:52:57] 1 tRNA-Asn c[71,144] 34 (gtt)
[10:52:57] 1 tRNA-Glu [2326,2398] 34 (ttc)
[10:52:58] 1 tRNA-Asp c[3028,3102] 35 (gtc)
[10:52:58] 1 tRNA-Leu c[284,374] 34 (gag)
[10:52:58] 1 tRNA-Gln [1173,1247] 35 (ttg)
[10:52:58] 1 tRNA-Gly c[935,1008] 33 (tcc)
[10:52:58] 1 tRNA-Ala c[811,886] 34 (cgc)
[10:52:58] 1 tRNA-Tyr c[371,453] 35 (gta)
[10:52:58] 1 tRNA-Ala [609,683] 34 (ggc)
[10:52:58] 1 tRNA-Trp [1963,2038] 34 (cca)
[10:52:58] 1 tRNA-Gln [621,695] 35 (ttg)
[10:52:58] 1 tRNA-Asp c[3026,3100] 35 (gtc)
[10:52:58] 1 tRNA-Glu c[3939,4011] 34 (ttc)
[10:52:58] 1 tRNA-Asp c[2351,2425] 35 (gtc)
[10:52:58] 1 tRNA-Cys c[224,296] 34 (gca)
[10:52:58] 2 tRNA-Cys c[332,404] 34 (gca)
[10:52:58] 1 tRNA-Thr [331,404] 34 (cgt)
[10:52:58] 2 tRNA-Gly [436,507] 33 (ccc)
[10:52:58] 1 tRNA-Gly c[1341,1412] 33 (ccc)
[10:52:58] 2 tRNA-Thr c[1444,1517] 34 (cgt)
[10:52:58] 1 tRNA-Gly c[2043,2116] 33 (ccc)
[10:52:58] 1 tRNA-Asp c[3012,3086] 35 (gtc)
[10:52:58] 1 tRNA-Glu [250,322] 34 (ttc)
[10:52:58] 1 tRNA-Ala [294,367] 34 (ggc)
[10:52:58] 1 tRNA-Met c[1197,1273] 35 (cat)
[10:52:58] 1 tRNA-Ala c[2254,2329] 34 (cgc)
[10:52:58] 1 tRNA-Leu [67,153] 35 (taa)
[10:52:58] 1 tRNA-Thr [654,728] 35 (tgt)
[10:52:59] 1 tRNA-His [409,484] 34 (gtg)
[10:52:59] 1 tRNA-Arg c[276,351] 34 (cct)
[10:52:59] 1 tRNA-Trp [-2,74] 34 (cca)
[10:52:59] 1 tRNA-Arg c[873,949] 35 (ccg)
[10:52:59] 1 tRNA-Ser c[1944,2030] 33 (gct)
[10:52:59] 1 tRNA-Leu [129,215] 35 (caa)
[10:52:59] 1 tRNA-Ser [205,291] 33 (gct)
[10:52:59] 1 tRNA-Arg [1850,1926] 35 (ccg)
[10:52:59] 1 tRNA-Leu [1924,2010] 35 (caa)
[10:52:59] 1 tRNA-Glu [2,78] 35 (ctc)
[10:52:59] 1 tRNA-Met [4363,4436] 35 (cat)
[10:52:59] 1 tRNA-Arg c[152,224] 34 (ccg)
[10:52:59] 1 tRNA-Asn c[1315,1389] 33 (gtt)
[10:52:59] 2 tRNA-Cys c[1401,1475] 34 (gca)
[10:52:59] 1 tRNA-Leu c[227,309] 35 (tag)
[10:52:59] 1 tRNA-Gly [181,254] 33 (tcc)
[10:52:59] 1 tRNA-Gly c[699,772] 33 (tcc)
[10:53:00] 1 tRNA-Met [4182,4256] 33 (cat)
[10:53:00] 1 tRNA-Asp c[1,76] 35 (gtc)
[10:53:00] 2 tRNA-Val c[326,401] 34 (tac)
[10:53:00] 1 tRNA-Leu [1524,1606] 35 (tag)
[10:53:00] 1 tRNA-Leu [129,211] 35 (tag)
[10:53:00] 1 tRNA-Leu [113,195] 35 (tag)
[10:53:00] 1 tRNA-Leu [112,194] 35 (tag)
[10:53:00] 1 tRNA-Ala [2363,2437] 35 (ggc)
[10:53:00] 1 tRNA-Met [1514,1586] 35 (cat)
[10:53:00] 1 tRNA-Gln c[66,140] 33 (ctg)
[10:53:00] 1 tRNA-Lys c[47,122] 34 (ttt)
[10:53:00] 2 tRNA-Val c[126,201] 34 (tac)
[10:53:00] 1 tRNA-Ile [570,646] 35 (gat)
[10:53:00] 1 tRNA-Met c[77,153] 35 (cat)
[10:53:00] 2 tRNA-Gln c[169,243] 33 (ttg)
[10:53:00] 1 tRNA-Glu [117,192] 35 (ttc)
[10:53:00] 1 tRNA-Glu c[46,121] 35 (ttc)
[10:53:00] 1 tRNA-Ala [1047,1122] 34 (ggc)
[10:53:00] 1 tRNA-Gly c[1081,1151] 33 (ccc)
[10:53:00] 1 tRNA-Met [922,998] 35 (cat)
[10:53:00] 1 tRNA-Ser [626,718] 35 (gct)
[10:53:01] 1 tRNA-Gly c[523,596] 33 (tcc)
[10:53:01] 2 tRNA-Tyr c[620,704] 35 (gta)
[10:53:01] 1 tRNA-Ala c[602,677] 34 (ggc)
[10:53:01] 1 tRNA-Arg [986,1062] 35 (acg)
[10:53:01] 2 tRNA-Glu [1073,1147] 34 (ttc)
[10:53:01] 1 tRNA-His c[22577,22652] 34 (gtg)
[10:53:01] 2 tRNA-Arg c[22672,22748] 35 (tct)
[10:53:01] 3 tRNA-Pro c[22787,22864] 36 (tgg)
[10:53:01] 1 tRNA-Ser c[32013,32102] 35 (cga)
[10:53:01] 1 tRNA-Glu c[27574,27648] 34 (ttc)
[10:53:01] 2 tRNA-Arg c[27659,27735] 35 (acg)
[10:53:01] 1 tRNA-His [30168,30244] 35 (gtg)
[10:53:01] 1 tRNA-Gln [5329,5403] 33 (ttg)
[10:53:01] 1 tRNA-Ser [157,245] 35 (tga)
[10:53:01] 1 tRNA-Tyr c[13490,13574] 35 (gta)
[10:53:01] 2 tRNA-Thr c[13600,13675] 34 (tgt)
[10:53:01] 1 tmRNA* [5025,5408] 255,293 ANDNYAPVALAA*
[10:53:01] Found 299 tRNAs
[10:53:01] Predicting Ribosomal RNAs
[10:53:01] You need either Barrnap or RNAmmer installed to predict rRNAs!
[10:53:01] Skipping ncRNA search, enable with --rfam if desired.
[10:53:01] Total of 289 tRNA + rRNA features
[10:53:01] Searching for CRISPR repeats
[10:53:03] CRISPR1 JS807606.1 10 with 11 spacers
[10:53:03] CRISPR2 JQ966982.1 30406 with 21 spacers
[10:53:03] CRISPR3 JQ966982.1 36994 with 6 spacers
[10:53:03] CRISPR4 JQ966982.1 37799 with 17 spacers
[10:53:03] Found 4 CRISPRs
[10:53:03] Predicting coding sequences
[10:53:03] Contigs total 36266595 bp, so using single mode
[10:53:03] Running: prodigal -i \/home\/remi\.gschwind\/resfinder_FG\/output\/output_prokka\/prokka\.fna -c -m -g 11 -p single -f sco -q


Warning:  Sequence is long (max 32000000 for training).
Training on the first 32000000 bases.

[10:53:24] Excluding CDS which overlaps existing RNA (tRNA) at KJ693454.1:393..686 on + strand
[10:53:24] Excluding CDS which overlaps existing RNA (tRNA) at KJ693528.1:234..527 on + strand
[10:53:24] Excluding CDS which overlaps existing RNA (tRNA) at KJ693689.1:407..700 on + strand
[10:53:25] Excluding CDS which overlaps existing RNA (tRNA) at KJ694194.1:3212..3343 on - strand
[10:53:25] Excluding CDS which overlaps existing RNA (tRNA) at KJ694206.1:3212..3343 on - strand
[10:53:25] Excluding CDS which overlaps existing RNA (tRNA) at KJ694453.1:40..204 on + strand
[10:53:25] Excluding CDS which overlaps existing RNA (tRNA) at KJ694482.1:254..823 on + strand
[10:53:27] Excluding CDS which overlaps existing RNA (tRNA) at KU608135.1:1455..1694 on + strand
[10:53:27] Excluding CDS which overlaps existing RNA (tRNA) at KY705327.1:2420..2698 on + strand
[10:53:27] Excluding CDS which overlaps existing RNA (tRNA) at KY705337.1:477..731 on - strand
[10:53:28] Excluding CDS which overlaps existing RNA (tRNA) at MN340017.1:34223..34654 on - strand
[10:53:28] Excluding CDS which overlaps existing RNA (tRNA) at MN340021.1:13331..14509 on - strand
[10:53:31] Excluding CDS which overlaps existing RNA (tRNA) at KX125842.1:44..301 on - strand
[10:53:31] Excluding CDS which overlaps existing RNA (tRNA) at KX128028.1:1030..1395 on + strand
[10:53:32] Excluding CDS which overlaps existing RNA (tRNA) at KX128623.1:731..949 on - strand
[10:53:32] Excluding CDS which overlaps existing RNA (tRNA) at KU545225.1:406..579 on + strand
[10:53:33] Excluding CDS which overlaps existing RNA (tRNA) at KU545925.1:1915..2220 on + strand
[10:53:33] Excluding CDS which overlaps existing RNA (tRNA) at KU546460.1:1369..1581 on - strand
[10:53:33] Excluding CDS which overlaps existing RNA (tRNA) at KU547400.1:1409..1627 on - strand
[10:53:33] Excluding CDS which overlaps existing RNA (tRNA) at KU547540.1:14..232 on - strand
[10:53:34] Excluding CDS which overlaps existing RNA (tRNA) at JS807419.1:576..761 on - strand
[10:53:34] Excluding CDS which overlaps existing RNA (tRNA) at JQ966977.1:22786..22950 on + strand
[10:53:34] Excluding CDS which overlaps existing RNA (CRISPR) at JQ966982.1:36819..37139 on + strand
[10:53:34] Found 41674 CDS
[10:53:34] Connecting features back to sequences
[10:53:34] Not using genus-specific database. Try --usegenus to enable it.
[10:53:34] Annotating CDS, please be patient.
[10:53:34] Will use 6 CPUs for similarity searching.
[10:53:48] There are still 41674 unannotated CDS left (started with 41674)
[10:53:48] Will use blast to search against /opt/progs/prokka/db/kingdom/Bacteria/IS with 6 CPUs
[10:53:48] Running: cat \/home\/remi\.gschwind\/resfinder_FG\/output\/output_prokka\/prokka\.IS\.tmp\.24\.faa | parallel --gnu --plain -j 6 --block 726362 --recstart '>' --pipe blastp -query - -db /opt/progs/prokka/db/kingdom/Bacteria/IS -evalue 1e-30 -qcov_hsp_perc 90 -num_threads 1 -num_descriptions 1 -num_alignments 1 -seg no > \/home\/remi\.gschwind\/resfinder_FG\/output\/output_prokka\/prokka\.IS\.tmp\.24\.blast 2> /dev/null
[10:55:20] Modify product: Tn3 family transposase Tn5393 => Tn3 family transposase
[10:55:24] Cleaned 1 /product names
[10:55:24] Deleting unwanted file: /home/remi.gschwind/resfinder_FG/output/output_prokka/prokka.IS.tmp.24.faa
[10:55:24] Deleting unwanted file: /home/remi.gschwind/resfinder_FG/output/output_prokka/prokka.IS.tmp.24.blast
[10:55:38] There are still 40787 unannotated CDS left (started with 41674)
[10:55:38] Will use blast to search against /opt/progs/prokka/db/kingdom/Bacteria/AMR with 6 CPUs
[10:55:38] Running: cat \/home\/remi\.gschwind\/resfinder_FG\/output\/output_prokka\/prokka\.AMR\.tmp\.24\.faa | parallel --gnu --plain -j 6 --block 709378 --recstart '>' --pipe blastp -query - -db /opt/progs/prokka/db/kingdom/Bacteria/AMR -evalue 9.99999999999999e-301 -qcov_hsp_perc 90 -num_threads 1 -num_descriptions 1 -num_alignments 1 -seg no > \/home\/remi\.gschwind\/resfinder_FG\/output\/output_prokka\/prokka\.AMR\.tmp\.24\.blast 2> /dev/null
[10:57:40] Deleting unwanted file: /home/remi.gschwind/resfinder_FG/output/output_prokka/prokka.AMR.tmp.24.faa
[10:57:40] Deleting unwanted file: /home/remi.gschwind/resfinder_FG/output/output_prokka/prokka.AMR.tmp.24.blast
[10:57:53] There are still 40402 unannotated CDS left (started with 41674)
[10:57:53] Will use blast to search against /opt/progs/prokka/db/kingdom/Bacteria/sprot with 6 CPUs
[10:57:53] Running: cat \/home\/remi\.gschwind\/resfinder_FG\/output\/output_prokka\/prokka\.sprot\.tmp\.24\.faa | parallel --gnu --plain -j 6 --block 689284 --recstart '>' --pipe blastp -query - -db /opt/progs/prokka/db/kingdom/Bacteria/sprot -evalue 1e-09 -qcov_hsp_perc 80 -num_threads 1 -num_descriptions 1 -num_alignments 1 -seg no > \/home\/remi\.gschwind\/resfinder_FG\/output\/output_prokka\/prokka\.sprot\.tmp\.24\.blast 2> /dev/null
