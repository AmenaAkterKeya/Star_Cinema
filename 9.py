class Star_Cinema:
    _hall_list = []
    
    @classmethod
    def entry_hall(cls, hall):
        Star_Cinema._hall_list.append(hall)

class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self._seats = {}
        self._show_list = []
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no
        Star_Cinema.entry_hall(self)
    
    #------entry_show()-------
    def entry_show(self, id, movie_name, time):
        shows = (id, movie_name, time)
        self._show_list.append(shows)
        self._seats[id] = [[0 for _ in range(self._cols)] for _ in range(self._rows)]
    
    #------book_seats()-------   
    def book_seats(self, id, seats_book):
        if id in self._seats:
            seat_av = self._seats[id]
            for row, col in seats_book:
                if  row < self._rows and  col < self._cols:
                    if seat_av[row][col] == 0:
                        seat_av[row][col] = 1
                        print(f"Seat {row+1},  {col+1} booked successfully.")
                    else:
                        print(f"Seat {row+1},  {col+1} is already booked.")
                else:
                    print(f"Invalid seat : {row+1}, {col+1}.")
        else:
            print("Invalid show ID.")
        
       
    #-------view_show_list------
    def view_show_list(self):
        print(f'Today show list: ')
        for show in self._show_list:
            print(f'Movie Name: {show[1]}, Show Id: {show[0]}, Time: {show[2]}')

    #-------view_available_seats------        
    def view_available_seats(self, id):
        if id in self._seats:
            seat_av = self._seats[id]
            print(f"Available seats for show ID {id}:")
            for i in range(len(seat_av)):
                for j in range(len(seat_av[0])):
                    if seat_av[i][j] == 0:
                        print(f"Seat ({i+1}, {j+1}): Available")
                    else:
                        print(f"Seat ({i+1}, {j+1}): Booked")
            for i in seat_av:
                print(i)
        else:
            print("Invalid.")

    
hall1 = Hall(5, 6, 'Cineplex')
hall1.entry_show(id=111, movie_name="Spiderman", time="25/18/2823 11:89 AM")
hall1.entry_show(id=333, movie_name="Imaginary", time="25/18/2029 2:88 PM")
while True:
    print("1. VIEW ALL SHOW TODAY")
    print("2. VIEW AVAILABLE SEATS")
    print("3. BOOK TICKET")
    print("4. Exit")
    option = input("ENTER OPTION: ")

    if option == "1":
        for hall in Star_Cinema._hall_list:
            hall.view_show_list()
    elif option == "2":
        show_id = input("Enter SHOW ID: ")
        hall1.view_available_seats(int(show_id)) 
    elif option == "3":
        show_id = input("Show Id: ")
        num_tickets = int(input("Number of Tickets: "))
        book = []
        for _ in range(num_tickets):
            seat_r = int(input("Enter Seat Row: "))
            seat_c = int(input("Enter Seat Col: "))
            book.append((seat_r - 1, seat_c -1))
        hall1.book_seats(int(show_id),book)
        print(f"Updated Seats  Hall {hall1._hall_no}:")
        for i in hall1._seats[int(show_id)]:
            print(i)
    elif option == "4":
       break
    else:
        print("Invalid .")
