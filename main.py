import pandas as pd

df = pd.read_csv("hotels.csv", dtype={"id": str})


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.hotel_name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        if df.loc[df["id"] == self.hotel_id, "available"].squeeze() == "yes":
            return True
        return False


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel_object = hotel_object

    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here are your booking details:
        Name: {self.customer_name}
        Hotel: {self.hotel_object.hotel_name}
        """
        return content


print(df)
input_id = input("Enter the id of the hotel: ")
hotel = Hotel(input_id)

if hotel.available():
    hotel.book()
    input_name = input("Enter your name: ")
    reservation_ticket = ReservationTicket(input_name, hotel)
    print(reservation_ticket.generate())
else:
    print("Hotel is not free")
