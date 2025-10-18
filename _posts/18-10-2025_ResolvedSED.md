---
title: 'Resolving the Internal Structures of z>5 Galaxies'
date: 2025-03-28
permalink: /posts/2025/RESOLVED/
tags:
  - JWST
  - sed
  - fitting
  - scicomm
  - galaxies
  - photometry
---

## Resolving the Internal Structures of z>5 Galaxies

Galaxies are complex, emergent phenomena which arise from a fundamentally simple set of physical laws. We observe a diversity of galaxies in the local Universe, and we can utilize cosmological redshifting to peer back into the early universe to study the ancestors of the local galaxy pantheon.

JWST has allowed us to push this frontier further back, and even the first JWST results showed evidence of ordered structure within galaxies earlier in the Universe (e.g. [Ferreria et al. 2022](https://iopscience.iop.org/article/10.3847/2041-8213/ac947c/meta)). More recent results have found evidence of ordered disky galaxies even at z>7, within the first billion years ([Rownland et al. 2024](https://academic.oup.com/mnras/article/535/3/2068/7811333)), suggesting that the structures we observe in local galaxies formed very quickly. At the same time, gravitational lensing, where massive galaxy clusters act as a cosmic magnifying glass, have enabled us to observe intrinsically faint, low-mass galaxies in unprecedented detail, such as the [Cosmic Gems](https://iopscience.iop.org/article/10.3847/1538-4357/adf638/meta) and the [Firefly Sparkle](https://www.nature.com/articles/s41586-024-08293-0). These observations allow us to resolve structures within these galaxies to the scale of <10 parsecs (about 30 light-years), which lets us resolve individual stellar clusters within these galaxies. 

Observations of nearby and lensed galaxies have shown us that when we fit observations of a galaxy using SED fitting, we can get a different answer depending on whether we fit individual components, or we fit all the light from the galaxy with a single model. One bias with this effect we have observed is called 'outshining', which is a consequence of how the luminosity of a star scales with its stellar mass. As stars emit essentially like black bodies, their luminosity scales with $$L \propto T^4$$, so that stars which are hotter are much brigter. The most massive stars are very hot and so bright that they dominate over all the lower mass stars, which are more numerous, but they also burn through their fuel more quickly and die within a few million years. 

When the galaxy light is dominated by these young, hot stars we can miss the presence of older stellar populations which can make up a signiciant fraction of the total galaxy mass, causing us to underestimate both the total stellar mass and the age of the galaxy. However, if the young and old stars are spatially seperated, we can split the galaxy into multiple components which we fit seperately to recover the true star formation history and stellar mass.

Here is an example of a star formation history showing the integrated and resolved fits, where you can see in the resolved case the SFHs is significantly more extended and older, whereas the integrated fit is dominated by a recent burst of SFH.
<center><img width="538" height="368" alt="Outshining SFH" src="https://github.com/user-attachments/assets/d0ce53da-d69b-4355-a9f9-d36220f871fd" /></center>

In [Harvey et al. 2025](https://arxiv.org/abs/2504.05244), now published in MNRAS, I studied a sample of 220 galaxies at $$z>5$$ using this resolved SED fitting technique. I found that outshining can cause a significant bias in the stellar mass estimates, by over an order of magnitude $$(10\times)$$ in low-mass galaxies with very bursty star formation histories. 

However I found that the overall impact on the distribution of galaxies at low masses was not that significant, with only a slight steepening in the slope of the galaxy stellar mass function (meaning there are slightly more low-mass galaxies than previously thought). Resolved SED fitting, powered by the excellent spatial resolution of JWST's NIRCam instrument, enables much more exciting science which we are only just beginning to explore, so watch this space!

