---
title: Assassin
layout: assassin
---

### The Ultimate Assassin was **Alexa!**

The site is now updated with some of the info that you may or may not have figured out while the game was going on. There's also some stuff under the _Stats_ and _Extras_ tabs as well. Let me know if there are any inaccuracies and feel free to ask questions in the chat.

## Event Log
* * *
For the _NewTarget_  entries with an arrow, e.g. Danner -> Abigail, means the asssassin killed someone that wasn't their target causing someone else's target to be updated.

<table>
  {% for row in site.data.assassin.eventlog %}
    {% if forloop.first %}
    <tr>
      {% for pair in row %}
        <th>{{ pair[0] }}</th>
      {% endfor %}
    </tr>
    {% endif %}
    
    <tr>
    {% if row["notes"] == "Event" %}
      <td colspan="6"> {{ row["assassin"] }} </td> 
    {% else %}
      {% for pair in row %}
        <td>{{ pair[1] }}</td>
      {% endfor %}
    {% endif %}
    </tr>
  {% endfor %}

</table>