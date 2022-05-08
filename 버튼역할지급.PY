import discord
from discord_components import DiscordComponents, Button, ButtonStyle, interaction


client = discord.Client()

token = 'OTcyNDg3OTA3OTYzMTgzMTg1.GobXHy.T0B9SFN2L6M4o0gxYvH41Qjif3jILye7awZgI4'

DiscordComponents(client)

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content == "!역할버튼":
        embed = discord.Embed(title='CS SHOP', description='인증을 하실려면 이 버튼을 눌러주세요')
        await message.channel.send(embed=embed, components=[[Button(label="역할받기", id="verify", style=ButtonStyle.gray)]])

@client.event
async def on_button_click(interaction: interaction):
    if interaction.component.custom_id == "verify":
        verify_role = '[USER]' #버튼을 누르면 줄 역할이름
        verifyrole = discord.utils.get(interaction.guild.roles, name=verify_role)
        if verifyrole in interaction.user.roles:
            await interaction.respond(content='이미 역할을 갖고계십니다')
            return
        await interaction.user.add_roles(verifyrole)
        await interaction.respond(content="역할이 지급되었습니다")



client.run(token)
