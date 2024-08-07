import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for ball in range(1, 6):
        await asyncio.sleep(10 / power)
        print(f'Силач {name} поднял {ball} мяч!')
    print(f'Силач {name} закончил соревнования.')


async def start_tournament(participants):
    all_tasks = []
    for name, power in participants.items():
        task = asyncio.create_task(start_strongman(name, power))
        all_tasks.append(task)
    for t in all_tasks:
        await t
    print(f'Все силачи закончили!')

participants = {'Pasha': 3, 'Denis': 4, 'Apollon': 5}
asyncio.run(start_tournament(participants))
