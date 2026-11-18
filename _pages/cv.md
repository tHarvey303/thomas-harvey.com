---
layout: archive
title: "CV"
permalink: /cv/
redirect_from:
  - /resume
wide: true
---
{% include base_path %}

<div class="prose" markdown="1">

A PDF version is available [here]({{ base_path }}/files/CV_Academic.pdf).

## Research experience

**Max-Planck-Institut für Astronomie, Heidelberg** — Postdoctoral Researcher, *Sept. 2026 –*
: Researching massive galaxy formation at high redshift with Dr. Anna de Graaff, as part of the ERC-funded FIRST-GIANTS project.

**Jodrell Bank Centre for Astrophysics, University of Manchester** — Postdoctoral Researcher, *May – Aug. 2026*; PhD Researcher, *Sept. 2022 – March 2026*
: Within the EPOCHS group, my PhD research focused on locating and characterising high-redshift galaxies in JWST imaging surveys.
: Contributed to more than ten published papers in the EPOCHS series, including the foundational galaxy catalogues and selection criteria, and collaborated internationally as part of the JWST PEARLS GTO team on strong lensing searches, galaxy cluster studies and statistical studies of galaxies and AGN.
: Helped to supervise and mentor undergraduate and Master's students, several of whose projects became student-led publications, and organised the journal club for the high-redshift group.

**Center for Astrophysics, Harvard & Smithsonian** — Visiting Research Fellow, *Sept. 2021 – May 2022*
: Researched AGN feedback with Dr. W. Peter Maksym in Dr. P. Fabbiano's group, using Chandra and Hubble imaging and spectroscopy to study how AGN-driven jets and winds excite X-ray emission from gas in a complex galaxy.

## Education

**PhD, Jodrell Bank Centre for Astrophysics, University of Manchester**, *Sept. 2022 – May 2026*
: Early galaxy evolution with JWST, supervised by Prof. C. Conselice and Dr. N. Adams.

**MPhys Astrophysics with a Year Abroad, University of Southampton**, *Sept. 2018 – July 2022*
: First class degree with an average of 86.2%, a Dean's Award, and selection for a research year at the Center for Astrophysics, Harvard & Smithsonian.

## Publications

{% assign pubs = site.data.publications %}{% assign n_first = pubs | where: "first_author", true | size %}
{{ pubs | size }} publications, including {{ n_first }} as first author. See the [full list]({{ base_path }}/publications/).

## Collaborations

- Euclid Consortium (full member)
- PEARLS / SKYSURF JWST GTO team

## Accepted proposals

</div>

{% include ledger-proposals.html %}

<div class="prose" markdown="1" style="margin-top:2em">

## Talks and conference presentations

</div>

{% assign talks = site.talks | sort: "date" | reverse %}
{% include ledger-talks.html items=talks %}

<div class="prose" markdown="1" style="margin-top:2em">

## Software development

{% for s in site.data.software %}{% if s.home %}- [{{ s.name }}]({{ s.url }}) ({{ s.role }}): {{ s.text }}
{% endif %}{% endfor %}

## Awards

- Dean's List Award for Outstanding Achievement, *2022*
- Selected for the flagship research year at the Harvard-Smithsonian Center for Astrophysics, *2021*
- Elected Fellow of the Royal Astronomical Society (FRAS), *2020*
- Inaugural Whittaker Trust Bursary recipient, *2019–2022*
- University of Southampton: best performance in Physics Part 1, *2019*
- Guernsey Grammar School & Sixth Form: R. Fulford Cup for Physics, *2018*

## Teaching, supervision and outreach

**Graduate Teaching Assistant, University of Manchester**, *2022–2026*
: Lead GTA for the Theory Computing Project module, teaching scientific programming and supporting semester-long group projects.
: Ran the introductory Python support lab for undergraduate physics students.
: Led small-group tutorials on undergraduate astrophysics and mathematics.

**Science communication**, *2018 –*
: Public lectures to astronomical societies and schools. See [outreach]({{ base_path }}/outreach/).
: Editor of the newsletter of La Société Guernesiaise Astronomy Section.

## Community service

- SOC member, "Simulation Based Inference for Galaxy Evolution 2026"
- Referee for Monthly Notices of the Royal Astronomical Society, *2025 –*

## Skills

- **Programming and data analysis:** Python (NumPy, SciPy, pandas, Astropy), Bayesian statistics
- **Machine learning and HPC:** PyTorch, JAX, sbi, LtU-ILI, scikit-learn, Optuna, Slurm
- **Astronomy tools:** Bagpipes, Prospector, eazy-py, pPXF, the JWST pipeline, specutils, photutils, SExtractor
- **Visualisation:** matplotlib, bokeh, panel, holoviews, plotly

</div>
