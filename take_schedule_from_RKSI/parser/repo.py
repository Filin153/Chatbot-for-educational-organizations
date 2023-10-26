from .models import Group, RawSubjectEntry


class ScheduleRepo:
    def __init__(self):
        self.document = Group()

    async def resolve_theme(self, theme: RawSubjectEntry):
        self.document.schedule.append()
