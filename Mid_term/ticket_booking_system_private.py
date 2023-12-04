class Star_Cinema:
    __hall_list = []

    def entry_hall(self, hall):
        self.__hall_list.append(hall)


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no) -> None:
        super().__init__()
        self.__seats = {}
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        self.entry_hall(self)

    def entry_show(self, show_id, movie_name, time):
        all_entry_info = (show_id, movie_name, time)
        self.__show_list.append(all_entry_info)

        seat_map = {}
        for i in range(self.__rows):
            seat_map[i] = {}
            for j in range(self.__cols):
                seat_map[i][j] = 0
        self.__seats[show_id] = seat_map

    def book_seats(self, show_id, quantity, seats):
        seat_map = self.__seats.get(show_id)
        self.__quantity = quantity
        if seat_map is not self.__seats:
            for row, col in seats:
                if row < self.__rows and col < self.__cols:
                    if seat_map[row][col] == 0:
                        seat_map[row][col] = 1
                        print(f'SEAT ({row}, {col}) BOOKED SUCCESFULLY FOR THE SHOW ID {show_id}.')
                    else:
                        print(f'SEAT ({row}, {col}) IS ALREADY BOOKED.')
                else:
                    print(f'INVALID SEAT ({row},{col}), PLEASE ENTER YOUR VALID ROW AND COLUMN !')

    def view_show_list(self):
        for show_id, movie_name, time in self.__show_list:
            print(f'SHOW ID: {show_id}, MOVIE NAME: {movie_name}, DATE & TIME: {time}')

    def view_available_seats(self, show_id):
        seat_map = self.__seats.get(show_id)

        if seat_map is not self.__seats:
            print(f'AVAILABLE SEATS FOR THE SHOW ID {show_id}:')
            for i in range(self.__rows):
                for j in range(self.__cols):
                    if seat_map[i][j] == 0:
                        print("O", end=" ")
                    else:
                        print("1", end=" ")
                print()


# Example usage:

star_cineplex = Hall(5, 5, 1001)
star_cineplex.entry_show('111', 'IRON MAN 3', '6:00 PM and 09/10/2023')

sony = Hall(5, 6, 1002)
sony.entry_show('222', 'SPAIDER MAN', '4:00 PM and 09/10/2023')

while True:
    print('MENU')
    print('1. VIEW ALL SHOW: ')
    print('2. VIEW AVAILABLE SEATS: ')
    print('3. BOOKING TICKET')
    print('4. EXIT!')

    ch = int(input('ENTER YOUR OPTION: '))

    if ch == 1:
        print('--------------------SHOW LIST--------------------')
        star_cineplex.view_show_list()
        sony.view_show_list()
        print('-------------------------------------------------')

    elif ch == 2:
        show_id = input('ENTER THE SHOW ID: ')
        if show_id == '111':
            star_cineplex.view_available_seats(show_id)
        elif show_id == '222':
            sony.view_available_seats(show_id)
        else:
            print(f'INVALID SHOW ID {show_id}')

    elif ch == 3:
        show_id = input('ENTER THE SHOW ID: ')
        quantity = int(input('ENTER NO OF TICKETS: '))
        seats = [(int(input('ENTER THE SEAT ROW: ')), int(input('ENTER THE SEAT COLUMN: '))) for _ in range(quantity)]
        if show_id == '111':
            star_cineplex.book_seats(show_id, quantity, seats)
        elif show_id == '222':
            sony.book_seats(show_id, quantity, seats)
        else:
            print(f'INVALID SHOW ID {show_id}')

    elif ch == 4:
        print('EXIT!')
        break
