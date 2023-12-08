import hondana
import asyncio

client = hondana.Client()

GROUP_IDS = [
    'c2c254d6-aa8d-4288-965b-82386653f896',
    'a2bd85fe-e18e-4b2f-9dcb-150c39a65d61',
    'bb82974e-3eaf-43e1-93b8-c5ff039883fc',
    'a86d5d9f-7934-4379-a756-9b432f31ae7b',
    '55bf647a-ddfd-46e2-bdb0-f567c3006ad7',
    '64c29f42-c325-4ff7-a571-ae53767076c2',
    'ec0c8781-552a-48ec-a090-818db7083acd',
]

async def main():
    list = []

    for group in GROUP_IDS:
        manga_list = await client.manga_list(group=group)
        for manga in manga_list.manga:
            if manga not in list:
                list.append(manga)

    for manga in list:
        print(manga)

    await client.close()

asyncio.run(main())