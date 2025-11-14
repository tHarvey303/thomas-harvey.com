---
title: ""
collection: publications
permalink: /publication/synference
excerpt: ''
date: 2025-11-14
venue: 'Submitted to MNRAS'
paperurl: 'https://arxiv.org/abs/'
---

<h3>Flexible Simulation Based Inference for Galaxy Photometric Fitting with Synthesizer</h3>

<h5>Abstract</h5>

We introduce Synference, a new, flexible Python framework for galaxy SED fitting using simulation-based inference (SBI). Synference leverages the \synthesizer{} package for flexible forward-modelling of galaxy SEDs and integrates the LtU-ILI package to ensure best practices in model training and validation. In this work we demonstrate Synference by training a neural posterior estimator on $10^6$ simulated galaxies, based on a flexible 8-parameter physical model, to infer galaxy properties from 14-band HST and JWST photometry. We validate this model, demonstrating excellent parameter recovery (e.g. R$^2>$0.99 for M$_\star$) and accurate posterior calibration against nested sampling results. We apply our trained model to 3,088 spectroscopically-confirmed galaxies in the JADES GOODS-South field. The amortized inference is exceptionally fast, having nearly fixed cost per posterior evaluation and processing the entire sample in $\sim$3 minutes on a single CPU (18 galaxies/CPU/sec), a $\sim$1700$\times$ speedup over traditional nested sampling or MCMC techniques. We demonstrate Synference's ability to simultaneously infer photometric redshifts and physical parameters, and highlight its utility for rapid Bayesian model comparison by demonstrating systematic stellar mass differences between two commonly used stellar population synthesis models. Synference is a powerful, scalable tool poised to maximise the scientific return of next-generation galaxy surveys.
[Download paper here](https://arxiv.org/abs/)

[Synference is available here](https://github.com/synthesizer-project/synference).
