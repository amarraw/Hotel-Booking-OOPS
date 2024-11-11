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
        Hotal Name : {self.hotel.hotel_name}
        City : {self.hotel.city}
        """
        return content
    
current_datetime = datetime.now()
print(df)

hotel_ID = input('Enter a id of the hotel : ')
hotel = Hotel(hotel_ID)

if hotel.available():
    hotel.book()
    name = input("Enter your name : ")
    reservation_ticket = ReservationTicket(customer_name=name,hotel_obj=hotel,date=current_datetime)
    print(reservation_ticket.generate())
else:
    print("Hotel room are full..!!")