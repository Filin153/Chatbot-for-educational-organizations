import requests
from bs4 import BeautifulSoup


async def take_group():
    all_group = []

    r = requests.get('ttps://rksi.ru/mobile_schedule')
    soup = BeautifulSoup(r.text, 'lxml')

    pr_tb_soup = soup.find('select', {'name': 'group'})
    all_group_soup = pr_tb_soup.find_all(
        'option',
    )

    for i in all_group_soup:
        all_group.append(str(i.text))
    return all_group
