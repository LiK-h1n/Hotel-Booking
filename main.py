import pandas as pd

df = pd.read_csv("hotels.csv", dtype={"id": str})

class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id

    def book(self):
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        if df.loc[df["id"] == self.hotel_id, "available"].squeeze() == "yes":
            return True
        return False


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        pass

    def generate(self):
        pass


print(df)
input_id = input("Enter the id of the hotel:")
hotel = Hotel(input_id)

if hotel.available():
    hotel.book()
    input_name = input("Enter your name: ")
    reservation_ticket = ReservationTicket(input_name, hotel)
    reservation_ticket.generate()
else:
    print("Hotel is not free")
