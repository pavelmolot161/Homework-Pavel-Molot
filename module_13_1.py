

import time
import asyncio

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for number_bol in range(1, 6):

### - добавленна обратная пропорция - "тот кто сильнее поднимает шар быстрее" _______

        delay = 5 / power
        await asyncio.sleep(delay)
###__________________________________________________________________________________
        print(f'Силач {name} поднял {number_bol}-й шар.')
    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    print('Старт')
    strongman1 = asyncio.create_task(start_strongman('Pasha', 5))
    strongman2 = asyncio.create_task(start_strongman('Denis', 4))
    strongman3 = asyncio.create_task(start_strongman('Apollon', 3))
    await strongman1
    await strongman2
    await strongman3

    print('Финиш')
start = time.time()
asyncio.run(start_tournament())
finish = time.time()
print(f'Рабочее время = {round(finish - start, 10)} секунд')

