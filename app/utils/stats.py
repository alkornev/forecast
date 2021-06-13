from app import db
import csv, io
from datetime import datetime
from app.models import Weather

class StatsApiException(Exception):
    pass


class StatsApi:
    @staticmethod
    def save_to_csv(startdate: datetime, enddate: datetime):
        csv_data = io.StringIO()
        with csv.DictWriter(csv_data) as writer:
            entries = Weather.query.filter(startdate <= Weather.datetime <= enddate)
            for entry in entries:
                writer.write_row(entry.to_dict())
        return csv_data
