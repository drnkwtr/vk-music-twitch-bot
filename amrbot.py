#bot author drnkwtr
#vk.com/drnkwtr
#twitch.tv/drnkwtr
#forblitz.ru
#t.me/drnkwtr
#if u have any questions write me on VK pm (russian, english languages)

from twitchio.ext import commands
import vk_api
import vk

token_user = "WRITE HERE VK USER TOKEN (WITH STATUS ACCESS)" 

session = vk.Session(access_token=token_user)
vk_api = vk.API(session ,v='5.92', lang='ru')

bot_name='WRITE HERE BOT NAME (ANY)'
bot = commands.Bot(
    token="WRITE HERE TWITCH TOKEN", #https://twitchapps.com/tmi/
    nick='WRITE HERE ACCOUNT NICKNAME',
    prefix='!', #you can choose any prefix, now its !song
    initial_channels=['WRITE HERE CHANNEL NICKNAME']
)

@bot.command(name='song') #command name !song
async def test(ctx):
    status = vk_api.status.get(user_id=WRITE HERE USER ID) #only numbers after id e.g 19607100
    audio = status["text"]
    if audio != 'WRITE YOUR VK STATUS HERE OR STAY EMPTY': #empty means like audio != ''
        await ctx.channel.send(f'@{ctx.author.name}, now playing: ' + audio)
        print('Done. Now playing: ' + audio)
    else:
        await ctx.channel.send(f'@{ctx.author.name}, now there is no song on VK status :)')
        print('Done. Nothing playing.')
 
if __name__ == '__main__':
    bot.run()