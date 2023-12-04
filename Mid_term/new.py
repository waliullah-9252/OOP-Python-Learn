class Star_Cinema:
    hall_list = []

    @classmethod
    def entry_hall(cls, hall):
        cls.hall_list.append(hall)


class Hall:
    def __init__(self, rows, cols, hall_no):
        self._seats = {}
        self._show_list = []
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no
        self._initialize_seats()
        Star_Cinema.entry_hall(self)

    def _initialize_seats(self):
        for i in range(1, self._rows + 1):
            for j in range(1, self._cols + 1):
                seat_key = f"{i}-{j}"
                self._seats[seat_key] = "free"

    def entry_show(self, show_id, movie_name, time):
        show_info = (show_id, movie_name, time)
        self._show_list.append(show_info)
        self._allocate_seats(show_id)

    def _allocate_seats(self, show_id):
        seat_map = []
        for i in range(1, self._rows + 1):
            row = []
            for j in range(1, self._cols + 1):
                row.append("free")
            seat_map.append(row)
        self._seats[show_id] = seat_map

    def book_seats(self, show_id, seat_list):
        if show_id not in self._seats:
            raise ValueError("Invalid show ID")

        for seat in seat_list:
            row, col = seat
            seat_key = f"{row}-{col}"
            if self._seats[show_id][row - 1][col - 1] == "booked" or \
                    row < 1 or row > self._rows or \
                    col < 1 or col > self._cols:
                raise ValueError("Invalid seat or already booked")

            self._seats[show_id][row - 1][col - 1] = "booked"

    def view_show_list(self):
        for show in self._show_list:
            print(f"Show ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}")

    def view_available_seats(self, show_id):
        if show_id not in self._seats:
            raise ValueError("Invalid show ID")

        seat_map = self._seats[show_id]
        for i in range(self._rows):
            for j in range(self._cols):
                if seat_map[i][j] == "free":
                    print(f"Seat {i + 1}-{j + 1} is available")



star_cineplex = Hall(5,5,1001)
star_cineplex.entry_show('111', 'Iron man - 3', '6:00 PM')

sony = Hall(5,6,1002)
sony.entry_show('222', 'Surango', '4:00 PM')

while True:
    print('Menu')
    print('1. View All Show: ')
    print('2. View Available Seats: ')
    print('3. Book Ticket')
    print('4. Exit!')

    print('Enter Your Option: ')

    ch = int(input())

    if ch == 1:
        print(star_cineplex.view_show_list())
        print(sony.view_show_list())

    elif ch == 2:
        print(star_cineplex.view_available_seats('111'))
        print(sony.view_available_seats('222'))

    elif ch == 3:
        print(star_cineplex.book_seats('111', [(1,4)]))
        print(sony.book_seats('222', [(2,4)]))

    elif ch == 4:
        print('Exit!')
















# Example Usage
# hall1 = Hall(5, 5, 1)
# hall1.entry_show("S1", "Movie 1", "12:00 PM")
# hall1.view_show_list()
# hall1.book_seats("S1", [(1, 1), (2, 2)])
# hall1.view_available_seats("S1")
