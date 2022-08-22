class Train:
    tickets=60

class Reservation(Train):
    def booking(self):
        if r.tickets > 0:
            print("ticket booked successfully!")
            r.tickets -= 1
            print("tickets left = ",r.tickets )
        else:
            print("ticket cannot be booked")


r=Reservation()
r.booking()
