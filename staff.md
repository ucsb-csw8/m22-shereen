---
layout: page
title: Who We Are
nav_order: 6
description: A listing of all the course members.
---

# Mentors

We - the Teaching Assistants (TAs) and Shereen - are what we will collectively refer to as "Mentors". We look forward to helping you learn and succeed in this class and beyond.
<!--Staff information is stored in the `_staffers` directory and rendered according to the layout file, `_layouts/staffer.html`.-->

## Instructors

{% assign instructors = site.staffers | where: 'role', 'Instructor' %}
{% for staffer in instructors %}
{{ staffer }}
{% endfor %}

{% assign teaching_assistants = site.staffers | where: 'role', 'Teaching Assistant' %}
{% assign num_teaching_assistants = teaching_assistants | size %}
{% if num_teaching_assistants != 0 %}
## Teaching Assistants
{% for staffer in teaching_assistants %}
{{ staffer }}
{% endfor %}
{% endif %}

{% assign learning_assistants = site.staffers | where: 'role', 'Undergraduate Learning Assistant' %}
{% assign num_learning_assistants = learning_assistants | size %}
{% if num_learning_assistants != 0 %}
## Undergraduate Learning Assistants
{% for staffer in learning_assistants %}
{{ staffer }}
{% endfor %}
{% endif %}
