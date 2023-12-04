class Star_Cinema:
    hall_list = []

    def entry_hall(self, hall):
        self.hall_list.append(hall)

class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no

    def entry_hall(self):
        pass

    def entry_show(self, show_id, movie_name, time):
        show_info = (show_id, movie_name, time)
        self.show_list.append(show_info)
        show_seats = {}
        for i in range(self.rows):
            show_seats[i] = {}
            for j in range(self.cols):
                show_seats[i][j] = 0
        self.seats[show_id] = show_seats

    def book_seats(self, show_id, quantity, row, col):
        show_seats = self.seats.get(show_id)

        if show_seats is not None:
            try:
                if show_seats[row][col] == 0:
                    show_seats[row][col] = 1
                    print(f"Seat ({row}, {col}) booked successfully for show ID {show_id}.")
                else:
                    print(f"Seat ({row}, {col}) is already booked.")
            except IndexError:
                print(f"Invalid seat ({row}, {col}).")
        else:
            print(f'Invalid Show ID {show_id}.')

    def view_show_list(self):
        for show_id, show_name, time in self.show_list:
            print(f'Show ID: {show_id}, Movie: {show_name}, Time: {time}')

    def view_available_seats(self, show_id):
        show_seats = self.seats.get(show_id)
        if show_seats is not None:
            print(f"Available Seats for Show ID {show_id}:")
            for i in range(self.rows):
                for j in range(self.cols):
                    if show_seats[i][j] == 0:
                        print("O", end=" ")
                    else:
                        print("1", end=" ")
                print()
        else:
            print(f"Invalid show ID {show_id}.")


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

    try:
        ch = int(input('Enter Your Option: '))

        if ch == 1:
            print('<----------Show List---------->')
            print(star_cineplex1.view_show_list())
            print(star_cineplex2.view_show_list())

        elif ch == 2:
            print(star_cineplex1.view_available_seats('111'))
            print(star_cineplex2.view_available_seats('222'))

        elif ch == 3:
            show_id = input('Enter the Show ID: ')
            quantity = int(input('Enter no of ticket? : '))
            row = int(input('Enter the seat row: '))
            col = int(input('Enter the seat column: '))
            star_cineplex1.book_seats(show_id, quantity, row, col)
            star_cineplex2.book_seats(show_id, quantity, row, col)

        elif ch == 4:
            print('Exit!')
            break

        else:
            print('Invalid option. Please enter a number between 1 and 4.')

    except ValueError:
        print('Invalid input. Please enter a number.')
