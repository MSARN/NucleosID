User Documentation
==================

About Nucleos'ID
----------------

Nucleos'ID is a software for untargeted identification of RNA
post-transcriptional modifications from MS/MS acquisitions.

It is a free software released under the `Apache license
<http://www.apache.org/licenses/LICENSE-2.0>`_.

The source code can be obtained from the Github repository:
https://github.com/MSARN/NucleosID

For reporting bugs or requesting new features, please use
the following ticketing system:
https://github.com/MSARN/NucleosID/issues


Interface Description
---------------------

The identification of RNA post-transcriptional modifications can
be tuned with the following parameters:

* Input file: selection of the MGF file that will be analyzed. Only
  files in MGF format are supported, whether their extension is *.mgf*
  or *.txt*.

* Output file: selection of the path and the name of the output file.

* Database: selection of the RNA modification database that will be
  used for the analysis. The following databases can be used:
  Eubacteria, Archaea and Eukarya and all the combination between them.

* MS mass tolerance: mass tolerance applied during the analysis process
  of MS spectra. It corresponds to the maximum difference between the
  m/z of the precursor ion contained in the MGF file and the
  theoretical m/z. This parameter can be given in Dalton (Da) or in
  ppm.

* MS/MS mass tolerance: mass tolerance applied during the analysis
  process of MS/MS spectra. It corresponds to the maximum difference
  between the m/z of the fragment contain in the MS/MS spectrum and 
  and the theorical m/z of the fragemnt defined in the ARN
  modification database.

* MS/MS intensity threshold: absolute value of the intensity below
  which the MS/MS peak is filtered out. This parameter must be
  carefully tuned, and is dependent on the used mass spectrometer.

* MS/MS score threshold: value of the score (in percent) below which
  the MS/MS peak is filtered out.

* Exclusion time: value of the minimum time (in second) between two
  consecutive MS spectra that contain the same modification.


Output File
-----------

The results of the analysis are saved in the *output file*. This file
can be either in *CSV* or *XLSX* format. Both format contain the
same kind of data:

* Modification: the short name of the modification found according
  to the MODOMICS nomenclature.

* Observed MS (Da): the m/z of the precursor ion in Da contained in
  the MGF file.

* Theoretical MS (Da): the m/z of the theoretical precursor ion in Da.

* Observed MS/MS (Da): the m/z of the product ions in Dalton contained
  in the MS spectrum.

* Theoretical MS/MS (Da): the m/z of the theoretical product ions in Da
  calculcated from the MODOMICS database.

* Score (%): the score value as percentage. It is based on the ratio
  between the intensity of the observed MS/MS ion and the most intense
  intensity for the MS/MS spectrum.

* Detection time (s): the time in seconds when the precursor ion was
  detected by the mass spectrometer. It is equivalent to the
  RTINSECONDS parameter in the MS spectra.


Credits
-------

The main contributors, in alphabetical order, to the Nucleos'ID project
are:

* Mévie Didierjean

* Clarisse Gosset-Erard

* Yannis François

* Jérôme Pansanel (maintainer)

Nucleos'ID is Copyright © 2022 CNRS and University of Strasbourg
