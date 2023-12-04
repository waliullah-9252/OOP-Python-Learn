class StarCinema:
    hall_list = []

    def entry_hall(self, hall):
        self.hall_list.append(hall)


class Hall:
    def __init__(self, rows, cols, hall_no):
        self.seats = {}  # Use a dictionary to represent seat bookings
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.allocate_seats()

        # Add the current hall instance to the StarCinema class attribute
        cinema = StarCinema()
        cinema.entry_hall(self)

    def allocate_seats(self):
        for i in range(1, self.rows + 1):
            for j in range(1, self.cols + 1):
                self.seats[(i, j)] = None

    def entry_show(self, show_id, movie_name, time):
        show_info = (show_id, movie_name, time)
        self.show_list.append(show_info)

    def book_seats(self, show_id,quantity, row, col):
        self.quantity = quantity
        seat_key = (row, col)

        if seat_key in self.seats:
            if self.seats[seat_key] is None:
                self.seats[seat_key] = "Booked"
                print(f"Seat ({row}, {col}) booked successfully for show ID {show_id}.")
            else:
                print(f"Seat ({row}, {col}) is already booked.")
        else:
            print(f"Invalid seat ({row}, {col}).")

    def view_show_list(self):
        print("Show List:")
        for show in self.show_list:
            print(f"Show ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}")

    def view_available_seats(self, show_id):
        show_seats = self.seats.copy()
        for seat_key, status in show_seats.items():
            if status is not None:
                show_seats.pop(seat_key)

        print(f"Available Seats for Show ID {show_id}:")
        for i in range(1, self.rows + 1):
            for j in range(1, self.cols + 1):
                if (i, j) in show_seats:
                    print("O", end=" ")  # "O" for available seats
                else:
                    print("1", end=" ")  # "X" for booked seats
            print()

# Example usage:
star_cineplex1 = Hall(5, 5, 1001)
star_cineplex1.entry_show('111', 'Iron man - 3', '6:00 PM')

star_cineplex2 = Hall(5, 6, 1002)
star_cineplex2.entry_show('222', 'Surango', '4:00 PM')

while True:
    print('Menu')
    print('1. View All Show: ')
    print('2. View Available Seats: ')
    print('3. Book Ticket')
    print('4. Exit!')

    print('Enter Your Option: ')

    ch = int(input())

    if ch == 1:
        star_cineplex1.view_show_list()
        star_cineplex2.view_show_list()

    elif ch == 2:
        star_cineplex1.view_available_seats('111')
        star_cineplex2.view_available_seats('222')

    elif ch == 3:
        show_id = input('Enter the Show ID: ')
        quantity = int(input('Enter no of ticket? : '))
        row = int(input('Enter the seat row: '))
        col = int(input('Enter the seat column: '))
        star_cineplex1.book_seats(show_id,quantity, row, col)
        star_cineplex2.book_seats(show_id,quantity, row, col)

    elif ch == 4:
        print('Exit!')
        break
