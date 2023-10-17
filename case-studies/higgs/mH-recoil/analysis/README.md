## Run baseline analysis for mass and cross-section

This repository contains the analysis files for the Higgs mass and model-independent cross-section at a center-of-mass of 240 GeV, in the muon and electron final states.

Both mass and cross-section analysis share the same baseline selection, except two differences:

- The mass analysis has an additional cos(theta) miss cut
- The cross-section analysis deploys a BDT on top of the baseline selection to further reduce the backgrounds



To run the analysis, first clone/load the main FCCAnalyses framework (see https://github.com/HEP-FCC/FCCAnalyses), then clone this repo and run:

```
mkdir output_ee output_mumu
fccanalysis run analysis.py
fccanalysis plots plots.py
```
The first command generates all the histograms for the processes using the Histmaker option (i.e. the histograms are directly produced without an intermediate tree stage). This mode of running is suitable for a multicore machine (it takes 40 mins to run the entire muon analysis on a 64 thread machine).


### Higgs mass analysis

The Higgs mass is obtained by fitting the Recoil distribution with a 2-side double Crystal Ball + Gausss PDF. More info woll be added later.

### Higgs model-independent cross-section

More infor later



