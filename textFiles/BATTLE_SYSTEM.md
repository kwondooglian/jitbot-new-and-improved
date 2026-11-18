# Battle System Mechanics

## Overview

`/battle` starts a turn based fight between your `/team` (up to 4 characters) and the enemy you pick.

- `battle.py` does all of the battle logic (turns, damage, buffs/debuffs, enemy AI, battle log)
- `utils.py` holds the data: stats and every ability written as option letters + numbers
- `main.py` only draws the battle (embed + buttons)

## Turn System

1. **Your team** - each character takes a turn in team order (knocked out or sleeping characters get skipped)
2. **Enemy turn** - every enemy uses all of its moves (Ruffian 2, Grunt 2, Jack Noir 3...) with randomly picked abilities
3. **End of the round** - Burn / Bleed / Regeneration tick, then every buff, debuff and cooldown counts down by 1 turn
4. **Repeat** until every enemy or every character is knocked out

A "turn" in the ability descriptions means one full round. Buffs/debuffs that an enemy gives out during its turn start counting on the next round, so an enemy's "for 4 turns" lasts for the players' next 4 turns.

## The Battle Embed

Updated after every button press:

- **Your Team / Enemies** - HP bar, HP and every buff, debuff and status on each character (`(2t)` = turns left), ▶ shows whose turn it is
- **Battle Log** - every player and enemy move, newest at the bottom

## Buttons

- One button per ability of the current character, greyed out while on cooldown `(2t)`, already used `(used)` or locked (Nihilism)
- Moves that hit one enemy show target buttons first when there is more than one enemy (with a **Back** button)
- **Retreat** ends the battle at any time
- Only the person who started the battle can press the buttons
- The battle ends by itself after 5 minutes without a button press

## Stats

- HP and DEF are combined into EHP at the start of the battle (DEF x1.0 for R, x1.5 for SR, x2.0 for SSR, x1.2 for enemies)
- Damage = the attacker's ATK, changed by attack buffs/debuffs (BB) and the target's defense buffs/debuffs (CC)
- Every attack rolls the attacker's accuracy, then the target's evasion

## Adding / Changing Abilities

Every ability is written in `utils.py` as option letters plus an optional dict of numbers:

```python
"Productivity Time": ['C', 'D', 'H', {"buff": {"BB": 10, "CC": 10}, "turns": 3, "cooldown": 4}]
```

= AOE at teammates (C) + Buff (D) + Cooldown (H): +10% attack and defense for the whole team for 3 turns, then it can't be used for 4 turns.

The full list of options (A-Z), stat codes (AA-EE) and numbers is written above `characterAbilities` in `utils.py`. Enemies use the exact same options in `enemyAbilities`.
