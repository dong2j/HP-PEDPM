## Reproduction of Figure 8

This code is provided to reproduce **Figure 8** from the manuscript.

## Prerequisites

- **Python Version:** >= Python 3.9.
- **Conda:** Ensure you have [Conda](https://docs.conda.io/en/latest/) installed to manage your environment.

## Installation

1. **STEP 1 Clone the Repository:**

   ```bash
   git clone https://github.com/dong2j/HP-PEDPM.git
   cd HP-PEDPM/2025verFeb11/Figure8

2. **STEP 2 Create the environment using the provided environment.yml file:**

   ```bash
   conda env create --file environment.yml
   conda activate mlpd

## Downloading Data

3. **STEP 3 Download the associated data from ZENODO (https://doi.org/10.5281/zenodo.15117456) and place the DATA folder within the Figure8 folder in the same directory as the Python script.**

## Plotting (ensure you have completed Step 3 first)

4. **STEP 4 Run the python script to plot Figure 8.**

   ```bash
   python fig8_phase_diagrams.py 

## Citation


If you use the phase diagrams, please cite the following manuscript:

Dong, J., Mardaru, G.D., Asimow, P.D., Stixrude, L.P., & Fischer, R.A. (2025). Structure and Melting of Fe, MgO, SiO<sub>2</sub> , and MgSiO<sub>3</sub>  in Planets: Database, Inversion, and Phase Diagram. *The Planetary Science Journal*. 

Publisher's version: https://doi.org/10.3847/PSJ/adc717
arXiv: https://doi.org/10.48550/arXiv.2503.21734

