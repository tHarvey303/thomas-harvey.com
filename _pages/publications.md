---
layout: archive
title: "Publications"
permalink: /publications/
note: "click a paper for its abstract"
wide: true
---
{% include base_path %}
{% assign pubs = site.data.publications %}
{% assign first = pubs | where: "first_author", true %}
{% assign n_co = pubs.size | minus: first.size %}

<h2 id="first-author">First author <span class="count">{{ first.size }} papers</span></h2>

<div class="cards" style="margin-bottom:50px">
{% for p in first %}{% include pub-card-data.html p=p %}{% endfor %}
</div>

<h2 id="co-author">Co-authored <span class="count">{{ n_co }} papers</span></h2>

<p>This list is rebuilt every week from arXiv and my <a href="{{ site.author.orcid }}">ORCID record</a>. For citations see <a href="{{ site.author.googlescholar }}">Google Scholar</a> or <a href="https://ui.adsabs.harvard.edu/search/q=orcid%3A0000-0002-4130-636X&sort=date%20desc">NASA ADS</a>.</p>

<div class="publist" id="publist">
{% assign year = 0 %}{% assign k = n_co | plus: 1 %}
{% for p in pubs %}{% if p.first_author %}{% continue %}{% endif %}{% assign k = k | minus: 1 %}
  {% if p.year != year %}{% assign year = p.year %}<div class="yr">{{ year }}</div>{% endif %}
  <details class="pub">
    <summary><span class="n">{{ k }}</span><span class="j">{{ p.journal | default: "preprint" }}</span>
      <span><span class="t">{{ p.title | escape }}</span>
      <span class="a">{{ p.authors | replace: "Harvey T.", "<b>Harvey T.</b>" }}</span></span></summary>
    <div class="more">
      <p>{{ p.abstract | escape }}</p>
      <p class="type">Author {{ p.position }} of {{ p.n_authors }} · {% if p.doi %}<a href="{{ p.url }}">Journal</a>{% endif %}{% if p.doi and p.arxiv %} · {% endif %}{% if p.arxiv %}<a href="https://arxiv.org/abs/{{ p.arxiv }}">arXiv:{{ p.arxiv }}</a>{% endif %}</p>
    </div>
  </details>
{% endfor %}
</div>
