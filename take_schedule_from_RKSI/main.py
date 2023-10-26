import asyncio
from datetime import date, timedelta

from take_schedule_from_RKSI.parser.rksi import RKSIScheduleParser


async def group_pars(group, today: bool = False, tomorrow: bool = False):
    parser = RKSIScheduleParser()

    if not await parser.is_alive():
        return

    themes = await parser.parse_group_themes(group)
    current_date = None
    json_themes = {}

    for i in themes:
        if current_date != i.date:
            current_date = i.date
            json_themes[i.date.strftime('%d.%m')] = []
        else:
            current_date = i.date

        json_themes[i.date.strftime('%d.%m')].append(
            {
                'start': i.starts_at.strftime('%H:%M'),
                'end': i.ends_at.strftime('%H:%M'),
                'name': i.name,
                'prepod': i.teacher,
                'audit': i.audience,
                'date': i.date.strftime('%d.%m.20%y'),
            }
        )

    if today:
        try:
            return json_themes[date.today().strftime('%d.%m')]
        except Exception:
            return
    elif tomorrow:
        try:
            return json_themes[
                (date.today() + timedelta(days=1)).strftime('%d.%m')
            ]
        except Exception:
            return
    else:
        return json_themes


async def prepod_pars(name, today: bool = False, tomorrow: bool = False):
    parser = RKSIScheduleParser()

    if not await parser.is_alive():
        return

    themes = await parser.parse_prepod_themes(name)
    current_date = None
    json_themes = {}

    for i in themes:
        if current_date != i.date:
            current_date = i.date
            json_themes[i.date.strftime('%d.%m')] = []
        else:
            current_date = i.date

        json_themes[i.date.strftime('%d.%m')].append(
            {
                'start': i.starts_at.strftime('%H:%M'),
                'end': i.ends_at.strftime('%H:%M'),
                'name': i.name,
                'prepod': i.teacher,
                'audit': i.audience,
                'date': i.date.strftime('%d.%m.20%y'),
            }
        )

    if today:
        try:
            return json_themes[date.today().strftime('%d.%m')]
        except Exception:
            return
    elif tomorrow:
        try:
            return json_themes[
                (date.today() + timedelta(days=1)).strftime('%d.%m')
            ]
        except Exception:
            return
    else:
        return json_themes


async def main():
    result = await prepod_pars('Бурда Е.Г.', tomorrow=True)
    result = await group_pars('ИС-28', today=True)
    print(result)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
