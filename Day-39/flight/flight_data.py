class FlightData:
    def __init__(self, origin_place, price, start_time, des_place, return_data, out_time, origin_city):
        self.from_place = origin_city
        self.price = price
        self.start_time = start_time
        self.destination_place = des_place
        self.return_date = return_data
        self.return_time = out_time
        self.from_airport = origin_place
