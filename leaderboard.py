import hondana
import asyncio
import configparser
import ast

client = hondana.Client()

config = configparser.ConfigParser()
config.read('config.ini')

GROUP_IDS = []
BLACKLIST = []

async def read_config():
    global GROUP_IDS, BLACKLIST

    config.read('config.ini')

    GROUP_IDS = ast.literal_eval(config['DEFAULT']['GROUP_IDS'])
    BLACKLIST = ast.literal_eval(config['DEFAULT']['BLACKLIST'])

async def main():
    list = []
    await read_config()

    for group in GROUP_IDS:
        manga_list = await client.manga_list(group=group)
        for manga in manga_list.manga:
                if manga not in list:
                    if manga.id not in BLACKLIST:
                        list.append(manga)

    for manga in list:
        print(manga)

    await client.close()

asyncio.run(main())
