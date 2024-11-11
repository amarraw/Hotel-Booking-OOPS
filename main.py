import pandas
from datetime import datetime

df = pandas.read_csv("hotels.csv", dtype={"id" : str})

class Hotel:
    
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.hotel_name = df.loc[df["id"] == self.hotel_id , "name" ].squeeze()
        self.city = df.loc[df["id"] == self.hotel_id , "city"].squeeze()

    def book(self):
        # book a hotel by changing it's availability to no
        df.loc[df["id"] == self.hotel_id , "available" ] = "no"
        df.to_csv("hotels.csv", index=False)
    
    def available(self):
        # check if hotel is available or not 
        availability = df.loc[df["id"] == self.hotel_id , "available" ].squeeze()
        if availability == 'yes' :
            return True
        else:
            return False


class ReservationTicket:

    def __init__(self, customer_name , hotel_obj,date ):
        self.customer_name = customer_name
        self.hotel = hotel_obj
        self.date = date

    def generate(self):
        content  = f"""
        Thank you for your reservation
        Here are your booking date : {self.date}
        Name : {self.customer_name}
        Hotel Name : {self.hotel.hotel_name}
        City : {self.hotel.city}
        """
        return content
    
class CreditCard:
    def __init__(self, number):
        self.number = number

    def validate(self, exp_date, holder, cvc):
        if not self._check_length():
            print("Invalid card number length.")
            return False

        if not self._luhn_algorithm():
            print("Invalid card number (Luhn check failed).")
            return False

        if not self._check_cvc(cvc):
            print("Invalid CVC format.")
            return False


        return True

    def _check_length(self):
        """Check if the card number length is valid (usually 13 to 19 digits)."""
        return 13 <= len(self.number) <= 19 and self.number.isdigit()

    def _luhn_algorithm(self):
        """Validate the card number using the Luhn algorithm."""
        total = 0
        reverse_digits = self.number[::-1]

        for i, digit in enumerate(reverse_digits):
            n = int(digit)
            if i % 2 == 1:
                n *= 2
                if n > 9:
                    n -= 9
            total += n

        return total % 10 == 0


    def _check_cvc(self, cvc):
        """Check if CVC is a 3-digit or 4-digit number."""
        return cvc.isdigit() and len(cvc) in [3, 4]


current_datetime = datetime.now()
print(df)

hotel_ID = input('Enter a id of the hotel : ')
hotel = Hotel(hotel_ID)

if hotel.available():
    credit_card = CreditCard(number="4111111111111111")
    if credit_card.validate(exp_date="12/26", holder="John Cena", cvc="123"):
        hotel.book()
        name = input("Enter your name : ")
        reservation_ticket = ReservationTicket(customer_name=name,hotel_obj=hotel,date=current_datetime)
        print(reservation_ticket.generate())
    else:
        print("there is problem with payment..!")
else:
    print("Hotel room are full..!!")