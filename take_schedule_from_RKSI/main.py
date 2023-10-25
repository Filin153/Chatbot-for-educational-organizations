import asyncio
from bs4 import BeautifulSoup
from datetime import date, timedelta
from fastapi import FastAPI
from parser.rksi import RKSIScheduleParser



app = FastAPI()


@app.get('/schedule/g')
async def get_group_schedule(group: str, today: bool = False, tomorrow: bool = False):
    sched = await group_pars(group.upper())
    key = list(sched.keys())

    print(key)
    print(date.today().strftime("%d.%m"))

    if today:
        try:
            return sched[date.today().strftime("%d.%m")]
        except:
            return
    elif tomorrow:
        try:
            return sched[(date.today() + timedelta(days=1)).strftime("%d.%m")]
        except:
            return
    else:
        return sched

@app.get('/schedule/p')
async def get_prepod_schedule(name: str):
    sched = await prepod_pars(name)

    return sched

async def group_pars(group):
    parser = RKSIScheduleParser()

    if not await parser.is_alive():
        return print('Not alive')

    themes = await parser.parse_group_themes(group)
    current_date = None
    json_themes = {}

    for i in themes:
        if current_date != i.date:
            current_date = i.date
            # print('=' * 20)
            # print(i.date.strftime('%d.%m'))
            json_themes[i.date.strftime('%d.%m')] = []
        else:
            current_date = i.date
        # print(i.starts_at.strftime('%H:%M'), '-', i.ends_at.strftime('%H:%M'), i.name, f'({i.teacher})')

        json_themes[i.date.strftime('%d.%m')].append({"start": i.starts_at.strftime('%H:%M'), "end": i.ends_at.strftime('%H:%M'), "name": i.name, "prepod": i.teacher, "audit": i.audience, "date": i.date.strftime('%d.%m.20%y')})

    return json_themes

async def prepod_pars(name):
    parser = RKSIScheduleParser()

    if not await parser.is_alive():
        return print('Not alive')

    themes = await parser.parse_prepod_themes(name)
    current_date = None
    json_themes = {}

    for i in themes:
        if current_date != i.date:
            current_date = i.date
            # print('=' * 20)
            # print(i.date.strftime('%d.%m'))
            json_themes[i.date.strftime('%d.%m')] = []
        else:
            current_date = i.date
        # print(i.starts_at.strftime('%H:%M'), '-', i.ends_at.strftime('%H:%M'), i.name, f'({i.teacher})')

        json_themes[i.date.strftime('%d.%m')].append({"start": i.starts_at.strftime('%H:%M'), "end": i.ends_at.strftime('%H:%M'), "name": i.name, "prepod": i.teacher, "audit": i.audience, "date": i.date.strftime('%d.%m.20%y')})

    return json_themes




if __name__ == '__main__':
    print(asyncio.run(prepod_pars("Алексеенко О.Н.")))
    # print(take_all_prepod("Алексеенко О"))
