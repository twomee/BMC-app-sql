import sqlite3

from models.Passenger import Passenger


class TitanicPassengerDao(object):
    CSV_FILE_PATH = "./titanic.csv"
    DB_NAME = "passengers.db"

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
