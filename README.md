openmm-constph
==============

[![Build Status](https://travis-ci.org/choderalab/openmm-constph.svg?branch=master)](https://travis-ci.org/choderalab/openmm-constph)

Testbed for constant-pH methodologies using OpenMM.

## Manifest ##

`constph/`
```
   constph.py            - Python module implementing constant-pH methodologies in Python
   cnstphgbforces.py     - CustomGBForces that exclude contributions from discharged protons
   examples/explicit-solvent-example.py - explicit solvent NCMC example
   amber-example/        - example system set up with AmberTools constant-pH tools
calibration-implicit/ - terminally-blocked amino acids parameterized for implicit solvent relative free energy calculations
calibration-explicit/ - terminally-blocked amino acids parameterized for explicit solvent relative free energy calculations
```
```
references/           - some relevant literature references
```

## Contributors / coauthors ##

* John D. Chodera <choderaj@mskcc.org>
* Patrick Grinaway <grinawap@mskcc.org>
* Jason Swails <jason.swails@gmail.com>
* Jason Wagoner <jawagoner@gmail.com>
