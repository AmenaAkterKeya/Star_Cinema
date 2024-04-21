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
hall1 = Hall(5, 6, ' Cineplex')
hall1.entry_show(id=111, movie_name="Spiderman", time="25/18/2823 11:89 AM")
print(hall1.show_list)