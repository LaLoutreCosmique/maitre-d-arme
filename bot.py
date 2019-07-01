import discord
import asyncio
from discord.ext.commands import Bot
from discord.utils import get
import time
import os

PREFIX = '!'

vbot = Bot(command_prefix=PREFIX)


@vbot.event
async def on_ready():
    print(vbot.user.name, 'est en marche')

@vbot.command(pass_context=True)
async def w(ctx):
    await vbot.delete_message(ctx.message)

    hache = get(vbot.get_all_emojis(), name='hache')
    guandao = get(vbot.get_all_emojis(), name='guandao')
    lance = get(vbot.get_all_emojis(), name='lance')
    nodachi = get(vbot.get_all_emojis(), name='nodachi')
    arc_court = get(vbot.get_all_emojis(), name='arc_court')    

    embed = discord.Embed(title='LISTE DES ARMES', color=0xfcf235)
    embed.add_field(name='Saisissez les armes que vous jouez...', value='*Cela permettra de savoir quelles armes vous jouez en regardant le rôle que vous avez.*')
    embed.add_field(name='-------------------------------------------------', value='------------------------------------------------', inline=False)
    embed.add_field(name='Épée longue et bouclier : :shield:', value='------------------------------------------------', inline=False)
    embed.add_field(name='Épée courte et bouclier : :dagger:', value='------------------------------------------------', inline=False)
    embed.add_field(name="Hache d'arme: {}".format(hache), value='------------------------------------------------', inline=False)
    embed.add_field(name='Guandao : {}'.format(guandao), value='------------------------------------------------', inline=False)
    embed.add_field(name='Lance : {}'.format(lance), value='------------------------------------------------', inline=False)
    embed.add_field(name='Mousquet : :gun:', value='------------------------------------------------', inline=False)
    embed.add_field(name='Nodachi : {}'.format(nodachi), value='------------------------------------------------', inline=False)
    embed.add_field(name='Lames jumelles : :crossed_swords:', value='------------------------------------------------', inline=False)
    embed.add_field(name='Arc long : :bow_and_arrow:', value='------------------------------------------------', inline=False)
    embed.add_field(name='Arc court : {}'.format(arc_court), value='------------------------------------------------', inline=False)

    message = await vbot.say(embed=embed)

    await vbot.add_reaction(message, '\N{SHIELD}')
    await vbot.add_reaction(message, '\N{DAGGER KNIFE}')
    await vbot.add_reaction(message, hache)
    await vbot.add_reaction(message, guandao)
    await vbot.add_reaction(message, lance)
    await vbot.add_reaction(message, '\N{PISTOL}')
    await vbot.add_reaction(message, nodachi)
    await vbot.add_reaction(message, '\N{CROSSED SWORDS}')
    await vbot.add_reaction(message, '\N{BOW AND ARROW}')
    await vbot.add_reaction(message, arc_court)


@vbot.event
async def on_reaction_add(reaction, user):

    hache = get(vbot.get_all_emojis(), name='hache')
    guandao = get(vbot.get_all_emojis(), name='guandao')
    lance = get(vbot.get_all_emojis(), name='lance')
    nodachi = get(vbot.get_all_emojis(), name='nodachi')
    arc_court = get(vbot.get_all_emojis(), name='arc_court')

    channel = vbot.get_channel('594255053989347340')

    role = discord.utils.get(user.server.roles, name='------------- ARMES JOUÉES -------------')
    rhache = discord.utils.get(user.server.roles, name="Hache d'arme")
    rguandao = discord.utils.get(user.server.roles, name='Guandao')
    rlance = discord.utils.get(user.server.roles, name='Lance')
    rnodachi = discord.utils.get(user.server.roles, name='Nodachi')
    rarc_court = discord.utils.get(user.server.roles, name='Arc court')
    rarc_long = discord.utils.get(user.server.roles, name='Arc long')
    rlames_jumelles = discord.utils.get(user.server.roles, name='Lames jumelles')
    repee_courte = discord.utils.get(user.server.roles, name='Épée courte et bouclier')
    repee_longue = discord.utils.get(user.server.roles, name='Épée longue et bouclier')
    rmousquet = discord.utils.get(user.server.roles, name='Mousquet')

    fait = 1

    if reaction.message.channel == channel and user.id != '594204133448482816':

        if reaction.emoji == hache:
            await vbot.add_roles(user, rhache)
            time.sleep(0.5)
            await vbot.add_roles(user, role)
            fait = 0
            time.sleep(0.5)

        elif reaction.emoji == guandao and fait:
            await vbot.add_roles(user, rguandao)
            time.sleep(0.5)
            await vbot.add_roles(user, role)
            fait = 0
            time.sleep(0.5)

        elif reaction.emoji == lance and fait:
            await vbot.add_roles(user, rlance)
            time.sleep(0.5)
            await vbot.add_roles(user, role)
            fait = 0
            time.sleep(0.5)

        elif reaction.emoji == nodachi and fait:
            await vbot.add_roles(user, rnodachi)
            await vbot.add_roles(user, role)
            fait = 0

        elif reaction.emoji == arc_court and fait:
            await vbot.add_roles(user, rarc_court)
            time.sleep(0.5)
            await vbot.add_roles(user, role)
            fait = 0
            time.sleep(0.5)

        elif reaction.emoji == '\N{BOW AND ARROW}' and fait:
            await vbot.add_roles(user, rarc_long)
            time.sleep(0.5)
            await vbot.add_roles(user, role)
            fait = 0
            time.sleep(0.5)

        elif reaction.emoji == '\N{CROSSED SWORDS}' and fait:
            await vbot.add_roles(user, rlames_jumelles)
            time.sleep(0.5)
            await vbot.add_roles(user, role)
            fait = 0
            time.sleep(0.5)

        elif reaction.emoji == '\N{DAGGER KNIFE}' and fait:
            await vbot.add_roles(user, repee_courte)
            time.sleep(0.5)
            await vbot.add_roles(user, role)
            fait = 0
            time.sleep(0.5)

        elif reaction.emoji == '\N{SHIELD}' and fait:
            await vbot.add_roles(user, repee_longue)
            time.sleep(0.5)
            await vbot.add_roles(user, role)
            fait = 0
            time.sleep(0.5)

        elif reaction.emoji == '\N{PISTOL}' and fait:
            await vbot.add_roles(user, rmousquet)
            time.sleep(0.5)
            await vbot.add_roles(user, role)
            fait = 0
            time.sleep(0.5)
        
    else:
        return


@vbot.event
async def on_reaction_remove(reaction, user):

    hache = get(vbot.get_all_emojis(), name='hache')
    guandao = get(vbot.get_all_emojis(), name='guandao')
    lance = get(vbot.get_all_emojis(), name='lance')
    nodachi = get(vbot.get_all_emojis(), name='nodachi')
    arc_court = get(vbot.get_all_emojis(), name='arc_court')

    channel = vbot.get_channel('594255053989347340')

    role = discord.utils.get(user.server.roles, name='------------- ARMES JOUÉES -------------')
    rhache = discord.utils.get(user.server.roles, name="Hache d'arme")
    rguandao = discord.utils.get(user.server.roles, name='Guandao')
    rlance = discord.utils.get(user.server.roles, name='Lance')
    rnodachi = discord.utils.get(user.server.roles, name='Nodachi')
    rarc_court = discord.utils.get(user.server.roles, name='Arc court')
    rarc_long = discord.utils.get(user.server.roles, name='Arc long')
    rlames_jumelles = discord.utils.get(user.server.roles, name='Lames jumelles')
    repee_courte = discord.utils.get(user.server.roles, name='Épée courte et bouclier')
    repee_longue = discord.utils.get(user.server.roles, name='Épée longue et bouclier')
    rmousquet = discord.utils.get(user.server.roles, name='Mousquet')

    fait = 1

    if reaction.message.channel == channel and user.id != '594204133448482816':

        if reaction.emoji == hache:
            await vbot.remove_roles(user, rhache)
            fait = 0
            time.sleep(0.5)

        elif reaction.emoji == guandao and fait:
            await vbot.remove_roles(user, rguandao)
            fait = 0
            time.sleep(0.5)

        elif reaction.emoji == lance and fait:
            await vbot.remove_roles(user, rlance)
            fait = 0
            time.sleep(0.5)

        elif reaction.emoji == nodachi and fait:
            await vbot.remove_roles(user, rnodachi)
            fait = 0
            time.sleep(0.5)

        elif reaction.emoji == arc_court and fait:
            await vbot.remove_roles(user, rarc_court)
            fait = 0
            time.sleep(0.5)

        elif reaction.emoji == '\N{BOW AND ARROW}' and fait:
            await vbot.remove_roles(user, rarc_long)
            fait = 0
            time.sleep(0.5)

        elif reaction.emoji == '\N{CROSSED SWORDS}' and fait:
            await vbot.remove_roles(user, rlames_jumelles)
            fait = 0
            time.sleep(0.5)

        elif reaction.emoji == '\N{DAGGER KNIFE}' and fait:
            await vbot.remove_roles(user, repee_courte)
            fait = 0
            time.sleep(0.5)

        elif reaction.emoji == '\N{SHIELD}' and fait:
            await vbot.remove_roles(user, repee_longue)
            fait = 0
            time.sleep(0.5)

        elif reaction.emoji == '\N{PISTOL}' and fait:
            await vbot.remove_roles(user, rmousquet)
            fait = 0
            time.sleep(0.5)
            
    else:
        return


vbot.run(os.environ['DISCORD_TOKEN'])
