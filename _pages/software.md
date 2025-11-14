---
layout: archive
title: "Software"
permalink: /software/
author_profile: true
---

{% include base_path %}


## Software

I believe code transparency is crucial for reproducibility in science. I endevour to provide code and data used in my research on public repositories. Below I list some astronmomical software packages I have contributed to.

### Synference 

Synference is a Python framework for SED fitting using [Simulation-Based Inference](https://arxiv.org/abs/2508.12939), which is a technique which combines the speed of machine learning with robust Bayesian statistics in order to accelerate inference by $10^3 - 10^5 \times$ compared to traditional Bayesian inference. Synference utilizes Synthesizer (see below) to build complex and realistic forward models of galaxy photometry and spectroscopy, which are used to train SBI models that can then be directly appplied to constrain new observations at scale. 

Synference is on GitHub [here](https://github.com/synthesizer-project/synference/) and the documentation is [here](https://synthesizer-project.github.io/synference/).

### EXPANSE

EXPANSE is a Python package for flexible resolved SED fitting and analysis. Whilst it is still in active development, the code is available on GitHub [here](https://github.com/tHarvey303/EXPANSE) along with some example usecases. Please get in touch if you have any questions.

### BD-Finder

BD-Finder is a Python package for fitting brown dwarf templates to photometry for a variety of synthetic brown dwarf templates. It is available on GitHub [here](https://github.com/tHarvey303/BD-Finder/).

### FITS Table Viewer

FITS Table Viewer is a VS Code extension for viewing tabular FITS (Flexible Image Transport System) files, commonly used in astronomy. It provides an interactive interface (powered by [Tabulator](www.tabulator.info/)) within VS Code to view single and multi-extension tabular FITS files. Data streaming means larger file sizes are supported, and the user can filter and sort by column values. 

### GALFIND

GALFIND is a Python package for automated pipelining of astronomical data processing. It can produce catalogues from raw imaging, measure local noise levels, run SED fitting with multiple different tools, filter catalogues, and estimate distribution functions such as the UV luminosity function or stellar mass function. I helped create GALFIND along with Duncan Austin. The repository is available [here](github.com/duncanaustin98/galfind/) and the documentation is [here](https://galfind.readthedocs.io/en/latest/).


### Synthesizer 

Synthesizer is a package for creating synthetic observables (spectra, photometry, imaging and IFU data cubes) from astronomical simulations and simple parametric models. It is designed to be fast and flexible. 

Check out the release paper submitted to the JOSS [here](https://arxiv.org/abs/2506.15811), the documentation [here](https://synthesizer-project.github.io/synthesizer/) and the repository [here](https://github.com/synthesizer-project/synthesizer). 
