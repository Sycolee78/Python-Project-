#
#Author : emmanuel buruvuru
#Date : 
#
#
 
import discord
import requests
import json
import random
from replit import db
from alive import alive

Tokken = "MTAwMTg2MTQ0NzI3OTcxMDM0MQ.GXu1xl.boP5YJuWP91TyUmwqKeqhpc3lvk5HOSY8FlOT4"

client = discord.Client()

sadwords = [
    "depressed", "unhappy", "suicidal", "kill", "sad", "down", "stuck", "die",
    "suicide"
]

starter_encouragements = [
    "You are not alone", "You can do this", "Hang in there pal",
    "Do be scared to ask for help", "I love you don't you give up on me"
    " Hang in there pal"
    " Dont be alone"
]

if "responding" not in db.keys():
    db["responding"] = True


def get_quote():

    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']

    return quote


def udate_msg(ecouranging_msg):
    if "ecourangements" in db.keys():
        encouragements = db["encouragements"]
        encouragements.append(ecouranging_msg)
        db["encouragements"] = encouragements

    else:
        db["encouragenments"] = [ecouranging_msg]


def delete_encouragment(index):
    encouragements = db["encouragements"]
    if len(encouragements) > index:
        del encouragements[index]
        db["encouragements"] = encouragements


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):

    msg = message.content

    if message.author == client.user:
        return

    if message.content.startswith('$inspire'):

        quote = get_quote()
        await message.channel.send(quote)
    if db["responding"]:
        options = starter_encouragements
        if "encouragements" in db.keys():
            options = options + db["encouragements"]

        if any(word in msg for word in sadwords):
            await message.channel.send(random.choice(starter_encouragements))

    if msg.startswith("$new"):
        encouraging_message = msg.split("$new ", 1)[1]
        udate_msg(encouraging_message)
        await message.channel.send("New encouraging message added.")

    if msg.startswith("$del"):
        encouragements = []
        if "encouragements" in db.keys():
            index = int(msg.split("$del", 1)[1])
            delete_encouragment(index)
            encouragements = db["encouragements"]

        await message.channel.send(encouragements)
å
    if msg.startswith("$list"):
        encouragements = []
        if "encouragements" in db.keys():
            encouragements = db["encouragements"]

        await message.channel.send(encouragements)
    if msg.startswith("$responding"):
        value = msg.split("$responding ", 1)[1]

        if value.lower() == "true":
            db[" responding"] = True
            await message.channel.send("Responding is on.")
        else:
            db[" responding"] = False
            await message.channel.send("Responding is off.")


alive()
client.run(Tokken)
