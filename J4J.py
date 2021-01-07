import re,requests,os
from discord.ext import commands
codeRegex = re.compile("(discord.gg/|discord.com/invite/|discord.com/)([a-zA-Z0-9]+)")
selectedmessage = "please may you now join my server , discord.gg/invitelinkherelol"
token = "token-here"


bot = commands.Bot(command_prefix="follow me on github - github.com/kieronia", self_bot=True)

print(" > Started Successfully")

joined = 0

while True:
    try:
        @bot.event
        async def on_message(ctx):
            global selectedmessage
            global joined
            message = ctx.content

            if codeRegex.search(message):
                server = codeRegex.search(message).group(2)
                if ctx.author.bot or ctx.author.id == bot.user.id:
                    print(" > Bot sent it - Ignoring")
                else:
                    print(f" > Server Found - discord.gg/{server}")
                    headers = {'Authorization': token, 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', 'Accept': '*/*',}
                    joining = requests.post(f"https://discord.com/api/v8/invites/{server}", headers=headers)
                    if joining.status_code == 200:
                        joined = joined + 1
                        os.system(f" title J4J Automator - [github.com/kieronia] - Joined {joined} Servers!")
                        print(f" > Joined discord.gg/{server}")
                        print(f" > Now messaging them the following:\n 1 I joined discord.gg/{server} \n 2 {selectedmessage}")
                        try:
                            await ctx.author.send(f"I joined discord.gg/{server}")
                            await ctx.author.send(selectedmessage)
                        except:
                            await ctx.send(f"{ctx.message.author.mention} I joined discord.gg/{server}")
                            await ctx.send(ctx.message.author.mention + selectedmessage)
                            
                    else:
                        print(f" > Could not join discord.gg/{server}")


        bot.run(token, bot=False)
    except:
        print(" > Error - Check the token is valid maybe?")
