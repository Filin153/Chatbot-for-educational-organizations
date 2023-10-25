from pydantic import BaseModel
from datetime import date, timedelta
import requests
from take_schedule_from_RKSI.main import group_pars, prepod_pars


class ScheduleModel(BaseModel):
    group: str = None
    prepod_name: str = None
    today: bool = False
    tomorow: bool = False
    schedule: str = None


class MakeSchedule:
    SPLIT_SYMBOL = "--------------------------------------------------"
    SMILE_PAR = {"08:00": "1️⃣",
                 "09:40": "2️⃣",
                 "11:30": "3️⃣",
                 "13:05": "⌛️Классный час",
                 "13:40": "4️⃣",
                 "14:10": "4️⃣",
                 "13:10": "4️⃣",
                 "15:00": "5️⃣",
                 "15:30": "5️⃣",
                 "16:00": "5️⃣",
                 "16:40": "6️⃣",
                 "17:10": "6️⃣",
                 "17:40": "6️⃣",
                 "18:20": "7️⃣",
                 "18:50": "7️⃣",
                 "20:00": "8️⃣",
                 "20:30": "8️⃣", }

    def __init__(self, group: str = None, today: bool = False, tomorow: bool = False):
        self.doc = ScheduleModel()
        self.doc.group = group
        self.doc.today = today
        self.doc.tomorow = tomorow

    def share_msg(self, msg):
        split_symbol = self.SPLIT_SYMBOL
        all_day = msg.split(split_symbol)
        yield split_symbol.join(all_day[:int(len(all_day) / 2)])
        yield split_symbol.join(all_day[int(len(all_day) / 2):])

    def check_for_prepod(self):
        if len(self.doc.group.split('.')) > 1:
            temp = self.doc.group
            self.doc.group = self.data['prepod']
            self.data['prepod'] = temp

    def make_msg(self) -> ScheduleModel:
        SMILE_PAR = self.SMILE_PAR
        r_j = self.resp
        today = self.doc.today
        tomorow = self.doc.tomorow

        if not tomorow and not today:
            msg_data = ["🚨 <b>Расписание с сайта</b> 🚨\n\n"]
            key = list(r_j.keys())
            for k in key:
                msg_data.append(f"\n🗓Расписание на {str(r_j[k][0]['date'])}\n")
                for i in r_j[k]:
                    self.data = i
                    self.check_for_prepod()
                    try:
                        msg_data.append(
                            f"\n{SMILE_PAR[i['start']]}\n⏰Время: {i['start']} - {i['end']}\n🚪Кабинет - {i['audit'].split('-')[0]}\n#️⃣Группа: {self.doc.group}\n👨‍💻Преподователь: {i['prepod']}\n📖Предмет:  {i['name']}\n")
                    except:
                        msg_data.append(
                            f"\n{SMILE_PAR[i['start']]}\n⏰Время: {i['start']} - {i['end']}\n📖Предмет:  {i['name']}\n")

                msg_data.append("-" * 50)

            self.doc.schedule = ''.join(msg_data)
        elif (date.today().strftime('%d.%m.20%y') == r_j[0]['date']) or (((date.today() + timedelta(days=1)).strftime('%d.%m.20%y')) == r_j[0]['date']):
            msg_data = ["🚨 <b>Расписание с сайта</b> 🚨\n\n"]
            msg_data.append(f"🗓Расписание на {str(r_j[0]['date'])}\n")
            for i in r_j:
                self.data = i
                self.check_for_prepod()
                try:
                    msg_data.append(
                        f"\n{SMILE_PAR[i['start']]}\n⏰Время: {i['start']} - {i['end']}\n🚪Кабинет - {i['audit'].split('-')[0]}\n#️⃣Группа: {self.doc.group}\n👨‍💻Преподователь: {i['prepod']}\n📖Предмет:  {i['name']}\n")
                except:
                    msg_data.append(
                        f"\n{SMILE_PAR[i['start']]}\n⏰Время: {i['start']} - {i['end']}\n📖Предмет:  {i['name']}\n")

            self.doc.schedule = ''.join(msg_data)
        else:
            self.doc.schedule = "🥲Что-то пошло не так, вы можете написать в поддержку"
            return self.doc

        return self.doc


class GroupSchedule(MakeSchedule):

    async def run(self, *args, **kwargs):
        try:
            await self.requests_to_group_schedule()
            return self.make_msg()
        except Exception as e:
            self.doc.schedule = str(e)
            return self.doc


    async def requests_to_group_schedule(self):
        resp = await group_pars(self.doc.group, today=self.doc.today, tomorrow=self.doc.tomorow)
        assert resp, "🥲Расписания нету"
        self.resp = resp
        return self.resp

class PrepodSchedule(MakeSchedule):

    async def run(self, *args, **kwargs) -> ScheduleModel:
        try:
            await self.requests_to_prepod_schedule()
            return self.make_msg()
        except:
            self.doc.schedule = '🥲Расписания нету'
            return self.doc

    async def requests_to_prepod_schedule(self):
        resp = await prepod_pars(self.doc.group, today=self.doc.today, tomorrow=self.doc.tomorow)
        assert resp, "🥲Расписания нету"
        self.resp = resp
        return self.resp




if __name__ == '__main__':
    import asyncio

    async def main():
        # pt = await PrepodSchedule(group="Бурда Е.Г.", tomorow=True).run()
        pt = await GroupSchedule(group="ИС-28", today=True).run()
        print(pt.schedule)
        return pt

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

