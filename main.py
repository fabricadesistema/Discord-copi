try:
    import subprocess
    import os
    import sys
    import json
    import time
    import discord
    from utils.cloner import Cloner
    from utils.panel import Panel, Panel_Run
    from discord import Client, Intents
    from rich.prompt import Prompt, Confirm
    from time import sleep

    if discord.__version__ != "1.7.3":
        print("Atualizando Discord.py...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("Requisitos de instalação atualizados com sucesso!")
        print("Reiniciando...")
        os.execl(sys.executable, sys.executable, *sys.argv)
except Exception:
    print("Instalando requisitos...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    print("Requisitos instalados com sucesso!")
    print("Reiniciando...")
    os.execl(sys.executable, sys.executable, *sys.argv)

try:
    client = Client(intents=Intents.all())
except Exception as e:
    print("> Falha ao criar cliente Discord: ", e)

with open("./utils/config.json", "r") as json_file:
    data = json.load(json_file)

os.system('cls' if os.name == 'nt' else 'clear')


def clear(option=False):
    sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    if option:
        user = client.user
        guild = client.get_guild(int(INPUT_GUILD_ID))
        Panel_Run(guild, user)
    else:
        Panel()


async def clone_server():
    start_time = time.time()
    guild_from = client.get_guild(int(INPUT_GUILD_ID))
    guild_to = client.get_guild(int(GUILD))

    if guild_from is None or guild_to is None:
        print("> Erro: Um dos servidores não foi encontrado. Verifique os IDs.")
        return

    print("\n> Clonando servidor...")

    # Editar nome e ícone
    await Cloner.guild_create(guild_to, guild_from)

    await Cloner.channels_delete(guild_to)

    if data["copy_settings"].get("cargos", False):
        await Cloner.roles_create(guild_to, guild_from)

    if data["copy_settings"].get("categoria", False):
        await Cloner.categories_create(guild_to, guild_from)

    if data["copy_settings"].get("channels", False):
        await Cloner.channels_create(guild_to, guild_from)

    if data["copy_settings"].get("emojis", False):
        await Cloner.emojis_create(guild_to, guild_from)

    print("\n> Clonagem concluída em " + str(round(time.time() - start_time, 2)) + " segundos 😜")


@client.event
async def on_ready():
    clear(True)
    await clone_server()


class ClonerBot:

    def __init__(self):
        self.INPUT_GUILD_ID = None
        with open("./utils/config.json", "r") as json_file:
            self.data = json.load(json_file)

    def clear(self):
        sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        Panel()

    def edit_config(self, option, value, copy_settings=False):
        if copy_settings:
            self.data["copy_settings"][option] = value
        else:
            self.data[option] = value
        with open("./utils/config.json", "w") as json_file:
            json.dump(self.data, json_file, indent=4)

    def edit_settings_function(self):
        print("\nVocê quer copiar:")
        categories = Confirm.ask("> Categoria?")
        channels = Confirm.ask("> Canais?")
        roles = Confirm.ask("> Cargos?")
        emojis = Confirm.ask("> Emojis?")
        for option in ["categoria", "channels", "cargos", "emojis"]:
            self.edit_config(option, locals()[option], copy_settings=True)

    def main(self):
        self.clear()

        if not self.data.get("token"):
            self.TOKEN = Prompt.ask("\n> Insira seu Token")
            self.edit_config("token", self.TOKEN)
            sleep(0.5)
        else:
            self.TOKEN = self.data["token"]
            print("> Token encontrado!")

        self.clear()
        edit_settings = Confirm.ask("\n> Você quer editar as configurações?")
        self.clear()
        if edit_settings:
            self.edit_settings_function()
        self.clear()

        self.GUILD = Prompt.ask('\n> ID do servidor de destino (já criado manualmente)')
        self.INPUT_GUILD_ID = Prompt.ask("\n> ID do servidor que será copiado")
        sleep(0.5)

        return self.INPUT_GUILD_ID, self.TOKEN, self.GUILD


if __name__ == "__main__":
    bot = ClonerBot()
    INPUT_GUILD_ID, TOKEN, GUILD = bot.main()

    # Definir como global para uso em clone_server e clear
    globals()["INPUT_GUILD_ID"] = INPUT_GUILD_ID
    globals()["GUILD"] = GUILD

    try:
        client.run(TOKEN, bot=False)
        clear()
    except Exception as e:
        print(e)
        print("> Token inválido ou erro na execução.")
        data["token"] = False
        with open("./utils/config.json", "w") as json_file:
            json.dump(data, json_file, indent=4)
