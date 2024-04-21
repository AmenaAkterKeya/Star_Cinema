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
        
       
    #-------view_show_list------
    def view_show_list(self):
        print(f'Today show list: ')
        for show in self.show_list:
            print(f'Movie Name: {show[1]}, Show Id: {show[0]}, Time: {show[2]}')

    #-------view_available_seats------        
    def view_available_seats(self, id):
        if id in self.seats:
            seat_av = self.seats[id]
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
hall1.entry_show(id=111, movie_name="Jawan Maji", time="25/18/2823 11:89 AM")
show_id = input("Enter SHOW ID: ")
hall1.view_available_seats(int(show_id)) 

