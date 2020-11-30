import requests
import discord
from selenium import webdriver

#query being used to find the stonks
#https://www.google.com/search?q=asx:cba

#Your bot token here
TOKEN = "xxxxxxxxxxxxxxxxxxxxxxxxxx"

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        print('Stonk bot standing by...')

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        if message.content.startswith('$ping'):
            await message.channel.send('Pong!')
        elif message.content.startswith('$shut'):
            await message.channel.send('shutting down...')
            exit()
        elif message.content.startswith('$'):
            print(":P stonk")
            print(message.content)
            param = message.content[1:]
            dump = lookupStock(param)
            #invalid stock
            if (dump[0] == 'error'):
                print("Could not find stock!")
                await message.channel.send('Could not find stock!')
            await message.channel.send("=====================\n" + "Company: " + dump[0] + "\n" + "STONK: " + dump[1] + "\n" + "Performance: " + dump[2] + "\n" + "Time Updated: " + dump[3])

def lookupStock(stockArg):
    #Used to find the section with finance data
    GoogleFinanceId = 'N9cLBc'
    stock = stockArg

    #Create driver
    browser = webdriver.Firefox()
    browser.get('https://www.google.com/search?q=' + stock)

    #Load Page and grab data
    try:
        print("Waiting on webpage to fully load")
        el = browser.find_element_by_class_name(GoogleFinanceId)
        dump = el.text
        print(dump)
        browser.quit()
    except:
        browser.quit()
        dump = ['error']
        return dump

    #filter data
    dump = dump.split('\n')
    print(dump)
    return dump

client = MyClient()
client.run(TOKEN)
