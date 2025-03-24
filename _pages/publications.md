---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

For the most up-to-date list of publiations, inclduing pre-prints, please see my (ADS library)[https://ui.adsabs.harvard.edu/search/filter_database_fq_database=NOT&filter_database_fq_database=(((database%3Aastronomy%20OR%20database%3Aphysics))%20OR%20database%3A%22astronomy%22%20OR%20database%3A%22physics%22)&filter_database_fq_database=database%3A%22earthscience%22&fq=%7B!type%3Daqp%20v%3D%24fq_database%7D&fq_database=((((database%3Aastronomy%20OR%20database%3Aphysics))%20OR%20database%3A%22astronomy%22%20OR%20database%3A%22physics%22)%20NOT%20database%3A%22earthscience%22)&q=-docs(d8d80c3ce55c58e084fe4ed7d7208304)%20%20author%3A%22Harvey%2C%20T.%22%20%20year%3A2023-&sort=date%20desc%2C%20bibcode%20desc&p_=0].

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}

{% for post in site.publications_2ndauthor reversed %}
  {% include archive-single.html %}
{% endfor %}
