from discord.ext import commands
import discord
from gtts import gTTS

import setting
import message

GIBARA_TOKEN = setting.GIBARA_TOKEN
MAKE_CHANNEL_CATEGORY_ID = setting.MAKE_CHANNEL_CATEGORY_ID
BOT_HelloWorld = int(setting.BOT_HelloWorld)
TEST_Channel = setting.TEST_Channel
AFK = setting.AFK
GUILD = setting.GUILD
JIHOU = setting.JIHOU
ROOM1 = setting.ROOM1
help_mes = message.help_mes
bot = commands.Bot(command_prefix="/gibara ")

global vc

@bot.event
async def on_ready():
    print("Login OK!")
    await bot.get_channel(BOT_HelloWorld).send("おとぎばらぁ・・・・ｴﾗﾃﾞｪｽ!!!!ﾊｧ！")

@bot.command()
async def find_voice(ctx):
    channel = commands.utils.get(
        bot.get_all_channels(), id=ROOM1)
    print(len(channel.members))

@bot.command()
async def connect(ctx):
    global vc
    vc = await ctx.author.voice.channel.connect()

@bot.command()
async def ts(ctx, arg):
    global vc
    if vc is None:
        vc = await ctx.author.voice.channel.connect()
        print("ボイスチャンネルに入りま～す")
    else:
        tts = gTTS(text=arg, lang='ja')
        tts.save('a.mp3')
        vc.play(discord.FFmpegPCMAudio(
            'a.mp3'))

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    await bot.process_commands(message)
    global vc
    try:
        vc
    except NameError:
        vc = await message.author.voice.channel.connect()
        print("ボイスチャンネルに入りま～す")
    finally:
        tts = gTTS(text=message.content, lang='ja')
        tts.save('a.mp3')
        vc.play(discord.FFmpegPCMAudio(
            'a.mp3'))


@bot.command()
async def hlp(ctx):
    if ctx.channel.id == int(ROOM1):
        await ctx.send(help_mes)
    else:
        return

@bot.command()
async def discon(ctx):
    global vc
    await vc.disconnect()

@bot.command()
async def make2ch(ctx, *args):
    category_id = int(MAKE_CHANNEL_CATEGORY_ID)
    category = ctx.guild.get_channel(category_id)
    print(category)
    if len(args) < 2:
        new_channel = await ctx.guild.create_text_channel(name=args[0], category=category)
    else:
        await ctx.send("引数が不正です")

bot.run(GIBARA_TOKEN)