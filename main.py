import asyncio
import os
import discord
from discord.ext import commands
from discord import app_commands
from pymongo import MongoClient
import random
from collections import Counter
from PIL import Image
from dotenv import load_dotenv
import time
import traceback

from battle import *
from utils import *

load_dotenv("token.env")

MONGO_URI = "mongodb://localhost:27017"
DB_NAME = "jitstuck"
COLLECTION_NAME = "inventory"

# Mongo Uses DBS called "jitstuck" and assumes a collection called "inventory"

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
inventory_collection = db[COLLECTION_NAME]

# main.py - basic discord.py bot that goes online

# Put your bot token in the DISCORD_TOKEN environment variable
TOKEN = os.getenv("DISCORD_TOKEN")

if not TOKEN:
    raise RuntimeError("DISCORD_TOKEN environment variable not set")

intents = discord.Intents.default()
intents.message_content = True  # enable if you want text commands (enable in dev portal if required)
intents.members = True

bot = commands.Bot(command_prefix="/", intents=intents, help_command=None)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Gacha Game"))
    print("teeesst")

    # Change inBattle to false for all users on bot startup
    inventory_collection.update_many({}, {"$set": {"inBattle": False}})

    # Add all users from all guilds to MongoDB
    for guild in bot.guilds:
        for member in guild.members:
            #print("Checking user:", member.name)
            if not member.bot:  # Skip bots
                print("User: " + member.name)
                user_data = {
                    "user_id": member.id,
                    "username": str(member),
                    "inventory": {},
                    "rolls": 10,  # Starting rolls,
                    "counter": 0,
                    "team": []
                }
                # Use upsert to avoid duplicates
                inventory_collection.update_one(
                    {"user_id": member.id},
                    {"$setOnInsert": user_data},
                    upsert=True
                )
    print(f"Initialized users in database from {len(bot.guilds)} guild(s)")


# Roll, inventory, Character, battle, challenge, team, viewteam, recycle, help

# Create all character choices for autocomplete
all_characters = rChar + srChar + ssrChar + specialChar# + secretChar
character_choices = [
    app_commands.Choice(name=characterTitles[char], value=char)
    for char in all_characters
]

# Use abraizeEmbed as example for other characters
# HP attack and defense are integers
# evasion and accuracy are percentages

# each character will have an 8 length array that includes all attributes
# hp, atk, def, eva, acc, skill1, skill2, skill3
# the only exxception is that ssr characters will have an ultimate skill making it a 9 length array

def r_abraizeEmbed():
    embed = discord.Embed(title=characterTitles["r_abraize"], description="Abraize Masood", color=0x3f48cc)
    # add image from bannerGifs dict
    embed.set_image(url=bannerGifs["r_abraize_gif"])
    embed.add_field(name="HP:", value=characterAttributes["r_abraize"][0], inline=True)
    embed.add_field(name="ATK:", value=characterAttributes["r_abraize"][1], inline=True)
    embed.add_field(name="DEF:", value=characterAttributes["r_abraize"][2], inline=True)
    embed.add_field(name="EVA:", value=characterAttributes["r_abraize"][3], inline=True)
    embed.add_field(name="ACC:", value=characterAttributes["r_abraize"][4], inline=True)
    embed.add_field(name=characterAttributes["r_abraize"][5], value="Throws a mean right hook at the enemy.", inline=False)
    embed.add_field(name=characterAttributes["r_abraize"][6], value="Take a nap on the field, reducing self's evasion score to 0%. \nFor one turn, unable to attack or act. After said turn, gain a 15% atk and def buff to self for 2 turns.", inline=False)
    embed.add_field(name=characterAttributes["r_abraize"][7], value="Getting these done really lifted a weight off your chest. +5% acc boost for one turn.", inline=False)
    return embed

def r_abraize2Embed():
    embed = discord.Embed(title=characterTitles["r_abraize2"], description="Abraize Masood", color=0x3f48cc)
    embed.set_image(url=R_ABRAIZE2_GIF)
    embed.add_field(name="HP:", value=characterAttributes["r_abraize2"][0], inline=True)
    embed.add_field(name="ATK:", value=characterAttributes["r_abraize2"][1], inline=True)
    embed.add_field(name="DEF:", value=characterAttributes["r_abraize2"][2], inline=True)
    embed.add_field(name="EVA:", value=characterAttributes["r_abraize2"][3], inline=True)
    embed.add_field(name="ACC:", value=characterAttributes["r_abraize2"][4], inline=True)
    embed.add_field(name=characterAttributes["r_abraize2"][5], value="Throws a mean right hook at the enemy.", inline=False)
    embed.add_field(name=characterAttributes["r_abraize2"][6], value="Apply a +10% evasion buff to self for one turn, but cost 25 HP.", inline=False)
    embed.add_field(name=characterAttributes["r_abraize2"][7], value="Apply a 10% atk and def buff to all allies for 3 turns, cannot be used for 4 turns.", inline=False)
    return embed

def sr_abraizeEmbed():
    embed = discord.Embed(title=characterTitles["sr_abraize"], description="Abraize Masood", color=0x3f48cc)
    embed.set_image(url=SR_ABRAIZE_GIF)
    embed.add_field(name="HP:", value=characterAttributes["sr_abraize"][0], inline=True)
    embed.add_field(name="ATK:", value=characterAttributes["sr_abraize"][1], inline=True)
    embed.add_field(name="DEF:", value=characterAttributes["sr_abraize"][2], inline=True)
    embed.add_field(name="EVA:", value=characterAttributes["sr_abraize"][3], inline=True)
    embed.add_field(name="ACC:", value=characterAttributes["sr_abraize"][4], inline=True)
    embed.add_field(name=characterAttributes["sr_abraize"][5], value="Throws a mean right hook at the enemy.", inline=False)
    embed.add_field(name=characterAttributes["sr_abraize"][6], value="Applies a -15% accuracy debuff to one enemy.", inline=False)
    embed.add_field(name=characterAttributes["sr_abraize"][7], value="Attempt to travel back in time without being doomed. Has an 85% chance of doing nothing. 15% chance that health is healed by 50% and all allies atk is buffed by 20% for one turn.", inline=False)
    return embed

def ssr_abraizeEmbed():
    embed = discord.Embed(title=characterTitles["ssr_abraize"], description="Abraize Masood", color=0x3f48cc)
    embed.set_image(url=SSR_ABRAIZE_GIF)
    embed.add_field(name="HP:", value=characterAttributes["ssr_abraize"][0], inline=True)
    embed.add_field(name="ATK:", value=characterAttributes["ssr_abraize"][1], inline=True)
    embed.add_field(name="DEF:", value=characterAttributes["ssr_abraize"][2], inline=True)
    embed.add_field(name="EVA:", value=characterAttributes["ssr_abraize"][3], inline=True)
    embed.add_field(name="ACC:", value=characterAttributes["ssr_abraize"][4], inline=True)
    embed.add_field(name=characterAttributes["ssr_abraize"][5], value="Accelerate yourself to punch the opponent. Guaranteed to hit. Applies one stack of 'Accelerated' state to self. Gain +10% atk for every consecutive 'Accelerated' state with a maximum of +100% atk. All 'Accelerated' stacks are removed when using another move.", inline=False)
    embed.add_field(name=characterAttributes["ssr_abraize"][6], value="Apply a +5% acc bonus, +40% atk bonus, and +15% def bonus to all allies for one turn and allows you to immediately take another turn. Cannot be used for another 5 turns.", inline=False)
    embed.add_field(name=characterAttributes["ssr_abraize"][7], value="Revert all party member's stats to the state they were in during the prior turn. Cannot be used for another 2 turns.", inline=False)
    embed.add_field(name=characterAttributes["ssr_abraize"][8], value="Your status as an anchor of time and your experience lends you well to combat. Turn back the wheels of time to make everything right again. Applies debuff nullification (cannot be debuffed) and a +50% atk bonus to all allies for 5 turns. Heals all allies to full. Cannot be used again.", inline=False)
    return embed

def r_treyEmbed():
    embed = discord.Embed(title=characterTitles["r_trey"], description="Treyvaughn Lewis", color=0x3f48cc)
    embed.set_image(url=R_TREY_GIF)
    embed.add_field(name="HP:", value=characterAttributes["r_trey"][0], inline=True)
    embed.add_field(name="ATK:", value=characterAttributes["r_trey"][1], inline=True)
    embed.add_field(name="DEF:", value=characterAttributes["r_trey"][2], inline=True)
    embed.add_field(name="EVA:", value=characterAttributes["r_trey"][3], inline=True)
    embed.add_field(name="ACC:", value=characterAttributes["r_trey"][4], inline=True)
    embed.add_field(name=characterAttributes["r_trey"][5], value="Throws a mean right hook at the enemy.", inline=False)
    embed.add_field(name=characterAttributes["r_trey"][6], value="Apply a one time +10% eva buff to self for one turn. Can be used again after 2 turns", inline=False)
    embed.add_field(name=characterAttributes["r_trey"][7], value="Throws cheesy fries at one enemy of choice, applies Burn on them for one turn. 70% chance to hit", inline=False)
    return embed

def sr_treyEmbed():
    embed = discord.Embed(title=characterTitles["sr_trey"], description="Treyvaughn Lewis", color=0x3f48cc)
    embed.set_image(url=SR_TREY_GIF)
    embed.add_field(name="HP:", value=characterAttributes["sr_trey"][0], inline=True)
    embed.add_field(name="ATK:", value=characterAttributes["sr_trey"][1], inline=True)
    embed.add_field(name="DEF:", value=characterAttributes["sr_trey"][2], inline=True)
    embed.add_field(name="EVA:", value=characterAttributes["sr_trey"][3], inline=True)
    embed.add_field(name="ACC:", value=characterAttributes["sr_trey"][4], inline=True)
    embed.add_field(name=characterAttributes["sr_trey"][5], value="Throws a mean right hook at the enemy.", inline=False)
    embed.add_field(name=characterAttributes["sr_trey"][6], value="Applies a -10% acc debuff to all opponents for one turn.", inline=False)
    embed.add_field(name=characterAttributes["sr_trey"][7], value="The horrorterrors beckon. Give a +10% acc boost to all allies", inline=False)
    return embed

def ssr_treyEmbed():
    embed = discord.Embed(title=characterTitles["ssr_trey"], description="Treyvaughn Lewis", color=0x3f48cc)
    embed.set_image(url=SSR_TREY_GIF)
    embed.add_field(name="HP:", value=characterAttributes["ssr_trey"][0], inline=True)
    embed.add_field(name="ATK:", value=characterAttributes["ssr_trey"][1], inline=True)
    embed.add_field(name="DEF:", value=characterAttributes["ssr_trey"][2], inline=True)
    embed.add_field(name="EVA:", value=characterAttributes["ssr_trey"][3], inline=True)
    embed.add_field(name="ACC:", value=characterAttributes["ssr_trey"][4], inline=True)
    embed.add_field(name=characterAttributes["ssr_trey"][5], value="Throw a mean right hook at the enemy.", inline=False)
    embed.add_field(name=characterAttributes["ssr_trey"][6], value="Add a +100% eva buff and +10% acc buff to self for one turn. Performs a stabbing attack on one enemy that deals 10% max hp and true damage. Cannot be used for 2 turns.", inline=False)
    embed.add_field(name=characterAttributes["ssr_trey"][7], value="Redistribute the void into those around you. +50% eva buff to all allies for 3 turns, but draws attacks to you for one turn. Cannot be used again for 4 turns.", inline=False)
    embed.add_field(name=characterAttributes["ssr_trey"][8], value="Nothing can't be seen, right? Centering all of the void you control into one spot should be able to create a concentrated spot of nothing, a nothing so strong that no thing can escape it. Create a miniature \"void spot\" that stays on the battle for 3 turns. When on the stage, all ranged attacks automatically miss. For each ranged attack performed, the power grows by 50%. After every turn, power grows by 100%. At the end of 3 turns, deals the combined percentage of atk to all enemies in one burst. Cannot be used again.", inline=False)
    return embed

def r_noahEmbed():
    embed = discord.Embed(title=characterTitles["r_noah"], description="Noah Cave", color=0x3f48cc)
    embed.set_image(url=R_NOAH_GIF)
    embed.add_field(name="HP:", value=characterAttributes["r_noah"][0], inline=True)
    embed.add_field(name="ATK:", value=characterAttributes["r_noah"][1], inline=True)
    embed.add_field(name="DEF:", value=characterAttributes["r_noah"][2], inline=True)
    embed.add_field(name="EVA:", value=characterAttributes["r_noah"][3], inline=True)
    embed.add_field(name="ACC:", value=characterAttributes["r_noah"][4], inline=True)
    embed.add_field(name=characterAttributes["r_noah"][5], value="Throws a mean right hook at the enemy.", inline=False)
    embed.add_field(name=characterAttributes["r_noah"][6], value="Send an annoying text message to one enemy, applying a -5% acc debuff to them.", inline=False)
    embed.add_field(name=characterAttributes["r_noah"][7], value="Apply \"Interfere\" state to self permanently until exhausted. \"Interfere\" state allows a 50% chance of an incoming enemy attack to be negated one time before the state is exhausted and removed from self. Can only be used again after 2 turns.", inline=False)
    return embed

def r_freemanEmbed():
    embed = discord.Embed(title=characterTitles["r_freeman"], description="Freeman", color=0x3f48cc)
    embed.set_image(url=R_FREEMAN_GIF)
    embed.add_field(name="HP:", value=characterAttributes["r_freeman"][0], inline=True)
    embed.add_field(name="ATK:", value=characterAttributes["r_freeman"][1], inline=True)
    embed.add_field(name="DEF:", value=characterAttributes["r_freeman"][2], inline=True)
    embed.add_field(name="EVA:", value=characterAttributes["r_freeman"][3], inline=True)
    embed.add_field(name="ACC:", value=characterAttributes["r_freeman"][4], inline=True)
    embed.add_field(name=characterAttributes["r_freeman"][5], value="Bitch slap the opponent with your weak arm.", inline=False)
    embed.add_field(name=characterAttributes["r_freeman"][6], value="Apply a 3% eva buff to all allies for 1 turn.", inline=False)
    embed.add_field(name=characterAttributes["r_freeman"][7], value="Apply a temporary +10% atk buff to self and deal damage to one opponent. The damage dealt is then subtracted from your hp.", inline=False)
    return embed

def sr_freemanEmbed():
    embed = discord.Embed(title=characterTitles["sr_freeman"], description="Freeman", color=0x3f48cc)
    embed.set_image(url=SR_FREEMAN_GIF)
    embed.add_field(name="HP:", value=characterAttributes["sr_freeman"][0], inline=True)
    embed.add_field(name="ATK:", value=characterAttributes["sr_freeman"][1], inline=True)
    embed.add_field(name="DEF:", value=characterAttributes["sr_freeman"][2], inline=True)
    embed.add_field(name="EVA:", value=characterAttributes["sr_freeman"][3], inline=True)
    embed.add_field(name="ACC:", value=characterAttributes["sr_freeman"][4], inline=True)
    embed.add_field(name=characterAttributes["sr_freeman"][5], value="Nobody expects a good clocking from a gun.", inline=False)
    embed.add_field(name=characterAttributes["sr_freeman"][6], value="80% chance of the safety being on, dealing no damage. 20% that the safety was left off, dealing 10% of the enemy's current hp.", inline=False)
    embed.add_field(name=characterAttributes["sr_freeman"][7], value="Apply \"Nervous\" state to self. As long as self has \"Nervous\" state, apply a 25% chance that each attack made by an enemy can be interrupted (similar to R Noah). When an attack is interrupted, trigger Ability 2 on the attacking enemy.", inline=False)
    return embed

def r_stephenEmbed():
    embed = discord.Embed(title=characterTitles["r_stephen"], description="Stephen Goraynov", color=0x3f48cc)
    embed.set_image(url=R_STEPHEN_GIF)
    embed.add_field(name="HP:", value=characterAttributes["r_stephen"][0], inline=True)
    embed.add_field(name="ATK:", value=characterAttributes["r_stephen"][1], inline=True)
    embed.add_field(name="DEF:", value=characterAttributes["r_stephen"][2], inline=True)
    embed.add_field(name="EVA:", value=characterAttributes["r_stephen"][3], inline=True)
    embed.add_field(name="ACC:", value=characterAttributes["r_stephen"][4], inline=True)
    embed.add_field(name=characterAttributes["r_stephen"][5], value="Kick the shit out of one enemy.", inline=False)
    embed.add_field(name=characterAttributes["r_stephen"][6], value="Light your BALLER CIGARETTE, drawing everyone's attention towards you. Applies \"Baller\" status to self for 3 turns. If hit during \"Baller\" status, remove one stack.", inline=False)
    embed.add_field(name=characterAttributes["r_stephen"][7], value="Add +5% atk bonus for one turn per each \"Baller\" status self has.", inline=False)
    return embed

def sr_stephenEmbed():
    embed = discord.Embed(title=characterTitles["sr_stephen"], description="Stephen Goraynov", color=0x3f48cc)
    embed.set_image(url=SR_STEPHEN_GIF)
    embed.add_field(name="HP:", value=characterAttributes["sr_stephen"][0], inline=True)
    embed.add_field(name="ATK:", value=characterAttributes["sr_stephen"][1], inline=True)
    embed.add_field(name="DEF:", value=characterAttributes["sr_stephen"][2], inline=True)
    embed.add_field(name="EVA:", value=characterAttributes["sr_stephen"][3], inline=True)
    embed.add_field(name="ACC:", value=characterAttributes["sr_stephen"][4], inline=True)
    embed.add_field(name=characterAttributes["sr_stephen"][5], value="Kick the shit out of an enemy.", inline=False)
    embed.add_field(name=characterAttributes["sr_stephen"][6], value="Applies 1 stack of \"Considering\" state to self for 3 turns.", inline=False)
    embed.add_field(name=characterAttributes["sr_stephen"][7], value="Converts each stack of \"Considering\" into a 10% damage buff and then attacks one enemy.", inline=False)
    return embed

def ssr_jaydenEmbed():
    embed = discord.Embed(title=characterTitles["ssr_jayden"], description="Jayden Ceballos", color=0x3f48cc)
    embed.set_image(url=SSR_JAYDEN_GIF)
    embed.add_field(name="HP:", value=characterAttributes["ssr_jayden"][0], inline=True)
    embed.add_field(name="ATK:", value=characterAttributes["ssr_jayden"][1], inline=True)
    embed.add_field(name="DEF:", value=characterAttributes["ssr_jayden"][2], inline=True)
    embed.add_field(name="EVA:", value=characterAttributes["ssr_jayden"][3], inline=True)
    embed.add_field(name="ACC:", value=characterAttributes["ssr_jayden"][4], inline=True)
    embed.add_field(name=characterAttributes["ssr_jayden"][5], value="Throw a mean right hook at the enemy.", inline=False)
    embed.add_field(name=characterAttributes["ssr_jayden"][6], value="Leverage your dreadful reputation as the Butler of Ill Repute. -30% acc for all enemies.", inline=False)
    embed.add_field(name=characterAttributes["ssr_jayden"][7], value="33% chance to buff all allies atk and def by 20%, 33% chance to debuff all enemies atk and def by 20%, 33% chance to deal 1 hp of damage to self.", inline=False)
    embed.add_field(name=characterAttributes["ssr_jayden"][8], value="With the power of creation on your side, it is your sworn duty to bring about its influence in this world. It is your job to decrease the space between you and your allies, and to increase the space between your allies and your enemies. Apply \"Regeneration\" status (5% hp heal every turn) for the next 7 turns, as well as apply \"Warped\" status (-25% acc penalty, -35% max hp, -25% def) to all enemies for the next 7 turns. Cannot be used again.", inline=False)
    return embed

def sr_homestuckEmbed():
    embed = discord.Embed(title=characterTitles["sr_homestuck"], description="Homestuck", color=0x3f48cc)
    embed.set_image(url=SR_HOMESTUCK_GIF)
    embed.add_field(name="HP:", value=characterAttributes["sr_homestuck"][0], inline=True)
    embed.add_field(name="ATK:", value=characterAttributes["sr_homestuck"][1], inline=True)
    embed.add_field(name="DEF:", value=characterAttributes["sr_homestuck"][2], inline=True)
    embed.add_field(name="EVA:", value=characterAttributes["sr_homestuck"][3], inline=True)
    embed.add_field(name="ACC:", value=characterAttributes["sr_homestuck"][4], inline=True)
    embed.add_field(name=characterAttributes["sr_homestuck"][5], value="Roll a die! Deal damage in increments of 10 based on what you get!", inline=False)
    embed.add_field(name=characterAttributes["sr_homestuck"][6], value="Apply a -15% atk debuff to one random ally for one turn, provide a +15% atk buff to self for one turn.", inline=False)
    embed.add_field(name=characterAttributes["sr_homestuck"][7], value="Apply a -100% acc penalty to all enemies and a +100% acc bonus to all allies for one turn. Cannot be used again for 5 turns.", inline=False)
    return embed

def ssr_scottieEmbed():
    embed = discord.Embed(title=characterTitles["ssr_scottie"], description="Scottie Jenkins", color=0x3f48cc)
    embed.set_image(url=SSR_SCOTTIE_GIF)
    embed.add_field(name="HP:", value=characterAttributes["ssr_scottie"][0], inline=True)
    embed.add_field(name="ATK:", value=characterAttributes["ssr_scottie"][1], inline=True)
    embed.add_field(name="DEF:", value=characterAttributes["ssr_scottie"][2], inline=True)
    embed.add_field(name="EVA:", value=characterAttributes["ssr_scottie"][3], inline=True)
    embed.add_field(name="ACC:", value=characterAttributes["ssr_scottie"][4], inline=True)
    embed.add_field(name=characterAttributes["ssr_scottie"][5], value="Unique Property is that the attack is unaffected by accuracy debuffs and is guaranteed to connect, Low Damage and If used twice applies a doom mark", inline=False)
    embed.add_field(name=characterAttributes["ssr_scottie"][6], value="Debuff targets all enemies Reduces accuracy and damage for 3 turns Accuracy and damage reduction scale for the amount of doom marks an enemy has 15%+7.5(marks) for damage reduction 20%+5(marks) for accuracy Doom marks are consumed and removed upon use", inline=False)
    embed.add_field(name=characterAttributes["ssr_scottie"][7], value="Redirects enemies to attack Scottie for 2 turns Damage reduction 30% Each successfull attack landed on Scottie inflicts 1 doom mark to the assailant (If an enemy does a single strong hit only one mark will apply, but if an enemy does a barrage; the amount of marks will follow accordingly) 1x12=1 mark 3x4=3 marks If Scottie is to die during martyrdom the doom marks that were already applied will explode dealing major damage to enemies", inline=False)
    embed.add_field(name=characterAttributes["ssr_scottie"][8], value="Only usable after a minimum of 3 turns and if the total amount of doom makes on the field is 5 For 3 turns every enemy on the field will lose all sense of will and reason Causing a chance event for each turn applied 33% chance for an enemy to harm itself 33% chance for an enemy to attack on of its allies 33% chance for an enemy to lay motionless allowing all attack done to them be guaranteed to land", inline=False)
    return embed

def sssr_maxEmbed():
    embed = discord.Embed(title=characterTitles["sssr_max"], description="???", color=0x000000)
    embed.set_image(url=SSSR_MAX_GIF)
    embed.add_field(name="HP:", value=characterAttributes["sssr_max"][0], inline=True)
    embed.add_field(name="ATK:", value=characterAttributes["sssr_max"][1], inline=True)
    embed.add_field(name="DEF:", value=characterAttributes["sssr_max"][2], inline=True)
    embed.add_field(name="EVA:", value=characterAttributes["sssr_max"][3], inline=True)
    embed.add_field(name="ACC:", value=characterAttributes["sssr_max"][4], inline=True)
    embed.add_field(name=characterAttributes["sssr_max"][5], value="???", inline=False)
    embed.add_field(name=characterAttributes["sssr_max"][6], value="???", inline=False)
    embed.add_field(name=characterAttributes["sssr_max"][7], value="???", inline=False)
    embed.add_field(name=characterAttributes["sssr_max"][8], value="???", inline=False)
    embed.add_field(name="Lore:", value="An entity beyond comprehension. Its true nature is unknown.", inline=False)
    return embed


def roll_character(banner: str) -> str:
    # Define character pools by rarity

    # Roll for rarity (60% R, 29% SR, 11% SSR total)
    # Note: SSR pool has 3 chars, so each gets ~3.67% for 11% total
    # Adjusted to 1% per SSR = 3% total, with 60% R and 37% SR
    rarity_roll = random.random() * 100
    if banner == "standard":
        if rarity_roll < 1:
            # 1% chance for SSR
            return random.choice(ssrChar)
        elif rarity_roll < 30:
            # 29% chance for SR (1% to 30%)
            return random.choice(srChar)
        else:
            # 70% chance for R (30% to 100%)
            return random.choice(rChar)

    if banner == "special":
        if rarity_roll < 1:
            return random.choice(specialChar)
        elif rarity_roll < 30:
            return random.choice(srChar)
        else:
            return random.choice(rChar)

    return "Error"  # Example character


@bot.tree.command(name="roll")
@app_commands.choices(banner = [
    app_commands.Choice(name="standard", value="standard"),
    app_commands.Choice(name="special", value="special"),
])
async def roll(interaction: discord.Interaction, banner: app_commands.Choice[str], amount: int = None):
    """Pick a banner of: Standard or Special. Optionally specify amount to roll; otherwise roll all available."""

    if banner.name == "standard":
        user_data = inventory_collection.find_one({"user_id": interaction.user.id})
        if not user_data:
            await interaction.response.send_message("No inventory data found.")
            return

        rolls_available = user_data.get("rolls", 0)
        if rolls_available <= 0:
            await interaction.response.send_message("You do not have any rolls left for the **Standard** banner.")
            return

        # Determine how many rolls to perform
        if amount is None or amount <= 0:
            to_roll = rolls_available
        else:
            to_roll = min(amount, rolls_available)

        rolled_characters = []
        embed = discord.Embed(title=f"Standard Rolls: x{to_roll}", color=0x3f48cc)
        if amount is not None and amount > rolls_available:
            embed.description = f"Requested {amount}, using {rolls_available} available."

        for _ in range(to_roll):
            rolled_character = roll_character("standard")
            rolled_characters.append(rolled_character)
            inventory_collection.update_one(
                {"user_id": interaction.user.id},
                {"$inc": {f"inventory.{rolled_character}": 1}},
            )

        # Decrement only the number of rolls used
        inventory_collection.update_one(
            {"user_id": interaction.user.id},
            {"$inc": {"rolls": -to_roll}},
        )

        # Group results by rarity
        ssr_rolled = [char for char in rolled_characters if char in ssrChar]
        sr_rolled = [char for char in rolled_characters if char in srChar]
        r_rolled = [char for char in rolled_characters if char in rChar]

        def format_group(chars):
            if not chars:
                return None
            counts = Counter(chars)
            lines = []
            for char, cnt in counts.items():
                title = characterTitles.get(char, char)
                lines.append(f"**{title}** +{cnt}")
            return "\n".join(lines)

        ssr_text = format_group(ssr_rolled)
        sr_text = format_group(sr_rolled)
        r_text = format_group(r_rolled)

        if ssr_text:
            embed.add_field(name="SSR Characters:", value=ssr_text, inline=False)
        if sr_text:
            embed.add_field(name="SR Characters:", value=sr_text, inline=False)
        if r_text:
            embed.add_field(name="R Characters:", value=r_text, inline=False)

        await interaction.response.send_message(embed=embed)

    elif banner.name == "special":
        # Special banner logic
        user_data = inventory_collection.find_one({"user_id": interaction.user.id})
        if not user_data:
            await interaction.response.send_message("No inventory data found.")
            return
        rolls_available = user_data.get("rolls", 0)
        if rolls_available <= 0:
            await interaction.response.send_message("You do not have any rolls left for the **Special** banner.")
            return
        # swtich SSR with specialChar
        if amount is None or amount <= 0:
            to_roll = rolls_available
        else:
            to_roll = min(amount, rolls_available)
        rolled_characters = []
        embed = discord.Embed(title=f"Special Rolls: x{to_roll}", color=0x3f48cc)
        if amount is not None and amount > rolls_available:
            embed.description = f"Requested {amount}, using {rolls_available} available."
        for _ in range(to_roll):
            rolled_character = roll_character("special")
            rolled_characters.append(rolled_character)
            inventory_collection.update_one(
                {"user_id": interaction.user.id},
                {"$inc": {f"inventory.{rolled_character}": 1}},
            )
        # Decrement only the number of rolls used
        inventory_collection.update_one(
            {"user_id": interaction.user.id},
            {"$inc": {"rolls": -to_roll}},
        )
        # Group results by rarity
        special_rolled = [char for char in rolled_characters if char in specialChar]
        sr_rolled = [char for char in rolled_characters if char in srChar]
        r_rolled = [char for char in rolled_characters if char in rChar]
        def format_group(chars):
            if not chars:
                return None
            counts = Counter(chars)
            lines = []
            for char, cnt in counts.items():
                title = characterTitles.get(char, char)
                lines.append(f"**{title}** +{cnt}")
            return "\n".join(lines)
        special_text = format_group(special_rolled)
        sr_text = format_group(sr_rolled)
        r_text = format_group(r_rolled)
        if special_text:
            embed.add_field(name="Special Characters:", value=special_text, inline=False)
        if sr_text:
            embed.add_field(name="SR Characters:", value=sr_text, inline=False)
        if r_text:
            embed.add_field(name="R Characters:", value=r_text, inline=False)

        await interaction.response.send_message(embed=embed)
    else:
        await interaction.response.send_message("Please select a Banner to roll from!")

@bot.tree.command()
async def inventory(ctx):
    """Show Inventory"""
    # display inventory in some cool way maybe like how maki does and have buttons to flip through pages
    user_data = inventory_collection.find_one({"user_id": ctx.user.id})
    if user_data:
        rolls = user_data.get("rolls", 0)
        inventory = user_data.get("inventory", {})

      #  special_inventory = {char: count for char, count in inventory.items() if char in specialChar}
        ssr_inventory = {char: count for char, count in inventory.items() if char in ssrChar or char in specialChar}
        sr_inventory = {char: count for char, count in inventory.items() if char in srChar}
        r_inventory = {char: count for char, count in inventory.items() if char in rChar}

        embed = discord.Embed(title=f"{ctx.user.display_name}'s Inventory", color=0x3f48cc)

     #   if special_inventory:
      #      embed.add_field(name="Special Characters:", value="\n".join([f"{characterTitles[char]}: {count}" for char, count in special_inventory.items()]), inline=False)
        if ssr_inventory:
            embed.add_field(name="SSR Characters:", value="\n".join([f"{characterTitles[char]}: {count}" for char, count in ssr_inventory.items()]), inline=False)

        if sr_inventory:
            embed.add_field(name="SR Characters:", value="\n".join([f"{characterTitles[char]}: {count}" for char, count in sr_inventory.items()]), inline=False)
        if r_inventory:
            embed.add_field(name="R Characters:", value="\n".join([f"{characterTitles[char]}: {count}" for char, count in r_inventory.items()]), inline=False)

        embed.add_field(name="Rolls:", value=str(rolls), inline=False)
        embed.add_field(name="Points Needed for Next Roll:", value=str(10 - user_data.get("counter", 0)), inline=False)

        await ctx.response.send_message(embed=embed)
    else:
        await ctx.response.send_message(f"{ctx.user.mention} No inventory data found.")

# Ephemeral Message
@bot.tree.command()
@app_commands.choices(character_name=character_choices)
async def char(interaction: discord.Interaction, character_name: app_commands.Choice[str]):
    """Show Character Info"""
    yesMax = False
    # Get the character dev name from the choice value
    char_dev_name = character_name.value

    # Check if user owns the character
    user_data = inventory_collection.find_one({"user_id": interaction.user.id})
    if user_data:
        inventory = user_data.get("inventory", {})
        if inventory.get(char_dev_name, 0) < 1:
            # if sssr_max then continue even if user does not own
            if char_dev_name == "sssr_max":
                pass
            else:
                await interaction.response.defer()
                await interaction.followup.send(file=discord.File(otherImages["no_own_png"]))
                return
    else:
        await interaction.followup.send("No inventory data found.")
        return

    if char_dev_name == "sssr_max":
        await interaction.response.defer()
    else:
        await interaction.response.defer(ephemeral=True)

    # The message below will be hidden from other users.
    if char_dev_name == "r_abraize":
        embed = r_abraizeEmbed()
    elif char_dev_name == "r_abraize2":
        embed = r_abraize2Embed()
    elif char_dev_name == "sr_abraize":
        embed = sr_abraizeEmbed()
    elif char_dev_name == "ssr_abraize":
        embed = ssr_abraizeEmbed()
    elif char_dev_name == "r_trey":
        embed = r_treyEmbed()
    elif char_dev_name == "sr_trey":
        embed = sr_treyEmbed()
    elif char_dev_name == "ssr_trey":
        embed = ssr_treyEmbed()
    elif char_dev_name == "r_noah":
        embed = r_noahEmbed()
    elif char_dev_name == "r_freeman":
        embed = r_freemanEmbed()
    elif char_dev_name == "sr_freeman":
        embed = sr_freemanEmbed()
    elif char_dev_name == "ssr_jayden":
        embed = ssr_jaydenEmbed()
    elif char_dev_name == "r_stephen":
        embed = r_stephenEmbed()
    elif char_dev_name == "sr_stephen":
        embed = sr_stephenEmbed()
    elif char_dev_name == "sr_homestuck":
        embed = sr_homestuckEmbed()
    elif char_dev_name == "ssr_scottie":
        embed = ssr_scottieEmbed()
    elif char_dev_name == "sssr_max":
        embed = sssr_maxEmbed()
        yesMax = True
    else:
        await interaction.followup.send(f"Character **{char_dev_name}** does not exist!")
        return

    await interaction.followup.send(embed=embed)
    if yesMax:
        time.sleep(2)
        await interaction.delete_original_response()


class View(discord.ui.View):
    @discord.ui.button(label="Yes", style=discord.ButtonStyle.green, custom_id="yes_button", emoji="♻️")
    async def yes_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()

    @discord.ui.button(label="No", style=discord.ButtonStyle.red, custom_id="no_button", emoji="🥺")
    async def no_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()

#Recycle Command
@bot.tree.command()
@app_commands.choices(character_name=character_choices)
async def recycle(ctx: discord.Interaction, character_name: app_commands.Choice[str], amount: int):
    # SSR = 100 points to counter, SR = 5 points to counter, R = 1 point to counter
    # 10 r's for 1 roll, 2 sr for 2 rolls and 1 ssr for 10 rolls
    # if counter = 10 inside mongodb per user then give 1 roll otherwise update and tell user to recycle more
    """Recycle Characters for Rolls"""
    # Example: /recycle r_abraize 10
    # then show embed saying "Would you like to recycle" [character_name] x [amount], "you will gain [calculated rolls] rolls" (calculated rolls may be in decimal format for example if they recycle 15 r's then it will say 1.5 rolls)

    # Get the character dev name from the choice value
    char_dev_name = character_name.value
    char_title = character_name.name

    user_data = inventory_collection.find_one({"user_id": ctx.user.id})
    if user_data:
        inventory = user_data.get("inventory", {})
        char_count = inventory.get(char_dev_name, 0)

        # Check if user owns the character
        if char_count < 1:
            if char_dev_name == "sssr_max":
                embed = discord.Embed(title="You Can't Recycle What You Don't Know", color=0x000000)
                await ctx.response.send_message(embed=embed)
                time.sleep(2)
                await ctx.delete_original_response()
                return
            await interaction.response.defer()
            await interaction.followup.send(file=discord.File(otherImages["no_own_png"]))
            return

        if char_count >= amount:
            # Determine points based on character rarity
            if char_dev_name in ssrChar:
                points = 100 * amount
            elif char_dev_name in srChar:
                points = 5 * amount
            elif char_dev_name in rChar:
                points = 1 * amount
            else:
                await ctx.response.send_message(f"Character **{char_title}** does not exist!")
                return

            # Calculate rolls to add
            # rolls to add must be integer never float
            current_points = user_data.get("counter", 0)
            total_points = current_points + points
            rolls_to_add = total_points // 10  # 10 points = 1 roll

            # embed awaiting user confirmation by button click yes or no to recycle or not
            embed = discord.Embed(title=f"Would you like to recycle {char_title} x {amount}? ", color=0x3f48cc)
            await ctx.response.send_message(embed=embed, view=View())

            # if view is custom id of yes button then proceed with recycling
            def check(interaction: discord.Interaction):
                return interaction.user.id == ctx.user.id and interaction.data["custom_id"] in ["yes_button", "no_button"]
            try:
                interaction = await bot.wait_for("interaction", check=check, timeout=10.0)

                if interaction.data["custom_id"] == "yes_button":
                    # Proceed with recycling
                    # Counter examples: if points = 20 then add 2 rolls and counter = 0, if points = 15 then add 1 roll and counter = 5, if points = 7 then add 0 rolls and counter = 7
                    # if points = 5 and they recycled 1 sr which is 5 points then add 1 roll and set coutner to 0
                    # Remove full tens from the counter and convert them into rolls
                    new_total = current_points + points
                    rolls_gain = new_total // 10
                    new_counter = new_total % 10

                    inventory_collection.update_one(
                        {"user_id": ctx.user.id},
                        {
                            "$inc": {
                                f"inventory.{char_dev_name}": -amount,
                                "rolls": rolls_gain
                            },
                            "$set": {
                                "counter": new_counter
                            }
                        }
                    )

                    # if character count goes to 0 then remove character from inventory
                    updated_user_data = inventory_collection.find_one({"user_id": ctx.user.id})
                    updated_inventory = updated_user_data.get("inventory", {})
                    if updated_inventory.get(char_dev_name, 0) == 0:
                        inventory_collection.update_one(
                            {"user_id": ctx.user.id},
                            {"$unset": {f"inventory.{char_dev_name}": ""}}
                        )
                   # user_data = inventory_collection.find_one({"user_id": ctx.user.id})


                  #  if rolls_to_add == 0:
                    embed = discord.Embed(title=f"Recycled **{char_title} x{amount}**. Your total rolls is **{rolls_gain + user_data.get('rolls', 0)}** rolls.", color=0x3f48cc)
                    embed.set_image(url=otherImages["recycle_gif"])
                    await ctx.followup.send(embed=embed)
                else:  # no_button pressed
                    await ctx.followup.send("Recycling cancelled.")
            except asyncio.TimeoutError:
                await ctx.followup.send("Recycling timed out. Please try again.")


        else:
            await ctx.response.send_message(f"You do not have enough **{char_title}'s** to recycle **x{amount}**. You currently have **x{char_count}**.")
    else:
        await ctx.response.send_message(f"{ctx.user.mention} No inventory data found. Please contact an Admin immediately.")

@bot.tree.command()
async def viewteam(ctx: discord.Interaction):
    """View your Team of maximum 4 Characters"""
    user_data = inventory_collection.find_one({"user_id": ctx.user.id})
    if user_data:
        team = user_data.get("team", [])
        if team:
            embed = discord.Embed(title=f"{ctx.user.display_name}'s Team", color=0x3f48cc)
            team_titles = [characterTitles.get(char, char) for char in team]
            for i, title in enumerate(team_titles, 1):
                embed.add_field(name=f"Slot {i}", value=title, inline=False)
            await ctx.response.send_message(embed=embed)
        else:
            embed = discord.Embed(title="No Team Set", description="You have not set a team yet. Use the /team command to set your team of 4 characters.", color=0x3f48cc)
            await ctx.response.send_message(embed=embed)
    else:
        embed = discord.Embed(title="Error", description=f"{ctx.user.mention} No inventory data found.", color=0xff0000)
        await ctx.response.send_message(embed=embed)

# there cannot be 2 of the same character for example /team r_abraize r_abraize r_noah r_freeman is invalid and /team r_abraize sr_abraize r_noah r_freeman is invalid
@bot.tree.command()
@app_commands.choices(
    char1=character_choices,
    char2=character_choices,
    char3=character_choices,
    char4=character_choices
)
async def team(ctx: discord.Interaction, char1: app_commands.Choice[str] = None, char2: app_commands.Choice[str] = None, char3: app_commands.Choice[str] = None, char4: app_commands.Choice[str] = None):
    """Set your Team of maximum 4 Characters"""
    team_choices = [c for c in [char1, char2, char3, char4] if c]

    if not team_choices:
        await ctx.response.send_message("Please provide at least one character to add to your team.")
        return

    # Convert choices to dev names
    team_chars = [c.value for c in team_choices]
    team_titles = [c.name for c in team_choices]

    # Check for duplicates
    if len(team_chars) != len(set(team_chars)):
        await ctx.response.send_message("You cannot have duplicate characters in your team!")
        return

    # cannot have 2 versions of the same character for example r_abraize and ssr_abraize
    base_names = set()
    for char in team_chars:
        parts = char.split('_', 1)
        base_name = parts[1] if len(parts) > 1 else char
        if base_name in base_names:
            await ctx.response.send_message(f"You cannot have multiple versions of the same character in your team! **({base_name})**")
            return
        base_names.add(base_name)

    # Check if user owns the characters
    user_data = inventory_collection.find_one({"user_id": ctx.user.id})
    if user_data:
        inventory = user_data.get("inventory", {})
        for i, char in enumerate(team_chars):
            if inventory.get(char, 0) < 1:
                if char == "sssr_max":
                    embed = discord.Embed(title="Is It On Your Team?", color=0x000000)
                    await ctx.response.send_message(embed=embed)
                    time.sleep(2)
                    await ctx.delete_original_response()
                    return
                await ctx.response.defer()
                await ctx.followup.send(file=discord.File(otherImages["no_own_png"]))
                return

    # Update team in database
    inventory_collection.update_one(
        {"user_id": ctx.user.id},
        {"$set": {"team": team_chars}}
    )

    # show titles of characters in team
    await ctx.response.send_message("Team Updated Successfully! Your team order is:\n" + "\n".join(team_titles))

# ============================================================================
# CHARACTER ABILITIES MAPPING
# ============================================================================
# Maps character names to their abilities (skills 1, 2, 3, and optional ultimate)
# Format: character_name: [skill1, skill2, skill3] or [skill1, skill2, skill3, ultimate]

# Battle Command - PvE
# The battle screen has 8 total slots, 4 for the player's team and 4 for the enemy team (enemy team does not have to fill all 4 slots)
# There are multiple enemy types to fight
# Currently: Ruffian, Grunt, Spearman, Agent
# There will be multiple backgrounds to choose from but currently will be randomly decided
# Using Pillow (PIL) we will create a battle screen image that shows the player's team on the right and the enemy team on the left with background

# ============================================================================
# DYNAMIC CHARACTER POSITIONING SYSTEM
# ============================================================================
#
# This system ensures characters are properly placed on the battle screen
# based on their "feet" position, preventing cutoff issues.
#
# HOW TO ADD A NEW CHARACTER:
# 1. Add the character's PNG file to the repository
# 2. Add an entry to characterImages dictionary (already done for most)
# 3. Calculate the character's feet position:
#    - Open the character image
#    - Find the width and height (e.g., using PIL: Image.open("char.png").size)
#    - Default feet position is (width/2, height) - bottom-middle of image
#    - Add entry to characterFeet dictionary below
# 4. If the character floats, add an entry to characterFloatingOffset
#    - Use negative values to move up (floating)
#    - Use positive values to move down
#
# HOW TO FINE-TUNE CHARACTER POSITIONING:
# 1. Run the battle command and examine the output
# 2. If a character's feet don't align properly:
#    - Adjust the X coordinate in characterFeet to shift left/right
#    - Adjust the Y coordinate in characterFeet to change where feet are
# 3. If a character should float or sink:
#    - Add/modify entry in characterFloatingOffset
#
# EXAMPLE:
# For a character image that is 100x200 pixels:
# - Default feet position would be (50, 200) - center bottom
# - If feet are actually 10 pixels from the left: use (10, 200)
# - If character should float 15 pixels up: add to characterFloatingOffset with value -15
# ============================================================================

# Character "feet" positions - where the character's feet/bottom-middle are located within their sprite
# Format: (x_offset_from_left, y_offset_from_top)
# By default, feet are at (width/2, height), but can be adjusted manually for fine-tuning
characterFeet = {
    "r_abraize": (53, 252),
    "r_abraize2": (57, 226),
    "sr_abraize": (70, 209),
    "ssr_abraize": (87, 235),
    "r_trey": (52, 247),
    "sr_trey": (68, 263),
    "ssr_trey": (72, 291),
    "r_noah": (39, 214),
    "r_freeman": (49, 241),
    "sr_freeman": (57, 206),
    "ssr_jayden": (56, 278),
    "r_stephen": (52, 215),
    "sr_stephen": (72, 222),
    "sr_homestuck": (117, 228),
    "ssr_scottie": (55, 283),
}

# Special Y-axis adjustments for floating characters
# Negative values move character UP (floating effect)
# Positive values move character DOWN (sinking effect)
characterFloatingOffset = {
    "ssr_scottie": -20,  # Floating character - moves up 20 pixels
}

# Target ground positions for team slots on the battle screen
# These are the positions where character feet should be placed
# Format: (x, y) - coordinates on the background where feet touch the ground
# Note: These use 0-based indexing (slot_index 0-3 in code)
teamSlotGroundPositions = [
    (470, 450),  # Index 0 (Slot 1 in /viewteam) - Down
    (360, 380),  # Index 1 (Slot 2 in /viewteam) - Left
    (580, 360),  # Index 2 (Slot 3 in /viewteam) - Right
    (440, 340),  # Index 3 (Slot 4 in /viewteam) - Up
]

def calculate_character_position(char_name, slot_index, background_size):
    """
    Calculate the paste position for a character based on their feet position.

    Args:
        char_name: Character identifier (e.g., "r_abraize")
        slot_index: Team slot index (0-3)
        background_size: Tuple of (width, height) of the background image

    Returns:
        Tuple of (x, y) coordinates where the character image should be pasted
    """
    # Get the target ground position for this slot
    target_x, target_y = teamSlotGroundPositions[slot_index]

    # Get the character's feet position within their sprite
    # If not defined, calculate default position from the image
    if char_name not in characterFeet:
        char_image_path = characterImages.get(char_name)
        if char_image_path and os.path.exists(char_image_path):
            char_img = Image.open(char_image_path)
            char_width, char_height = char_img.size
            # Default: bottom-middle of the image
            feet_x, feet_y = char_width // 2, char_height
        else:
            # Fallback if image doesn't exist
            feet_x, feet_y = 0, 0
    else:
        feet_x, feet_y = characterFeet[char_name]

    # Calculate where to paste the character so their feet align with the target
    paste_x = target_x - feet_x
    paste_y = target_y - feet_y

    # Apply floating offset if this character is a floater
    floating_offset = characterFloatingOffset.get(char_name, 0)
    paste_y += floating_offset

    # Prevent cutoff on the edges
    char_image_path = characterImages.get(char_name)
    if char_image_path and os.path.exists(char_image_path):
        char_img = Image.open(char_image_path)
        char_width, char_height = char_img.size

        # Ensure character doesn't go off the right edge
        if paste_x + char_width > background_size[0]:
            paste_x = background_size[0] - char_width

        # Ensure character doesn't go off the bottom edge
        if paste_y + char_height > background_size[1]:
            paste_y = background_size[1] - char_height

        # Ensure character doesn't go off the left edge
        if paste_x < 0:
            paste_x = 0

        # Ensure character doesn't go off the top edge
        if paste_y < 0:
            paste_y = 0

    return (int(paste_x), int(paste_y))

# ============================================================================
# BATTLE EMBED + BUTTONS
# ============================================================================
# battle.py does all of the battle logic, this part only shows it to the user:
#   - the embed shows everyone's hp, their buffs/debuffs and the battle log (updated after every turn)
#   - the buttons are the current character's abilities, target buttons (Options F / G) and Retreat

BATTLE_TIMEOUT = 300  # seconds without a button press before the battle ends by itself

# reason numbers for endBattle() in battle.py
BATTLE_END_REASONS = {"retreat": 0, "defeat": 1, "victory": 2, "timeout": 3, "error": 4}

# text + embed color for every way a battle can end
BATTLE_ENDINGS = {
    "victory": ("🏆 **Victory!** Your team won the battle!", 0x2ecc71),
    "defeat": ("☠️ **Defeat...** Your whole team got knocked out.", 0xe74c3c),
    "retreat": ("🏳️ You retreated from the battle!", 0x95a5a6),
    "timeout": ("⌛ The battle ended because no buttons were pressed for 5 minutes.", 0x95a5a6),
    "error": ("⚠️ Something went wrong so the battle was ended. The error is in the bot console.", 0xe74c3c),
}


def hp_bar(hp, max_hp, length=10):
    """Text hp bar like ██████░░░░"""
    filled = round(length * hp / max_hp) if max_hp > 0 else 0
    if hp > 0:
        filled = max(1, filled)  # never looks empty while still standing
    return "█" * filled + "░" * (length - filled)


def format_battle_units(rows):
    """One line per character with their hp bar, plus a line under it for their buffs/debuffs."""
    lines = []
    for row in rows:
        if not row["alive"]:
            lines.append(f"~~{row['name']}~~ 💀")
            continue
        marker = "▶ " if row["current"] else ""
        lines.append(f"{marker}**{row['name']}** `{hp_bar(row['hp'], row['maxHp'])}` {row['hp']}/{row['maxHp']}")
        if row["effects"]:
            effects = row["effects"] if len(row["effects"]) <= 150 else row["effects"][:147] + "..."
            lines.append(f"   ↳ {effects}")
    return "\n".join(lines)[:1024] or "\u200b"


def newest_lines(lines, limit=1024):
    """Embed fields can only hold 1024 characters, so keep the newest log lines that fit."""
    kept, size = [], 0
    for line in reversed(lines):
        if len(line) > limit:
            line = line[:limit - 3] + "..."
        if size + len(line) + 1 > limit:
            break
        kept.append(line)
        size += len(line) + 1
    return "\n".join(reversed(kept)) or "\u200b"


def build_battle_embed(user_id, enemy_name, prompt=None, ending=None):
    """The battle embed: whose turn it is, hp of both teams, the battle log and the battle screen image."""
    summary = getBattleSummary(user_id)
    embed = discord.Embed(title=f"⚔️ Battle vs {enemy_name} — Round {summary['round']}", color=0x3f48cc)
    if ending:
        embed.description, embed.colour = BATTLE_ENDINGS[ending]
    else:
        embed.description = prompt or f"It's **{summary['turn']}**'s turn, pick an ability!"
    embed.add_field(name="Your Team", value=format_battle_units(summary["players"]), inline=False)
    enemies_text = format_battle_units(summary["enemies"])
    if summary["field"]:
        enemies_text = (enemies_text + "\n" + summary["field"])[:1024]
    embed.add_field(name="Enemies", value=enemies_text, inline=False)
    embed.add_field(name="Battle Log", value=newest_lines(summary["log"]), inline=False)
    # the image is already attached to the message, pointing at it again keeps it inside the embed after edits
    embed.set_image(url=f"attachment://battle_screen_{user_id}.png")
    embed.set_footer(text="(2t) = turns left • The battle ends after 5 minutes without a button press")
    return embed


# it seems that you need to have a "view" to allow buttons
class BattleView(discord.ui.View):
    """Buttons for one battle. They get rebuilt every turn from what battle.py says the current character can do."""

    def __init__(self, user_id: int, enemy_name: str):
        super().__init__(timeout=BATTLE_TIMEOUT)
        self.user_id = user_id
        self.enemy_name = enemy_name
        self.last_interaction = None  # newest interaction on this battle, used to edit the message if the battle times out
        self.layout = 0               # goes up every time the buttons change so clicks on old buttons get ignored
        self.show_ability_buttons()

    def show_ability_buttons(self):
        """Row 1: the current character's abilities (greyed out while on cooldown), row 2: Retreat."""
        self.layout += 1
        self.clear_items()
        for index, ability in enumerate(getAbilityButtons(self.user_id)):
            label = ability["name"] if ability["ready"] else f"{ability['name']} ({ability['note']})"
            button = discord.ui.Button(label=label[:80], style=discord.ButtonStyle.primary, disabled=not ability["ready"], row=0)
            button.callback = self.ability_pressed(index, self.layout)
            self.add_item(button)
        self.add_retreat_button()

    def show_target_buttons(self, ability_index, targets):
        """Options F / G: one button per possible target, plus Back and Retreat."""
        self.layout += 1
        self.clear_items()
        for unit, name in targets:
            button = discord.ui.Button(label=name[:80], style=discord.ButtonStyle.success, row=0)
            button.callback = self.target_pressed(ability_index, unit, self.layout)
            self.add_item(button)
        back = discord.ui.Button(label="Back", style=discord.ButtonStyle.secondary, row=1)
        back.callback = self.back_pressed(self.layout)
        self.add_item(back)
        self.add_retreat_button()

    def add_retreat_button(self):
        retreat = discord.ui.Button(label="Retreat", style=discord.ButtonStyle.danger, row=1)
        retreat.callback = self.retreat_pressed
        self.add_item(retreat)

    async def check_press(self, interaction: discord.Interaction, layout=None):
        """Only the person battling can press the buttons, and only the newest ones."""
        if interaction.user.id != self.user_id:
            await interaction.response.send_message("This is not your battle!", ephemeral=True)
            return False
        if not battleExists(self.user_id) or (layout is not None and layout != self.layout):
            await interaction.response.send_message("Those buttons are out of date!", ephemeral=True)
            return False
        self.last_interaction = interaction
        return True

    def ability_pressed(self, ability_index, layout):
        async def callback(interaction: discord.Interaction):
            if not await self.check_press(interaction, layout):
                return
            # moves with Option F / G need a target picked first when there is more than 1 choice
            targets = getTargetChoices(self.user_id, ability_index)
            if targets:
                ability_name = getAbilityButtons(self.user_id)[ability_index]["name"]
                self.show_target_buttons(ability_index, targets)
                embed = build_battle_embed(self.user_id, self.enemy_name, prompt=f"Who should **{ability_name}** target?")
                await interaction.response.edit_message(embed=embed, view=self)
                return
            await self.take_turn(interaction, ability_index, None)
        return callback

    def target_pressed(self, ability_index, target, layout):
        async def callback(interaction: discord.Interaction):
            if not await self.check_press(interaction, layout):
                return
            await self.take_turn(interaction, ability_index, target)
        return callback

    def back_pressed(self, layout):
        async def callback(interaction: discord.Interaction):
            if not await self.check_press(interaction, layout):
                return
            self.show_ability_buttons()
            await interaction.response.edit_message(embed=build_battle_embed(self.user_id, self.enemy_name), view=self)
        return callback

    async def retreat_pressed(self, interaction: discord.Interaction):
        """Retreat button to end the battle."""
        if not await self.check_press(interaction):
            return
        await self.finish(interaction, "retreat")

    async def take_turn(self, interaction, ability_index, target):
        # battle.py does the move, then the rest of the turn order (enemy turn + end of round included)
        advanceBattle(self.user_id, ability_index, target)
        result = getBattleResult(self.user_id)
        if result:
            await self.finish(interaction, result)
            return
        self.show_ability_buttons()
        await interaction.response.edit_message(embed=build_battle_embed(self.user_id, self.enemy_name), view=self)

    async def finish(self, interaction, ending):
        embed = build_battle_embed(self.user_id, self.enemy_name, ending=ending)  # before battle.py throws the battle away
        self.end_battle(ending)
        await interaction.response.edit_message(embed=embed, view=self)

    def end_battle(self, ending):
        """Cleans up the battle in battle.py, sets inBattle back to false and disables every button."""
        if battleExists(self.user_id):
            endBattle(self.user_id, BATTLE_END_REASONS[ending])
        # set in mongodb battle over
        inventory_collection.update_one(
            {"user_id": self.user_id},
            {"$set": {"inBattle": False}}
        )
        for item in self.children:
            item.disabled = True
        self.stop()

    async def on_timeout(self):
        if not battleExists(self.user_id):
            return
        embed = build_battle_embed(self.user_id, self.enemy_name, ending="timeout")
        self.end_battle("timeout")
        if self.last_interaction:
            try:
                await self.last_interaction.edit_original_response(embed=embed, view=self)
            except discord.HTTPException as error:
                print("Could not update the timed out battle message:", error)

    async def on_error(self, interaction: discord.Interaction, error: Exception, item):
        # a bug in the battle code ends the battle instead of leaving the user stuck "in battle"
        print(f"Battle error for user {self.user_id}:")
        traceback.print_exception(type(error), error, error.__traceback__)
        embed = None
        if battleExists(self.user_id):
            try:
                embed = build_battle_embed(self.user_id, self.enemy_name, ending="error")
            except Exception:
                embed = None
        self.end_battle("error")
        try:
            if interaction.response.is_done():
                await interaction.followup.send(BATTLE_ENDINGS["error"][0], ephemeral=True)
            elif embed:
                await interaction.response.edit_message(embed=embed, view=self)
            else:
                await interaction.response.edit_message(content=BATTLE_ENDINGS["error"][0], view=self)
        except discord.HTTPException:
            pass


@bot.tree.command(name = "battle")
@app_commands.choices(enemies=[
    app_commands.Choice(name="Ruffian", value="Ruffian"),
    app_commands.Choice(name="Grunt", value="Grunt"),
    app_commands.Choice(name="Spearman", value="Spearman"),
    app_commands.Choice(name="Agent", value="Agent"),
    app_commands.Choice(name="Jack Noir", value="Jack Noir"),
])
async def battle(interaction: discord.Interaction,enemies:app_commands.Choice[str]):
    """Battle an Enemy"""
    # Get user's team
    user_data = inventory_collection.find_one({"user_id": interaction.user.id})
    if not user_data:
        await interaction.response.send_message(f"{interaction.user.mention} No inventory data found. Please contact an Admin immediately.")
        return

    # Check if user is already in a battle
    if user_data.get("inBattle", False):
        await interaction.response.send_message("You are already in a battle! Please finish your current battle before starting a new one.", ephemeral=True)
        return

    team = user_data.get("team", [])
    if len(team) < 1:
        await interaction.response.send_message("You are not ready to fight!\nSet a team first using the /team command otherwise you will perish!")
        return

    # get a random background from the backgrounds hashmap
    background_name, background_file = random.choice(list(backgrounds.items()))

    # comnbine background and sprite images ontop one another using PIL
    background_image = Image.open(background_file)
    background_size = background_image.size

    # Place enemies first (in the background layer)
    enemy_count = 1  # Default to 1 enemy
    enemyList = []

    if enemies.name == "Grunt":
        enemy_image = Image.open(enemyImages[enemies.name])
        background_image.paste(enemy_image, enemySpots[enemies.name], enemy_image)
        enemyList.append(enemies.name)
    elif enemies.name == "Ruffian":
        # 50/50 if 2 or 1 ruffians show up
        roll = random.random()
        if roll < 0.5:
            enemy_count = 2
            ruffianB = Image.open(enemyImages["RuffianBack"])
            ruffianF = Image.open(enemyImages["RuffianFront"])
            background_image.paste(ruffianB, enemySpots["RuffianBack"], ruffianB)
            background_image.paste(ruffianF, enemySpots["RuffianFront"], ruffianF)
            for i in range(enemy_count):
                enemyList.append(f"Ruffian{i+1}")
        else:
            ruffianB = Image.open(enemyImages["RuffianBack"])
            background_image.paste(ruffianB, enemySpots["RuffianSolo"], ruffianB)
            enemyList.append("Ruffian1")
    else:
        enemy_image = Image.open(enemyImages[enemies.name])
        background_image.paste(enemy_image, enemySpots[enemies.name], enemy_image)
        enemyList.append(enemies.name)

    for a in enemyList:
        print("ENEMY IN LIST:", a)

    # Place team characters dynamically based on their feet positions
    # Reverse order so slot 1 (index 0) is pasted last and appears on top
    for i, char_name in reversed(list(enumerate(team))):
        if char_name in characterImages:
            char_image_path = characterImages[char_name]
            if os.path.exists(char_image_path):
                char_image = Image.open(char_image_path)
                char_position = calculate_character_position(char_name, i, background_size)
                background_image.paste(char_image, char_position, char_image)

    # save the combined image to a new file
    # save to new file based on discord id, example: battle_screen_123456789.png
    combined_image_path = f"./graphics/battle/battle_screen_{interaction.user.id}.png"
    background_image.save(combined_image_path)

    # battle.py sets up the turn order, hp and abilities for this user's battle
    startBattle(interaction.user.id, team, enemyList)
    # set inbattle in mongodb
    inventory_collection.update_one(
        {"user_id": interaction.user.id},
        {"$set": {"inBattle": True}}
    )

    enemy_title = enemies.name if len(enemyList) == 1 else f"{len(enemyList)} {enemies.name}s"
    battle_view = BattleView(interaction.user.id, enemy_title)
    try:
        await interaction.response.send_message(file=discord.File(combined_image_path), embed=build_battle_embed(interaction.user.id, enemy_title), view=battle_view)
    except Exception:
        battle_view.end_battle("error")  # don't leave the user stuck "in battle" if the message never got sent
        raise
    battle_view.last_interaction = interaction


HELP_GIF_URL = "https://media.discordapp.net/attachments/796742546910871562/1442307872490000432/JITSTUCKMOBILEGAME.gif?ex=6926efa1&is=69259e21&hm=160f8b3552a36078f4941e02aafbb3408a95be77be4f5ffa6697ff3aacd53397&format=webp&animated=true"
@bot.tree.command(name="help")
async def help_command(ctx):
    """Show Help"""
    await ctx.response.send_message(HELP_GIF_URL)

@bot.tree.command(name="embedtest")
async def embed_test(ctx: discord.Interaction):
    """Test Embed"""
    embed = discord.Embed(
        title="Test Embed",
        description="This is a test embed. " + "x" * 400,  # Max description length
        color=0x00ff00,
        url="https://discord.com"
    )

    # Add maximum fields (25 is the limit)
    for i in range(1, 26):
        embed.add_field(
            name=f"Field {i}: " + "x" * 25,
            value="This is the value for field " + str(i) + ". " + "y" * 100,
            inline=False if i % 2 == 0 else True
        )

    embed.set_author(name="Author Name " + "z" * 20, url="https://discord.com", icon_url="https://cdn.discordapp.com/embed/avatars/0.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/embed/avatars/0.png")
    embed.set_image(url="https://cdn.discordapp.com/embed/avatars/0.png")
    embed.set_footer(text="This is a footer. " + "f" * 200, icon_url="https://cdn.discordapp.com/embed/avatars/0.png")

    # Add timestamp
    embed.timestamp = discord.utils.utcnow()

    await ctx.response.send_message(embed=embed)

@bot.command()
@commands.is_owner()  # Prevent other people from using the command
async def syncapp(ctx: commands.Context) -> None:
    """Sync app commands to Discord."""
    await ctx.bot.tree.sync()
    await ctx.send('Application commands synchronized!')



if __name__ == "__main__":
    bot.run(TOKEN)