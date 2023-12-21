from datetime import datetime, timedelta


class DateHandler:
    def __init__(self):
        self.days = 0

    def dates_list_sync(self, days):
        current_date = datetime.now()
        dates = [current_date - timedelta(days=i) for i in range(days + 1)]
        return [date.strftime("%d.%m.%Y") for date in dates]

    async def dates_list(self, days):  # Make dates_list an async generator
        current_date = datetime.now()
        for i in range(days + 1):
            yield (current_date - timedelta(days=i)).strftime("%d.%m.%Y")
