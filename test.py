import asyncio

import requests
from bs4 import BeautifulSoup
from fuzzywuzzy import fuzz, process


async def take_all_prepod(name):
    all_prepod = []
    similarity = []

    r = requests.get('https://rksi.ru/mobile_schedule')
    soup = BeautifulSoup(r.text, 'lxml')
    pr_tb_soup = soup.find('select', {'name': 'teacher'})
    all_prepod_soup = pr_tb_soup.find_all(
        'option',
    )

    for i in all_prepod_soup:
        all_prepod.append(str(i.text))

    if all_prepod.count(name) == 0:
        matching_strings = process.extract(
            name, all_prepod, scorer=fuzz.partial_token_sort_ratio, limit=3
        )

        for string, score in matching_strings:
            similarity.append(f'<code>{string}</code>\n')

        return similarity


async def main():
    result = await take_all_prepod('Щипанкина А.А')
    print(result)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
