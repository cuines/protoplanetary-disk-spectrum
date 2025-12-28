# Protoplanetary Disk Spectrum Analysis: Water Vapor Infrared Line

This repository contains a Python script that demonstrates the analysis of infrared spectral signatures in protoplanetary disks, with a focus on the water vapor (H₂O) rotational line at **17.22 µm**. The project illustrates how macroscopic observations of disk gaps can be linked to microscopic molecular properties, bridging the fields of stellar system evolution and molecular structure.

## Context

Protoplanetary disks are the birthplaces of planets. Their chemical composition, traced by infrared spectroscopy, provides crucial clues about the physical conditions (temperature, UV radiation, density) and the processes that shape planet formation. The Spitzer Space Telescope’s Infrared Spectrometer (IRS) has been instrumental in detecting numerous molecular lines in the mid‑infrared (5–40 µm), among which water vapor is a key tracer of the warm, inner disk regions.

## Molecule: Water (H₂O)

### Astrophysical Significance

Water vapor is one of the most abundant molecules in protoplanetary disks and a primary carrier of oxygen. Its detection in the mid‑infrared (especially the rotational line complexes near 15.17 µm and 17.22 µm) probes gas at temperatures of a few hundred to a few thousand Kelvin, typically located within a few astronomical units of the central star.

In disk **gaps** – regions where dust and gas have been partially cleared by forming planets – the presence (or absence) of water vapor carries important information:

- **Temperature diagnostic**: The excitation of H₂O lines depends strongly on the local kinetic temperature. A detected line indicates that the gas in the gap is still warm enough to excite rotational transitions.
- **UV‑shielding**: Water molecules can be dissociated by far‑ultraviolet (FUV) photons. In a gap, dust clearing reduces the shielding, potentially leading to lower water abundances. The detection of water vapor in some gaps (e.g., the pre‑transitional disk DoAr 44) suggests that other shielding mechanisms (dust‑self‑shielding or gas migration) are at work.
- **Chemical evolution**: Water is a product of gas‑phase reactions and ice‑mantle sublimation. Its abundance relative to other molecules (CO, OH, CO₂) constrains the chemical history and the degree of thermal processing in the disk.

Thus, observing the 17.22 µm water line in a disk gap helps astronomers distinguish between different gap‑formation scenarios and understand the survival of molecules in planet‑forming environments.

### Molecular Structure

Water (H₂O) is a simple triatomic molecule composed of **two hydrogen atoms** and **one oxygen atom**. Its geometry is **bent**, with a bond angle of approximately **104.5°** (in the gas phase). The O–H bonds are polar covalent, and the molecule possesses a permanent electric dipole moment (~1.85 D). This dipole moment allows water to emit and absorb rotational line radiation in the infrared and microwave regimes.

The rotational energy levels of H₂O are described by quantum numbers *J*, *Kₐ*, *Kᶜ*. The line at 17.22 µm corresponds to a blend of several rotational transitions with upper‑level energies around 2300–3000 K, originating from the ground vibrational state. The detailed rotational structure is sensitive to the molecular geometry and the masses of the constituent atoms, linking the macroscopic spectral feature directly to the quantum‑mechanical properties of the molecule.

## Running the Script

### Dependencies

The script requires Python 3.7 or later and the following packages:

- `numpy`
- `matplotlib`
- `pyspeckit` (which itself depends on `astropy`, `scipy`, and `lmfit`)

You can install the dependencies via pip:

```bash
pip install numpy matplotlib pyspeckit
```

### Usage

1. Clone this repository:
   ```bash
   git clone https://github.com/cuines/protoplanetary-disk-spectrum.git
   cd protoplanetary-disk-spectrum
   ```

2. Run the script:
   ```bash
   python plot_spectrum.py
   ```

The script `plot_spectrum.py` performs the following steps:

- Generates a synthetic mid‑infrared spectrum covering 10–30 µm.
- Adds a Gaussian emission feature near 17.22 µm to simulate the water‑vapor line.
- Plots the spectrum with labeled axes (Wavelength [µm] vs. Normalized Flux).
- Draws a vertical red line at 17.22 µm and annotates it as the H₂O rotational line.

The resulting figure is saved as `water_line_spectrum.png` in the current directory.

### Example Output

![Example spectrum with annotated water line](water_line_spectrum.png)

*Figure: Simulated mid‑infrared spectrum of a protoplanetary disk. The red vertical line marks the 17.22 µm rotational line of water vapor, a key diagnostic for warm gas in disk gaps.*

## References

- Pontoppidan, K. M., Salyk, C., Blake, G. A., et al. 2010, ApJ, 720, 887 (*A Spitzer Survey of Mid‑infrared Molecular Emission from Protoplanetary Disks*). [arXiv:1006.4189](https://arxiv.org/abs/1006.4189)
- Salyk, C., Pontoppidan, K. M., Blake, G. A., et al. 2015, ApJL, 810, L24 (*Water Vapor in the Inner Region of a Pre‑transitional Disk*)
- Du, F., & Bergin, E. A. 2014, ApJ, 792, 2 (*Water Vapor Distribution in Protoplanetary Disks*)

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.