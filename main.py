import pandas as pd

df_hotels = pd.read_csv("hotels.csv", dtype={"id": str})
df_cards = pd.read_csv("cards.csv", dtype=str).to_dict(orient="records")
df_card_security = pd.read_csv("card_security.csv", dtype=str)


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.hotel_name = df_hotels.loc[df_hotels["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        df_hotels.loc[df_hotels["id"] == self.hotel_id, "available"] = "no"
        df_hotels.to_csv("hotels.csv", index=False)

    def available(self):
        if df_hotels.loc[df_hotels["id"] == self.hotel_id, "available"].squeeze() == "yes":
            return True
        return False


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel_object = hotel_object

    def generate(self):
        content = f"\nThank you for your reservation!\nHere are your booking details:\nName: {self.customer_name}\n" \
                  f"Hotel: {self.hotel_object.hotel_name}"
        return content


class CreditCard:
    def __init__(self, creditcard_no):
        self.creditcard_no = creditcard_no

    def validate(self, creditcard_expiration_date, creditcard_cvc, creditcard_holder):
        if {"number": self.creditcard_no, "expiration": creditcard_expiration_date, "cvc": creditcard_cvc,
            "holder": creditcard_holder} in df_cards:
            return True
        return False


class SecureCreditCard(CreditCard):
    def authenticate(self, secure_creditcard_password):
        if df_card_security.loc[df_card_security["number"] == self.creditcard_no, "password"].squeeze() \
                == secure_creditcard_password:
            return True
        return False


print(df_hotels)
input_id = input("\nEnter the ID of the Hotel: ")
hotel = Hotel(input_id)
if hotel.available():
    input_fullname = input("\nEnter your full name: ")
    input_creditcard_no = input("Enter your credit card number: ")
    input_creditcard_expiration_date = input("Enter your credit card expiration date: ")
    input_creditcard_cvc = input("Enter your credit cvc: ")
    input_creditcard_password = input("Enter your password: ")
    secure_creditcard = SecureCreditCard(input_creditcard_no)
    if secure_creditcard.validate(input_creditcard_expiration_date, input_creditcard_cvc, input_fullname.upper()):
        if secure_creditcard.authenticate(input_creditcard_password):
            reservation_ticket = ReservationTicket(input_fullname, hotel)
            print(reservation_ticket.generate())
            hotel.book()
        else:
            print("\nCredit card authentication failed.")
    else:
        print("\nThere was a problem with your payment.")
else:
    print("\nHotel is not available.")
