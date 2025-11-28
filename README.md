A collection of verification and validation suites for [MC/DC](https://github.com/CEMeNT-PSAAP/MCDC).

# Verification

- Analytical
  - [Suite A](https://github.com/CEMeNT-PSAAP/MCDC-VV/tree/master/verification/analytical/suite_A): Analytical fixed-source multigroup neutron problems

    Verification includes observing the $`N^{-0.5}`$ convergence in the errors (against analytical solutions) as the number of source particles $`N`$ is increased. The problems include:
    - Steady-state flux distribution of a purely-absorbing multi-layer slab system
    - Reed's classic 1D problem [[reference](https://www.tandfonline.com/doi/abs/10.13182/NSE46-309)]
    - Flux temporal propagation from an isotropic planar surface source
    - Variations of the AZURV1 transient benchmark [[reference](https://www.osti.gov/servlets/purl/975281)]
    - Spectrum temporal evolutions from pulsed homogeneous infinite SHEM361-group thermal systems
    
- [Benchmark](https://github.com/CEMeNT-PSAAP/MCDC-VV/tree/master/verification/benchmark): Code-to-code comparison benchmark problems
  
  Verification includes observing the $`N^{-0.5}`$ convergence in the result relative differences of two codes (MC/DC and [OpenMC](https://github.com/openmc-dev/openmc)) as the number of source particles $`N`$ is increased. The problems include
  - Time-dependent version of the Kobayashi Dog-Leg transport benchmark [[Zenodo link](https://zenodo.org/records/15069882)]
  - Four-phase C5G7 transient benchmark [[Zenodo link](https://zenodo.org/records/15719118)]
