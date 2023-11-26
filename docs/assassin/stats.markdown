---
title: Assassin | Stats
layout: assassin
---
## Player Stats
<div>
{% for player in site.data.assassin.players %}
  {% if player.Name == "Alexa" %}
    <h3> {{player.Name}} <span style="color:#EAEAEA">| {{player.Pod}} Pod | Ultimate Assassin </span> </h3>
    <p> Kills: {{player.Kills | join: ", "}} </p>
  {% else %}
    <h3> {{player.Name}} <span style="color:#EAEAEA">| {{player.Pod}} Pod | Victim {{player.VictimNumber}}</span></h3>
    <p> Assassin: {{player.Assassin}}</p>
    <p> Date of Death: {{player.DeathDate}}</p>
    <p> Kills: {{player.Kills | join: ", "}} </p>
    <hr style="border-color:#EAEAEA">
  {% endif %}
{% endfor %}
</div>

<br>
* * *
<br>

## Pod Stats
<div>
{% for pod in site.data.assassin.pods %}
  {% if pod.Name == "German" %}
    <h3> {{pod.Name}} <span style="color:#EAEAEA"> </span> </h3>
  {% else %}
    <h3> {{pod.Name}} <span style="color:#EAEAEA">| Date of Extinction: {{pod.Extinction}}</span></h3>
  {% endif %}
  <p> Members: {{pod.Members | join: ", "}}</p>
  <p> Leathality: {{pod.Leathality}}</p>
  <p> K/D: {{pod.KD}} </p>
  {% unless forloop.last %}
    <hr style="border-color:#EAEAEA">
  {% endunless %}
{% endfor %}
</div>