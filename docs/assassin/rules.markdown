---
title: Assassin | Rules
layout: assassin
---

## Rules
* * *

### ==GOAL==
Everybody should have received an email from me with the name and picture of their secret target. Likewise, someone else in the game has received your name and picture and targeting you. Your job is to find and kill your target without dying. 

You win the game by being the last player standing.

### ==KILLING==
You kill another player by hitting them with a *clean* balled up sock. I would recommend giving some sort of verbal signal that you killed them such as saying, "You're dead", otherwise they may think some rando is throwing a sock at them. You can only kill another player if they are your target. After you've killed your target take a picture with them and send me a *dm* on groupMe to let me know you've killed them. It's important to dm me to kill so that no one else knows you've killed another player. 

After you kill another player, you take their target. So, if you have Player A, B, and C
A's target is B
B's target is C
A kills B
A's new target is C

Ask the person you just killed for your new target's info, you can also dm me for your new target’s info.

### ==UPDATES==
Every day if there is anything new to report such as deaths or immunities it will be posted at 7-7:30pm-ish. If there is no announcement it means no one has died since the last update. 

Immunities are scenarios where players are immune to death if the meet certain conditions. For e.g., tomorrow's immunity is wearing red, holding a textbook etc. Anytime on that day when a person meets a condition, they are un-killable. 

There will be no immunities until the first kill.

Everyone who filled out the form is playing the game, not everyone in the group chat filled out the form. You can probably figure it out if you try hard enough, but I won't reveal the number of players in the game until there is only 1 player left.

### ==SAFE ZONES==
No kills are allowed in the following areas/times:
Shea House 
Bathrooms
Class (for target and assassin)
Work (for target and assassins)
Anywhere 60 seconds after someone has left one of the above (basically you can't directly camp someone's classroom, a shea house exit etc.)

Every other library, school building, dining hall, etc. is valid place to kill

### ==NEW RULES==
Throughout the game new rules may be added and will be explained then

Anyone who has not filled out the form yet and still wants to play, fill out the form, there may be some ways for you to join later on

### ==NEW RULE LOG/CLARIFICATIONS==
- You may ask anyone for info on your target, but do not do so in a way that exposes who your target is. E.g. do not ask "Do you know anything about X?"
- IM sports are valid places to kill as long as your target is not actively playing
- `New Rule 1` (10/19 Update): Dead people do not talk, so never reveal your target even after you're dead. After you make a kill dm me, and I'll send you an update on who to kill next. *Do not* get this info from your victim
- `New Rule 2` (10/19 Update): If you witness a kill, you have permission to assassinate the killer regardless of if they are your target or not. However, once they return to a safe zone, you can no longer kill them.
- Kills with dirty socks count, but you will be severely penalized
- `New Rule 3` (10/25 Late Update): If you're witness killing in public, your immunity is disabled, meaning anyone trying to kill you via `New Rule 2` can do so regardless of if you have immunity
- `New Rule 4` (10/27 Update): Anybody designated as a celebrity assassin can be killed by anyone (including dead players) and can try to kill anyone in the game. There will be a reward for killing a celebrity assassin. Dead players cannot come back to life but will also be given a reward to torment living players.
- You may not try to kill your assassin if they attempt to kill you, you can only run or have immunity 
- If you kill a player wearing/holding an immunity the kill is invalid, your target knowing who their assassin's identity is penalty enough


## Event Log
* * *

<table>
  {% for row in site.data.assassin.events %}

    {% if forloop.first %}
    <tr>
      {% for pair in row limit:3 %}
        <th>{{ pair[0] }}</th>
      {% endfor %}
    </tr>
    {% endif %}
    
    <tr>
    {% if row["notes"] == "Event" %}
      <td colspan="3"> {{ row["assassin"] }} </td> 
    {% else %}
      {% for pair in row limit:3  %}
        <td>{{ pair[1] }}</td>
      {% endfor %}
    {% endif %}
    </tr>
  {% endfor %}

</table>