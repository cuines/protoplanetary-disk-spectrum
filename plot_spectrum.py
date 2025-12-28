#!/usr/bin/env python
"""
Plot a synthetic mid-infrared spectrum with an annotated water vapor line.

This script generates a simple model spectrum of a protoplanetary disk
in the 10–30 µm range, highlighting the rotational line of water vapor
at 17.22 µm. The line is marked with a vertical red line and a label,
demonstrating how spectral signatures of molecules can be identified
in infrared observations.

Dependencies: numpy, matplotlib, pyspeckit (and its dependencies:
astropy, scipy, lmfit).
"""

import numpy as np
import matplotlib.pyplot as plt
import pyspeckit
from pyspeckit.spectrum.units import SpectroscopicAxis

def main():
    # --------------------------------------------------------------------
    # 1. Create a wavelength axis (mid-infrared range)
    # --------------------------------------------------------------------
    wave_min = 10.0   # µm
    wave_max = 30.0   # µm
    n_points = 500
    wavelength = np.linspace(wave_min, wave_max, n_points)  # µm

    # --------------------------------------------------------------------
    # 2. Build a synthetic spectrum: continuum + a Gaussian emission line
    # --------------------------------------------------------------------
    # Simple linear continuum (normalized to ~1)
    continuum = 1.0 + 0.02 * (wavelength - 20.0)

    # Gaussian line parameters (water vapor line at 17.22 µm)
    line_center = 17.22          # µm
    line_width  = 0.15           # µm (FWHM ~ 0.35 µm)
    line_ampl   = 0.3            # strength relative to continuum

    line_profile = line_ampl * np.exp(-(wavelength - line_center)**2
                                      / (2.0 * line_width**2))

    # Add some random noise (typical for a Spitzer‑IRS spectrum)
    rng = np.random.default_rng(seed=12345)
    noise = 0.02 * rng.standard_normal(n_points)

    flux = continuum + line_profile + noise

    # --------------------------------------------------------------------
    # 3. Create a pyspeckit Spectrum object
    # --------------------------------------------------------------------
    # pyspeckit expects the spectral axis as a SpectroscopicAxis.
    # We give it units of 'micron' (µm).
    xaxis = SpectroscopicAxis(wavelength, unit='micron')
    sp = pyspeckit.Spectrum(data=flux, xarr=xaxis,
                            xarrkwargs={'unit': 'micron'},
                            unit='erg s⁻¹ cm⁻² µm⁻¹')

    # --------------------------------------------------------------------
    # 4. Plot the spectrum using pyspeckit's built‑in plotter
    # --------------------------------------------------------------------
    fig = plt.figure(figsize=(10, 6))
    sp.plotter(figure=fig, color='k', linewidth=1.5, label='Synthetic spectrum')
    sp.plotter.axis.set_xlabel('Wavelength [µm]', fontsize=14)
    sp.plotter.axis.set_ylabel('Normalized Flux', fontsize=14)
    sp.plotter.axis.set_title('Mid‑infrared spectrum of a protoplanetary disk',
                              fontsize=16, pad=15)

    # --------------------------------------------------------------------
    # 5. Mark the water‑vapor line
    # --------------------------------------------------------------------
    # Vertical line at 17.22 µm
    sp.plotter.axis.axvline(line_center, color='red', linestyle='--',
                            linewidth=2, alpha=0.8,
                            label='H₂O rotational line (17.22 µm)')

    # Annotation
    sp.plotter.axis.annotate('H₂O 17.22 µm',
                             xy=(line_center, sp.data.max() * 0.9),
                             xytext=(line_center + 1.0, sp.data.max() * 0.95),
                             arrowprops=dict(arrowstyle='->', color='red',
                                             lw=1.5),
                             fontsize=13, color='red', ha='center')

    sp.plotter.axis.legend(loc='upper right', fontsize=12)
    sp.plotter.axis.grid(True, alpha=0.3)

    # --------------------------------------------------------------------
    # 6. Save the figure
    # --------------------------------------------------------------------
    plt.tight_layout()
    plt.savefig('water_line_spectrum.png', dpi=150)
    print('Figure saved as water_line_spectrum.png')

    # Uncomment the next line if you want to display the plot interactively
    # plt.show()

if __name__ == '__main__':
    main()