---
layout: archive
title: "Research"
permalink: /research/
note: "click a figure to enlarge it"
---
{% include base_path %}

I study how galaxies formed their stars in the first few billion years of the Universe. For each galaxy I want its star formation history, the stellar populations it contains and its stellar mass. None of these can be observed directly: they are inferred by fitting models to the galaxy's light, and a large part of my research is finding out how far that inference can be trusted. I am a postdoctoral researcher at the Max Planck Institute for Astronomy in Heidelberg, where I work with Anna de Graaff on the ERC-funded FIRST-GIANTS project. Before that I did my PhD with Christopher Conselice and Nathan Adams at the Jodrell Bank Centre for Astrophysics in Manchester.

## How much mass, how early?

Soon after JWST launched, several teams reported galaxies in the early Universe that looked too massive to have formed in the time available. For my first PhD project I built a sample of 1,120 candidate galaxies at redshifts 6.5 to 13.5 from NIRCam imaging of PEARLS and the public surveys, and fitted their spectral energy distributions (SEDs) many times over, changing one modelling assumption at a time: the star formation history, the dust law, the priors, the fitting code.

The choice of star formation history matters most. Swapping a standard parametric history for a flexible one raises the cosmic stellar mass density at z = 10.5 by 0.75 dex, a factor of about five. Even so, we found no conflict between the measured masses and standard cosmological models. The figure below shows the stellar mass density against simulations and earlier measurements. The paper is [EPOCHS IV]({{ base_path }}/publication/epochsiv), published in ApJ.

![Cosmic stellar mass density at redshifts 6.5 to 13.5, compared with simulations]({{ base_path }}/images/papers/smd.png)

## Looking inside early galaxies

A galaxy that has just formed a burst of young stars is dominated by their light. The older stars, which hold most of the mass, are still there but contribute little to the total, so a fit to the whole galaxy can miss them. This is called outshining.

JWST resolves galaxies at these distances into many pixels, so the fit can be done region by region. I wrote [EXPANSE](https://github.com/tHarvey303/EXPANSE) to do this, and applied it to more than 200 galaxies at z ≥ 4.5 in the JADES Origins Field, which has imaging in 19 bands. Low-mass galaxies with bursty star formation come out typically 1.25 to 2.5 times more massive when resolved, and more than ten times in individual cases. The paper is [Behind the spotlight]({{ base_path }}/publication/outshining), published in MNRAS.

![Stellar mass from resolved fits against the integrated fit, for four ways of binning pixels]({{ base_path }}/images/papers/outshining_mass_comparison.png)

I am now building [arachne](https://github.com/tHarvey303/arachne), which replaces the stellar population model with a neural emulator so that a whole multi-band image, including the telescope's point spread function, can be forward-modelled on a GPU.

![arachne fitting a catalogue, separate light components, and maps of mass, dust and age]({{ base_path }}/images/papers/arachne_frontpage.png)

## Inference at survey scale

Fitting one galaxy with nested sampling takes minutes to hours. Euclid and Roman will observe more galaxies than that approach can handle.

[synference](https://synthesizer-project.github.io/synference/) uses simulation-based inference instead. A neural network is trained once on a large set of simulated galaxies made with [Synthesizer](https://synthesizer-project.github.io), and afterwards returns the full posterior for a new galaxy in a fraction of a second. In the release paper we fitted 3,088 spectroscopically confirmed galaxies in about three minutes on one CPU, roughly 1,700 times faster than nested sampling, with posteriors that agree with it. The paper is [published in MNRAS]({{ base_path }}/publication/synference).

![Inference time per galaxy for synference and for conventional SED-fitting codes]({{ base_path }}/images/papers/synference_speed.png)

## The brightest galaxies, with Euclid

JWST observes very deep but over a small area, so the brightest and rarest early galaxies are mostly absent from its surveys. The Euclid Deep Fields cover about 53 square degrees in the near-infrared, roughly a hundred times the area of the largest JWST survey. As a member of the Euclid Consortium I am searching them for luminous galaxies at z > 7, to measure the bright end of the ultraviolet luminosity function.

At Euclid's depth and resolution, a galaxy at z > 7 and a cool brown dwarf in our own Galaxy can have nearly the same colours. Much of the work is separating the two and measuring how complete the search is. I wrote [BD-Finder](https://github.com/tHarvey303/BD-Finder) for the first of those.

## Massive galaxies and black holes

At MPIA I am working on how the most massive galaxies in the early Universe formed, and on what the galaxies we see at later times looked like earlier on. I am also a co-author on work showing that JWST's "little red dots" are young supermassive black holes cocooned in dense ionised gas, [published in Nature]({{ base_path }}/publication/jwst-little-red-dots).

My interest in black holes goes back to my Master's year at the Center for Astrophysics, Harvard & Smithsonian, where I worked with Peter Maksym. NGC 5972 is a nearby galaxy surrounded by a cloud of ionised gas larger than the galaxy itself. The cloud is lit by a quasar at the centre that has since faded: its output has dropped by more than a factor of a hundred in the last 50,000 years. Using Chandra X-ray and Hubble observations, I studied how outflows from the black hole heat that gas. The paper is [published in MNRAS]({{ base_path }}/publication/ngc5972_feedback), and there is a [short introduction to active galaxies]({{ base_path }}/posts/2021/AGN/) on the blog.

![Hubble image of NGC 5972 and its extended emission-line region]({{ base_path }}/images/ngc597_hubble_small.jpg)

## Telescope time

</div>

{% include ledger-proposals.html %}

<div class="prose" markdown="1" style="margin-top:2em">

The full list of papers is on the [publications page]({{ base_path }}/publications/), and the code is on the [software page]({{ base_path }}/software/).
