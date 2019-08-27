---
layout: default
title: Contemporary Reviews
---
<h2>Contemporary Reviews</h2>
Nineteenth- and early-twentieth century reviews of Hume's work. <strong>WARNING</strong>: here there be <em>spoilers</em>.

<ul>
  {% for post in site.posts %}
    <li>
      <h3><a href="{{ post.url }}">{{ post.title }}</a></h3>
    </li>
  {% endfor %}
</ul>
