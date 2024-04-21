class Star_Cinema:
    hall_list = []
    
    @classmethod
    def entry_hall(self, hall):
        Star_Cinema.hall_list.append(hall)

class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        Star_Cinema().entry_hall(self)
    
    #------entry_show()-------
    def entry_show(self, id, movie_name, time):
        shows = (id, movie_name, time)
        self.show_list.append(shows)
        self.seats[id] = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
    #------book_seats()-------   
    def book_seats(self, id, seats_book):
        if id in self.seats:
            seat_av = self.seats[id]
            for row, col in seats_book:
                if 0 <= row < self.rows and 0 <= col < self.cols:
                    if seat_av[row][col] == 0:
                        seat_av[row][col] = 1
                        print(f"Seat {row+1},  {col+1} booked successfully.")
                    else:
                        print(f"Seat {row+1},  {col+1} is already booked.")
                else:
                    print(f"Invalid seat : {row+1}, {col+1}.")
        else:
            print("Invalid show ID.")
