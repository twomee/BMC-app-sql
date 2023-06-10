import numpy as np
from dao.titanic_passenger_dao_module import TitanicPassengerDao


class TitanicPassengerService(object):

    def __init__(self):
        self.dao = TitanicPassengerDao()

    def get_histogram_data(self):
        try:
            fare_data = self._get_fare_data()
            percentiles = np.percentile(fare_data, range(0, 101, int(len(fare_data) / 10)))
            counts = np.histogram(fare_data, percentiles)[0]
            return {'percentiles': percentiles.tolist(), 'counts': counts.tolist()}
        except Exception as e:
            raise Exception(e)

    def _get_fare_data(self):
        fare_data = []
        passengers_data = self.get_all_passengers()
        for passenger in passengers_data:
            fare_data.append(float(passenger.get("fare")))
        return fare_data

    def get_passenger_data(self, passenger_id):
        try:
            passenger = self.dao.get_passenger_data_by_id(passenger_id)
            if passenger:
                return passenger.to_dict()
        except Exception as e:
            raise Exception(e)

    def get_requested_attribute(self, passenger_id, attribute_list):
        try:
            requested_attribute_list = []
            attribute_list = [attribute.lower() for attribute in attribute_list]
            passenger = self.dao.get_passenger_data_by_id(passenger_id)
            if passenger:
                passenger = passenger.to_dict()
                for attribute, value in passenger.items():
                    attribute = attribute.lower()
                    if attribute in attribute_list:
                        requested_attribute_list.append(value)
                return requested_attribute_list
        except Exception as e:
            raise Exception(e)

    def get_all_passengers(self):
        try:
            passengers = self.dao.get_all_passenger()
            passengers_data = [passenger.to_dict() for passenger in passengers]
            return passengers_data
        except Exception as e:
            raise Exception(e)



