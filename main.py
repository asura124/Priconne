import discord
from discord import app_commands
from discord.ext import commands
from decouple import config
import database_connector
from ButtonMenu import ButtonMenu
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from characters import characters


intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
mycursor = database_connector.mydb.cursor()

@client.event
async def on_ready():
    await tree.sync()
    print('We have logged in as {0.user}'.format(client))

@tree.command(name = 'character',description = "Enter an unit's name:")
@app_commands.describe(char_name='Char name')
async def unit_search(interaction, char_name:str):
    similarity, unit_name = 0,""
    for i in characters:
        temp = fuzz.token_sort_ratio(char_name,i)
        if(temp>similarity):
            similarity = temp
            unit_name = i
    version_name = unit_name
    similarity = fuzz.token_sort_ratio(char_name,version_name) + fuzz.ratio(char_name,version_name)
    for i in characters[unit_name]:
        temp = fuzz.token_sort_ratio(char_name,i) + fuzz.ratio(char_name,i)
        if(temp>similarity):
            similarity = temp
            version_name = i
    database_query = 'SELECT * from unit_info where unit_name="' + version_name + '";'
    mycursor.execute(database_query)
    result = mycursor.fetchall()
    all_embeds = []
    character_embed = discord.Embed(description = "The Numbers shown below are when they're lvl 268. \n For more information, Go [Here](https://docs.google.com/spreadsheets/d/1JjK7Ws4gfzKChRs5ueoxEZVN5SXK10nhDC1-nbm0NUs/edit#gid=1918232313)")
    character_embed.set_author(name=version_name)
    character_embed.add_field(name="UB",value = "\n\u200b",inline=False)
    if(result[0][2]=="None"):
        character_embed.set_thumbnail(url=result[0][1])
    else:
        character_embed.set_thumbnail(url=result[0][2])
    if(result[0][4]=="None"):
        character_embed.set_image(url=result[0][3])
    else:
        character_embed.set_image(url=result[0][4])
    if(result[0][7]=="None" and result[0][8]=="None"):
        character_embed.add_field(name=result[0][5],value=result[0][6],inline=False)
    else:
        character_embed.add_field(name=result[0][5]+'\n',value = result[0][6],inline=True)
        character_embed.add_field(name="Unlock at 6⭐️: \n" + result[0][7]+'\n',value = result[0][8],inline=True)
    character_embed.add_field(name="Skill 1",value = "\n\u200b",inline=False)
    if(result[0][11]=="None" and result[0][12]=="None"):
        character_embed.add_field(name=result[0][9],value=result[0][10],inline=False)
    else:
        character_embed.add_field(name=result[0][9]+'\n',value = result[0][10],inline=True)
        character_embed.add_field(name="Unlock after UE: \n" + result[0][11]+'\n',value = result[0][12],inline=True)
    character_embed.add_field(name="Skill 2",value = "\n\u200b",inline=False)
    character_embed.add_field(name=result[0][13],value = result[0][14],inline=False)
    character_embed.add_field(name="EX Skill",value = "\n\u200b",inline=False)
    character_embed.add_field(name=result[0][15],value=result[0][16],inline=False)
    all_embeds.append(character_embed)
    if(result[0][17]!="None" and result[0][18]!="None"):
        special_unique_skills = discord.Embed()
        special_unique_skills.set_author(name="Special/Unique/Hidden Skills")
        special_unique_skills.add_field(name=result[0][17],value=result[0][18],inline=True)
        if(result[0][19]!="None" and result[0][20]!="None"):
            special_unique_skills.add_field(name=result[0][19],value=result[0][20],inline=True)
        if(result[0][21]!="None" and result[0][22]!="None"):
            special_unique_skills.add_field(name=result[0][21],value=result[0][22],inline=False)
        if(result[0][23]!="None" and result[0][24]!="None"):
            special_unique_skills.add_field(name=result[0][23],value=result[0][24],inline=False)
        all_embeds.append(special_unique_skills)
    misc = discord.Embed()
    misc.set_author(name="MISC")
    misc.add_field(name="Initial movement: " ,value=result[0][-2],inline=False)
    misc.add_field(name="Loop pattern: ",value = result[0][-1],inline=False)
    all_embeds.append(misc)
    await interaction.response.send_message(embeds = [all_embeds[0]],view = ButtonMenu(all_embeds,60,interaction.user))


client.run(config('TOKEN'))
