# This file will store any big things to share between Main or Battle that isn't logic but just data

'''
Technically every character that exists HERE must actually exist below
abraizeChar = ["r_abraize", "r_abraize2", "sr_abraize", "ssr_abraize"]
treyChar = ["r_trey", "ssr_trey"]
noahChar = ["r_noah", "sr_noah"]
freemanChar = ["r_freeman", "r_freeman2", "sr_freeman"]
stephenChar = ["r_stephen", "sr_stephen"]
jaydenChar = ["ssr_jayden", "r_jaiden"]
homestuckChar = ["r_homestuck", "sr_homestuck"]
scottieChar = ["ssr_scottie"]
maxChar = ["r_max", "sssr_max"]
binktopChar = ["sr_binktop"]
caseyChar = ["ssr_casey"]
stevenChar = ["ssr_steven"]
'''

# Characters that exists here are every character in the game but in each section
rChar = ["r_abraize", "r_abraize2", "r_trey", "r_noah", "r_freeman", "r_stephen", "r_homestuck", "r_max", "r_jaiden", "r_freeman2"]
srChar = ["sr_freeman", "sr_stephen", "sr_homestuck", "sr_abraize", "sr_trey", "sr_noah", "sr_binktop"]
ssrChar = ["ssr_abraize", "ssr_trey", "ssr_jayden"]
specialChar = ["ssr_scottie", "ssr_casey", "ssr_steven"]
secretChar = ["sssr_max"]

# Character Titles for displaying to user
characterTitles = {
    "r_abraize": "[Rolling in Success] Abraize Masood",
    "r_abraize2": "[Productivity Time] Abraize Masood",
    "sr_abraize": "[Time on my Side] Abraize Masood",
    "ssr_abraize": "[Rewind] Abraize Masood",
    "r_trey": "[Irish Golden Standard] Treyvaughn Lewis",
    "sr_trey": "[Heavy Sleeper] Treyvaughn Lewis",
    "ssr_trey": "[Seeker of Silence] Treyvaughn Lewis",
    "r_noah": "[pillagingPirate] Noah Cave",
    "sr_noah": "[S'all Good, Man] Noah Cave",
    "r_freeman": "[Who I am to Me] Freeman",
    "sr_freeman": "[Freedom in Jeopardy] Freeman",
    "r_stephen": "[You Marlowe?] Stephen Goraynov",
    "sr_stephen": "[Master of Intervention] Stephen Goraynov",
    "ssr_jayden": "[Sworn Protectorate of Creation] Jayden Ceballos",
    "sr_homestuck": "[Thief in God's Clothing] Homestuck",
    "r_homestuck": "[Tour of a Lifetime] Homestuck",
    "r_max": "[I can make a-] Max Yakuvobich",
    "r_jaiden": "[Picked up, Packed up] Jaiden Ceballos",
    "r_freeman2": "[On the Run] Freeman",
    "ssr_scottie": "[Overwhelming Dread] Scottie Jenkins",
    "sr_binktop": "[Saviour of the Digital Realm] Binktop",
    "ssr_casey": "[Even if I don't have to, I will] Casey Cranberry",
    "ssr_steven": "[Reopen Old Wounds] Steven Toony",
    "sssr_max": "[???] ???"
}

backgrounds = {
    "purple1": "./graphics/battle/purple1.png",
    "purple2": "./graphics/battle/purple2.png",
    "garrysmod": "./graphics/battle/garrysmodbackground.png",
    "dersiteroyalty": "./graphics/battle/dersiteroyaltybackground.png",
    "barrier": "./graphics/battle/barrier.png"
}
# /battle uses purple2, unless the enemy has its own background here
DEFAULT_BACKGROUND = "purple2"
enemyBackgrounds = {
    "Garry's Mod": "garrysmod",
    "Teniente": "dersiteroyalty",
    "Conquistador": "dersiteroyalty",
    "John": "barrier",
    "Rose": "barrier",
    "Dave": "barrier",
    "Jade": "barrier",
    "Heroes of Legend": "barrier",
}

characterImages ={
    "r_abraize": "./graphics/battle/r_abraize.png",
    "r_abraize2": "./graphics/battle/r_abraize2.png",
    "sr_abraize": "./graphics/battle/sr_abraize.png",
    "ssr_abraize": "./graphics/battle/ssr_abraize.png",
    "r_trey": "./graphics/battle/r_trey.png",
    "sr_trey": "./graphics/battle/sr_trey.png",
    "ssr_trey": "./graphics/battle/ssr_trey.png",
    "r_noah": "./graphics/battle/r_noah.png",
    "sr_noah": "./graphics/battle/sr_noah.png",   # cut out of r_noah2.png (that file has 4 characters in it)
    "r_freeman": "./graphics/battle/r_freeman.png",
    "sr_freeman": "./graphics/battle/sr_freeman.png",
    "ssr_jayden": "./graphics/battle/ssr_jayden.png",
    "r_stephen": "./graphics/battle/r_stephen.png",
    "sr_stephen": "./graphics/battle/sr_stephen.png",
    "sr_homestuck": "./graphics/battle/sr_homestuck.png",
    "ssr_scottie": "./graphics/battle/ssr_scottie.png",
    "r_homestuck": "./graphics/battle/r_homestuck.png",
    "r_max": "./graphics/battle/r_max.png",
    "r_jaiden": "./graphics/battle/r_jaiden.png",
    "r_freeman2": "./graphics/battle/r_freeman2.png",
    "sr_binktop": "./graphics/battle/sr_binktop.png",
    "ssr_casey": "./graphics/battle/ssr_casey.png",
    "ssr_steven": "./graphics/battle/ssr_steven.png"
}
enemyImages = {
    "RuffianBack": "./graphics/battle/ruffianBack.png",   # file names match the capital letters of the real files
    "RuffianFront": "./graphics/battle/ruffianFront.png", # (Windows doesn't care, but Linux / Mac servers can't find them otherwise)
    "Grunt": "./graphics/battle/grunt.png",
    "Spearman": "./graphics/battle/spearman.png",
    "Agent": "./graphics/battle/agent.png",
    "Jack Noir": "./graphics/battle/jackNoir.png",
    "Garry's Mod": "./graphics/battle/gmod.png",
    "Addonshield": "./graphics/battle/addonshield.png",
    "Teniente": "./graphics/battle/teniente.png",
    "Conquistador": "./graphics/battle/conquistador.png",
    "Draconian Dignitary": "./graphics/battle/draconianDignitary.png",
    "Courtyard Droll": "./graphics/battle/droll.png",
    "Hegemonic Brute": "./graphics/battle/hegemonic.png",
    "John": "./graphics/battle/john.png",
    "Rose": "./graphics/battle/rose.png",
    "Dave": "./graphics/battle/dave.png",
    "Jade": "./graphics/battle/jade.png"
}

# Character Banner GIFs
bannerGifs = {
    "r_abraize_gif": "https://media.discordapp.net/attachments/1426812344549380136/1442262933018251467/R_ABRAIZE.gif?ex=692a1187&is=6928c007&hm=ea36ca7f4742ec74ad4786385624dbbbf1c69ba9c809bf2499c5b23b85f39b38&=&width=813&height=524",
}

otherImages = {
    "recycle_gif": "https://media.discordapp.net/attachments/796742546910871562/1455728132240703593/recycled_B.gif?ex=69873838&is=6985e6b8&hm=6b929831bdc757d1cdd10794bbb60f8c7d946ab84f13f5e5f58d011f93e7f99b&=&width=813&height=524",
    "no_own_png": "./graphics/broke.png"
}

NO_OWN_PNG = "./graphics/broke.png"

R_ABRAIZE2_GIF = "https://media.discordapp.net/attachments/796742546910871562/1444044329583640748/R_ABRAIZE_PROD.gif?ex=692b4695&is=6929f515&hm=1ecc69064ddd0b38a7b3e9be1d13e2541c99e9e7c0948619b3d486e3ac440f06&=&width=678&height=438"
SR_ABRAIZE_GIF = "https://media.discordapp.net/attachments/907662210619289600/1441575065413091500/SR_ABRAIZ.gif?ex=69414626&is=693ff4a6&hm=c51aa1cf7872069ee96e7365b27d288de2e9cb3d9780375137cebaf6d7196d89&=&width=813&height=524"
SSR_ABRAIZE_GIF = "https://media.discordapp.net/attachments/796742546910871562/1453592615822950450/SSR_ABRAIZE.gif?ex=6955435e&is=6953f1de&hm=ef8fb3a6bcb7f6fccec9f36850b8b8d3954a9bfc118843171d03fdf9af369e68&=&width=678&height=438"
R_TREY_GIF = "https://media.discordapp.net/attachments/1426812344549380136/1442262950055251978/R_TREY.gif?ex=692aba4b&is=692968cb&hm=6467f2663cac2d80ffd3f61f9de3436133557568e4b00cec63ee4cbdb1d6da40&=&width=813&height=524"
SR_TREY_GIF = "https://media.discordapp.net/attachments/907662210619289600/1442648569579307180/SR_TREY.gif?ex=6941396e&is=693fe7ee&hm=d12a52705f4952d3860d273dcce43f3598f971d5d581209f61fd46108823194d&=&width=813&height=524"
SSR_TREY_GIF = "https://media.discordapp.net/attachments/1426812344549380136/1438298186409185393/SSR_TREY.gif?ex=692ace51&is=69297cd1&hm=705ffe6482d8c46a88742a82e6565c28ff53cbba9ea15eebe990dfacde708469&=&width=813&height=524"
R_NOAH_GIF = "https://media.discordapp.net/attachments/1426812344549380136/1438298195829719193/R_NOAH.gif?ex=692ace54&is=69297cd4&hm=a4ab137787708b382bd26b0659a39b768dece0b7d0eb03898b4fe4b180428133&=&width=601&height=438"
R_NOAH2_GIF = "https://cdn.discordapp.com/attachments/907662210619289600/1572809217637621830/SR_NOAH_3.gif?ex=6affb83a&is=6afe66ba&hm=cd228f4e33d18f6ec0f959a5bb3a79fc35dcbe6c22fddb36663aed0f72f05298&"
R_FREEMAN_GIF = "https://media.discordapp.net/attachments/1426812344549380136/1442262942660952268/R_FREEMAN.gif?ex=692aba49&is=692968c9&hm=3f1edc05a01b0c793ab7ddfe3519054630c1523e68b5c29ec5d4be6624d0e1c0&=&width=813&height=524"
SR_FREEMAN_GIF = "https://media.discordapp.net/attachments/1426812344549380136/1438298206193586187/SR_FREEMAN.gif?ex=692ace56&is=69297cd6&hm=6e42e1d45a353ffc60916f54593933273fea88e2d69d400c91f8c6899172174e&=&width=678&height=438"
R_STEPHEN_GIF = "https://media.discordapp.net/attachments/1426812344549380136/1443821437378105444/R_STEPHEN.gif?ex=692b1fbf&is=6929ce3f&hm=97986106339c3febd0bb243c25c13f870c331eb2376c2b3bcefc053fac64e26b&=&width=813&height=524"
SR_STEPHEN_GIF = "https://media.discordapp.net/attachments/1426812344549380136/1443821457846046741/SR_STEPHEN.gif?ex=692b1fc4&is=6929ce44&hm=fbccf7579c4c5189be6d18689bc65a7e62b064bdd075647ddc64428721d53b3e&=&width=813&height=524"
SSR_JAYDEN_GIF = "https://media.discordapp.net/attachments/1426812344549380136/1441662516672331836/SSR_JAYDEN.gif?ex=692a8558&is=692933d8&hm=c5f5376d3603ce635598548977465872e7a3662802986c6f742c1f590eadd7a4&=&width=813&height=524"
SR_HOMESTUCK_GIF = "https://media.discordapp.net/attachments/907662210619289600/1441689825911505026/SR_HOMESTUCK.gif?ex=6941b107&is=69405f87&hm=181544c05734a721ea53bbe630dcb4b25ed7b95327661a807b97bdba81cc7506&=&width=813&height=524"
SSR_SCOTTIE_GIF = "https://media.discordapp.net/attachments/1426812344549380136/1441591428042985492/SSR_SCOTTIE.gif?ex=69551be3&is=6953ca63&hm=9a1141a0f327f2f16ed80b996243679e62491b0fa2b985babdc1bc09d82cccaa&=&width=813&height=524"
SSSR_MAX_GIF = "https://media.discordapp.net/attachments/1442548563879133357/1460374051834040505/000.png?ex=6966aed2&is=69655d52&hm=2daa8e27abbb1eae7996c33f6b705308567264b3bbaa4bfaa9c889ca95c4e244&=&format=webp&quality=lossless&width=1240&height=698"
R_HOMESTUCK_GIF = "https://media.discordapp.net/attachments/907662210619289600/1572833434982817802/R_HOMESTUCK.gif?ex=6affcec8&is=6afe7d48&hm=ca625cfb04880771fd058c6b5d9ff076c2781b5c117970f0a9152d4ade002888"
R_MAX_GIF = "https://media.discordapp.net/attachments/907662210619289600/1572833434357727273/R_MAX2.gif?ex=6affcec8&is=6afe7d48&hm=e52418210d467478e525be4e53f2c69e93381a93178ec72f27427d9ffb7f2005"
R_JAIDEN_GIF = "https://media.discordapp.net/attachments/907662210619289600/1572833434643202190/R_JAIDEN.gif?ex=6affcec8&is=6afe7d48&hm=2734c1b5863d9073f6402b039175ba1e8a9f77356c484ef07962dffd7b6f7933"
R_FREEMAN2_GIF = "https://cdn.discordapp.com/attachments/907662210619289600/1573984017836150864/R_FREEMAN2.gif?ex=6b03fe59&is=6b02acd9&hm=bcd9fe7a84ee5e7f70eb12a3522b77619be63699e0ce18d87219f6d52b28d46e&"
SSR_CASEY_GIF = "https://media.discordapp.net/attachments/907662210619289600/1468808958016880904/SSR_CASEY_AGAIN.gif?ex=6b05abb0&is=6b045a30&hm=8c9e5aa0f30b25727c0ae6efbc1b75d269288981deb83b16f77c64a7ae9a3f0e"  # put the link to the gif here
SSR_STEVEN_GIF = "https://media.discordapp.net/attachments/1426812344549380136/1456530363277906000/SSR_STEVEN.gif?ex=6b05d35b&is=6b0481db&hm=10597e416aba519858b7bb20ff686cd77a5b4cc7b22dffc6c5d4a0d438762f8f"  # put the link to the gif here
SR_BINKTOP_GIF = "https://cdn.discordapp.com/attachments/907662210619289600/1573813352096989287/SR_BINKTOP.gif?ex=6b035f67&is=6b020de7&hm=4a67c5ce7dd236e655fecd00395fac6965e21b6c082a1a8f7a71d4029e412791&"



enemySpots = {
    "Grunt": (0, 0),
    "RuffianBack": (-25, 130),
    "RuffianFront": (0, 260),
    "RuffianSolo": (0, 150),
    "Spearman": (15, 145),
    "Agent": (20, 150),
    "Jack Noir": (0, 150),
    "Garry's Mod": (0, 37),
    "Teniente": (0, 59),       # his picture is 360 tall, this puts his feet on the bottom like the others
    "Conquistador": (0, 0),
    "Draconian Dignitary": (0, 86),
    "Courtyard Droll": (25, 270),
    "Hegemonic Brute": (0, 0),  # his picture is as big as the whole battle screen
    "John": (0, 221),
    "Rose": (0, 212),
    "Dave": (20, 115),
    "Jade": (30, 125)
}

# Enemies that get summoned during a battle (Garry's Mod's Addonshields) are drawn onto the battle screen when they show up:
# the 1st one goes in the 1st spot, the 2nd in the 2nd... (more than there are spots start again from the 1st)
# "scale" shrinks the picture (0.6 = 60% of its size)
summonSpots = {
    "Addonshield": {"scale": 0.6, "spots": [(150, 232), (30, 236), (190, 160), (75, 150)]},
}

# Enemies that summon more enemies during the battle: every "everyDamage" damage they take, 1 "summon" shows up
# (the summon needs its own enemyAttributes and enemyAbilities line, and it vanishes if the enemy that summoned it is defeated)
enemySummons = {
    "Garry's Mod": {"summon": "Addonshield", "everyDamage": 161},
}

# Enemy Attributes and Character Attributes (5 basic stats, how many moves they get, plus abilities name)
# HP, Attack, Defense, Moves, Evasion, Accuracy, Abilities
enemyAttributes = {
    "Ruffian1": [125, 5, 5, 2, 0, 80, "Punch"],
    "Ruffian2": [125, 5, 5, 2, 0, 80, "Punch"],
    "Grunt": [400, 25, 45, 2, 0, 65, "Punch", "Slam, Deal 15 Damage to all party members"],
    "Spearman": [175, 5, 5, 2, 0, 80, "Punch", "Swipe, Deal 20 damage to all party members", "Stab, Apply 15%% attack damage bonus to self for this turn and deal damage"],
    "Agent": [175, 15, 5, 2, 0, 80, "Punch", "Sneak, Add 15%% evasion to self for next 4 turns, then use Punch"],
    "Jack Noir": [1000, 30, 10, 3, 5, 90, "Stab", "Shiv, Deal damage and apply bleed to player (-3% hp per turn) for one turn, this can stack", "Slash, Deal only 5 damage to all party members, but apply bleed to all party members for one turn.", "Extra Passive: Attack lowest health party member each turn"],
    "Garry's Mod": [650, 70, 65, 2, 0, 85, "Hit, Deal 50% of atk to a targeted enemy", "Addon-Smash!, Rear up for 1 turn then come crashing down on all enemies for full atk", "Passive: Every 161 damage taken, summon an Addonshield in front of himself"],
    "Addonshield": [100, 0, 15, 1, 0, 0, "Draw Attack, The player team's attacks on Garry's Mod hit the Addonshield instead"],
    "Teniente": [450, 40, 20, 2, 2, 95, "Thrust, Basic attack", "Code of Honour, +15% atk and def for himself and 1 party member, then he Thrusts at them (he only attacks them this turn)", "Riposte, Until the end of his next turn every hit on him costs the attacker 30 + 10% of their max hp, ends his turn"],
    "Conquistador": [600, 60, 60, 2, 0, 85, "Slash, Attack all party members with 25% less power", "Stab, Attack 1 party member", "Battle Cry, -35% def for every party member for 1 turn, his next move is a Stab or a Slash", "Passive: Loot & Pillage, Every party member that goes down while he is standing steals 10 Grist, beating him gets it all back"],
    "Draconian Dignitary": [1000, 35, 40, 3, 4, 95, "Cue Whack, Deal 50% more damage and stun the party member who was hit for 1 turn", "Careful Planning, Always goes first, his next move is guaranteed to hit and deals 75% more damage", "Cue Swipe, Attack all party members"],
    "Courtyard Droll": [550, 30, 15, 3, 35, 80, "Bull Penis Cane, 3 swipes at 1 party member: the 1st always hits, the 2nd has a 75% chance and the 3rd 50%", "Scamper, -20% acc for every party member for 2 turns", "Passive: Hidden C4, Once he drops below half HP it blows up: everyone on the battlefield takes 25% of their max HP, including himself"],
    "Hegemonic Brute": [1750, 55, 70, 2, 0, 75, "Smash, Rear up for 1 turn then smash all party members for full atk", "Unforeseen Bite, Bite 1 party member for 40 damage + 10% of their max HP and apply 2 stacks of bleed (-3% hp each, not if they already have 2)", "Trusty Axe, Attack all party members for 50% of atk"],
    "John": [425, 40, 35, 2, 75, 50, "Scarf Swipe, Basic attack", "Pop-O-Matic Vrillyhoo Hammer, 50 damage to 1 party member + 1 of 8 random effects: nothing / 2 stacks of bleed / -15% atk / -15% def / -15% eva / -15% acc / stun / heal himself for the damage done", "Windy Thing, Every 4 turns: 15% of max HP damage and -30% acc for 3 turns to all party members"],
    "Rose": [375, 25, 35, 2, 10, 100, "Needlewand, Ranged basic attack", "Quill of Echidna, Ranged attack for 40 true damage, ignores the HP that comes from def", "Lessons in Showmanship, When 1 of her allies or herself has more than 4 different debuffs: clears all debuffs on all of them", "Passive: Premonition, Every 6 turns the party can't choose their moves, everyone uses their basic attack", "Passive: Foresight, Her attacks always land and she can't get acc debuffs", "Passive: When she is defeated, all party members get -100% acc for 1 turn"],
    "Dave": [700, 70, 50, 2, 5, 90, "1/2Sword Swipe, Attack all party members and apply 1 stack of freeze for 2 turns (3 stacks = frozen, they skip their next turn)", "Record Scratch, +25% atk and def for himself and all his allies until the end of the next turn, and all their attacks land", "Passive: Rewind, If an ally takes more than 150 damage in 1 turn, he clears all debuffs and heals himself and all his allies for that much right away", "Passive: His allies can't die from Burn / Bleed or from a move that makes him Rewind while he is standing, he rewinds them to 150 HP instead", "Passive: Moves that deal 250 or more damage to an enemy are negated and whoever used it gets 1 stack of freeze", "Passive: When he is defeated, +50% def for all his allies and -50% def for all party members for 3 turns"],
    "Jade": [500, 35, 40, 2, 8, 90, "Distort, Attack all party members for 50% of atk", "Sucker Punch, 15 damage to 1 party member, can't miss and stuns them for 1 turn", "Radioactive Spatial Rift, 3 stacks of bleed (-3% hp each) for all party members", "Spatial Shuffle, Every 3 turns: puts the party in a random order", "Passive: When she is defeated, a Doggysplosion deals 25% of max HP to all party members"]
}

# Enemies that blow up the first time they drop below "belowHP" % of their max hp (the Courtyard Droll's Hidden C4): everyone on
# the battlefield takes "percentMaxHP" % of their own max hp, the enemy too (right after the move that did it, it can't be dodged)
enemyBlasts = {
    "Courtyard Droll": {"name": "Hidden C4", "belowHP": 50, "percentMaxHP": 25},
}

# Enemies that can see the future (Rose's Foresight): all their attacks land (Reality Sink, Interfere... still stop them) and
# accuracy debuffs don't work on them
enemyForesight = ["Rose"]
# Enemies with premonitions (Rose): every that many turns (6, 12, 18...) the players can't choose, everyone uses their basic attack
enemyPremonitions = {
    "Rose": 6,
}

# Enemies that Rewind (Dave): if one of their allies takes more than that much damage in 1 turn, all debuffs (and Burn / Bleed) on the
# enemy team are cleared and everyone on it heals that damage, right after the move that did it and as many times as it happens
enemyRewinds = {
    "Dave": 150,
}
# Enemies that don't let their allies die from chip damage (Dave): while they are standing, an ally that would go down to Burn / Bleed
# gets rewound instead, it goes on with that much hp and without its debuffs, as many times as it happens
# (allies that go down in the same move that makes him Rewind come back with that much hp too)
enemyChipRewinds = {
    "Dave": 150,
}
# Enemies that negate big attacks (Dave): while they are standing, a move of the party that does "damage" or more to 1 of the enemies does
# nothing at all to any of them (no damage, no status effects), and whoever used it gets a stack of Freeze (the same as 1/2Sword Swipe's)
enemyNegates = {
    "Dave": {"damage": 250, "freeze": {"turns": 2, "frozenAt": 2}},
}
# What enemies do when they are defeated: "text" is for the battle log, "percentMaxHP" = damage to every party member (it can't be dodged),
# "buff" for all enemies that are still standing, "debuff" on every party member, for "turns" (no turns = the rest of the battle)
enemyLastWords = {
    "Rose": {"text": "goes out in a burst of light", "debuff": {"DD": 100}, "turns": 1},
    "Dave": {"text": "goes out with style", "buff": {"CC": 50}, "debuff": {"CC": 50}, "turns": 3},
    "Jade": {"text": "goes out in a Doggysplosion", "percentMaxHP": 25},
}

# Enemies that steal Grist (the Conquistador's Loot & Pillage): every party member that goes down while this enemy is standing
# takes that much Grist from the player. Beating the battle gets all of it back, losing / retreating / timing out loses it
enemyLoot = {
    "Conquistador": 10,
}

# Fights against several different enemies at once, picked in /battle by this name (it needs a category and a Grist reward like an enemy)
# "enemies" = who is in it, in their turn order
# "spots" = where they stand (the top left corner of their picture), in the order they get drawn (the last one is in front of the others)
# "goesFirst" = the enemies get a turn before round 1, "noItems" = the player's equipped item does nothing in this fight
enemyGroups = {
    "Heroes of Legend": {
        "enemies": ["Dave", "Rose", "Jade", "John"],
        "spots": {"Dave": (14, 83), "Rose": (0, 212), "Jade": (106, 102), "John": (58, 221)},
        "goesFirst": True,
        "noItems": True,
    },
}

# The /battle categories and the enemies in each one, in the order the menus show them
# (a new enemy has to be added to one of these, otherwise nobody can fight it. John, Rose, Dave and Jade are only in Heroes of Legend)
battleCategories = {
    "Dersites": ["Ruffian", "Grunt", "Spearman", "Agent", "Teniente", "Conquistador"],
    "Bosses": ["Jack Noir", "Draconian Dignitary", "Courtyard Droll", "Hegemonic Brute", "Heroes of Legend"],
    "Event Characters": ["Garry's Mod"],
}

# Grist the player gets for WINNING a /battle (losing, retreating or timing out gives nothing)
# The names are the /battle choices. "Ruffian" is when 1 ruffian shows up, "Ruffian x2" is when 2 show up
# A new enemy needs a line here too, otherwise beating it gives 0 Grist
gristRewards = {
    "Ruffian": 5,
    "Ruffian x2": 7,
    "Spearman": 7,
    "Agent": 9,
    "Grunt": 15,
    "Jack Noir": 40,
    "Draconian Dignitary": 50,
    "Courtyard Droll": 30,
    "Hegemonic Brute": 35,
    "Heroes of Legend": 0,
    "Garry's Mod": 50,
    "Teniente": 18,
    "Conquistador": 22,
}
# Bosses: once a player has beaten a boss BOSS_FULL_REWARD_WINS times, that boss only gives them half Grist (rounded up)
# for BOSS_HALF_REWARD_HOURS hours, after that their wins against it count from 0 again
# (every player's wins are counted per boss, in "boss_wins" on their inventory document in MongoDB,
#  and when their half Grist ends in "boss_half_until")
bossEnemies = ["Jack Noir", "Draconian Dignitary", "Courtyard Droll", "Hegemonic Brute", "Garry's Mod"]
BOSS_FULL_REWARD_WINS = 5
BOSS_HALF_REWARD_HOURS = 24

# How much Grist 1 roll costs in /item store (a whole number above 0)
rollPrice = 15
# The 10 rolls deal in /item store: how many rolls it gives and how much Grist it costs (whole numbers above 0)
rollBundleAmount = 10
rollBundlePrice = 135
# Only Get the 5 stats from here (abilities are defined in characterAbilities)
# HP, Attack, Defense, Evasion, Accuracy, Abilities
characterAttributes = {
    "r_abraize": [120, 10, 10, 3, 90, "Punch", "Sleep", "Missing Assignments"],
    "r_abraize2": [120, 10, 10, 3, 90, "Punch", "Eat Note", "Productivity Time"],
    "sr_abraize":  [220, 15, 20, 3, 90, "Punch", "Slow", "Attempt"],
    "ssr_abraize": [400, 35, 35, 3, 90, "Accelerated Punch", "Fast Forward", "Rewind", "Universal Stabilizer"],
    "r_trey": [150, 12, 8, 3, 90, "Punch", "Irish Goodbye", "Cheesy Fries"],
    "sr_trey": [250, 15, 20, 3, 75, "Punch", "Drowsy", "Whispers from Beyond"],
    "ssr_trey": [425, 30, 25, 30, 90, "Void Doohickey", "Cloak and Dagger", "Shroud", "Reality Sink"],
    "r_noah": [125, 10, 8, 3, 90, "Punch", "Fiddle", "Bo"],
    "sr_noah": [180, 15, 8, 3, 92, "Gavel Strike", "Mock", "Defense Lawyer"],
    "r_freeman": [100, 8, 8, 10, 90, "Slap", "Ponder", "SMASH!"],
    "sr_freeman": [180, 8, 8, 10, 90, "Pistol Whip", "Shoot", "Hide"],
    "r_stephen": [130, 9, 8, 3, 90, "Dropkick", "Light up", "Lock the fuck in"],
    "sr_stephen": [180, 9, 8, 3, 90, "Dropkick", "Consider Intervening", "HIYAAAHHH!"],
    "ssr_jayden": [400, 30, 30, 5, 90, "Distort", "Butler of Swatabi", "Indecision", "Genesis"],
    "sr_homestuck": [180, 18, 15, 5, 90, "Impractical Assailants", "Plunder", "Thief"],
    "ssr_scottie": [320, 40, 40, 5, 90, "Fated Strike", "Existential Dread", "Martyrdom", "Nihilism"],
    "r_homestuck": [140, 11, 7, 5, 90, "Punch", "Spotlight Shift", "Rules for thee"],
    "r_max": [165, 10, 13, 2, 90, "Punch", "Brick Eating", "Tour Alliance"],
    "r_jaiden": [120, 9, 10, 3, 90, "Punch", "Pick Up", "Commitment and Fuck"],
    "r_freeman2": [100, 8, 8, 20, 65, "Running Slap", "Huss", "Charging Tackle"],
    "sr_binktop": [270, 20, 25, 0, 90, "Viruslash", "McAfee 265+ Antivirus Shield", "Premium Subscription Malware Annihilating Slash"],
    "ssr_casey": [325, 20, 30, 5, 95, "Music Box", "Ballad of Fortune", "Refrain", "Grand Finale"],
    "ssr_steven": [210, 45, 19, 5, 90, "Wrathful Swipe", "Gussy Charge", "Ragebait", "Reopen Old Wounds"],
    "sssr_max": ["?", "??", "???", "???", "???", "???", "???", "???", "???", "?????"]
}


# HP, Attack, Defense are all Flat Numbers
# Evasion and Accuracy are percentages

# Character titles do not matter in Battle.py as main.py will convert the names to the correct format when needed

# ============================================================================
# HOW AN ABILITY IS WRITTEN
# ============================================================================
# "Ability Name": [option letters..., {numbers}]
#   - the letters say WHAT the move does (Options below)
#   - the dict at the end is optional and says HOW MUCH / HOW LONG
#   - example: "Productivity Time": ['C', 'D', 'H', {"buff": {"BB": 10, "CC": 10}, "turns": 3, "cooldown": 4}]
#       = AOE at Teammates (C) + Buff (D) + Cooldown (H)
#       = +10% attack and +10% defense for the whole team for 3 turns, then it can't be used for 4 turns
#
# A "turn" is one full round: every player goes, then every enemy goes
# Anything an enemy does during its turn starts counting on the next round,
# so an enemy's "for 4 turns" covers the players' next 4 turns
# ============================================================================

# Option A = Damage using Attack Stat (Should be extra parameter in function when calling damaging moves to add damage)
#            Hits 1 enemy (all of them with Option B) and rolls accuracy vs evasion
#            numbers: "power" = % of attack used (default 100), "damage" = flat damage instead of the attack stat,
#                     "percentMaxHP" / "percentCurrentHP" = damage is a % of the target's hp, "trueDamage" = ignores defense buffs,
#                     "trueHP" = that much damage to their hp without the battle hp from defense: the more of their battle hp comes
#                                from defense the more it does, and attack buffs don't change it (Rose's Quill of Echidna),
#                     "plusPercentCurrentHP" = that % of the target's current hp gets added on top (SR Freeman's Shoot),
#                     "plusPercentMaxHP" = the same with their max hp (the Hegemonic Brute's Unforeseen Bite),
#                     "stun" = a hit that lands Stuns the target for that many turns (it skips its turns, R Freeman2's Charging Tackle),
#                     "freeze": {"turns", "frozenAt"} = a hit that lands gives a stack of Freeze for that many turns, at "frozenAt" stacks they
#                                are used up and the target is Frozen (it skips its next turn, Dave's 1/2Sword Swipe),
#                     "missSelfDamage" = if the attack misses (or is evaded) the user takes that much damage (it can't knock them out),
#                     "sureHit" = can't miss or be evaded, "recoil" = % of the damage dealt that the user takes too,
#                     "lifesteal" = % of the damage dealt that the user heals (John's Pop-O-Matic Vrillyhoo Hammer),
#                     "hits" = how many times each target gets hit (each hit rolls to hit on its own, SR Binktop's Viruslash),
#                     "eachHit": [{...}, {...}] = with "hits", the "sureHit" / "accuracy" of the 1st hit, the 2nd... (Bull Penis Cane),
#                     "hitDebuff": {"name", "chance", "debuff", "turns"} = every hit that lands has a chance to debuff the target (Code Rot),
#                     "bonusVsDebuffed": {stat: %} = that much more damage if the target has a debuff on that stat (SSR Casey's Music Box),
#                     "foeBuff": {stat: %} = the target that was hit gets that buff for "turns" (SSR Steven's Wrathful Swipe)
# Option B = Area of Effect at Enemies
# Option C = Area of Effect at Teammates
# Option D = Buff: the whole team with Option C, one picked teammate with Option G, otherwise yourself
#            numbers: "buff": {stat: %}, "turns", "heal" = % of max hp healed, "healHP" = flat hp healed, "debuffImmune" = can't be debuffed while it lasts,
#                     "damageImmune" = can't take any damage while it lasts (hits, Burn, Bleed), paying your own hp still works,
#                     "sureHitsNextTurn": "status name" = every attack they make on their next turn hits (R Jaiden's Commitment),
#                                         a move's own chances ("accuracy", Option O "chance" / "outcomes") are still rolled,
#                                         "sureHitsDamage" = that move does that % more damage too (the Draconian Dignitary's Careful Planning),
#                     "sureHitsForTurns": "status name" = the same, but for every attack during "turns" (Dave's Record Scratch),
#                     "allyBuff": {stat: %} = a different buff for every other teammate at the same time (R Freeman2's Huss, SSR Trey's Shroud),
#                     "crit": {"name", "chance", "multiplier", "nextHit"} = a status that adds to the chance of a critical hit (it works
#                             like Lucky Coin and adds on top of it), "nextHit" = it lasts until their next hit that lands instead of "turns",
#                     "refrain": % = Refrain: the next attack they use is remembered, using it again does that much more damage (once),
#                     "reverseDebuffs" = debuffs turn into buffs (Burn / Bleed heal instead) for as long as they had left,
#                     "coversTheirTurn" = a teammate who already went this round keeps it through their next turn (Ballad of Fortune)
# Option E = Debuff: every enemy with Option B, one picked enemy with Option F (or the enemy hit by Option A),
#            with no target letter it lands on yourself (or a random teammate with Option O "randomAlly")
#            numbers: "debuff": {stat: %}, "turns"
#            (a buff never goes to the enemies and B / F always aim the debuff at them,
#             that is how Thief can debuff all enemies AND buff the whole team in 1 move)
# Option F = Specific Target on opposing team (the player picks with buttons when there is more than 1, enemies pick on their own)
# Option G = Specific Target on own team (the player picks with buttons when there is more than 1)
#            numbers: "othersOnly" = the user can't pick themselves (SSR Casey)
# Option H = Cooldown before you can use the same move again, numbers: "cooldown" = how many turns
# Option I = Stacks of same kind on targets which works with 1 or multiple targets
#            numbers: "stacks": {"name", "add", "max", "turns", "perStack": {stat: % for each stack}, "resetOnOtherMove", "loseStackWhenHit"}
#                     "consumeStacks": {"name", "bonusPerStack"} = uses up all the stacks for extra % damage
#                                      {"name", "flatPerStack"}  = uses up all the stacks for extra flat damage (+10 = 10 more damage per stack)
#                     "buffPerStack": {"name", "stats"} = the buff is multiplied by how many stacks you have
# Option J = Rewind (SSR Abraize): the team's hp, buffs and debuffs go back to how they were at the start of the previous turn
# Option K = Sleep (R Abraize): skip your next turn then wake up with a buff, numbers: "sleepTurns", "wakeBuff": {stat: %}, "wakeTurns"
# Option L = Taunt: the other side's single target attacks have to go at you, numbers: "taunt" = how many turns
#            (an enemy taunting, like Addonshield's Draw Attack, makes the party's attacks on its teammates hit it instead)
# Option M = Lingering effect that does something every turn, numbers: "lingering": {...}
#            "Burn" / "Bleed" = lose "percent" of max hp every turn (lands on the other side like Option E, "stackable" lets it stack,
#                               "stacks" = how many of it land at once)
#            "Regeneration" with "heal": True = heal "percent" of max hp every turn (lands on your side like Option D)
#            "Void Spot" (SSR Trey) = sits on the field, ranged attacks miss and power it up, it grows every turn and then bursts
# Option N = Interrupt: "interrupt": {"name", "chance", "guardsAllies", "counter"} = a status with a chance to cancel an enemy
#            attack, it is used up once it works (R Noah's Interfere protects Noah, SR Freeman's Nervous protects the whole team)
# Option O = Luck: "chance" = % the move works at all, "outcomes" = list of moves and 1 gets picked at random,
#            "weights" = how likely each outcome is (same order as outcomes, leave it out for equal chances),
#            "outcomeText" (inside an outcome) = what the battle log says when that outcome is picked,
#            an F next to the outcomes lets the player pick the enemy first (R Jaiden's Pick Up),
#            "randomAlly" = the debuff lands on a random teammate, "dice": [sides, damage for each number rolled]
# Option P = Doom Marks (SSR Scottie): "doom" = "fatedStrike" / "dread" / "martyrdom" / "nihilism"
# Option Q = Jack Noir Special Passive (Attack lowest health target each turn)
# Option R = Future Boss Special Reserved
# OPtion S = Future Boss Special Reserved
# Option T = Future Boss Special Reserved
# Option U = Future Boss Special Reserved
# Option V = Future Boss Special Reserved
# OPtion W = Future Boss Special Reserved
# Option X = reserved
# Option Y = reserved
# Option Z = Skip Move (For Dev, the Skip button in /battle uses it too), "skipText" = what the battle log says

# Other numbers any move can have
#   "turns" = how long buffs/debuffs last (default 1, 0 = only for the rest of the current turn)
#   "once" = can only be used once per battle (ultimates)
#   "requiresRound" = can only be used from that turn on (Nihilism, Grand Finale, Reopen Old Wounds)
#   "selfDebuff": {stat: %} = a debuff on the user for "turns", whatever the move does to the enemies (SSR Steven's Gussy Charge)
#   "hurtToAttack" = once "turns" are over, the % of max hp the user lost to damage in them becomes an attack buff on the user for
#            "hurtToAttack" turns (SSR Steven's Ragebait)
#   "repeatDamage" = the damage your team's moves did last turn hits the same enemies again (SSR Steven's Reopen Old Wounds)
#   "extraTurn" = the user goes again straight away
#   "selfDamage" = flat hp the user pays, "selfHeal" = % of max hp the user heals, "selfHealHP" = flat hp the user heals
#   "allyCost" = every other teammate pays that % of their max hp (it can't knock them out)
#   "skipEnemyTurn" = the enemies skip their next turn (R Homestuck's Rules for thee)
#   "missNextAttack": "status name" = the user's next attack misses no matter what (R Max's Brick Eating)
#   "accuracy" = replaces the user's accuracy for this move (and makes a move without Option A roll to hit too)
#   "ranged" = it is a ranged attack (these miss while a Void Spot is on the field)
#   "buffName" / "debuffName" = name shown in the embed for the buff/debuff (like "Warped")
#   "failText" = what the battle log says when an Option O "chance" move doesn't work
#   "parry": {"buff", "counter"} = buff + Parry on yourself for "turns", every attack that lands on you gets the "counter" move back,
#            with Option G the picked teammate is defended (single target attacks on them hit you instead) (SR Binktop's Antivirus Shield)
#   "windUp": "status name" = enemies only: using the move just winds up (shown as that status) and ends the enemy's turn,
#            the move really happens at the start of its next turn, "windUpText" / "releaseText" = the battle log (Garry's Mod's Addon-Smash!)
#   "channel": {"skipTurns", "damage", "percentMaxHP", "stunTurns"} = Channeling: your next "skipTurns" turns are skipped and getting hit
#            cancels it (you can act again), if it runs out you hit the Option F enemy for damage + % of its max hp, then you're Stunned
#            (SR Binktop's Annihilating Slash)
#   "duel": {stat: %} = challenge 1 random unit of the other side: you and they both get that buff for "turns", and your single
#            target attacks only go at them for the rest of this turn (the Teniente's Code of Honour)
#   "riposte": % = for "turns", every hit that lands on you costs the attacker that % of their own max hp (the Teniente's Riposte)
#            "riposteFlat" = that much damage on top of it
#   "goesFirst" = enemies only: when the enemy picks this move it happens before its other moves that turn (the Teniente's Code of Honour)
#   "endsTurn" = enemies only: using the move ends the enemy's turn, its other moves that turn don't happen (the Teniente's Riposte)
#   "shuffleTeam" = enemies only: the party's turn order gets randomized (Jade's Spatial Shuffle)
#   "useWhenReady" = enemies only: never picked at random, it is the enemy's first move on every turn it can be used (John's Windy Thing)
#   "cleanseTeam" = clears all debuffs (and Burn / Bleed) on the user's whole team (Rose's Lessons in Showmanship)
#   "moreDebuffsThan" = can only be used while 1 member of the user's team has more different debuffs than that: every move that debuffed
#            them counts as 1, and so do Burn and Bleed no matter how many stacks (Rose's Lessons in Showmanship)
#   "debuffSource": "name" = the Option E debuff counts as coming from that instead of the move (so different ones from 1 move add up)
#   "nextMove": [move names] = enemies only: the enemy's next move is one of these (picked at random), even when it is
#            next turn (Code of Honour -> Thrust, the Conquistador's Battle Cry -> Stab or Slash)

# Options D and E are Basic buffs meaning they only change the 5 main stats of HP, Attack, Defense, Evasion, and Accuracy
# These are the stat codes used inside "buff" / "debuff":
#   AA = HP       -> changes max hp by that % (current hp can't go above the new max)
#   BB = Attack   -> +10 = deals 10% more damage
#   CC = Defense  -> +10 = takes 10% less damage (base defense is already inside ehp, so defense buffs change damage taken instead)
#   DD = Accuracy -> added straight onto the percentage (90% accuracy with DD +10 = 100%)
#   EE = Evasion  -> added straight onto the percentage
statNames = {"AA": "HP", "BB": "ATK", "CC": "DEF", "DD": "ACC", "EE": "EVA"}

# The Skip button in /battle: an Option Z move, so the current character does nothing and the next one goes
skipMove = ['Z', {"skipText": "and stood idle, boggling vacantly at the enemy"}]

# Abilities Moveset + Options for abilities (what every move does is written in the /char embeds in main.py)
characterAbilities = {
  "r_abraize": {
    "Punch": ['A', 'F'],                                            # Flat Damage using Attack Stat
    # Evasion drops to 0% and you skip your next turn, then wake up with +15% atk and def for 2 turns
    "Sleep": ['E', 'K', {"debuff": {"EE": 100}, "turns": 2, "sleepTurns": 1, "wakeBuff": {"BB": 15, "CC": 15}, "wakeTurns": 2}],
    "Missing Assignments": ['D', {"buff": {"DD": 5}, "turns": 2}]   # +5% accuracy to self for 2 turns
  },
  "r_abraize2": {
    "Punch": ['A', 'F'],                                            # Flat Damage using Attack Stat
    "Eat Note": ['D', {"buff": {"EE": 10}, "turns": 2, "selfDamage": 25}],  # +10% evasion to self for 2 turns, costs 25 hp
    # +10% atk and def for the whole team for 3 turns, 4 turn cooldown
    "Productivity Time": ['C', 'D', 'H', {"buff": {"BB": 10, "CC": 10}, "turns": 3, "cooldown": 4}]
  },
  "sr_abraize": {
    "Punch": ['A', 'F'],                                            # Flat Damage using Attack Stat
    "Slow": ['E', 'F', {"debuff": {"DD": 15}, "turns": 2}],         # -15% accuracy to 1 enemy for 2 turns
    # 15% chance to work: heals the whole team for 25% of their max hp and gives them +20% atk for 2 turns
    "Attempt": ['C', 'D', 'O', {"chance": 15, "heal": 25, "buff": {"BB": 20}, "turns": 2,
                                "failText": "but the timeline was doomed..."}]
  },
  "ssr_abraize": {
    # +1 Accelerated stack (+10% atk each, max 10 = +100%) even if it misses, all stacks are lost when using any other move
    "Accelerated Punch": ['A', 'F', 'I', {"stacks": {"name": "Accelerated", "add": 1, "max": 10,
                                                     "perStack": {"BB": 10}, "resetOnOtherMove": True}}],
    # +5% acc, +40% atk, +15% def for the team for 1 turn and you go again straight away, 5 turn cooldown
    "Fast Forward": ['C', 'D', 'H', {"buff": {"DD": 5, "BB": 40, "CC": 15}, "turns": 1, "extraTurn": True, "cooldown": 5}],
    "Rewind": ['H', 'J', {"cooldown": 3}],                          # Team goes back to how it was last turn, 3 turn cooldown
    # Ultimate: the team can't be debuffed, +50% atk for 5 turns and everyone heals 250 hp, once per battle
    "Universal Stabilizer": ['C', 'D', {"buff": {"BB": 50}, "turns": 5, "debuffImmune": True, "healHP": 250, "once": True}]
  },
  "r_trey": {
    "Punch": ['A', 'F'],                                            # Flat Damage using Attack Stat
    "Irish Goodbye": ['D', 'H', {"buff": {"EE": 10}, "turns": 1, "cooldown": 2}],  # +10% evasion to self for 1 turn, 2 turn cooldown
    # 70% chance to hit 1 enemy with Burn (loses 5% of their max hp at the end of the turn)
    "Cheesy Fries": ['F', 'M', {"accuracy": 70, "ranged": True, "lingering": {"name": "Burn", "percent": 5, "turns": 1}}]
  },
  "sr_trey": {
    "Punch": ['A', 'F'],                                            # Flat Damage using Attack Stat
    "Drowsy": ['B', 'E', {"debuff": {"DD": 10}, "turns": 1}],       # -10% accuracy to all enemies for 1 turn
    "Whispers from Beyond": ['C', 'D', 'H', {"buff": {"DD": 10}, "turns": 2, "cooldown": 1}]  # +10% accuracy for the team for 2 turns, 1 turn cooldown
  },
  "ssr_trey": {
    "Void Doohickey": ['A', 'F', {"ranged": True}],                 # Flat Damage using Attack Stat, ranged (the Void Spot swallows it)
    # +100% eva and +10% acc to self for 1 turn, then stab 1 enemy for 80 + 5% of their max hp as true damage, 2 turn cooldown
    "Cloak and Dagger": ['A', 'D', 'F', 'H', {"buff": {"EE": 100, "DD": 10}, "turns": 1, "damage": 80, "plusPercentMaxHP": 5,
                                              "trueDamage": True, "cooldown": 2}],
    # +50% evasion for every other teammate for 3 turns, but enemies have to attack you for 1 turn, 4 turn cooldown
    "Shroud": ['D', 'H', 'L', {"allyBuff": {"EE": 50}, "turns": 3, "taunt": 1, "cooldown": 4}],
    # Ultimate: Void Spot for 3 turns, ranged attacks miss (+50% power each), +100% power every turn, then it bursts on all enemies
    "Reality Sink": ['M', {"lingering": {"name": "Void Spot", "turns": 3, "growPerTurn": 100, "growPerRanged": 50}, "once": True}]
  },
  "r_noah": {
    "Punch": ['A', 'F'],                                            # Flat Damage using Attack Stat
    "Fiddle": ['E', 'F', {"debuff": {"DD": 5}, "turns": 2}],        # -5% accuracy to 1 enemy for 2 turns
    "Bo": ['H', 'N', {"interrupt": {"name": "Interfere", "chance": 50}, "cooldown": 2}]  # 50% to cancel the next hit on self, 2 turn cooldown
  },
  "sr_noah": {
    "Gavel Strike": ['A', 'F'],                                     # Flat Damage using Attack Stat
    # -15% accuracy to all enemies and enemies have to attack you, both for 1 turn
    "Mock": ['B', 'E', 'L', {"debuff": {"DD": 15}, "turns": 1, "taunt": 1}],
    # the whole team can't take any damage for the rest of this turn, 3 turn cooldown
    "Defense Lawyer": ['C', 'D', 'H', {"damageImmune": True, "turns": 0, "cooldown": 3}]
  },
  "r_freeman": {
    "Slap": ['A', 'F'],                                             # Flat Damage using Attack Stat
    "Ponder": ['C', 'D', {"buff": {"EE": 3}, "turns": 1}],          # +3% evasion for the team for 1 turn
    "SMASH!": ['A', 'D', 'F', {"buff": {"BB": 100}, "turns": 1, "recoil": 100}]  # +100% atk to self then attack, take the same damage back
  },
  "sr_freeman": {
    "Pistol Whip": ['A', 'F'],                                      # Flat Damage using Attack Stat
    # pick an enemy: 35% the safety is off (45 damage + 5% of its current hp), 65% it's on and he throws the gun (15 damage), 1 turn cooldown
    "Shoot": ['F', 'H', 'O', {"cooldown": 1, "weights": [35, 65], "outcomes": [
      ['A', 'F', {"damage": 45, "plusPercentCurrentHP": 5, "sureHit": True, "ranged": True, "outcomeText": "the safety was off"}],
      ['A', 'F', {"damage": 15, "sureHit": True, "ranged": True, "outcomeText": "the safety was on, so he throws the gun"}]
    ]}],
    # Nervous: 25% chance to interrupt any enemy attack on the team and Shoot the attacker back (used up once it works)
    "Hide": ['N', {"interrupt": {"name": "Nervous", "chance": 25, "guardsAllies": True, "counter": "Shoot"}}]
  },
  "r_stephen": {
    "Dropkick": ['A', 'F'],                                         # Flat Damage using Attack Stat
    # +1 Baller stack for 3 turns and enemies have to attack you for 3 turns, every hit you take removes a stack
    "Light up": ['I', 'L', {"stacks": {"name": "Baller", "add": 1, "turns": 3, "loseStackWhenHit": False}, "taunt": 3}],
    "Lock the fuck in": ['D', 'I', {"buffPerStack": {"name": "Baller", "stats": {"BB": 5}}, "turns": 1}]  # +5% atk per Baller stack for 1 turn
  },
  "sr_stephen": {
    "Dropkick": ['A', 'F'],                                         # Flat Damage using Attack Stat
    "Consider Intervening": ['I', {"stacks": {"name": "Considering", "add": 1, "turns": 3}}],  # +1 Considering stack (lasts 3 turns)
    "HIYAAAHHH!": ['A', 'F', 'I', {"consumeStacks": {"name": "Considering", "flatPerStack": 15}}]  # +15 damage per stack, uses them up
  },
  "ssr_jayden": {
    "Distort": ['A', 'B', {"power": 50}],                           # 50% of atk as damage to all enemies (less damage since it hits all of them)
    "Butler of Swatabi": ['B', 'E', 'H', {"debuff": {"DD": 30}, "turns": 2, "cooldown": 2}],  # -30% accuracy to all enemies for 2 turns, 2 turn cooldown
    # 1/3: +20% atk and def for the team, 1/3: -20% atk and def to all enemies, 1/3: lose 1 hp
    "Indecision": ['O', {"outcomes": [
      ['C', 'D', {"buff": {"BB": 20, "CC": 20}, "turns": 2}],
      ['B', 'E', {"debuff": {"BB": 20, "CC": 20}, "turns": 2}],
      [{"selfDamage": 1}]
    ]}],
    # Ultimate: Regeneration (5% hp every turn) for the team and Warped (-25% acc, -35% max hp, -25% def) on all enemies for 5 turns
    "Genesis": ['B', 'C', 'E', 'M', {"lingering": {"name": "Regeneration", "percent": 5, "turns": 7, "heal": True},
                                     "debuff": {"DD": 25, "AA": 35, "CC": 25}, "debuffName": "Warped", "turns": 5, "once": True}]
  },
  "sr_homestuck": {
    "Impractical Assailants": ['A', 'F', 'O', {"dice": [6, 10]}],  # Roll a die, 10 damage for every number rolled
    # +15% atk to self and -15% atk to a random teammate for 1 turn
    "Plunder": ['D', 'E', 'O', {"buff": {"BB": 15}, "debuff": {"BB": 15}, "randomAlly": True, "turns": 2}],
    # -100% accuracy to all enemies and +100% accuracy for the team for 1 turn, 5 turn cooldown
    "Thief": ['B', 'C', 'D', 'E', 'H', {"buff": {"DD": 100}, "debuff": {"DD": 100}, "turns": 2, "cooldown": 5}]
  },
  "ssr_scottie": {
    # Low damage (50% atk) that can't miss, every 2nd hit on the same enemy gives it a Doom Mark
    "Fated Strike": ['A', 'F', 'P', {"power": 50, "sureHit": True, "doom": "fatedStrike"}],
    # All enemies: -(15% + 7.5% per Doom Mark) atk and -(20% + 5% per Doom Mark) acc for 3 turns, uses up the marks
    "Existential Dread": ['B', 'E', 'P', {"doom": "dread", "debuff": {"BB": 15, "DD": 20}, "perMark": {"BB": 7.5, "DD": 5}, "turns": 3}],
    # Enemies have to attack you and you take 30% less damage for 2 turns, every hit you take gives the attacker a Doom Mark
    # If you get knocked out during it, every Doom Mark explodes for 150% of your atk, 2 turn cooldown
    "Martyrdom": ['D', 'H', 'L', 'P', {"buff": {"CC": 30}, "turns": 2, "taunt": 2, "doom": "martyrdom", "explodePower": 150, "cooldown": 2}],
    # Ultimate: from turn 4 with 5+ Doom Marks out, for 3 turns the picked enemy hurts itself, hits an ally or lies still each turn
    "Nihilism": ['F', 'P', {"doom": "nihilism", "requiresRound": 4, "requiresMarks": 5, "turns": 3, "once": True}]
  },
  "r_homestuck": {
    "Punch": ['A', 'F'],                                            # Flat Damage using Attack Stat
    # enemies have to attack you for 1 turn and you take 5% less damage this turn (+5 DEF)
    "Spotlight Shift": ['D', 'L', {"buff": {"CC": 5}, "turns": 0, "taunt": 2}],
    # the enemies skip their next turn, but every other teammate loses 10% of their max hp (it can't knock them out), 2 turn cooldown
    "Rules for thee": ['H', {"skipEnemyTurn": True, "allyCost": 10, "cooldown": 2}]
  },
  "r_max": {
    "Punch": ['A', 'F'],                                            # Flat Damage using Attack Stat
    # heal 25 hp, but the next attack misses no matter what
    "Brick Eating": [{"selfHealHP": 25, "missNextAttack": "Full of Brick"}],
    # pick a teammate: +25% to every stat for 1 turn, 2 turn cooldown
    "Tour Alliance": ['D', 'G', 'H', {"buff": {"AA": 25, "BB": 25, "CC": 25, "DD": 25, "EE": 25}, "turns": 2, "cooldown": 2}]
  },
  "r_jaiden": {
    "Punch": ['A', 'F'],                                            # Flat Damage using Attack Stat
    # throw a box at the enemy you pick (ranged), what's inside decides the damage, "weights" = the % chance of each box
    "Pick Up": ['F', 'O', {"weights": [15, 15, 30, 20, 19, 1], "outcomes": [
      ['A', 'F', {"damage": 1, "ranged": True, "outcomeText": "the box had a teddy bear"}],
      ['A', 'F', {"damage": 15, "ranged": True, "outcomeText": "the box had a lovely vase"}],
      ['A', 'F', {"damage": 10, "ranged": True, "outcomeText": "the box had school supplies"}],
      ['A', 'F', {"damage": 15, "ranged": True, "outcomeText": "the box had a precious game console"}],
      ['A', 'F', {"damage": 2, "ranged": True, "outcomeText": "the box had rolled up posters"}],
      ['A', 'F', {"damage": 50, "ranged": True, "outcomeText": "the box had a live beartrap"}]
    ]}],
    # pick a teammate: every attack they make on their next turn is guaranteed to hit
    "Commitment and Fuck": ['D', 'G', {"sureHitsNextTurn": "Committed"}]
  },
  "r_freeman2": {
    "Running Slap": ['A', 'F'],                                     # Flat Damage using Attack Stat
    # runs away instead of attacking: +35% eva to self for this turn, 1 turn cooldown
    "Huss": ['D', 'H', {"buff": {"EE": 35}, "turns": 2, "cooldown": 1}],
    # 45% chance to hit 1 enemy for 45 damage and Stun it (it skips its turn), if it misses he takes 15 damage himself
    "Charging Tackle": ['A', 'F', {"damage": 45, "accuracy": 45, "stun": 1, "missSelfDamage": 15}]
  },
  "sr_binktop": {
    # 2 swipes at 1 enemy, 75% atk each, every swipe that lands has a 15% chance of Code Rot (-10% atk for 2 turns)
    "Viruslash": ['A', 'F', {"power": 75, "hits": 2, "hitDebuff": {"name": "Code Rot", "chance": 15, "debuff": {"BB": 10}, "turns": 2}}],
    # +75% def and Parry for this turn (every attack that lands on him gets a Viruslash back), 3 turn cooldown
    # pick a teammate to defend (their single target attacks hit him instead), picking himself defends nobody
    "McAfee 265+ Antivirus Shield": ['G', 'H', {"parry": {"buff": {"CC": 75}, "counter": "Viruslash"}, "turns": 0, "cooldown": 3}],
    # pick an enemy, Channeling skips his next 2 turns (getting hit cancels it and he can act again), then 265 + 7.5% of the
    # enemy's max hp as damage and he is Stunned for 1 turn, 6 turn cooldown
    "Premium Subscription Malware Annihilating Slash": ['F', 'H', {"channel": {"skipTurns": 2, "damage": 265, "percentMaxHP": 7.5, "stunTurns": 1},
                                                                   "cooldown": 6}]
  },
  "ssr_casey": {
    # Ranged, double damage (+100%) against an enemy with an accuracy debuff on it
    "Music Box": ['A', 'F', {"ranged": True, "bonusVsDebuffed": {"DD": 100}}],
    # pick another teammate: +15% acc and 33% Critical Chance (1.5x damage like Lucky Coin) for 1 of their turns, 2 turn cooldown
    "Ballad of Fortune": ['D', 'G', 'H', {"buff": {"DD": 15}, "crit": {"name": "Critical Chance", "chance": 33, "multiplier": 1.5},
                                          "turns": 1, "coversTheirTurn": True, "othersOnly": True, "cooldown": 2}],
    # pick another teammate without Refrain: the next attack they use is remembered (their Melody), the next time they use
    # that same move it does +50% damage and Refrain is used up
    "Refrain": ['D', 'G', {"refrain": 50, "othersOnly": True}],
    # Ultimate: from turn 5, the team's debuffs turn into buffs (Burn / Bleed heal) for as long as they had left,
    # and the next hit everyone lands is a guaranteed critical hit (only that 1 hit, not the whole move)
    "Grand Finale": ['C', 'D', {"reverseDebuffs": True, "crit": {"name": "Guaranteed Critical", "chance": 100, "multiplier": 1.5, "nextHit": True},
                                "requiresRound": 5, "once": True}]
  },
  "ssr_steven": {
    # Flat Damage using Attack Stat, the enemy that was hit gets +15% atk but -15% acc for 2 turns
    "Wrathful Swipe": ['A', 'E', 'F', {"debuff": {"DD": 15}, "foeBuff": {"BB": 15}, "turns": 2}],
    # +50% atk but -50% def to self for 2 turns, then 100% of atk to all enemies (the +50% counts for this hit already)
    "Gussy Charge": ['A', 'B', 'D', {"buff": {"BB": 50}, "selfDebuff": {"CC": 50}, "turns": 2}],
    # draws all attacks to himself with -75% def for 1 turn, then the % of his max hp he lost becomes an atk buff for 2 turns, 3 turn cooldown
    "Ragebait": ['H', 'L', {"taunt": 1, "selfDebuff": {"CC": 75}, "turns": 1, "hurtToAttack": 2, "cooldown": 3}],
    # Ultimate: from turn 4, all the damage your team's moves did last turn hits the same enemies again (only the damage),
    # then 2 stacks of Bleed (3% of max hp, like Jack Noir's) on all enemies
    "Reopen Old Wounds": ['B', 'M', {"repeatDamage": True, "requiresRound": 4, "once": True,
                                     "lingering": {"name": "Bleed", "percent": 3, "turns": 1, "stackable": True, "stacks": 2}}]
  }
}

enemyAbilities = {
  "Ruffian1": {
    "Punch": ['A', 'F']                                             # Flat Damage using Attack Stat
  },
  "Ruffian2": {
    "Punch": ['A', 'F']                                             # Flat Damage using Attack Stat
  },
  "Grunt": {
    "Punch": ['A', 'F'],                                            # Flat Damage using Attack Stat
    "Slam": ['A', 'B', {"damage": 20}]                              # 20 damage to all party members
  },
  "Spearman": {
    "Punch": ['A', 'F'],                                            # Flat Damage using Attack Stat
    "Swipe": ['A', 'B', {"damage": 20}],                            # 20 damage to all party members
    "Stab": ['A', 'D', 'F', {"buff": {"BB": 15}, "turns": 0}]       # +15% atk for the rest of this turn, then attack
  },
  "Agent": {
    "Punch": ['A', 'F'],                                            # Flat Damage using Attack Stat
    "Sneak": ['A', 'D', 'F', {"buff": {"EE": 15}, "turns": 4}]      # +15% evasion for the next 4 turns, then Punch
  },
  "Jack Noir": {
    "Stab": ['A', 'F', 'Q'],                                        # Hits the party member with the lowest hp
    # Hits the lowest hp party member and makes them Bleed (3% of max hp next turn), Bleed stacks
    "Shiv": ['A', 'F', 'I', 'M', 'Q', {"lingering": {"name": "Bleed", "percent": 3, "turns": 1, "stackable": True}}],
    # Only 5 damage, but to all party members and they all Bleed
    "Slash": ['A', 'B', 'M', {"damage": 5, "lingering": {"name": "Bleed", "percent": 3, "turns": 1, "stackable": True}}]
  },
  "Garry's Mod": {
    "Hit": ['A', 'F', {"power": 50}],                               # 50% of atk to 1 party member
    # rears up (that ends his turn), then at the start of his next turn comes crashing down for 100% of atk on every party member
    "Addon-Smasg!": ['A', 'B', {"windUp": "Rearing Up", "windUpText": "rears up", "releaseText": "comes crashing down"}]
  },
  "Addonshield": {
    # Taunt for enemies: the party's single target attacks on Garry's Mod hit the Addonshield instead
    "Draw Attack": ['L', {"taunt": 1}]
  },
  "Teniente": {
    "Thrust": ['A', 'F'],                                           # Flat Damage using Attack Stat
    # challenges 1 random party member: both get +15% atk and def for 1 turn, and he only attacks them for the rest of this turn
    # (goesFirst: when he picks it, it happens before his other move this turn, and his next move is always a Thrust)
    "Code of Honour": [{"duel": {"BB": 15, "CC": 15}, "turns": 1, "goesFirst": True, "nextMove": ["Thrust"]}],
    # until the end of his next turn, every hit that lands on him costs the attacker 30 + 10% of their own max hp, it ends his turn
    "Riposte": [{"riposte": 10, "riposteFlat": 30, "turns": 1, "endsTurn": True}]
  },
  "Conquistador": {
    "Slash": ['A', 'B', {"power": 75}],                             # 75% of atk to every party member
    "Stab": ['A', 'F'],                                             # Flat Damage using Attack Stat
    # -35% def (35% more damage taken) for every party member, his next move is always a Stab or a Slash
    "Battle Cry": ['E', 'B', {"debuff": {"CC": 35}, "turns": 1, "nextMove": ["Stab", "Slash"]}]
    # Loot & Pillage is his passive, it is in enemyLoot
  },
  "Draconian Dignitary": {
    "Cue Whack": ['A', 'F', {"power": 150, "stun": 1}],             # 150% of atk, whoever gets hit is Stunned for their next turn
    # his next move can't miss and does 75% more damage (goesFirst: it happens before his other moves, and his next move is always an attack)
    "Careful Planning": ['D', {"sureHitsNextTurn": "Careful Planning", "sureHitsDamage": 75, "goesFirst": True, "nextMove": ["Cue Whack", "Cue Swipe"]}],
    "Cue Swipe": ['A', 'B']                                         # 100% of atk to every party member
  },
  "Courtyard Droll": {
    # 3 swipes of 100% of atk at 1 party member: the 1st always hits, the 2nd has 75% accuracy and the 3rd 50%
    "Bull Penis Cane": ['A', 'F', {"hits": 3, "eachHit": [{"sureHit": True}, {"accuracy": 75}, {"accuracy": 50}]}],
    "Scamper": ['E', 'B', {"debuff": {"DD": 20}, "turns": 2}]       # -20% acc for every party member for 2 turns
    # Hidden C4 is his passive, it is in enemyBlasts
  },
  "Hegemonic Brute": {
    # the same move as Garry's Mod's Addon-Smasg!: rears up (that ends his turn), then 100% of atk on every party member next turn
    "Smash": ['A', 'B', {"windUp": "Rearing Up", "windUpText": "rears up", "releaseText": "smashes the ground"}],
    # 40 damage + 10% of their max hp to 1 party member and 2 stacks of Bleed (3% of max hp each, like Jack Noir's), 2 stacks at most
    "Unforeseen Bite": ['A', 'F', 'M', {"damage": 40, "plusPercentMaxHP": 10,
                                        "lingering": {"name": "Bleed", "percent": 3, "turns": 1, "stackable": True, "stacks": 2, "maxStacks": 2}}],
    "Trusty Axe": ['A', 'B', {"power": 50}]                         # 50% of atk to every party member
  },
  "John": {  # can only be fought in Heroes of Legend (enemyGroups)
    "Scarf Swipe": ['A', 'F'],                                      # Flat Damage using Attack Stat
    # 50 damage to 1 party member + 1 of 8 random effects on whoever got hit (all equally likely)
    "Pop-O-Matic Vrillyhoo Hammer": ['O', {"outcomes": [
      ['A', 'F', {"damage": 50, "outcomeText": "rolled a 1 (no effect)"}],
      ['A', 'F', 'M', {"damage": 50, "lingering": {"name": "Bleed", "percent": 5, "turns": 2, "stackable": True, "stacks": 2}, "outcomeText": "rolled a 2"}],
      ['A', 'E', 'F', {"damage": 50, "debuff": {"BB": 45}, "turns": 2, "debuffSource": "Hammer ATK", "outcomeText": "rolled a 3"}],
      ['A', 'E', 'F', {"damage": 50, "debuff": {"CC": 45}, "turns": 2, "debuffSource": "Hammer DEF", "outcomeText": "rolled a 4"}],
      ['A', 'E', 'F', {"damage": 50, "debuff": {"EE": 45}, "turns": 2, "debuffSource": "Hammer EVA", "outcomeText": "rolled a 5"}],
      ['A', 'E', 'F', {"damage": 50, "debuff": {"DD": 45}, "turns": 2, "debuffSource": "Hammer ACC", "outcomeText": "rolled a 6"}],
      ['A', 'F', {"damage": 50, "stun": 1, "outcomeText": "rolled a 7"}],
      ['A', 'F', {"damage": 50, "lifesteal": 100, "outcomeText": "rolled an 8"}]
    ]}],
    # Ultimate: used on turn 4, 8, 12... can't miss, 15% of max hp to every party member and -30% acc for 3 turns
    "Windy Thing": ['A', 'B', 'E', 'H', {"percentMaxHP": 45, "sureHit": True, "debuff": {"DD": 30}, "turns": 3,
                                         "useWhenReady": True, "requiresRound": 4, "cooldown": 3}]
  },
  "Rose": {  # can only be fought in Heroes of Legend (enemyGroups)
    "Needlewand": ['A', 'F', {"ranged": True}],                     # Flat Damage using Attack Stat, ranged
    # 40 true damage, ranged: the battle hp that comes from defense and defense buffs don't help against it
    "Quill of Echidna": ['A', 'F', {"trueHP": 70, "trueDamage": True, "ranged": True}],
    # used when 1 of the enemies has more than 4 different debuffs: clears all debuffs on all of them
    "Lessons in Showmanship": ['C', {"cleanseTeam": True, "moreDebuffsThan": 4, "useWhenReady": True}]
    # her premonition and Foresight are in enemyPremonitions and enemyForesight
  },
  "Dave": {  # can only be fought in Heroes of Legend (enemyGroups)
    # 100% of atk to every party member and 1 stack of Freeze for 2 turns, at 3 stacks they are Frozen (they skip their next turn)
    "1/2Sword Swipe": ['A', 'B', {"freeze": {"turns": 2, "frozenAt": 2}}],
    # +25% atk and def for the enemy team until the end of the next turn, and all their attacks land
    "Record Scratch": ['C', 'D', {"buff": {"BB": 25, "CC": 25}, "turns": 1, "sureHitsForTurns": "Sees the Future"}]
    # his Rewind is in enemyRewinds, saving his allies from Burn / Bleed is in enemyChipRewinds
  },
  "Jade": {  # can only be fought in Heroes of Legend (enemyGroups)
    "Distort": ['A', 'B'],                           # 50% of atk to every party member (the same as SSR Jayden's)
    "Sucker Punch": ['A', 'F', {"damage": 15, "sureHit": True, "stun": 1}],  # 15 damage to 1 party member, can't miss and Stuns them
    # 3 stacks of Bleed (3% of max hp each, like Jack Noir's) for every party member, it doesn't have to hit
    "Radioactive Spatial Rift": ['B', 'M', {"lingering": {"name": "Burn", "percent": 3, "turns": 2, "stackable": True, "stacks": 3}}],
    # Ultimate: used on turn 3, 6, 9... the party goes in a new random order
    "Spatial Shuffle": ['H', {"shuffleTeam": True, "useWhenReady": True, "requiresRound": 2, "cooldown": 1}]
  }
}
