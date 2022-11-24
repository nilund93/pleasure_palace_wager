
import os
import discord
from resources import *
from discord.ext import commands
from dotenv import load_dotenv

class MyClient(discord.Client):
    
    # async def on_ready(self):
    #     print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        
        
    # @discord.Client.event
    async def on_ready(self):
        for guild in client.guilds:
            if guild.name == GUILD:
                break

        print(
            f'{client.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})'
        )
        members = '\n - '.join([member.name for member in guild.members])
        print(f'Guild Members:\n - {members}')


def import_statements():
    with open("statements.txt", "rt", encoding = "utf-8") as f:
        return_statements = []
        for line in f.readlines():
            this_statement = line.split("<>")
            this_statement[1] = this_statement[1].rstrip("\n")
            if this_statement[1] == "True": this_statement[1] = True
            else: this_statement[1] = False
            return_statements.append(Statement(this_statement[0],this_statement[1]))
        return return_statements 
     
def save_statements(statements):
    with open("statements.txt", "wt", encoding = "utf-8") as f:
        for state in statements:
            w_string = state.to_file()
            f.write(w_string + '\n')
    print("Statements have been saved.")

def append_statements():
    with open("statements.txt", "at", encoding = "utf-8") as f:
        while True:
            print("New statement. Type x to exit.")
            new_statement = input(">")
            if new_statement.lower() == "x": break
            f.write(new_statement + "<>False\n")


if __name__ == "__main__":
    statements = import_statements()
        
        
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')
    GUILD = os.getenv('DISCORD_GUILD')


    intents = discord.Intents().all()
    
    client = MyClient(command_prefix='!',intents=intents)
    client.run(TOKEN)  
    
    
    
    