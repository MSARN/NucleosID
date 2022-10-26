Nucleos'ID data
===============

The data stored in the ``data`` directory of the Nucleos'ID project
can be used to check that the software is working correctly in your
environment.


Input data
----------

The input dataset is composed of three MGF files, obtained by the
LSMIS laboratory through the analysis of biological samples digested
using RNAase P1 and BAP:

* total_tRNA_extract_B_taurus.mgf

* tRNA_Phe_GAA_S_cerevisiae.mgf

* ribosome_P_aeruginosa_70S.mgf

These analysis have been performed on a Mass spectrometer (Bruker
maXis) coupled to a capillary electrophoresis (CESI 8000).


Output data
-----------

The output dataset is composed of three *csv* files, that contain the
RNA modifications that have been found using the NucleosID software:

* tRNA_Phe_GAA_S_cerevisiae.csv

* total_tRNA_extract_B_taurus.csv

* ribosome_P_aeruginosa_70S.csv

For the first two samples, the following parameters have been used:

* Database: Archaea_Eubacteria_Eukaryota

* MS mass tolreance: 0.02 Da

* MS/MS mass tolerance: 0.5 Da

* MS/MS intensity threshold: 0 AU

* MS/MS score threshold: 20 %

* Exclusion time: 60 s

For the last sample, only the *Eubacteria* database is used and the
MS/MS score threshold parameter is set to *0*.


License
-------

The three MGF files and the three CSV files are made available under the Open Data Commons Attribution
License (ODC-By). You can obtain a copy of the licence at
http://opendatacommons.org/licenses/by/1.0/
