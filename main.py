import discord
import asyncio
from discord.ext import commands
from itertools import cycle
import youtube_dl

token= 'token'

client = commands.Bot(command_prefix= '>')

#subnick
status = ['cassio fei dms','pepe moreno']

client.remove_command('help')

#canais de voz q o bot ta
servers = {}

#fila de musicas
fila ={}

#comando pra qnd iniciar
@client.event
async def on_ready():
    print('bot online')
    frase = cycle(status)
    await client.send_message(client.get_channel('130839383262756865'), 'TO LIGADO')
    while not client.is_closed:
        status_atual = next(frase)
        await client.change_presence(game=discord.Game(name=status_atual))
        await asyncio.sleep(20)

#comando pra checar a fila de musicas
def checar_fila(id):
    if fila[id]!=[]:
        player = fila[id].pop(0)
        servers[id] = player
        player.start()


#GLR DO SERVER
@client.command()
async def mateus():
    await client.say('fala mais ai pf')
@client.command()
async def tomas():
    await client.say('CALA A BOCA TOMAS')
@client.command()
async def jota():
    await client.say('É NAO VOVÓ!')
@client.command()
async def lopes():
    await client.say('arduino teu cu')
@client.command()
async def daniel():
    await client.say('e as ferias daniel?')
@client.command()
async def joba():
    await client.say('GUGU NEGRO!')
@client.command()
async def jma():
    await client.say('menino daora simpatico')
@client.command()
async def nami():
    await client.say('deve ta usando droga')
@client.command()
async def lana():
    await client.say('essa foi boa lana kkkkkkkk :joy: :joy: :joy:')
@client.command()
async def nagato():
    await client.say('ALOOOOOOOOOOOOOOOOOOOOOOOO')
@client.command()
async def victor():
    await client.say('CALMA FELPINHO !!')
@client.command()
async def jamal():
    await client.say('tem rima')
@client.command()
async def jose():
    await client.say('CALMA GALERINEA')
@client.command()
async def mouth():
    await client.say('vai pra outra sala com jma ai namoral')



#COMANDOS DE TEXTO:


@client.command()
async def apolo():
    await client.say('comendo parede')
@client.command()
async def kiki():
    await client.say('ta mto gorda e fofinha')
@client.command()
async def airhorn():
    await client.say('bot errado desgraça')
@client.command()
async def fabinho():
    await client.say('HEHE - fabinho')
@client.command()
async def fortnite():
    await client.say('FORRRRRRRRRRRRRRRRRRR')
@client.command()
async def cs():
    await client.say('lopes ta recarregando')
@client.command()
async def luck():
    await client.say('fãfiunnn fãfiiinn')
@client.command()
async def cassio():
    await client.say('fei dms porra')
@client.command()
async def tricky():
    await client.say('TRIQ TEURS TRIC TEIUR')
@client.command()
async def dontstarve():
    await client.say('DONT STEUVE')
@client.command()
async def deregue():
    await client.say('ss fon trab')
@client.command()
async def circo():
    await client.say('CIRRRRRRRRCO DE SOLED')
@client.command()
async def pau():
    await client.say('ai q gostoson...')
@client.command()
async def sexo():
    await client.say('SEXO SEXO SEXO')
@client.command(pass_context=True)
async def xinga(ctx,nome):
    await client.say('VAI TOMA NO CU {}'.format(nome.upper()))
@client.command()
async def mary():
    await client.say('N FALE DA MINHA MAE N')
@client.command()
async def droga():
    await client.say('http://bibliaonline.com.br')
@client.command()
async def simone():
    await client.say('mulher incrivel maravilhosa')
@client.command()
async def skip():
    await client.say('''NÃO IAI NÃO A GENTE SEMPRE JOGOU JUNTO QUANDO CRUCIFICARAM O YETZ VOCE
NÃO É CRIANÇA E NEM EU SOU XIU É O CARALHO, 1 VEZ VOCÊ ME DESRESPEITO E FALOU DA
MINHA FAMÍLIA E AGORA EU TO FALANDO CONTIGO IGUAL HOMEM É ENTÃO BELEZA ENTÃO
FODA-SE SEU MERDA SEU BABACA SEU CRIANÇA SEU MERDA''')
@client.command()
async def felpx():
    await client.say('PRIMEIRO GANHADOR DA COMPETIÇÃO DE ADIVINHAÇÃO DO GEMIDÃO DOS CARAS LEGAIS')
@client.command()
async def cosmonauta():
    await client.say('SEGUNDO GANHADOR DA COMPETIÇÃO DE ADIVINHAÇÃO DO GEMIDÃO DOS CARAS LEGAIS')
@client.command()
async def laura():
    await client.say('TERCEIRA GANHADORA DA COMPETIÇÃO DE ADIVINHAÇÃO DO GEMIDÃO DOS CARAS LEGAIS')
@client.command()
async def naomi():
    await client.say('nao eh macho')
@client.command()
async def binho():
    await client.say('bom dia. pinho voi embora quando levatei a gaola nao estava aberta mais ele nao estava ja procurei mais binho nao encontramos misterio')




#AQUI EH SO COMANDO DE VOZ
@client.command(pass_context=True)
async def help(ctx):
    autor = ctx.message.author
    embed = discord.Embed(
        colour=discord.Colour.blue()
    )
    embed.set_author(name='TAI A AJUDA')
    embed.add_field(name='>xinga', value='oq q vc acha q um comando chamado XINGA faz?', inline=True)
    embed.add_field(name='>pau', value='gostoso dms', inline=True)
    embed.add_field(name='>nome da glr do discord', value='cada um faz alguma coisa', inline=False)
    embed.add_field(name='>sai', value='vc eh idiota eh?', inline=False)
    embed.add_field(name='>eoq', value='eoq\n(tem outros do yodao)', inline=False)
    await client.send_message(autor,embed=embed)


@client.command(pass_context=True)
async def sai(ctx):
    try:
        server = ctx.message.server
        canal_de_voz= client.voice_client_in(server)
        await canal_de_voz.disconnect()
    except AttributeError:
        client.say('nem to ai porra')


@client.command(pass_context=True)
async def novinha(ctx):
    try:
        try:
            canal = ctx.message.author.voice.voice_channel
            await client.join_voice_channel(canal)
        except discord.errors.InvalidArgument:
            await client.say('tu nem ta num canal porra')
    except discord.errors.ClientException:
        pass
    try:
        server = ctx.message.server
        canal_de_voz = client.voice_client_in(server)
        player = canal_de_voz.create_ffmpeg_player('novinha.mp3')
        servers[server.id]=player
        player.start()
        while not player.is_done():
            await asyncio.sleep(1)
        await canal_de_voz.disconnect()
    except youtube_dl.utils.DownloadError:
        client.say('?play {}'.format(url))
        client.say('1')

@client.command(pass_context=True)
async def peru(ctx):
    try:
        try:
            canal = ctx.message.author.voice.voice_channel
            await client.join_voice_channel(canal)
        except discord.errors.InvalidArgument:
            await client.say('tu nem ta num canal porra')
    except discord.errors.ClientException:
        pass
    try:
        server = ctx.message.server
        canal_de_voz = client.voice_client_in(server)
        player = canal_de_voz.create_ffmpeg_player('peru.mp3')
        servers[server.id]=player
        player.start()
        while not player.is_done():
            await asyncio.sleep(1)
        await canal_de_voz.disconnect()
    except youtube_dl.utils.DownloadError:
        client.say('?play {}'.format(url))
        client.say('1')

@client.command(pass_context=True)
async def nip(ctx):
    try:
        try:
            canal = ctx.message.author.voice.voice_channel
            await client.join_voice_channel(canal)
        except discord.errors.InvalidArgument:
            await client.say('tu nem ta num canal porra')
    except discord.errors.ClientException:
        pass
    try:
        server = ctx.message.server
        canal_de_voz = client.voice_client_in(server)
        player = canal_de_voz.create_ffmpeg_player('canto-do-nip.mp3')
        servers[server.id]=player
        player.start()
        while not player.is_done():
            await asyncio.sleep(1)
        await canal_de_voz.disconnect()
    except youtube_dl.utils.DownloadError:
        client.say('?play {}'.format(url))
        client.say('1')

@client.command(pass_context=True)
async def hehe(ctx):
    try:
        try:
            canal = ctx.message.author.voice.voice_channel
            await client.join_voice_channel(canal)
        except discord.errors.InvalidArgument:
            await client.say('tu nem ta num canal porra')
    except discord.errors.ClientException:
        pass
    try:
        server = ctx.message.server
        canal_de_voz = client.voice_client_in(server)
        player = canal_de_voz.create_ffmpeg_player('fabinho.mp3')
        servers[server.id]=player
        player.start()
        while not player.is_done():
            await asyncio.sleep(1)
        await canal_de_voz.disconnect()
    except youtube_dl.utils.DownloadError:
        client.say('?play {}'.format(url))
        client.say('1')

@client.command(pass_context=True)
async def wololo(ctx):
    try:
        try:
            canal = ctx.message.author.voice.voice_channel
            await client.join_voice_channel(canal)
        except discord.errors.InvalidArgument:
            await client.say('tu nem ta num canal porra')
    except discord.errors.ClientException:
        pass
    try:
        server = ctx.message.server
        canal_de_voz = client.voice_client_in(server)
        player = canal_de_voz.create_ffmpeg_player('wololo.mp3')
        servers[server.id]=player
        player.start()
        while not player.is_done():
            await asyncio.sleep(1)
        await canal_de_voz.disconnect()
    except youtube_dl.utils.DownloadError:
        client.say('?play {}'.format(url))
        client.say('1')

@client.command(pass_context=True)
async def solado(ctx):
    try:
        try:
            canal = ctx.message.author.voice.voice_channel
            await client.join_voice_channel(canal)
        except discord.errors.InvalidArgument:
            await client.say('tu nem ta num canal porra')
    except discord.errors.ClientException:
        pass
    try:
        server = ctx.message.server
        canal_de_voz = client.voice_client_in(server)
        player = canal_de_voz.create_ffmpeg_player('solado.mp3')
        servers[server.id]=player
        player.start()
        while not player.is_done():
            await asyncio.sleep(1)
        await canal_de_voz.disconnect()
    except youtube_dl.utils.DownloadError:
        client.say('?play {}'.format(url))
        client.say('1')

@client.command(pass_context=True)
async def eoq(ctx):
    try:
        try:
            canal = ctx.message.author.voice.voice_channel
            await client.join_voice_channel(canal)
        except discord.errors.InvalidArgument:
            await client.say('tu nem ta num canal porra')
    except discord.errors.ClientException:
        pass
    try:
        server = ctx.message.server
        canal_de_voz = client.voice_client_in(server)
        player = canal_de_voz.create_ffmpeg_player('eoq.mp3')
        servers[server.id]=player
        player.start()
        while not player.is_done():
            await asyncio.sleep(1)
        await canal_de_voz.disconnect()
    except youtube_dl.utils.DownloadError:
        client.say('?play {}'.format(url))
        client.say('1')

@client.command(pass_context=True)
async def festa(ctx):
    try:
        try:
            canal = ctx.message.author.voice.voice_channel
            await client.join_voice_channel(canal)
        except discord.errors.InvalidArgument:
            await client.say('tu nem ta num canal porra')
    except discord.errors.ClientException:
        pass
    try:
        server = ctx.message.server
        canal_de_voz = client.voice_client_in(server)
        player = canal_de_voz.create_ffmpeg_player('festa.mp3')
        servers[server.id]=player
        player.start()
        while not player.is_done():
            await asyncio.sleep(1)
        await canal_de_voz.disconnect()
    except youtube_dl.utils.DownloadError:
        client.say('?play {}'.format(url))
        client.say('1')

@client.command(pass_context=True)
async def hastad(ctx):
    try:
        try:
            canal = ctx.message.author.voice.voice_channel
            await client.join_voice_channel(canal)
        except discord.errors.InvalidArgument:
            await client.say('tu nem ta num canal porra')
    except discord.errors.ClientException:
        pass
    try:
        server = ctx.message.server
        canal_de_voz = client.voice_client_in(server)
        player = canal_de_voz.create_ffmpeg_player('hastad.mp3')
        servers[server.id]=player
        player.start()
        while not player.is_done():
            await asyncio.sleep(1)
        await canal_de_voz.disconnect()
    except youtube_dl.utils.DownloadError:
        client.say('?play {}'.format(url))
        client.say('1')

@client.command(pass_context=True)
async def cabalo(ctx):
    try:
        try:
            canal = ctx.message.author.voice.voice_channel
            await client.join_voice_channel(canal)
        except discord.errors.InvalidArgument:
            await client.say('tu nem ta num canal porra')
    except discord.errors.ClientException:
        pass
    try:
        server = ctx.message.server
        canal_de_voz = client.voice_client_in(server)
        player = canal_de_voz.create_ffmpeg_player('cabaloimundo.mp3')
        servers[server.id]=player
        player.start()
        while not player.is_done():
            await asyncio.sleep(1)
        await canal_de_voz.disconnect()
    except youtube_dl.utils.DownloadError:
        client.say('?play {}'.format(url))
        client.say('1')

@client.command(pass_context=True)
async def catota(ctx):
    try:
        try:
            canal = ctx.message.author.voice.voice_channel
            await client.join_voice_channel(canal)
        except discord.errors.InvalidArgument:
            await client.say('tu nem ta num canal porra')
    except discord.errors.ClientException:
        pass
    try:
        server = ctx.message.server
        canal_de_voz = client.voice_client_in(server)
        player = canal_de_voz.create_ffmpeg_player('gemidao.mp3')
        servers[server.id]=player
        player.start()
        while not player.is_done():
            await asyncio.sleep(1)
        await canal_de_voz.disconnect()
    except youtube_dl.utils.DownloadError:
        client.say('?play {}'.format(url))
        client.say('1')

@client.command(pass_context=True)
async def nha(ctx):
    try:
        try:
            canal = ctx.message.author.voice.voice_channel
            await client.join_voice_channel(canal)
        except discord.errors.InvalidArgument:
            await client.say('tu nem ta num canal porra')
    except discord.errors.ClientException:
        pass
    try:
        server = ctx.message.server
        canal_de_voz = client.voice_client_in(server)
        player = canal_de_voz.create_ffmpeg_player('nha.mp3')
        servers[server.id]=player
        player.start()
        while not player.is_done():
            await asyncio.sleep(1)
        await canal_de_voz.disconnect()
    except youtube_dl.utils.DownloadError:
        client.say('?play {}'.format(url))
        client.say('1')

@client.command(pass_context=True)
async def renato(ctx):
    try:
        try:
            canal = ctx.message.author.voice.voice_channel
            await client.join_voice_channel(canal)
        except discord.errors.InvalidArgument:
            await client.say('tu nem ta num canal porra')
    except discord.errors.ClientException:
        pass
    try:
        server = ctx.message.server
        canal_de_voz = client.voice_client_in(server)
        player = canal_de_voz.create_ffmpeg_player('renato.mp3')
        servers[server.id]=player
        player.start()
        while not player.is_done():
            await asyncio.sleep(1)
        await canal_de_voz.disconnect()
    except youtube_dl.utils.DownloadError:
        client.say('?play {}'.format(url))
        client.say('1')

@client.command(pass_context=True)
async def yoda(ctx):
    try:
        try:
            canal = ctx.message.author.voice.voice_channel
            await client.join_voice_channel(canal)
        except discord.errors.InvalidArgument:
            await client.say('tu nem ta num canal porra')
    except discord.errors.ClientException:
        pass
    try:
        server = ctx.message.server
        canal_de_voz = client.voice_client_in(server)
        player = canal_de_voz.create_ffmpeg_player('yoda.mp3')
        servers[server.id]=player
        player.start()
        while not player.is_done():
            await asyncio.sleep(1)
        await canal_de_voz.disconnect()
    except youtube_dl.utils.DownloadError:
        client.say('?play {}'.format(url))
        client.say('1')

@client.command(pass_context=True)
async def fon(ctx):
    try:
        try:
            canal = ctx.message.author.voice.voice_channel
            await client.join_voice_channel(canal)
        except discord.errors.InvalidArgument:
            await client.say('tu nem ta num canal porra')
    except discord.errors.ClientException:
        pass
    try:
        server = ctx.message.server
        canal_de_voz = client.voice_client_in(server)
        player = canal_de_voz.create_ffmpeg_player('airhorn.mp3')
        servers[server.id]=player
        player.start()
        while not player.is_done():
            await asyncio.sleep(1)
        await canal_de_voz.disconnect()
    except youtube_dl.utils.DownloadError:
        client.say('?play {}'.format(url))
        client.say('1')

@client.command(pass_context=True)
async def zoio(ctx):
    try:
        try:
            canal = ctx.message.author.voice.voice_channel
            await client.join_voice_channel(canal)
        except discord.errors.InvalidArgument:
            await client.say('tu nem ta num canal porra')
    except discord.errors.ClientException:
        pass
    try:
        server = ctx.message.server
        canal_de_voz = client.voice_client_in(server)
        player = canal_de_voz.create_ffmpeg_player('marreta.mp3')
        servers[server.id]=player
        player.start()
        while not player.is_done():
            await asyncio.sleep(1)
        await canal_de_voz.disconnect()
    except youtube_dl.utils.DownloadError:
        client.say('?play {}'.format(url))
        client.say('1')

@client.command(pass_context=True)
async def dale(ctx):
    try:
        try:
            canal = ctx.message.author.voice.voice_channel
            await client.join_voice_channel(canal)
        except discord.errors.InvalidArgument:
            await client.say('tu nem ta num canal porra')
    except discord.errors.ClientException:
        pass
    try:
        server = ctx.message.server
        canal_de_voz = client.voice_client_in(server)
        player = canal_de_voz.create_ffmpeg_player('dale.mp3')
        servers[server.id]=player
        player.start()
        while not player.is_done():
            await asyncio.sleep(1)
        await canal_de_voz.disconnect()
    except youtube_dl.utils.DownloadError:
        client.say('?play {}'.format(url))
        client.say('1')

@client.command(pass_context=True)
async def treta(ctx):
    try:
        try:
            canal = ctx.message.author.voice.voice_channel
            await client.join_voice_channel(canal)
        except discord.errors.InvalidArgument:
            await client.say('tu nem ta num canal porra')
    except discord.errors.ClientException:
        pass
    try:
        server = ctx.message.server
        canal_de_voz = client.voice_client_in(server)
        player = canal_de_voz.create_ffmpeg_player('treta_axt_e_skip.mp3')
        servers[server.id]=player
        player.start()
        while not player.is_done():
            await asyncio.sleep(1)
        await canal_de_voz.disconnect()
    except youtube_dl.utils.DownloadError:
        client.say('?play {}'.format(url))
        client.say('1')

@client.command(pass_context=True)
async def jotinha(ctx):
    try:
        try:
            canal = ctx.message.author.voice.voice_channel
            await client.join_voice_channel(canal)
        except discord.errors.InvalidArgument:
            await client.say('tu nem ta num canal porra')
    except discord.errors.ClientException:
        pass
    try:
        server = ctx.message.server
        canal_de_voz = client.voice_client_in(server)
        player = canal_de_voz.create_ffmpeg_player('jotinha.mp3')
        servers[server.id]=player
        player.start()
        while not player.is_done():
            await asyncio.sleep(1)
        await canal_de_voz.disconnect()
    except youtube_dl.utils.DownloadError:
        client.say('?play {}'.format(url))
        client.say('1')

client.run(token)
