import pandas as pd
import sqlite3

from models.Passenger import Passenger


class TitanicPassengerDao(object):
    CSV_FILE_PATH = "./titanic.csv"
    DB_NAME = "passengers.db"

    def __init__(self):
        self._csv_to_sqllite(self.CSV_FILE_PATH)

    def _csv_to_sqllite(self, path):
        try:
            df = pd.read_csv(path)
            conn = sqlite3.connect(self.DB_NAME)
            df.to_sql("passengers", conn, if_exists='replace', index=False)
            conn.close()
        except Exception as e:
            conn.close()
            raise Exception(e)

    def get_passenger_data_by_id(self, passenger_id):
        try:
            conn = sqlite3.connect(self.DB_NAME)
            cursor = conn.cursor()
            cursor.execute(f'SELECT * FROM passengers WHERE passengerId={passenger_id}')
            row = cursor.fetchone()
            if row:
                passenger = Passenger(*row)
            else:
                passenger = None
            conn.close()
            return passenger
        except Exception as e:
            conn.close()
            raise Exception(e)

    def get_all_passenger(self):
        try:
            passengers = []
            conn = sqlite3.connect(self.DB_NAME)
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM passengers')
            rows = cursor.fetchall()
            for row in rows:
                passengers.append(Passenger(*row))
            conn.close()
            return passengers
        except Exception as e:
            conn.close()
            raise Exception(e)
