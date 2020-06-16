import discord
import discord.ext.commands as commands

TOKEN = ""
CHANNEL = 0
MAIN_ROLE = 0
SUB_ROLE = 0
BOT_ROLE = 0
MAIN_EMOJI = ""
SUB_EMOJI = ""

bot = commands.Bot('}}')


@bot.event
async def on_ready():
    print("Ready")

    guild: discord.Guild = bot.guilds[0]
    channel: discord.TextChannel = guild.get_channel(CHANNEL)

    # Delete Messages
    messages = []
    async for message in channel.history():
        messages.append(message)

    await channel.delete_messages(messages)

    # Send Message
    embed = discord.Embed(title="**Welcome to our Server!**", colour=discord.Colour(0x4a90e2), description="Congratulations on joining our server, now there's one more thing you need to do before you're offically a member.\n\nOur Discord Server actually consists of 2 individual *sub-servers* rather than 1 main server.\n\n**To join a sub-server, you must click on of the reactions under this message.\nMake sure you click the correct one!**\n\n If you need help with anything on the server, DM <@528575736270028800> or <@670988528594976801>.\n\n*Thanks, Matt & Cameron*")
    embed.set_author(name="Server Bot", icon_url="https://lh3.googleusercontent.com/proxy/aYtZgrNm2LB5jhDFMCm1mINjHqWwJr1AZ4k0EbrXh2ybria7AFZxdORjZJ8S96vlz5upXuCwJxqUmWKbd5LD_H2sAQulwESDzz7W6EKc4_aOsDztFy0EnbfBn72kZnFUOVp2y7zPv7fAqCHRsVa8FixSCqAJEMjL7F1JwYVYVNAqUHiwt5qLrk510IejSw9YLPNjDtrPsw")
    embed.set_footer(text="Bot written by Matt French")
    await channel.send(embed=embed)

    # Add Reactions
    for emoji in guild.emojis:
        if emoji.name == MAIN_EMOJI:
            main_emoji = emoji

        elif emoji.name == SUB_EMOJI:
            sub_emoji = emoji

    async for in_msg in channel.history():  # Loop through messages
        message = in_msg                    # Get Latest Message

    await message.add_reaction(main_emoji)  # Add Reaction
    await message.add_reaction(sub_emoji)   # Add Reaction

    def check(*args):
        return True

    while True:
        reaction, user = await bot.wait_for('reaction_add', check=check)

        reaction: discord.Reaction = reaction
        user: discord.Member = user

        if not user.bot:    # Make sure we didn't get detected

            has_role = False
            for role in user.roles:
                if role.id == MAIN_ROLE or role.id == SUB_ROLE:
                    has_role = True

            if not has_role:   # Check they dont have a role
                # Lets add them
                if reaction.emoji.name == MAIN_EMOJI:
                    # Add them to the main server
                    await user.add_roles(guild.get_role(MAIN_ROLE))

                elif reaction.emoji.name == SUB_EMOJI:
                    # Add them to the sub server
                    await user.add_roles(guild.get_role(SUB_ROLE))


if __name__ == '__main__':
    bot.run(TOKEN)
