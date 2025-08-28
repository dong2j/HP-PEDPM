## High Pressure Phase Equilibria Database for Planetary Materials (HP-PEDPM)

### Dataset Description

This data set presents the experimental data available in the literature on Fe, MgO, SiO2, and MgSiO3. While we have tried to include as much literature data as possible, the database may not be complete due to the large number of publications on these materials. This provisional version will be updated regularly as new data or previously overlooked literature becomes available. The latest version of the database is 2025verFeb11. A benchmark code to reproduce the phase diagrams (Figure 8) is now included. Since the associated data is too large for GitHub, it is hosted on Zenodo. Download the DATA folder from https://doi.org/10.5281/zenodo.15117456 and use it alongside the benchmark code.

### Data Structure

The dataset consists of the following columns:
- Pressure (GPa): Pressure conditions under which the phase observations were recorded
- Temperature (K): Corresponding temperature at the given pressure
- Phase: Phase of the material observed at the recorded P-T conditions
- Author: Source
- Method: Technique used

### Phase Diagrams
| MgO | SiO₂ |
|-----|------|
| <img src="Phase Diagrams/MgO.png" alt="MgO" width="300"/> | <img src="Phase Diagrams/SiO2.png" alt="SiO2" width="300"/> |

| Fe | MgSiO₃ |
|----|--------|
| <img src="Phase Diagrams/Fe.png" alt="Fe" width="300"/> | <img src="Phase Diagrams/MgSiO3.png" alt="MgSiO3" width="300"/> |

### Citation

If you use the phase diagrams, please cite the following manuscript:

Dong, J., Mardaru, G.D., Asimow, P.D., Stixrude, L.P., & Fischer, R.A. (2025). Structure and Melting of Fe, MgO, SiO<sub>2</sub> , and MgSiO<sub>3</sub>  in Planets: Database, Inversion, and Phase Diagram. *The Planetary Science Journal*. 

Publisher's version: https://doi.org/10.3847/PSJ/adc717
arXiv: https://doi.org/10.48550/arXiv.2503.21734
